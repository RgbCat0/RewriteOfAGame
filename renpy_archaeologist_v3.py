#!/usr/bin/env python3
"""
Ren'Py Archaeologist v3
=======================

A read-only static-analysis helper for Ren'Py projects.

v3 improvements:
- Understands screen blocks well enough to stop mistaking screen-language
  `label` displayables for script labels.
- Fixes commented-out-code detection.
- Separates fall-through warnings into:
    * definite / strong
    * call-screen return paths
    * compound / uncertain
- Finds obvious test/debug/temp labels.
- Gives typo suggestions for unresolved labels and screens.
- Produces both a human-readable report and optional JSON.
- Friendly to double-clicking on Windows: folder picker, completion popup,
  and crash log.

This is deliberately conservative. It never edits your project.

Usage:
    python renpy_archaeologist_v3.py
    python renpy_archaeologist_v3.py "C:\\path\\to\\project"
    python renpy_archaeologist_v3.py "C:\\path\\to\\project\\game" --json
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import traceback
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional


# =============================================================================
# Configuration
# =============================================================================

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

DEBUG_LABEL_WORDS = (
    "test",
    "tester",
    "debug",
    "temp",
    "temporary",
    "sandbox",
)

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

# IMPORTANT: # must be escaped because this pattern uses re.VERBOSE.
CODE_LIKE_COMMENT_RE = re.compile(
    r"""^\s*\#\s*
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

JUMP_RE = re.compile(
    r"^\s*jump\s+(?!expression\b)(?P<name>[A-Za-z_][\w.]*)\b"
)

CALL_RE = re.compile(
    r"^\s*call\s+(?!screen\b)(?!expression\b)(?P<name>[A-Za-z_][\w.]*)\b"
)

SCREEN_STATEMENT_RE = re.compile(
    r"^\s*(?P<verb>show|hide|call|use)\s+screen\s+"
    r"(?P<name>[A-Za-z_][\w.]*)\b",
    re.IGNORECASE,
)

CALL_SCREEN_RE = re.compile(
    r"^\s*call\s+screen\s+(?P<name>[A-Za-z_][\w.]*)\b",
    re.IGNORECASE,
)

SHOW_SCREEN_RE = re.compile(
    r"^\s*show\s+screen\s+(?P<name>[A-Za-z_][\w.]*)\b",
    re.IGNORECASE,
)

COMPOUND_RE = re.compile(
    r"^\s*(menu\s*:|if\b|elif\b|else\s*:|while\b|for\b)",
    re.IGNORECASE,
)

TERMINAL_RE = re.compile(
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


# =============================================================================
# Data structures
# =============================================================================

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


@dataclass
class ScreenRange:
    name: str
    start_line: int
    end_line: int
    indent: int


# =============================================================================
# Utility
# =============================================================================

def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def indent_width(line: str) -> int:
    prefix = line[: len(line) - len(line.lstrip(" \t"))]
    return len(prefix.expandtabs(4))


def strip_inline_comment(line: str) -> str:
    """Strip # comments while respecting ordinary quoted strings."""
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

    try:
        root.attributes("-topmost", True)
    except Exception:
        pass

    selected = filedialog.askdirectory(
        title="Choose the Ren'Py project folder or game folder"
    )

    root.destroy()
    return Path(selected) if selected else None


def show_message(title: str, message: str, error: bool = False) -> None:
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()

        try:
            root.attributes("-topmost", True)
        except Exception:
            pass

        if error:
            messagebox.showerror(title, message, parent=root)
        else:
            messagebox.showinfo(title, message, parent=root)

        root.destroy()
    except Exception:
        pass


def find_scan_root(path: Path) -> Path:
    path = path.resolve()
    game_dir = path / "game"

    if game_dir.is_dir() and any(game_dir.glob("*.rpy")):
        return game_dir

    return path


def iter_rpy_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for path in root.rglob("*.rpy"):
        # Compare only directory names relative to root, not absolute path parts.
        try:
            rel_parts = path.relative_to(root).parts[:-1]
        except ValueError:
            rel_parts = path.parts[:-1]

        if any(part.lower() in SKIP_DIR_NAMES for part in rel_parts):
            continue

        files.append(path)

    return sorted(files, key=lambda p: str(p).lower())


def closest_matches(
    name: str,
    candidates: Iterable[str],
    n: int = 3,
) -> list[str]:
    return difflib.get_close_matches(
        name,
        list(candidates),
        n=n,
        cutoff=0.58,
    )


def is_debug_label(name: str) -> bool:
    lowered = name.lower()
    return any(word in lowered for word in DEBUG_LABEL_WORDS)


# =============================================================================
# Context helpers
# =============================================================================

def build_screen_ranges(lines: list[str]) -> list[ScreenRange]:
    """
    Find top-level Ren'Py screen blocks.

    This is enough to distinguish:

        screen history():
            ...
            label "[h.who]"

    from a real script:

        label something:
            ...

    A screen block ends when a nonblank/noncomment line dedents to the screen
    statement's indentation or less.
    """
    ranges: list[ScreenRange] = []

    for i, raw in enumerate(lines):
        code = strip_inline_comment(raw)
        match = SCREEN_DEF_RE.match(code)

        if not match:
            continue

        start_line = i + 1
        screen_indent = indent_width(raw)
        end_line = len(lines)

        for j in range(i + 1, len(lines)):
            candidate_raw = lines[j]
            candidate = strip_inline_comment(candidate_raw)

            if not candidate.strip():
                continue

            if indent_width(candidate_raw) <= screen_indent:
                end_line = j
                break

        ranges.append(
            ScreenRange(
                name=match.group("name"),
                start_line=start_line,
                end_line=end_line,
                indent=screen_indent,
            )
        )

    return ranges


def line_inside_screen(line_no: int, ranges: list[ScreenRange]) -> bool:
    for screen in ranges:
        if screen.start_line < line_no <= screen.end_line:
            return True
    return False


# =============================================================================
# Analyzer
# =============================================================================

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

        screen_ranges = build_screen_ranges(lines)
        blocks_in_file: list[LabelBlock] = []

        for line_no, raw in enumerate(lines, start=1):
            self._collect_comments(rel, line_no, raw)

            code = strip_inline_comment(raw)
            if not code.strip():
                continue

            in_screen = line_inside_screen(line_no, screen_ranges)

            # Real screen definition.
            screen_match = SCREEN_DEF_RE.match(code)
            if screen_match:
                self.screens[screen_match.group("name")].append(
                    Location(rel, line_no)
                )
                # Still allow action refs on same line if any, though unusual.

            # IMPORTANT: screen-language `label` displayables are NOT script labels.
            if not in_screen:
                label_match = LABEL_DEF_RE.match(code)
                if label_match:
                    name = label_match.group("name")
                    self.labels[name].append(Location(rel, line_no))

                    blocks_in_file.append(
                        LabelBlock(
                            name=name,
                            file=rel,
                            line=line_no,
                            indent=indent_width(raw),
                        )
                    )
                    continue

            # Script jump/call refs should not be read out of screen-language
            # text/displayables, but screen Action() references SHOULD be.
            if not in_screen:
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

                screen_statement_match = SCREEN_STATEMENT_RE.match(code)
                if screen_statement_match:
                    self.screen_refs.append(
                        Reference(
                            screen_statement_match.group("name"),
                            rel,
                            line_no,
                            f'{screen_statement_match.group("verb").lower()} screen',
                        )
                    )

            # Action constructors can legitimately appear inside screens.
            for kind, patterns in QUOTED_ACTION_PATTERNS.items():
                for pattern in patterns:
                    for match in pattern.finditer(code):
                        ref = Reference(
                            match.group("name"),
                            rel,
                            line_no,
                            "screen action/expression" if in_screen else "action/expression",
                        )

                        if kind == "label":
                            self.label_refs.append(ref)
                        else:
                            self.screen_refs.append(ref)

        self._finish_label_blocks(lines, rel, blocks_in_file, screen_ranges)
        self.label_blocks.extend(blocks_in_file)

    def _collect_comments(
        self,
        rel: str,
        line_no: int,
        raw: str,
    ) -> None:
        stripped = raw.lstrip()

        if not stripped.startswith("#"):
            return

        text = stripped[1:].strip()
        lowered = text.lower()

        if any(word in lowered for word in SUSPICIOUS_COMMENT_WORDS):
            self.suspicious_comments.append(
                {
                    "file": rel,
                    "line": line_no,
                    "text": text,
                }
            )

        if CODE_LIKE_COMMENT_RE.match(raw):
            self.commented_code.append(
                {
                    "file": rel,
                    "line": line_no,
                    "text": text,
                }
            )

    def _finish_label_blocks(
        self,
        lines: list[str],
        rel: str,
        blocks: list[LabelBlock],
        screen_ranges: list[ScreenRange],
    ) -> None:
        if not blocks:
            return

        for i, block in enumerate(blocks):
            start_idx = block.line  # immediately after label line, zero-based

            if i + 1 < len(blocks):
                next_block = blocks[i + 1]
                end_idx = next_block.line - 1
                block.next_label = next_block.name
                block.next_label_line = next_block.line
            else:
                end_idx = len(lines)

            body_entries: list[tuple[int, int, str]] = []

            for idx in range(start_idx, end_idx):
                line_no = idx + 1

                # Do not let weird screen-language contents pollute label flow.
                if line_inside_screen(line_no, screen_ranges):
                    continue

                raw = lines[idx]
                code = strip_inline_comment(raw)

                if not code.strip():
                    continue

                width = indent_width(raw)

                # At same/lower indentation, we've left this label.
                if width <= block.indent:
                    break

                body_entries.append((line_no, width, code.strip()))

            if not body_entries:
                continue

            valid_indents = [
                width
                for _, width, _ in body_entries
                if width > block.indent
            ]

            if not valid_indents:
                continue

            body_indent = min(valid_indents)

            top_level_entries = [
                entry
                for entry in body_entries
                if entry[1] == body_indent
            ]

            if top_level_entries:
                line_no, _, code = top_level_entries[-1]
                block.last_top_level_line = line_no
                block.last_top_level_code = code

    def _classify_fallthrough(self, block: LabelBlock) -> Optional[dict]:
        code = block.last_top_level_code

        if not code or not block.next_label:
            return None

        if TERMINAL_RE.match(code):
            return None

        if CALL_SCREEN_RE.match(code):
            return {
                "severity": "review",
                "category": "call-screen return path",
                "reason": (
                    "`call screen` blocks until the screen returns, but execution "
                    "then continues into the next label unless the screen always jumps "
                    "away or otherwise transfers control."
                ),
            }

        if COMPOUND_RE.match(code):
            return {
                "severity": "uncertain",
                "category": "compound control flow",
                "reason": (
                    "The label ends in a menu/if/loop block. Static analysis cannot "
                    "prove that every possible branch transfers control."
                ),
            }

        if SHOW_SCREEN_RE.match(code):
            return {
                "severity": "strong",
                "category": "definite continuation after show screen",
                "reason": (
                    "`show screen` does not block script execution. Unless another "
                    "statement intervenes, execution continues into the next label."
                ),
            }

        return {
            "severity": "strong",
            "category": "plain fall-through",
            "reason": (
                "The final top-level statement is not a jump/return. Ren'Py normally "
                "continues into the next label after it completes."
            ),
        }

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
            if len(locs) != 1:
                continue

            unreferenced_labels.append(
                {
                    "name": name,
                    "file": locs[0].file,
                    "line": locs[0].line,
                }
            )

        debug_labels = []
        for name, locs in self.labels.items():
            if is_debug_label(name):
                for loc in locs:
                    debug_labels.append(
                        {
                            "name": name,
                            "file": loc.file,
                            "line": loc.line,
                        }
                    )

        fallthroughs = []
        for block in self.label_blocks:
            classification = self._classify_fallthrough(block)

            if not classification:
                continue

            fallthroughs.append(
                {
                    "label": block.name,
                    "file": block.file,
                    "label_line": block.line,
                    "last_statement_line": block.last_top_level_line,
                    "last_statement": block.last_top_level_code,
                    "falls_into": block.next_label,
                    "next_label_line": block.next_label_line,
                    **classification,
                }
            )

        severity_counts = Counter(
            item["severity"] for item in fallthroughs
        )

        ref_kind_counts = Counter(
            ref.kind
            for ref in self.label_refs + self.screen_refs
        )

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
                "debug_test_labels": len(debug_labels),
                "possible_fallthroughs": len(fallthroughs),
                "strong_fallthroughs": severity_counts["strong"],
                "review_fallthroughs": severity_counts["review"],
                "uncertain_fallthroughs": severity_counts["uncertain"],
                "suspicious_comments": len(self.suspicious_comments),
                "commented_out_code_lines": len(self.commented_code),
                "reference_kinds": dict(sorted(ref_kind_counts.items())),
            },

            "duplicate_labels": duplicate_labels,
            "duplicate_screens": duplicate_screens,

            "unresolved_labels": sorted(
                unresolved_labels,
                key=lambda x: (x["file"].lower(), x["line"]),
            ),

            "unresolved_screens": sorted(
                unresolved_screens,
                key=lambda x: (x["file"].lower(), x["line"]),
            ),

            "unreferenced_labels": sorted(
                unreferenced_labels,
                key=lambda x: (x["file"].lower(), x["line"]),
            ),

            "debug_labels": sorted(
                debug_labels,
                key=lambda x: (x["file"].lower(), x["line"]),
            ),

            "possible_fallthrough": sorted(
                fallthroughs,
                key=lambda x: (
                    {"strong": 0, "review": 1, "uncertain": 2}.get(
                        x["severity"], 9
                    ),
                    x["file"].lower(),
                    x["label_line"],
                ),
            ),

            "suspicious_comments": self.suspicious_comments,
            "commented_code": self.commented_code,
        }


# =============================================================================
# Report formatting
# =============================================================================

def add_section(lines: list[str], title: str) -> None:
    lines.append("")
    lines.append("=" * 88)
    lines.append(title)
    lines.append("=" * 88)


def format_suggestions(item: dict) -> str:
    suggestions = item.get("suggestions") or []

    if not suggestions:
        return ""

    return f'  Did you mean: {", ".join(suggestions)}'


def build_text_report(results: dict) -> str:
    s = results["summary"]
    out: list[str] = []

    out.append("REN'PY ARCHAEOLOGIST v3 REPORT")
    out.append("=" * 88)
    out.append(f'Scan root: {results["root"]}')
    out.append("")
    out.append(f'Files scanned:                    {s["files"]}')
    out.append(f'Lines scanned:                    {s["lines"]:,}')
    out.append(f'Labels defined:                   {s["labels"]:,}')
    out.append(f'Screens defined:                  {s["screens"]:,}')
    out.append(f'Label references:                 {s["label_references"]:,}')
    out.append(f'Screen references:                {s["screen_references"]:,}')
    out.append(f'Duplicate labels:                 {s["duplicate_labels"]:,}')
    out.append(f'Duplicate screens:                {s["duplicate_screens"]:,}')
    out.append(f'Unresolved label refs:            {s["unresolved_label_references"]:,}')
    out.append(f'Unresolved screen refs:           {s["unresolved_screen_references"]:,}')
    out.append(f'Likely unreferenced labels:       {s["unreferenced_labels"]:,}')
    out.append(f'Test/debug/temp labels:           {s["debug_test_labels"]:,}')
    out.append(f'Possible fall-throughs total:     {s["possible_fallthroughs"]:,}')
    out.append(f'  Strong:                         {s["strong_fallthroughs"]:,}')
    out.append(f'  Review (`call screen`):         {s["review_fallthroughs"]:,}')
    out.append(f'  Uncertain compound flow:        {s["uncertain_fallthroughs"]:,}')
    out.append(f'Suspicious comments:              {s["suspicious_comments"]:,}')
    out.append(f'Commented-out code lines:         {s["commented_out_code_lines"]:,}')

    # ---------------------------------------------------------------------
    add_section(out, "PRIORITY 1 — UNRESOLVED SCREEN REFERENCES")

    if not results["unresolved_screens"]:
        out.append("None found.")
    else:
        for item in results["unresolved_screens"]:
            out.append(
                f'- {item["name"]} [{item["kind"]}] '
                f'{item["file"]}:{item["line"]}'
                f'{format_suggestions(item)}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "PRIORITY 1 — UNRESOLVED LABEL REFERENCES")

    if not results["unresolved_labels"]:
        out.append("None found.")
    else:
        for item in results["unresolved_labels"]:
            out.append(
                f'- {item["name"]} [{item["kind"]}] '
                f'{item["file"]}:{item["line"]}'
                f'{format_suggestions(item)}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "PRIORITY 1 — STRONG FALL-THROUGH WARNINGS")

    strong = [
        x for x in results["possible_fallthrough"]
        if x["severity"] == "strong"
    ]

    if not strong:
        out.append("None found.")
    else:
        for item in strong:
            out.append(
                f'- {item["label"]} -> {item["falls_into"]} '
                f'[{item["category"]}]'
            )
            out.append(
                f'    {item["file"]}:{item["label_line"]} '
                f'(next label line {item["next_label_line"]})'
            )
            out.append(
                f'    Last statement '
                f'(line {item["last_statement_line"]}): '
                f'{item["last_statement"]}'
            )
            out.append(f'    Why flagged: {item["reason"]}')

    # ---------------------------------------------------------------------
    add_section(out, "PRIORITY 2 — `call screen` RETURN PATHS")

    review = [
        x for x in results["possible_fallthrough"]
        if x["severity"] == "review"
    ]

    if not review:
        out.append("None found.")
    else:
        out.append(
            "These are not immediate fall-throughs. `call screen` blocks until "
            "the screen returns. If it returns normally, script execution then "
            "continues into the next label."
        )
        out.append("")

        for item in review:
            out.append(
                f'- {item["label"]} -> {item["falls_into"]}'
            )
            out.append(
                f'    {item["file"]}:{item["label_line"]}; '
                f'last statement line {item["last_statement_line"]}: '
                f'{item["last_statement"]}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "PRIORITY 3 — COMPOUND FLOW REQUIRES REVIEW")

    uncertain = [
        x for x in results["possible_fallthrough"]
        if x["severity"] == "uncertain"
    ]

    if not uncertain:
        out.append("None found.")
    else:
        out.append(
            "These end in menu/if/loop blocks. They may be perfectly safe if "
            "every reachable branch jumps or returns."
        )
        out.append("")

        for item in uncertain:
            out.append(
                f'- {item["label"]} -> {item["falls_into"]}'
            )
            out.append(
                f'    {item["file"]}:{item["label_line"]}; '
                f'last top-level statement line '
                f'{item["last_statement_line"]}: '
                f'{item["last_statement"]}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "TEST / DEBUG / TEMP-LIKE LABELS")

    if not results["debug_labels"]:
        out.append("None found.")
    else:
        for item in results["debug_labels"]:
            out.append(
                f'- {item["name"]}  {item["file"]}:{item["line"]}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "LIKELY UNREFERENCED LABELS")

    if not results["unreferenced_labels"]:
        out.append("None found.")
    else:
        out.append(
            "Treat this as a review list, NOT a delete list. Labels may be "
            "called dynamically, from Python, or by Ren'Py conventions."
        )
        out.append("")

        for item in results["unreferenced_labels"]:
            out.append(
                f'- {item["name"]}  {item["file"]}:{item["line"]}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "DUPLICATE LABELS")

    if not results["duplicate_labels"]:
        out.append("None found.")
    else:
        for name, locations in sorted(results["duplicate_labels"].items()):
            out.append(f"- {name}")

            for loc in locations:
                out.append(
                    f'    {loc["file"]}:{loc["line"]}'
                )

    # ---------------------------------------------------------------------
    add_section(out, "DUPLICATE SCREENS")

    if not results["duplicate_screens"]:
        out.append("None found.")
    else:
        out.append(
            "A duplicate screen may be intentional, version-specific, or an "
            "override. Inspect before changing it."
        )
        out.append("")

        for name, locations in sorted(results["duplicate_screens"].items()):
            out.append(f"- {name}")

            for loc in locations:
                out.append(
                    f'    {loc["file"]}:{loc["line"]}'
                )

    # ---------------------------------------------------------------------
    add_section(out, "SUSPICIOUS COMMENTS")

    if not results["suspicious_comments"]:
        out.append("None found.")
    else:
        for item in results["suspicious_comments"]:
            out.append(
                f'- {item["file"]}:{item["line"]}  # {item["text"]}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "COMMENTED-OUT CODE")

    if not results["commented_code"]:
        out.append("None found.")
    else:
        for item in results["commented_code"]:
            out.append(
                f'- {item["file"]}:{item["line"]}  # {item["text"]}'
            )

    # ---------------------------------------------------------------------
    add_section(out, "NOTES / LIMITATIONS")

    out.extend(
        [
            "- Screen-language `label` displayables are excluded from script-label analysis.",
            "- Dynamic `jump expression` / `call expression` targets are not resolved.",
            "- Dynamically constructed screen names are not resolved.",
            "- An 'unreferenced' label can still be perfectly valid if reached indirectly.",
            "- Compound control-flow analysis is intentionally conservative.",
            "- `call screen` is treated separately because it blocks until Return(), then resumes.",
            "- This script NEVER modifies your Ren'Py project.",
        ]
    )

    return "\n".join(out) + "\n"


def print_console_summary(
    results: dict,
    report_path: Path,
    json_path: Optional[Path],
) -> None:
    s = results["summary"]

    print()
    print("Ren'Py Archaeologist v3 finished.")
    print("-" * 52)
    print(f'Files scanned:                 {s["files"]}')
    print(f'Lines scanned:                 {s["lines"]:,}')
    print(f'Labels:                        {s["labels"]:,}')
    print(f'Screens:                       {s["screens"]:,}')
    print(f'Unresolved label refs:         {s["unresolved_label_references"]:,}')
    print(f'Unresolved screen refs:        {s["unresolved_screen_references"]:,}')
    print(f'Strong fall-throughs:          {s["strong_fallthroughs"]:,}')
    print(f'Call-screen return paths:      {s["review_fallthroughs"]:,}')
    print(f'Uncertain compound endings:    {s["uncertain_fallthroughs"]:,}')
    print(f'Likely unreferenced labels:    {s["unreferenced_labels"]:,}')
    print(f'Test/debug/temp labels:        {s["debug_test_labels"]:,}')
    print(f'Suspicious comments:           {s["suspicious_comments"]:,}')
    print(f'Commented-out code lines:      {s["commented_out_code_lines"]:,}')
    print()
    print(f"Text report: {report_path}")

    if json_path:
        print(f"JSON report: {json_path}")

    if results["unresolved_screens"]:
        print()
        print("Unresolved screens:")

        for item in results["unresolved_screens"][:10]:
            suffix = ""

            if item["suggestions"]:
                suffix = f' -> maybe {", ".join(item["suggestions"])}'

            print(
                f'  {item["name"]} at '
                f'{item["file"]}:{item["line"]}{suffix}'
            )

    if results["unresolved_labels"]:
        print()
        print("Unresolved labels:")

        for item in results["unresolved_labels"][:10]:
            suffix = ""

            if item["suggestions"]:
                suffix = f' -> maybe {", ".join(item["suggestions"])}'

            print(
                f'  {item["name"]} at '
                f'{item["file"]}:{item["line"]}{suffix}'
            )

    strong = [
        x for x in results["possible_fallthrough"]
        if x["severity"] == "strong"
    ]

    if strong:
        print()
        print("Strong fall-through warnings:")

        for item in strong[:10]:
            print(
                f'  {item["label"]} -> {item["falls_into"]} '
                f'({item["file"]}:{item["label_line"]})'
            )

        if len(strong) > 10:
            print(f"  ... and {len(strong) - 10} more")


# =============================================================================
# CLI
# =============================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only static archaeology tool for Ren'Py .rpy source."
    )

    parser.add_argument(
        "path",
        nargs="?",
        help=(
            "Ren'Py project root or game/ directory. "
            "If omitted, a folder picker opens."
        ),
    )

    parser.add_argument(
        "--report",
        default="renpy_analysis_report_v3.txt",
        help="Text report path/filename.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Also write a JSON report.",
    )

    parser.add_argument(
        "--json-file",
        default="renpy_analysis_report_v3.json",
        help="JSON report path/filename.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    gui_mode = not bool(args.path)
    selected: Optional[Path] = None

    try:
        if args.path:
            selected = Path(args.path)
        else:
            selected = choose_folder()

            if selected is None:
                print("No folder selected.")
                return 0

        selected = selected.resolve()

        if not selected.exists() or not selected.is_dir():
            message = f"Folder does not exist:\n{selected}"
            print(message, file=sys.stderr)

            if gui_mode:
                show_message(
                    "Ren'Py Archaeologist",
                    message,
                    error=True,
                )

            return 2

        scan_root = find_scan_root(selected)
        files = iter_rpy_files(scan_root)

        if not files:
            message = (
                "No .rpy files were found.\n\n"
                f"Selected folder:\n{selected}\n\n"
                f"Scanned folder:\n{scan_root}\n\n"
                "Choose either the Ren'Py project root (the folder containing "
                "game/) or the game/ folder itself."
            )

            print(message, file=sys.stderr)

            if gui_mode:
                show_message(
                    "No .rpy files found",
                    message,
                    error=True,
                )

            return 1

        print(f"Scanning: {scan_root}")
        print(f"Found {len(files)} .rpy files...")

        analyzer = RenPyAnalyzer(scan_root)
        results = analyzer.analyze()

        # If double-clicked, write next to the folder the user selected.
        # If CLI path is provided, default relative output goes inside scan root.
        output_root = selected if gui_mode else scan_root

        report_path = Path(args.report)

        if not report_path.is_absolute():
            report_path = output_root / report_path

        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            build_text_report(results),
            encoding="utf-8",
        )

        json_path: Optional[Path] = None

        if args.json:
            json_path = Path(args.json_file)

            if not json_path.is_absolute():
                json_path = output_root / json_path

            json_path.parent.mkdir(parents=True, exist_ok=True)
            json_path.write_text(
                json.dumps(
                    results,
                    indent=2,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

        print_console_summary(
            results,
            report_path,
            json_path,
        )

        if gui_mode:
            s = results["summary"]

            message = (
                "Scan complete.\n\n"
                f"Files scanned: {s['files']}\n"
                f"Labels: {s['labels']}\n"
                f"Screens: {s['screens']}\n"
                f"Unresolved labels: {s['unresolved_label_references']}\n"
                f"Unresolved screens: {s['unresolved_screen_references']}\n"
                f"Strong fall-throughs: {s['strong_fallthroughs']}\n"
                f"Call-screen return paths: {s['review_fallthroughs']}\n"
                f"Uncertain compound flow: {s['uncertain_fallthroughs']}\n"
                f"Commented-out code: {s['commented_out_code_lines']}\n\n"
                f"Report written to:\n{report_path}"
            )

            show_message(
                "Ren'Py Archaeologist v3 finished",
                message,
            )

        return 0

    except Exception:
        error_text = traceback.format_exc()
        print(error_text, file=sys.stderr)

        candidates: list[Path] = []

        if selected is not None:
            candidates.append(
                selected / "renpy_archaeologist_error.txt"
            )

        candidates.append(
            Path.cwd() / "renpy_archaeologist_error.txt"
        )

        candidates.append(
            Path(__file__).resolve().parent
            / "renpy_archaeologist_error.txt"
        )

        error_path: Optional[Path] = None

        for candidate in candidates:
            try:
                candidate.write_text(
                    error_text,
                    encoding="utf-8",
                )
                error_path = candidate
                break
            except Exception:
                continue

        message = "The analyzer crashed.\n\n"

        if error_path:
            message += (
                f"Crash log written to:\n{error_path}\n\n"
            )

        message += error_text[-2500:]

        if gui_mode:
            show_message(
                "Ren'Py Archaeologist v3 crashed",
                message,
                error=True,
            )
        else:
            print(message, file=sys.stderr)

        return 1


if __name__ == "__main__":
    raise SystemExit(main())
