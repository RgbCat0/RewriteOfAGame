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
    def test_calendar_selects_the_actual_day_and_caps_only_the_image_at_30(self):
        text = body("game/script.rpy", "displaycalender")
        expression = re.search(r"^    scene expression (.+)$", text, re.MULTILINE).group(1)
        for day, image_day in ((1, 1), (29, 29), (30, 30), (31, 30), (32, 30), (100, 30)):
            with self.subTest(day=day):
                state = {"dayNumber": day}
                self.assertEqual(eval(expression, state),
                                 "calenderdays/calender%d.png" % image_day)
                self.assertEqual(state["dayNumber"], day)
        self.assertNotIn("image currentday", text)
        self.assertNotRegex(text, r"(?m)^\s*\$ dayNumber\s*=")
        self.assertIn('if timeofday == "Night":', text)

    def test_ava_pivot_returns_and_hides_all_ava_buttons(self):
        text = body("game/script.rpy", "avaPivot")
        active = [line for line in text.splitlines()
                  if line.strip() and not line.lstrip().startswith("#")]
        self.assertEqual(active[-1], "    jump returnwhereyouare")
        for screen in ("ava_atschool", "ava_atschoolhallway", "ava_atgym"):
            self.assertLess(text.index("hide screen " + screen), text.index("player \""))

    def test_no_jump_remains_to_the_eight_removed_or_undefined_routes(self):
        targets = ("avaphase2whereshouldwemeetagain", "avaphase2interaction1part3",
                   "avaphase1interaction2part2", "avaseemsfocused",
                   "avaphase1interaction2part3", "avaphase2interaction1part2",
                   "avaphase2whereshouldwemeetagain2", "miaphase2interaction3part1")
        for path in (ROOT / "game").rglob("*.rpy"):
            text = path.read_text(encoding="utf-8-sig")
            for target in targets:
                self.assertNotRegex(text, r"(?m)^\s*jump " + target + r"\s*$")

    def test_mia_night_call_does_not_start_or_advance_the_morning_scene(self):
        text = body("game/script.rpy", "miaPivot")
        branch = text.split('            if miaphase2interaction2 == 5:', 1)[1].split(
            '\n        else:', 1)[0]
        self.assertIn('if currentchapter == 3 and miaphase3interaction1 == 1:', branch)
        self.assertIn('player "I should visit Mia in her room in the morning."', branch)
        self.assertTrue(branch.rstrip().endswith("jump returnwhereyouare"))
        self.assertNotIn("$ ", branch)
        self.assertNotIn("jump miaphase3interaction1part2", branch)
        room = body("game/script.rpy", "gfroom1")
        self.assertIn('if miaphase3interaction1 == 1 and timeofday == "Morning" and currentchapter == 3:', room)
        self.assertIn("jump miaphase3interaction1part2", room)

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
