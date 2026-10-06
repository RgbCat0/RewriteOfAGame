"""Check the Ren'Py conditions and old-save hint conversion."""
from pathlib import Path
from types import SimpleNamespace
import ast
import re
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "game/systems/save_compatibility.rpy").read_text(encoding="utf-8")
LEGACY_HINTS = ast.literal_eval(SOURCE.split("define legacy_quest_hint_text = ", 1)[1].split("\ndefault ", 1)[0].strip())


def run_label(name, state):
    body = SOURCE.split("label " + name + ":", 1)[1].split("\nlabel ", 1)[0]
    lines = []
    for line in textwrap.dedent(body).splitlines():
        stripped = line.strip()
        if stripped == "return" or not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("call "):
            indent = line[:len(line) - len(line.lstrip())]
            lines.append(indent + "_run_label(" + repr(stripped.split()[1]) + ", globals())")
        else:
            lines.append(line.replace("$ ", "", 1))
    state["_run_label"] = run_label
    exec("\n".join(lines), state)


class QuestHintTests(unittest.TestCase):
    def scope(self, **changes):
        state = dict(quest_hint_version=0, currentchapter=2, dayNumber=30,
                     oliviatournyday=12, oliviaphase2interaction2=2,
                     oliviaquestlog="", charlottephase1interaction3=0,
                     charlottephase1interaction2=0, charlottephase2interaction1=0,
                     charlottephase2interaction2=0, charlottequestlog="",
                     avaphase1interaction2=0, avaphase1interaction3=0,
                     avaphase2interaction1=0, avaphase2interaction2=0, avaquestlog="",
                     avaphase2interaction3=0, avaphase3interaction1=0,
                     sophiaphase2interaction3=0, charlottephase2interaction3=0,
                     emilyphase2interaction2=0, emilyphase3interaction1=0,
                     katiephase2interaction1=0, miaphase2interaction2=0, pennyscene3=0)
        state.update(changes)
        for variable in LEGACY_HINTS:
            state.setdefault(variable, "")
        state["legacy_quest_hint_text"] = LEGACY_HINTS
        state["renpy"] = SimpleNamespace(block_rollback=lambda: None)
        return state

    def test_original_countdowns_convert_once(self):
        for text, nights in (("I gotta wait for the tournament in 2 days!", 2),
                             ("I gotta wait for the tournament tomorrow!", 1),
                             ("Olivia's tournament is tonight!", 0)):
            s = self.scope(oliviaquestlog=text)
            run_label("after_load", s)
            self.assertEqual(s["oliviatournyday"], 30 - (2 - nights))
            self.assertEqual(s["quest_hint_version"], 3)
            self.assertEqual(s["oliviaphase2interaction2"], 2)
            anchor = s["oliviatournyday"]
            s["dayNumber"] += 1
            run_label("after_load", s)
            self.assertEqual(s["oliviatournyday"], anchor)

    def test_two_nights_update_the_hint_without_changing_progress(self):
        s = self.scope(quest_hint_version=1, dayNumber=12)
        for day, expected in ((12, "two nights"), (13, "one more night"), (14, "arcade at Night")):
            s["dayNumber"] = day
            run_label("update_olivia_tournament_hint", s)
            self.assertIn(expected, s["oliviaquestlog"])
            self.assertEqual(s["oliviaphase2interaction2"], 2)
            self.assertEqual(s["oliviatournyday"], 12)
        for phase in (0, 1, 3):
            s.update(oliviaphase2interaction2=phase, oliviaquestlog="Other objective")
            run_label("update_olivia_tournament_hint", s)
            self.assertEqual(s["oliviaquestlog"], "Other objective")

    def test_inactive_completed_and_unknown_saves_keep_their_dates(self):
        for phase in (0, 1, 2, 3):
            s = self.scope(oliviaphase2interaction2=phase, oliviaquestlog="Custom hint")
            run_label("after_load", s)
            self.assertEqual(s["oliviatournyday"], 12)
            self.assertEqual(s["oliviaphase2interaction2"], phase)

    def test_charlotte_flags_refresh_old_hints(self):
        for chapter, expected in ((1, "track meet"), (2, "Cafe Seni")):
            s = self.scope(currentchapter=chapter, charlottephase1interaction3=2,
                           charlottephase1interaction2=4, charlottequestlog="Edited text")
            run_label("after_load", s)
            self.assertIn(expected, s["charlottequestlog"])
        s = self.scope(charlottephase2interaction2=4)
        run_label("after_load", s)
        self.assertIn("sleep at Night on a later day", s["charlottequestlog"])

    def test_all_legacy_hint_text_refreshes_without_advancing_quests(self):
        for variable, replacements in LEGACY_HINTS.items():
            for old, new in replacements.items():
                with self.subTest(variable=variable, old=old):
                    s = self.scope(quest_hint_version=1, oliviaphase2interaction2=0)
                    s[variable] = old
                    before = {key: value for key, value in s.items()
                              if not key.endswith("questlog") and key != "quest_hint_version"}
                    run_label("after_load", s)
                    self.assertEqual(s[variable], new)
                    for key, value in before.items():
                        self.assertEqual(s[key], value)
                    self.assertEqual(s["quest_hint_version"], 3)
                    run_label("after_load", s)
                    self.assertEqual(s[variable], new)

    def test_unknown_or_empty_hint_text_is_preserved(self):
        for text in ("", "A custom mod's objective"):
            s = self.scope(quest_hint_version=1, oliviaphase2interaction2=0)
            for variable in LEGACY_HINTS:
                s[variable] = text
            run_label("after_load", s)
            for variable in LEGACY_HINTS:
                self.assertEqual(s[variable], text)

    def test_original_ava_hint_uses_chapter_flags(self):
        old = "I feel like I'm making a real connection with Ava, I should see her at the gym again."
        for chapter, expected in ((1, "track meet"), (2, "gym during Morning")):
            s = self.scope(currentchapter=chapter, avaquestlog=old,
                           avaphase1interaction2=4, avaphase1interaction3=10)
            run_label("after_load", s)
            self.assertIn(expected, s["avaquestlog"])

    def test_mobile_hint_formatting_has_closed_size_tags(self):
        for source in (ROOT / "game").rglob("*.rpy"):
            if source.name == "save_compatibility.rpy":
                continue
            for hint in re.findall(r'\$ \w+questlog = ("[^"\n]*")', source.read_text(encoding="utf-8-sig")):
                text = ast.literal_eval(hint)
                self.assertEqual(text.count("{size="), text.count("{/size}"), (source, text))

    def test_fulfilled_dependencies_refresh_loaded_hints(self):
        s = self.scope(quest_hint_version=1, katiephase2interaction1=4,
                       miaphase2interaction2=4, pennyscene3=1)
        run_label("after_load", s)
        self.assertEqual(s["katiequestlog"], "Contact Mia on your phone to arrange a pizza party.")
        self.assertIn("Bring $50", s["pennyquestlog"])
        self.assertEqual(s["katiephase2interaction1"], 4)
        self.assertEqual(s["pennyscene3"], 1)

    def test_chapter_three_hints_do_not_overwrite_completed_scenes(self):
        s = self.scope(currentchapter=3, avaphase2interaction3=2,
                       sophiaphase2interaction3=2, charlottephase2interaction3=3,
                       emilyphase2interaction2=3)
        run_label("after_load", s)
        for variable in ("avaquestlog", "sophiaquestlog", "charlottequestlog"):
            self.assertIn("school during Morning", s[variable])
        self.assertIn("after day 21", s["emilyquestlog"])
        s = self.scope(currentchapter=3, avaphase2interaction3=2, avaphase3interaction1=2,
                       sophiaphase2interaction3=3, charlottephase2interaction3=4,
                       emilyphase2interaction2=3, emilyphase3interaction1=2)
        for variable in ("avaquestlog", "sophiaquestlog", "charlottequestlog", "emilyquestlog"):
            s[variable] = "Finished route"
        run_label("after_load", s)
        for variable in ("avaquestlog", "sophiaquestlog", "charlottequestlog", "emilyquestlog"):
            self.assertEqual(s[variable], "Finished route")

    def test_arcade_uses_progress_and_date_not_hint_wording(self):
        script = (ROOT / "game/script.rpy").read_text(encoding="utf-8-sig")
        self.assertIn("if oliviaphase2interaction2 == 2 and dayNumber >= oliviatournyday + 2:", script)
        self.assertNotRegex(script, r"(?:if|elif) .*questlog\s*==")
        self.assertIn("call update_olivia_tournament_hint", script)
        self.assertNotIn("init python:", SOURCE)
        self.assertNotIn("def ", SOURCE)

    def test_daytime_sleep_does_not_advance_the_tournament_date(self):
        script = (ROOT / "game/script.rpy").read_text(encoding="utf-8-sig")
        sleep = script.split("label gotosleep:", 1)[1].split("label explorebeach:", 1)[0]
        block = sleep.split('    scene fs playerroomDay\n', 1)[1].split('\n\n    scene fs blackblank', 1)[0]
        lines = [line for line in block.splitlines() if not line.lstrip().startswith("scene ")]
        code = textwrap.dedent("\n".join(lines)).replace("$ ", "")
        s = self.scope(dayNumber=12, dayName="Monday")
        for time in ("Morning", "Day"):
            s["timeofday"] = time
            exec(code, s)
            self.assertEqual(s["dayNumber"], 12)
        for expected_day in (13, 14):
            s["timeofday"] = "Night"
            exec(code, s)
            self.assertEqual(s["dayNumber"], expected_day)


if __name__ == "__main__":
    unittest.main()
