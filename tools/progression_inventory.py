"""Record static progression evidence; this does not interpret Ren'Py control flow.

Run from any directory. --check verifies that the checked-in inventory is current.
No dialogue is exported except objective assignments and conditional menu lines.
"""
from collections import defaultdict
import argparse
import io
import json
from pathlib import Path
import re
import tokenize


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/analysis/progression.json"
LABEL = re.compile(r"^\s*label\s+(\w+)\s*(?:\([^\n]*\))?\s*:")
JUMP = re.compile(r"^\s*(?:jump|call)\s+(\w+)\b|\b(?:Jump|Call)\(\s*[\"'](\w+)[\"']")
ASSIGN = re.compile(r"^\s*(?:\$\s*|default\s+)(\w+)\s*(?:=(?!=)|\+=|-=)")
GUARD = re.compile(r"^\s*(?:if|elif)\s+|^\s*[\"'].*\sif\s")


def without_comment(line):
    # Do not mistake color codes inside strings for comments.
    try:
        for token in tokenize.generate_tokens(io.StringIO(line).readline):
            if token.type == tokenize.COMMENT:
                return line[:token.start[1]]
    except (tokenize.TokenError, IndentationError):
        pass  # A single line may be part of a multiline Ren'Py expression.
    return line


def inventory():
    records = []
    incoming = defaultdict(list)
    duplicates = []
    definitions = set()
    for path in sorted((ROOT / "game").rglob("*.rpy")):
        # Translations repeat dialogue/labels and are not progression definitions.
        if "tl" in path.relative_to(ROOT / "game").parts:
            continue
        relative = path.relative_to(ROOT).as_posix()
        current = None
        for number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            match = LABEL.match(line)
            if match and match.group(1) != "_":
                name = match.group(1)
                if name in definitions:
                    duplicates.append({"label": name, "file": relative, "line": number})
                definitions.add(name)
                current = dict(label=name, file=relative, line=number,
                               assignments=[], conditions=[], outgoing=[])
                records.append(current)
            source = dict(file=relative, line=number, source=stripped)
            if current is not None:
                assign = ASSIGN.match(line)
                if assign and not assign.group(1).endswith("Sprite"):
                    current["assignments"].append(source)
                if GUARD.match(line):
                    current["conditions"].append(source)
            # Include screen actions before any label as inbound entry evidence.
            for target in JUMP.finditer(without_comment(line)):
                name = target.group(1) or target.group(2)
                if name in ("expression", "screen"):
                    continue
                reference = dict(source, target=name)
                incoming[name].append(source)
                if current is not None:
                    current["outgoing"].append(reference)
    for record in records:
        record["incoming"] = incoming.get(record["label"], [])
    return dict(
        format_version=1,
        limitation="Static evidence only. Conditions are not a verified eligibility expression; nested labels, fall-through, Python blocks and expression jumps need manual review.",
        labels=records,
        duplicate_definitions=duplicates,
        unresolved_targets={k: v for k, v in sorted(incoming.items()) if k not in definitions},
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = inventory()
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            parser.exit(1, "Progression inventory is stale; run tools/progression_inventory.py.\n")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"{'Verified' if args.check else 'Recorded'} {len(result['labels'])} labels; "
          f"{len(result['duplicate_definitions'])} duplicate definitions; "
          f"{len(result['unresolved_targets'])} unresolved static targets.")


if __name__ == "__main__":
    main()
