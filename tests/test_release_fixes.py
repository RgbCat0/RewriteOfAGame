"""Exercise the date, payment and late-entry decisions in the Ren'Py source."""
from pathlib import Path
import re
import textwrap
import unittest

from test_quest_hints import run_label, LEGACY_HINTS
from test_scene_routing import body

ROOT = Path(__file__).resolve().parents[1]


class Jump(Exception):
    pass


def run_decisions(source, state):
    """Run conditions, assignments and jumps; skip presentation statements."""
    lines = []
    for line in textwrap.dedent(source).splitlines():
        command = line.strip()
        indent = line[:len(line) - len(line.lstrip())]
        if command.startswith(("if ", "elif ")) or command == "else:":
            lines.extend((line, indent + "    pass"))
        elif command.startswith("$ "):
            lines.append(indent + command[2:])
        elif command.startswith("jump "):
            lines.append(indent + "raise Jump(" + repr(command.split()[1]) + ")")
        elif command == "call update_olivia_tournament_hint":
            lines.append(indent + "_update_hint()")
    state["Jump"] = Jump
    state["_update_hint"] = lambda: run_label("update_olivia_tournament_hint", state)
    try:
        exec("\n".join(lines), state)
    except Jump as target:
        return str(target)
    return None


class ReleaseFixTests(unittest.TestCase):
    def test_passing_night_advances_date_and_weekday_once(self):
        source = body("game/script.rpy", "passtime")
        for day in (8, 9, 19, 24, 30):
            for weekday, following in (("Monday", "Tuesday"), ("Sunday", "Monday")):
                with self.subTest(day=day, weekday=weekday):
                    state = dict(dayNumber=day, dayName=weekday, timeofday="Night",
                                 currentchapter=3, oliviaphase2interaction2=0)
                    self.assertEqual(run_decisions(source, state), "overworldmap")
                    self.assertEqual(state["dayNumber"], day + 1)
                    self.assertEqual(state["dayName"], following)
                    self.assertEqual(state["timeofday"], "Morning")

    def test_daytime_passage_leaves_date_and_weekday_unchanged(self):
        source = body("game/script.rpy", "passtime")
        for current, following in (("Morning", "Day"), ("Day", "Night")):
            state = dict(dayNumber=9, dayName="Friday", timeofday=current,
                         currentchapter=1, oliviaphase2interaction2=0)
            self.assertEqual(run_decisions(source, state), "overworldmap")
            self.assertEqual((state["dayNumber"], state["dayName"]), (9, "Friday"))
            self.assertEqual(state["timeofday"], following)

    def test_night_scene_cannot_skip_the_chapter_milestones(self):
        source = body("game/script.rpy", "passtime")
        for chapter, day, target in ((1, 9, "phase1ending"), (2, 19, "phase2ending"),
                                     (2, 9, "overworldmap"), (3, 19, "overworldmap")):
            state = dict(dayNumber=day, dayName="Friday", timeofday="Night",
                         currentchapter=chapter, oliviaphase2interaction2=0)
            self.assertEqual(run_decisions(source, state), target)
            self.assertEqual(state["dayNumber"], day + 1)

    def test_night_passage_updates_olivias_existing_wait(self):
        source = body("game/script.rpy", "passtime")
        state = dict(dayNumber=12, dayName="Monday", timeofday="Night",
                     currentchapter=2, oliviaphase2interaction2=2, oliviatournyday=12)
        run_decisions(source, state)
        self.assertIn("one more night", state["oliviaquestlog"])
        state["timeofday"] = "Night"
        run_decisions(source, state)
        self.assertIn("arcade at Night", state["oliviaquestlog"])
        self.assertEqual(state["oliviatournyday"], 12)
        self.assertEqual(state["oliviaphase2interaction2"], 2)

    def test_pennys_donation_checks_and_deducts_exactly_100(self):
        stream = body("game/characters/penny.rpy", "pennythirdstream")
        selected = stream.split('        "Donate $100":\n', 1)[1].split(
            '        "Don\'t Donate":', 1)[0]
        for money in (0, 99, 100, 135):
            with self.subTest(money=money):
                state = dict(money=money, pennyscene4=1, pennyscene5=0,
                             oliviaphase2interaction3=0, pennyquestlog="Pending stream")
                self.assertEqual(run_decisions(selected, state), "gotosleep")
                if money < 100:
                    self.assertEqual(state["money"], money)
                    self.assertEqual((state["pennyscene4"], state["pennyscene5"]), (1, 0))
                    self.assertEqual(state["pennyquestlog"], "Pending stream")
                else:
                    self.assertEqual(state["money"], money - 100)
                    self.assertEqual((state["pennyscene4"], state["pennyscene5"]), (2, 1))

    def test_charlotte_late_visit_keeps_items_time_and_completion_guards(self):
        source = body("game/script.rpy", "charlotteshouse")
        base = dict(dayNumber=25, timeofday="Night", charlottephase3interaction1=0,
                    charlottephase2interaction1=2, charlottephase1interaction2=4,
                    charlottephase1interaction3=2, handcuffcount=0, condomcount=0, cameracount=0)
        for chapter, time, stage, missing, expected in (
            (2, "Night", 2, False, "charlottephase2interaction1part2"),
            (3, "Night", 2, False, "charlottephase2interaction1part2"),
            (3, "Day", 2, False, "overworldmap"),
            (3, "Night", 2, True, "overworldmap"),
            (1, "Night", 2, False, "overworldmap"),
            (3, "Night", 3, False, "victoriaPivot"),
        ):
            state = dict(base, currentchapter=chapter, timeofday=time,
                         charlottephase2interaction1=stage, cameracount=int(missing))
            self.assertEqual(run_decisions(source, state), expected)

    def test_other_late_entries_still_require_unfinished_quest_steps(self):
        cases = (
            ("gym", "avaphase1interaction3 == 10", "avaphase2interaction1",
             dict(avaphase1interaction3=10, avaphase2interaction1=0, timeofday="Morning"), 1),
            ("gfroom1", "miaphase2interaction1 == 1", "miaphase2interaction1",
             dict(miaphase2interaction1=1, miaphase1interaction3=6, timeofday="Day"), 2),
            ("sophiahouse", "sophiaphase2interaction1 == 0", "sophiaphase2interaction1",
             dict(sophiaphase2interaction1=0, sophiaphase1interaction2=2), 1),
            ("schoolhallway", "emilyphase1interaction2 >= 5", "emilyphase2interaction2",
             dict(emilyphase1interaction2=6, emilyphase2interaction1=5,
                  emilyphase2interaction2=0), 1),
        )
        for label, marker, progress, values, complete in cases:
            source = body("game/script.rpy", label)
            condition = next(line.strip()[3:-1] for line in source.splitlines()
                             if line.strip().startswith("if ") and marker in line)
            for chapter in (1, 2, 3):
                state = dict(values, currentchapter=chapter)
                self.assertEqual(eval(condition, state), chapter >= 2, (label, chapter))
                state[progress] = complete
                self.assertFalse(eval(condition, state), label)
        arcade = body("game/script.rpy", "arcade")
        self.assertIn('elif timeofday == "Day" and currentchapter >= 2:', arcade)
        self.assertIn('if oliviaphase1interaction3 == 2:', arcade)

    def test_previous_hint_revision_refreshes_without_resetting_timer(self):
        state = dict(quest_hint_version=2, legacy_quest_hint_text=LEGACY_HINTS,
                     oliviaphase2interaction2=2, oliviatournyday=28, dayNumber=30)
        for variable in LEGACY_HINTS:
            state[variable] = "Finished objective"
        state["charlottequestlog"] = (
            "Get a camera, condoms, and handcuffs from the mall store. "
            "Visit Charlotte's house at Night in chapter 2.")
        state["renpy"] = type("Renpy", (), {"block_rollback": staticmethod(lambda: None)})()
        run_label("after_load", state)
        self.assertNotIn("in chapter 2", state["charlottequestlog"])
        self.assertEqual(state["quest_hint_version"], 3)
        self.assertEqual(state["oliviatournyday"], 28)
        self.assertEqual(state["miaquestlog"], "Finished objective")


if __name__ == "__main__":
    unittest.main()
