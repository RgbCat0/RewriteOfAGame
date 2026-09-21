#!/usr/bin/env python3
"""
Ren'Py Archaeologist
====================
Static-analysis helper for messy Ren'Py projects.

What it looks for:
- Labels and screens
- Duplicate labels/screens
- jump/call targets that do not exist
- show/hide/call/use screen references that do not exist
- likely unreferenced labels
- possible label fall-through into the next label
- suspicious comments (TODO, TEST, OLD, DEBUG, CHECK LATER, etc.)
- commented-out Ren'Py/Python-looking code
- typo suggestions for unresolved labels/screens

This is a heuristic static analyzer, not a Ren'Py parser.
Dynamic targets such as `jump expression something` cannot be resolved reliably.

Usage:
    python renpy_archaeologist.py
    python renpy_archaeologist.py path/to/game
    python renpy_archaeologist.py path/to/game --json
    python renpy_archaeologist.py path/to/game --report my_report.txt

If no path is supplied, a folder picker is opened when tkinter is available.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SUSPICIOUS_COMMENT_WORDS = (
    "todo",
    "fixme",
    "test",
    "tester",
    "debug",
    "old",
    "obsolete",
    "outdated",
    "remove",
    "delete",
    "check later",
    "check this",
    "don't know",
    "dont know",
    "broken",
    "temporary",
    "temp",
    "hack",
    "deprecated",
    "unused",
    "wtf",
)

# Labels Ren'Py can invoke by convention rather than through an obvious
# jump/call in the project's source.
KNOWN_RENPY_ENTRY_LABELS = {
    "start",
    "splashscreen",
    "before_main_menu",
    "main_menu",
    "after_load",
    "quit",
    "confirm_quit",
    "after_warp",
}

# Common generated/vendor directories we generally do not want to inspect.
SKIP_DIR_NAMES = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "cache",
    "saves",
    "renpy",
    "lib",
}

# Commented lines beginning with these are likely old code rather than prose.
CODE_LIKE_COMMENT_RE = re.compile(
    r"""^\s*#\s*
    (
        label\b|
        screen\b|
        jump\b|
        call\b|
        show\b|
        hide\b|
        scene\b|
        menu\s*:|
        if\b|
        elif\b|
        else\s*:|
        while\b|
        for\b|
        return\b|
        pause\b|
        play\b|
        stop\b|
        queue\b|
        image\b|
        transform\b|
        default\b|
        define\b|
        \$|
        python\s*:|
        init\b|
        "[^"]*"\s*:|
        '[^']*'\s*:
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)

LABEL_DEF_RE = re.compile(
    r"^(?P<indent>\s*)label\s+(?P<name>[A-Za-z_][\w.]*)\s*(?:\([^)]*\))?\s*:"
)
SCREEN_DEF_RE = re.compile(
    r"^(?P<indent>\s*)screen\s+(?P<name>[A-Za-z_][\w.]*)\s*(?:\([^)]*\))?\s*:"
)

# Static Ren'Py statement references.
JUMP_RE = re.compile(r"^\s*jump\s+(?!expression\b)(?P<name>[A-Za-z_][\w.]*)\b")
CALL_RE = re.compile(
    r"^\s*call\s+(?!screen\b)(?!expression\b)(?P<name>[A-Za-z_][\w.]*)\b"
)
SCREEN_STATEMENT_RE = re.compile(
    r"^\s*(?P<verb>show|hide|call|use)\s+screen\s+(?P<name>[A-Za-z_][\w.]*)\b",
    re.IGNORECASE,
)

# Action/Python-expression references commonly used in screens.
QUOTED_ACTION_PATTERNS = {
    "label": [
        re.compile(r"\bJump\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
        re.compile(r"\bCall\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
        re.compile(r"\brenpy\.jump\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
        re.compile(r"\brenpy\.call\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
    ],
    "screen": [
        re.compile(r"\bShow\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
        re.compile(r"\bHide\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
        re.compile(r"\bToggleScreen\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
        re.compile(r"\bShowMenu\s*\(\s*([\"'])(?P<name>[^\"']+)\1"),
    ],
}

# A top-level final statement matching one of these strongly suggests the label
# cannot accidentally continue into the next label.
TERMINAL_TOP_LEVEL_RE = re.compile(
    r"""^\s*
    (
        jump\b|
        return\b|
        renpy\.jump\s*\(|
        renpy\.return_statement\s*\(
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Location:
    file: str
    line: int

@dataclass(frozen=True)
class Reference:
    name: str
    file: str
    line: int
    kind: str

@dataclass
class LabelBlock:
    name: str
    file: str
    line: int
    indent: int
    next_label: Optional[str] = None
    next_label_line: Optional[int] = None
    last_top_level_code: Optional[str] = None
    last_top_level_line: Optional[int] = None


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------

def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def indent_width(line: str) -> int:
    """Approximate indentation width, treating tabs as 4 spaces."""
    prefix = line[: len(line) - len(line.lstrip(" \t"))]
    return len(prefix.expandtabs(4))


def strip_inline_comment(line: str) -> str:
    """
    Remove a # comment while respecting basic quoted strings.

    This is intentionally lightweight; it handles the overwhelming majority
    of ordinary Ren'Py source without pretending to be a full lexer.
    """
    out: list[str] = []
    quote: Optional[str] = None
    escaped = False

    for ch in line:
        if escaped:
            out.append(ch)
            escaped = False
            continue

        if ch == "\\":
            out.append(ch)
            escaped = True
            continue

        if quote is not None:
            out.append(ch)
            if ch == quote:
                quote = None
            continue

        if ch in ("'", '"'):
            quote = ch
            out.append(ch)
            continue

        if ch == "#":
            break

        out.append(ch)

    return "".join(out).rstrip()


def choose_folder() -> Optional[Path]:
    try:
        import tkinter as tk
        from tkinter import filedialog
    except Exception:
        return None

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    selected = filedialog.askdirectory(
        title="Choose the Ren'Py project folder or game folder"
    )
    root.destroy()

    return Path(selected) if selected else None


def find_scan_root(user_path: Path) -> Path:
    """
    Accept either the project root or the game/ folder.

    If the chosen path contains game/*.rpy, use game/.
    Otherwise scan the selected directory itself.
    """
    user_path = user_path.resolve()
    game_dir = user_path / "game"

    if game_dir.is_dir() and any(game_dir.glob("*.rpy")):
        return game_dir

    return user_path


def iter_rpy_files(root: Path) -> list[Path]:
    result: list[Path] = []

    for path in root.rglob("*.rpy"):
        if any(part.lower() in SKIP_DIR_NAMES for part in path.parts):
            continue
        result.append(path)

    return sorted(result, key=lambda p: str(p).lower())


def closest_matches(name: str, candidates: Iterable[str], n: int = 3) -> list[str]:
    return difflib.get_close_matches(name, list(candidates), n=n, cutoff=0.58)


# ---------------------------------------------------------------------------
# Analyzer
# ---------------------------------------------------------------------------

class RenPyAnalyzer:
    def __init__(self, root: Path):
        self.root = root
        self.files = iter_rpy_files(root)

        self.labels: dict[str, list[Location]] = defaultdict(list)
        self.screens: dict[str, list[Location]] = defaultdict(list)

        self.label_refs: list[Reference] = []
        self.screen_refs: list[Reference] = []

        self.label_blocks: list[LabelBlock] = []

        self.suspicious_comments: list[dict] = []
        self.commented_code: list[dict] = []

        self.stats = Counter()

    def analyze(self) -> dict:
        for path in self.files:
            self._analyze_file(path)

        return self._build_results()

    def _analyze_file(self, path: Path) -> None:
        rel = display_path(path, self.root)

        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="replace")

        lines = text.splitlines()
        self.stats["lines"] += len(lines)

        blocks_in_file: list[LabelBlock] = []

        for line_no, raw in enumerate(lines, start=1):
            self._collect_comments(rel, line_no, raw)

            code = strip_inline_comment(raw)
            if not code.strip():
                continue

            label_match = LABEL_DEF_RE.match(code)
            if label_match:
                name = label_match.group("name")
                loc = Location(rel, line_no)
                self.labels[name].append(loc)

                block = LabelBlock(
                    name=name,
                    file=rel,
                    line=line_no,
                    indent=indent_width(raw),
                )
                blocks_in_file.append(block)
                continue

            screen_match = SCREEN_DEF_RE.match(code)
            if screen_match:
                name = screen_match.group("name")
                self.screens[name].append(Location(rel, line_no))

            jump_match = JUMP_RE.match(code)
            if jump_match:
                self.label_refs.append(
                    Reference(
                        jump_match.group("name"),
                        rel,
                        line_no,
                        "jump",
                    )
                )

            call_match = CALL_RE.match(code)
            if call_match:
                self.label_refs.append(
                    Reference(
                        call_match.group("name"),
                        rel,
                        line_no,
                        "call",
                    )
                )

            screen_match = SCREEN_STATEMENT_RE.match(code)
            if screen_match:
                self.screen_refs.append(
                    Reference(
                        screen_match.group("name"),
                        rel,
                        line_no,
                        f'{screen_match.group("verb").lower()} screen',
                    )
                )

            for kind, patterns in QUOTED_ACTION_PATTERNS.items():
                for pattern in patterns:
                    for match in pattern.finditer(code):
                        ref = Reference(
                            match.group("name"),
                            rel,
                            line_no,
                            "action/expression",
                        )
                        if kind == "label":
                            self.label_refs.append(ref)
                        else:
                            self.screen_refs.append(ref)

        self._finish_label_blocks(lines, rel, blocks_in_file)
        self.label_blocks.extend(blocks_in_file)

    def _collect_comments(self, rel: str, line_no: int, raw: str) -> None:
        stripped = raw.lstrip()

        if not stripped.startswith("#"):
            return

        comment_text = stripped[1:].strip()
        lower = comment_text.lower()

        if any(word in lower for word in SUSPICIOUS_COMMENT_WORDS):
            self.suspicious_comments.append(
                {
                    "file": rel,
                    "line": line_no,
                    "text": comment_text,
                }
            )

        if CODE_LIKE_COMMENT_RE.match(raw):
            self.commented_code.append(
                {
                    "file": rel,
                    "line": line_no,
                    "text": comment_text,
                }
            )

    def _finish_label_blocks(
        self,
        lines: list[str],
        rel: str,
        blocks: list[LabelBlock],
    ) -> None:
        if not blocks:
            return

        # Determine boundaries using the next label in the same file.
        for i, block in enumerate(blocks):
            start_idx = block.line  # zero-based index immediately after label line

            if i + 1 < len(blocks):
                next_block = blocks[i + 1]
                end_idx = next_block.line - 1
                block.next_label = next_block.name
                block.next_label_line = next_block.line
            else:
                end_idx = len(lines)

            body_entries: list[tuple[int, int, str]] = []

            for idx in range(start_idx, end_idx):
                raw = lines[idx]
                code = strip_inline_comment(raw)

                if not code.strip():
                    continue

                # Ignore pure definitions that are not executable flow when
                # deciding the final statement where practical.
                width = indent_width(raw)

                # A new top-level construct outside this label means the label
                # has effectively ended before EOF.
                if width <= block.indent and not raw.lstrip().startswith(("$",)):
                    break

                body_entries.append((idx + 1, width, code.strip()))

            if not body_entries:
                continue

            # Find the shallowest actual body indentation.
            body_indent = min(width for _, width, _ in body_entries if width > block.indent)

            top_level_entries = [
                entry for entry in body_entries if entry[1] == body_indent
            ]

            if top_level_entries:
                line_no, _, code = top_level_entries[-1]
                block.last_top_level_line = line_no
                block.last_top_level_code = code

    def _build_results(self) -> dict:
        label_names = set(self.labels)
        screen_names = set(self.screens)

        duplicate_labels = {
            name: [asdict(loc) for loc in locs]
            for name, locs in self.labels.items()
            if len(locs) > 1
        }
        duplicate_screens = {
            name: [asdict(loc) for loc in locs]
            for name, locs in self.screens.items()
            if len(locs) > 1
        }

        unresolved_labels = []
        for ref in self.label_refs:
            if ref.name not in label_names:
                item = asdict(ref)
                item["suggestions"] = closest_matches(ref.name, label_names)
                unresolved_labels.append(item)

        unresolved_screens = []
        for ref in self.screen_refs:
            if ref.name not in screen_names:
                item = asdict(ref)
                item["suggestions"] = closest_matches(ref.name, screen_names)
                unresolved_screens.append(item)

        referenced_labels = {ref.name for ref in self.label_refs}

        unreferenced_labels = []
        for name, locs in self.labels.items():
            if name in referenced_labels:
                continue
            if name in KNOWN_RENPY_ENTRY_LABELS:
                continue

            # Duplicate definitions have a more serious dedicated report.
            if len(locs) != 1:
                continue

            unreferenced_labels.append(
                {
                    "name": name,
                    "file": locs[0].file,
                    "line": locs[0].line,
                }
            )

        possible_fallthrough = []
        for block in self.label_blocks:
            if not block.next_label:
                continue
            if not block.last_top_level_code:
                continue

            code = block.last_top_level_code

            # Explicit control transfer at label-body indentation = good.
            if TERMINAL_TOP_LEVEL_RE.match(code):
                continue

            # A top-level `menu:` may or may not terminate depending on its
            # branches. We flag it separately but with lower confidence.
            reason = "last top-level statement is not jump/return"
            confidence = "high"

            if re.match(r"^\s*(menu|if|elif|else|while|for)\b", code):
                reason = (
                    "label ends in a compound block; branch termination "
                    "cannot be proven statically"
                )
                confidence = "medium"

            possible_fallthrough.append(
                {
                    "label": block.name,
                    "file": block.file,
                    "label_line": block.line,
                    "last_statement_line": block.last_top_level_line,
                    "last_statement": code,
                    "falls_into": block.next_label,
                    "next_label_line": block.next_label_line,
                    "confidence": confidence,
                    "reason": reason,
                }
            )

        ref_kind_counts = Counter(ref.kind for ref in self.label_refs + self.screen_refs)

        return {
            "root": str(self.root),
            "summary": {
                "files": len(self.files),
                "lines": self.stats["lines"],
                "labels": len(self.labels),
                "screens": len(self.screens),
                "label_references": len(self.label_refs),
                "screen_references": len(self.screen_refs),
                "duplicate_labels": len(duplicate_labels),
                "duplicate_screens": len(duplicate_screens),
                "unresolved_label_references": len(unresolved_labels),
                "unresolved_screen_references": len(unresolved_screens),
                "unreferenced_labels": len(unreferenced_labels),
                "possible_fallthroughs": len(possible_fallthrough),
                "suspicious_comments": len(self.suspicious_comments),
                "commented_out_code_lines": len(self.commented_code),
                "reference_kinds": dict(sorted(ref_kind_counts.items())),
            },
            "duplicate_labels": duplicate_labels,
            "duplicate_screens": duplicate_screens,
            "unresolved_labels": unresolved_labels,
            "unresolved_screens": unresolved_screens,
            "unreferenced_labels": sorted(
                unreferenced_labels,
                key=lambda x: (x["file"].lower(), x["line"]),
            ),
            "possible_fallthrough": sorted(
                possible_fallthrough,
                key=lambda x: (x["file"].lower(), x["label_line"]),
            ),
            "suspicious_comments": self.suspicious_comments,
            "commented_code": self.commented_code,
        }


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def location_text(item: dict) -> str:
    return f'{item["file"]}:{item["line"]}'


def add_section(lines: list[str], title: str) -> None:
    lines.append("")
    lines.append("=" * 80)
    lines.append(title)
    lines.append("=" * 80)


def build_text_report(results: dict) -> str:
    summary = results["summary"]
    out: list[str] = []

    out.append("REN'PY ARCHAEOLOGIST REPORT")
    out.append("=" * 80)
    out.append(f'Scan root: {results["root"]}')
    out.append("")
    out.append(f'Files scanned:                 {summary["files"]}')
    out.append(f'Lines scanned:                 {summary["lines"]:,}')
    out.append(f'Labels defined:                {summary["labels"]:,}')
    out.append(f'Screens defined:               {summary["screens"]:,}')
    out.append(f'Label references:              {summary["label_references"]:,}')
    out.append(f'Screen references:             {summary["screen_references"]:,}')
    out.append(f'Duplicate labels:              {summary["duplicate_labels"]:,}')
    out.append(f'Duplicate screens:             {summary["duplicate_screens"]:,}')
    out.append(
        f'Unresolved label refs:         {summary["unresolved_label_references"]:,}'
    )
    out.append(
        f'Unresolved screen refs:        {summary["unresolved_screen_references"]:,}'
    )
    out.append(f'Likely unreferenced labels:    {summary["unreferenced_labels"]:,}')
    out.append(f'Possible label fall-throughs:  {summary["possible_fallthroughs"]:,}')
    out.append(f'Suspicious comments:           {summary["suspicious_comments"]:,}')
    out.append(
        f'Commented-out code lines:      {summary["commented_out_code_lines"]:,}'
    )

    add_section(out, "UNRESOLVED SCREEN REFERENCES")
    if not results["unresolved_screens"]:
        out.append("None found.")
    else:
        for item in results["unresolved_screens"]:
            suggestions = item.get("suggestions") or []
            suggestion_text = (
                f'  Did you mean: {", ".join(suggestions)}'
                if suggestions
                else ""
            )
            out.append(
                f'- {item["name"]}  [{item["kind"]}]  '
                f'{item["file"]}:{item["line"]}{suggestion_text}'
            )

    add_section(out, "UNRESOLVED LABEL REFERENCES")
    if not results["unresolved_labels"]:
        out.append("None found.")
    else:
        for item in results["unresolved_labels"]:
            suggestions = item.get("suggestions") or []
            suggestion_text = (
                f'  Did you mean: {", ".join(suggestions)}'
                if suggestions
                else ""
            )
            out.append(
                f'- {item["name"]}  [{item["kind"]}]  '
                f'{item["file"]}:{item["line"]}{suggestion_text}'
            )

    add_section(out, "DUPLICATE LABELS")
    if not results["duplicate_labels"]:
        out.append("None found.")
    else:
        for name, locations in sorted(results["duplicate_labels"].items()):
            out.append(f"- {name}")
            for loc in locations:
                out.append(f'    {loc["file"]}:{loc["line"]}')

    add_section(out, "DUPLICATE SCREENS")
    if not results["duplicate_screens"]:
        out.append("None found.")
    else:
        for name, locations in sorted(results["duplicate_screens"].items()):
            out.append(f"- {name}")
            for loc in locations:
                out.append(f'    {loc["file"]}:{loc["line"]}')

    add_section(out, "POSSIBLE LABEL FALL-THROUGH")
    if not results["possible_fallthrough"]:
        out.append("None found.")
    else:
        out.append(
            "These are heuristic warnings. A label may intentionally fall through, "
            "or every branch of a final menu/if may jump elsewhere."
        )
        out.append("")
        for item in results["possible_fallthrough"]:
            out.append(
                f'- {item["label"]} -> {item["falls_into"]} '
                f'[{item["confidence"]}]'
            )
            out.append(
                f'    {item["file"]}:{item["label_line"]} '
                f'(next label at line {item["next_label_line"]})'
            )
            out.append(
                f'    Last top-level statement '
                f'(line {item["last_statement_line"]}): '
                f'{item["last_statement"]}'
            )
            out.append(f'    Reason: {item["reason"]}')

    add_section(out, "LIKELY UNREFERENCED LABELS")
    if not results["unreferenced_labels"]:
        out.append("None found.")
    else:
        out.append(
            "WARNING: labels can be reached dynamically, from Python, from external "
            "code, or by Ren'Py conventions. Treat this as a review list, not a delete list."
        )
        out.append("")
        for item in results["unreferenced_labels"]:
            out.append(f'- {item["name"]}  {item["file"]}:{item["line"]}')

    add_section(out, "SUSPICIOUS COMMENTS")
    if not results["suspicious_comments"]:
        out.append("None found.")
    else:
        for item in results["suspicious_comments"]:
            out.append(f'- {item["file"]}:{item["line"]}  # {item["text"]}')

    add_section(out, "COMMENTED-OUT CODE")
    if not results["commented_code"]:
        out.append("None found.")
    else:
        for item in results["commented_code"]:
            out.append(f'- {item["file"]}:{item["line"]}  # {item["text"]}')

    add_section(out, "NOTES / LIMITATIONS")
    out.extend(
        [
            "- Dynamic `jump expression` / `call expression` targets are not resolved.",
            "- Dynamically constructed screen names are not resolved.",
            "- An 'unreferenced' label can still be valid if called indirectly.",
            "- Fall-through detection is intentionally conservative and heuristic.",
            "- This script never modifies your project.",
        ]
    )

    return "\n".join(out) + "\n"


def print_console_summary(results: dict, report_path: Path, json_path: Optional[Path]) -> None:
    s = results["summary"]

    print()
    print("Ren'Py Archaeologist finished.")
    print("-" * 44)
    print(f'Files scanned:               {s["files"]}')
    print(f'Lines scanned:               {s["lines"]:,}')
    print(f'Labels:                      {s["labels"]:,}')
    print(f'Screens:                     {s["screens"]:,}')
    print(f'Unresolved label refs:       {s["unresolved_label_references"]:,}')
    print(f'Unresolved screen refs:      {s["unresolved_screen_references"]:,}')
    print(f'Possible fall-throughs:      {s["possible_fallthroughs"]:,}')
    print(f'Likely unreferenced labels:  {s["unreferenced_labels"]:,}')
    print(f'Suspicious comments:         {s["suspicious_comments"]:,}')
    print(f'Commented-out code lines:    {s["commented_out_code_lines"]:,}')
    print()
    print(f"Text report: {report_path}")

    if json_path is not None:
        print(f"JSON report: {json_path}")

    # Give the most immediately useful discoveries right in the terminal.
    if results["unresolved_screens"]:
        print()
        print("Unresolved screens:")
        for item in results["unresolved_screens"][:10]:
            suffix = ""
            if item["suggestions"]:
                suffix = f' -> maybe {", ".join(item["suggestions"])}'
            print(
                f'  {item["name"]} at {item["file"]}:{item["line"]}{suffix}'
            )
        if len(results["unresolved_screens"]) > 10:
            print(f'  ... and {len(results["unresolved_screens"]) - 10} more')

    if results["possible_fallthrough"]:
        print()
        print("Possible fall-throughs:")
        for item in results["possible_fallthrough"][:10]:
            print(
                f'  {item["label"]} -> {item["falls_into"]} '
                f'({item["file"]}:{item["label_line"]})'
            )
        if len(results["possible_fallthrough"]) > 10:
            print(f'  ... and {len(results["possible_fallthrough"]) - 10} more')


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Static archaeology tool for Ren'Py .rpy source files."
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Ren'Py project root or game/ directory. Opens a folder picker if omitted.",
    )
    parser.add_argument(
        "--report",
        default="renpy_analysis_report.txt",
        help="Text report filename/path (default: renpy_analysis_report.txt).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Also write a machine-readable JSON report.",
    )
    parser.add_argument(
        "--json-file",
        default="renpy_analysis_report.json",
        help="JSON report filename/path.",
    )
    return parser.parse_args()


def resolve_output_path(value: str, scan_root: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return scan_root / path


def main() -> int:
    args = parse_args()

    if args.path:
        selected = Path(args.path)
    else:
        selected = choose_folder()
        if selected is None:
            print(
                "No folder selected and tkinter was unavailable. "
                "Pass the project path on the command line.",
                file=sys.stderr,
            )
            return 2

    if not selected.exists() or not selected.is_dir():
        print(f"Folder does not exist: {selected}", file=sys.stderr)
        return 2

    scan_root = find_scan_root(selected)
    files = iter_rpy_files(scan_root)

    if not files:
        print(f"No .rpy files found under: {scan_root}", file=sys.stderr)
        return 1

    print(f"Scanning: {scan_root}")
    print(f"Found {len(files)} .rpy files...")

    analyzer = RenPyAnalyzer(scan_root)
    results = analyzer.analyze()

    report_path = resolve_output_path(args.report, scan_root)
    report_path.write_text(build_text_report(results), encoding="utf-8")

    json_path: Optional[Path] = None
    if args.json:
        json_path = resolve_output_path(args.json_file, scan_root)
        json_path.write_text(
            json.dumps(results, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    print_console_summary(results, report_path, json_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
pause