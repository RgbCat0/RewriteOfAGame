# Review queue

The latest generated reports contain exact current locations. Severity here is
about observed source behavior; untested runtime effects are marked explicitly.

## Confirmed defects remaining

- **Missing route targets:** seven Ava labels and `miaphase2interaction3part1`
  are referenced but have no source definitions. Both static analysis and Ren'Py
  lint confirm them. Recover the missing scenes or review the corresponding
  branch intent; similar names are not evidence for substitution.
- **Missing assets:** Ren'Py lint lists unavailable images, including older Mia
  scenes, unfinished sleepover branches, sprite variants and puzzle images.
  Determine which are missing files versus stale declarations before altering
  scenes. There is no claim that the complete game is runnable from a fresh clone:
  `.gitignore` excludes `game/images/`, while the checkout has local images.
- **Display cleanup:** `hide window`, `hide textbox`, `hide fsplayer` and
  `hide contacts` use image statements where a window/screen/tag may have been
  intended. Review with the relevant scene visible before changing these.
- **Unknown phone screen:** three `hide screen phone` references have no declared
  `phone` screen. Hiding a missing screen is not the same as jumping to a missing
  label; inspect the actual contacts/phone screens to determine what should hide.

## Behavior requiring intent or playtesting

- Sophia home/lunch timing, the state-2 classroom bypass, and sleep priority:
  [mapped in detail](progression/sophia-chapter-1.md).
- `passtime` and `gotosleep` count nights differently; the former normally changes
  weekday without changing dayNumber. Treat changing this as a gameplay change.
- Olivia's tournament countdown compares quest hint strings and advances on
  calls to `gotosleep`, even Morning/Day calls, rather than strictly two nights.
  Decide pacing and save behavior before replacing it with explicit state.
- Charlotte's chapter-2 opening compares her quest hint string. Do not proofread
  that hint until its routing dependency has been removed.
- `office -> outsideoffice` is a static-analysis false positive for the current
  exhaustive time branches: every branch jumps before the final image statement.
- `checkphone -> gotophonefromcontacts` currently continues into a blocking
  contacts screen. This continuation may be intentional; don't add `return`
  without checking jump/call semantics.
- Debug test labels continue into one another; isolate or remove in a later
  development-tools batch. Credits continue to endgame; confirm intent.
- Unreachable/commented content, old image transforms and screen parameter-list
  warnings remain cleanup work. Do not treat all scanner warnings as bugs.

## Quest-text dependencies recorded for later conversion

| Gameplay use | Current text | Required replacement before proofreading |
| --- | --- | --- |
| Charlotte chapter-2 opening | `Think I should avoid Charlotte till after the track meet.` | Check mapped Charlotte progress instead of the displayed sentence |
| Olivia tournament availability | `Olivia's tournament is tonight!` | Explicit tournament readiness |
| Olivia waiting progression | `I gotta wait for the tournament in 2 days!` / `I gotta wait for the tournament tomorrow!` | Explicit wait state with an agreed clock rule |

Those checks remain unchanged while quest replacement is pending. No bulk grammar
pass has been applied. Narrow formatting repairs are listed in the checkpoint.

## Rollout gate

The owner selected **leave quest replacement pending**. Resume only after
reviewing this checkpoint, resolving Sophia's intent questions and deciding save
compatibility. Larger route conversions and exhaustive proofreading are later
batches, not completed work in this checkpoint.
