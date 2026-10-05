"""Exercise the production travel rules without opening the game."""
from pathlib import Path
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
CODE = textwrap.dedent((ROOT / "game/systems/travel.rpy").read_text(
    encoding="utf-8").split("init python:\n", 1)[1].split("\ndefault ", 1)[0])
MAIN = ("library", "school", "outsidegym", "gfhouse", "park",
        "playerlivingroom", "sophiahouse", "arcade", "charlotteshouse", "malllabel")
SUNNYSIDE = ("insidecafe", "insideclub", "apartmentlobbymenu", "beach")


class TravelTests(unittest.TestCase):
    def scope(self, **changes):
        state = dict(headtosunnyside=0, headtooffice=0, timeofday="Day",
                     SetVariable=lambda name, value: ("set", name, value),
                     Jump=lambda value: ("jump", value))
        state.update(changes)
        exec(compile(CODE, "travel.rpy", "exec"), state)
        return state

    def test_normal_day_preserves_destinations(self):
        s = self.scope()
        for target in MAIN + SUNNYSIDE + ("outsideoffice",):
            with self.subTest(target=target):
                self.assertEqual(s["map_destination_action"](target), ("jump", target))

    def test_night_blocks_mall_and_gym_but_keeps_club_available(self):
        s = self.scope(timeofday="Night")
        for target in ("malllabel", "mallstore", "outsidegym", "gym", "school"):
            with self.subTest(target=target):
                action = s["map_destination_action"](target)
                self.assertEqual(action[0][0:2], ("set", "_map_travel_message"))
                self.assertEqual(action[1], ("jump", "map_travel_denied"))
        for target in ("insideclub", "insidecafe", "apartmentlobbymenu"):
            self.assertEqual(s["map_destination_action"](target), ("jump", target))

    def test_pickup_blocks_both_maps_without_changing_state(self):
        s = self.scope(headtosunnyside=1)
        before = (s["headtosunnyside"], s["headtooffice"], s["timeofday"])
        for target in MAIN + SUNNYSIDE:
            with self.subTest(target=target):
                action = s["map_destination_action"](target)
                self.assertEqual(action[1], ("jump", "map_travel_denied"))
                self.assertIn("Mia and Katie", action[0][2])
        for target in ("overworldmap", "gotosunnyside", "outsideoffice"):
            self.assertEqual(s["map_destination_action"](target), ("jump", target))
        self.assertEqual(before, (s["headtosunnyside"], s["headtooffice"], s["timeofday"]))

    def test_office_requirement_blocks_both_maps(self):
        s = self.scope(headtooffice=1)
        for target in MAIN + SUNNYSIDE:
            with self.subTest(target=target):
                self.assertIn("office building", s["map_entry_block_reason"](target))
        self.assertIsNone(s["map_entry_block_reason"]("outsideoffice"))

    def test_pickup_takes_priority_over_closing_hours(self):
        s = self.scope(headtosunnyside=1, timeofday="Night")
        self.assertIn("Mia and Katie", s["map_entry_block_reason"]("malllabel"))


if __name__ == "__main__":
    unittest.main()
