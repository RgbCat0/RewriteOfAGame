"""Guard the new-game route against silently ending after initialization."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class StartupTests(unittest.TestCase):
    def test_new_game_reaches_intro_after_initialization(self):
        labels = {}
        for path in (ROOT / "game").rglob("*.rpy"):
            if "tl" in path.relative_to(ROOT / "game").parts:
                continue
            source = path.read_text(encoding="utf-8-sig")
            matches = list(re.finditer(r"^label (\w+).*:$", source, re.MULTILINE))
            for index, match in enumerate(matches):
                end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
                labels[match.group(1)] = source[match.end():end]

        # Follow the actual unconditional entry jumps until a scene can be shown.
        visited = []
        current = "start"
        while current != "gameIntro":
            self.assertNotIn(current, visited, "Startup contains a routing loop")
            visited.append(current)
            self.assertIn(current, labels)
            statements = [line.strip() for line in labels[current].splitlines()
                          if line.strip() and not line.lstrip().startswith("#")]
            self.assertTrue(statements)
            target = re.fullmatch(r"jump (\w+)", statements[-1])
            self.assertIsNotNone(target, f"{current} ends without entering the next startup label")
            current = target.group(1)
        self.assertIn("gameIntro", labels)
        self.assertIn("definevariables", visited, "New games must initialize their state")
        self.assertRegex(labels["gameIntro"], r"(?m)^\s+scene ")


if __name__ == "__main__":
    unittest.main()
