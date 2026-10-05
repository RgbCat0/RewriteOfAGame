"""Check route boundaries which caused session-1 playtest failures."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def body(path, label):
    text = (ROOT / path).read_text(encoding="utf-8-sig")
    match = re.search(r"^label " + re.escape(label) + r":\n", text, re.MULTILINE)
    tail = text[match.end():]
    return re.split(r"^label \w+.*:$", tail, maxsplit=1, flags=re.MULTILINE)[0]


class SceneRoutingTests(unittest.TestCase):
    def test_mia_pivot_cannot_fall_through_into_olivia(self):
        lines = [line for line in body("game/script.rpy", "miaPivot").splitlines()
                 if line.strip() and not line.lstrip().startswith("#")]
        self.assertEqual(lines[-1], "    jump returnwhereyouare")

    def test_mia_fallback_explains_the_daytime_text_requirement(self):
        text = body("game/script.rpy", "miaPivot")
        tail = text.split('    # if charlottephase1interaction2 == 2:', 1)[0]
        self.assertIn('if miaphase1interaction1 == 2 and timeofday != "Night":', tail)
        self.assertTrue(tail.rstrip().endswith('jump returnwhereyouare'))
        self.assertIn('player "I should text Mia at night in my room so I can uh...be alone."',
                      tail[-450:])

    def test_mia_dialogue_hides_school_buttons_before_speaking(self):
        text = body("game/script.rpy", "miaPivot")
        first_dialogue = text.index('player "')
        for screen in ("mia_atschool", "sophia_atschool", "mia_sophia_atschool"):
            self.assertLess(text.index("hide screen " + screen), first_dialogue)

    def test_map_denial_shows_dialogue_and_returns_without_a_scene_change(self):
        text = body("game/systems/travel.rpy", "map_travel_denied")
        self.assertIn('player "[_map_travel_message]"', text)
        self.assertTrue(text.rstrip().endswith("jump returnwhereyouare"))
        self.assertNotRegex(text, r"(?m)^\s*scene ")
        for screen in ("overworld", "overworldnight", "screen_sunnyside", "screen_sunnysidenight"):
            self.assertIn("hide screen " + screen, text)

    def test_sophia_visit_guards_precede_scene_setup(self):
        for label in ("sophiaphase1interaction1part2", "sophiaphase1interaction2part2"):
            with self.subTest(label=label):
                text = body("game/characters/sophia.rpy", label)
                condition = re.search(r'^    if (.+):$', text, re.MULTILINE).group(1)
                for time, blocked in (("Morning", True), ("Day", False), ("Night", True)):
                    self.assertEqual(eval(condition, {"timeofday": time}), blocked)
                self.assertLess(text.index("jump overworldmap"), text.index("scene "))

    def test_direct_travel_guards_precede_location_changes(self):
        for label in ("outsidegym", "gym", "school", "malllabel", "mallstore",
                      "insidecafe", "insideclub", "apartmentlobbymenu", "apartmentlobbyolivia"):
            with self.subTest(label=label):
                text = body("game/script.rpy", label)
                active = [line.strip() for line in text.splitlines() if line.strip()
                          and not line.lstrip().startswith("#")]
                self.assertTrue(active[0].startswith("if map_entry_block_reason("))


if __name__ == "__main__":
    unittest.main()
