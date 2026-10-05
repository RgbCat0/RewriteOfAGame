# Session 1 results and repairs

Reported by the owner on 2026-10-05. All six page-3 save files are present and
their archive metadata is readable. Saves were inspected read-only; the outcomes
below are the owner's playtest results, not independently replayed outcomes.

## Save checkpoints

| Page 3 slot | File | Reported checkpoint / result |
| --- | --- | --- |
| 1 | `3-1-LT1.save` | Immediately after the introduction |
| 2 | `3-2-LT1.save` | Sophia's chapter-1 content complete; some Ava, Mia and other opening content |
| 3 | `3-3-LT1.save` | Day 10, beginning the track meet |
| 4 | `3-4-LT1.save` | Sophia Romantic ending and first chapter-2 story work as intended |
| 5 | `3-5-LT1.save` | Sophia Naughty ending and first chapter-2 story work as intended |
| 6 | `3-6-LT1.save` | Nobody ending and first chapter-2 Sophia story work as intended |

## Ten reported notes

| Note | Repair / decision | Needs in-game confirmation |
| --- | --- | --- |
| 1 | Sophia's first home visit now requires **Day**, both in the house router and at the scene entry. | Morning/Night denied; Day proceeds. |
| 2 | The say screen draws above character/navigation buttons. `testing screenshots/error 1.png` confirms the previous overlap. | Sophia's overlay no longer covers dialogue. |
| 3 | Both maps check opening hours before jumping: mall and gym are blocked at Night. Direct-entry checks also run before location changes. | Map remains visible when a closed destination is clicked. |
| 4 | Sophia's invited home visit now requires **Day**, including direct scene entry. | Morning/Night denied; Day proceeds. |
| 5 | After buying the gym pass, repeat machine clicks refer to the unpleasant experience rather than discovering a strange machine again. Before purchase, the original discovery line remains. | Completed interaction displays the new reminder. |
| 6 | Added a final unconditional return to Mia's pivot. An unmatched bedroom/time combination cannot continue into Olivia's pivot. | Contacting Mia in Morning/Day never unexpectedly contacts Olivia. |
| 7 | Mia's invitation-by-phone exchange now uses `{cps=25}` consistently; damaged apostrophes in that exchange were corrected. | Four phone lines have the same pacing as nearby messages. |
| 8 | Gym and school map buttons now use the same story-travel checks as the mall. Checks run before showing a location background. | During the pickup requirement, no gym entrance or school flash. |
| 9 | Club, cafe and apartment map buttons obey the pickup and office requirements; the office and map transitions remain accessible. | Cannot enter unrelated Sunnyside locations while the requirement is active. |
| 10 | Sophia's chapter-1 ending sequence now uses the declared player character instead of a black inline speaker name; Sophia's red body-text overrides were removed. Character-name colors remain those of the normal character definitions. | Normal player name and dialogue styling in both endings. |

Map denials show the player's normal dialogue using the existing travel-reminder
text, then return to the same map without entering the destination. Map buttons
are hidden during that dialogue. The reminder uses a defaulted temporary string;
no quest progress or migration is introduced.

## Follow-up retest reported by the owner

All ten original problems were reported fixed. Notes 1, 4, 5, 7 and 10 need no
further changes from that retest. Three refinements were requested and implemented:

- Notes 3, 8 and 9: replace map notifications with normal player dialogue followed
  by a return to the current map.
- Note 2: hide the Mia/Sophia school buttons when their pivots begin, including
  Sophia's short classroom reminder. This prevents clicking another character
  during these lines.
- Note 6: the Mia fallback now repeats the existing nighttime/bedroom reminder
  for the blocked texting step. Other unmatched states show the same no-reason-to-
  call line used elsewhere before returning.

The owner subsequently confirmed all three refinements work. The session-1
repair batch is complete. Twenty automated tests pass; chapters 2 and 3 remain
later playtest sessions.

## Focused retest — no need to replay everything

Close and reopen the game to load the changes.

1. Use slot 1, or another save before Sophia's visits, to check the two Day-only
   visits. Save just before each visit and reload for Morning/Day/Night variations.
   Slot 2 is already past those scenes, so it cannot test their entry restrictions.
2. Use a relevant chapter-1 save to contact Mia from the bedroom at Morning/Day
   and to check the dialogue overlay. If it no longer has the original situation,
   report that rather than replaying unrelated content to recreate it.
3. Use a save after the gym-pass purchase to click the machine again. At Night,
   click mall/gym on the map and check that neither entrance appears.
4. Use slot 3 to replay Sophia's ending choices and inspect the text colors.
   Save before Romantic/Naughty if you can, so each can be repeated quickly.
5. Check both maps while the chapter-2 pickup requirement is still active. Slots
   4–6 may be after it clears; if so, start with the built-in chapter-2 skip and
   test during the opening story's pickup stage. Check gym/school/mall and
   cafe/club/apartments; the office must remain reachable.

The focused retest is complete according to the owner's confirmation. Full
chapters 2 and 3 remain later sessions; compilation and automated checks are not
a complete game playthrough.
