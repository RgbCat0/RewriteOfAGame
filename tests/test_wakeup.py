"""Run with python -m unittest discover -s tests -v (no Ren'Py UI needed)."""
from pathlib import Path
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "game/systems/wakeup.rpy").read_text(encoding="utf-8")
CODE = textwrap.dedent(SOURCE.split("init python:\n", 1)[1])


class WakeupTests(unittest.TestCase):
    def target(self, **changes):
        state = dict(whereami="playerRoom", timeofday="Morning", amountspent=0,
                     ashleychecker=0, watchcount=1, miaphase2interaction2=0,
                     currentchapter=1, dayNumber=1, miaphase1interaction2=0,
                     avaphase2interaction1=0, avadaycheck=1,
                     charlottephase2interaction2=0)
        state.update(changes)
        exec(compile(CODE, "wakeup.rpy", "exec"), state)
        before = {k: v for k, v in state.items() if not k.startswith("__")}
        result = state["special_wakeup_target"]()
        self.assertEqual(before, {k: v for k, v in state.items() if not k.startswith("__")})
        return result

    def test_idle_morning_has_no_scene(self):
        self.assertIsNone(self.target())

    def test_charlotte_requires_pending_state(self):
        self.assertEqual(self.target(charlottephase2interaction2=2), "charlottephase2interaction2part1")
        for phase in (0, 1, 3, 4):
            with self.subTest(phase=phase):
                self.assertIsNone(self.target(charlottephase2interaction2=phase))

    def test_ashley_requires_purchase_and_missing_watch(self):
        self.assertIsNone(self.target(amountspent=349, watchcount=0))
        self.assertIsNone(self.target(amountspent=350, watchcount=1))
        self.assertIsNone(self.target(amountspent=350, watchcount=0, ashleychecker=1))
        self.assertEqual(self.target(amountspent=350, watchcount=0), "ashleyinteraction1part1")

    def test_ava_waits_until_a_later_day(self):
        self.assertIsNone(self.target(avaphase2interaction1=1, avadaycheck=1, dayNumber=1))
        self.assertEqual(self.target(avaphase2interaction1=1, avadaycheck=1, dayNumber=2),
                         "avaphase2interaction2part1")

    def test_mia_chapter_three_threshold(self):
        self.assertIsNone(self.target(miaphase2interaction2=4, currentchapter=3, dayNumber=21))
        self.assertIsNone(self.target(miaphase2interaction2=4, currentchapter=2, dayNumber=22))
        self.assertEqual(self.target(miaphase2interaction2=4, currentchapter=3, dayNumber=22),
                         "miaphase3interaction1part1")

    def test_mia_chapter_one(self):
        self.assertEqual(self.target(miaphase1interaction2=4), "miaphase1interaction2part3wakeup")

    def test_competing_events_keep_existing_router_priority(self):
        pending = dict(amountspent=350, watchcount=0, miaphase2interaction2=4,
                       currentchapter=3, dayNumber=22, miaphase1interaction2=4,
                       avaphase2interaction1=1, charlottephase2interaction2=2)
        self.assertEqual(self.target(**pending), "ashleyinteraction1part1")
        pending["ashleychecker"] = 1
        self.assertEqual(self.target(**pending), "miaphase3interaction1part1")
        pending["miaphase2interaction2"] = 0
        self.assertEqual(self.target(**pending), "miaphase1interaction2part3wakeup")
        pending["miaphase1interaction2"] = 0
        self.assertEqual(self.target(**pending), "avaphase2interaction2part1")
        pending["avaphase2interaction1"] = 0
        self.assertEqual(self.target(**pending), "charlottephase2interaction2part1")

    def test_events_do_not_trigger_outside_morning_room(self):
        for location, time in (("playerRoom", "Night"), ("playerRoom", "Day"), ("gym", "Morning")):
            with self.subTest(location=location, time=time):
                self.assertIsNone(self.target(whereami=location, timeofday=time,
                                             charlottephase2interaction2=2,
                                             amountspent=350, watchcount=0))


if __name__ == "__main__":
    unittest.main()
