# Sophia chapter 1: current behavior and replacement boundary

This is a source-derived map of existing behavior, not a new quest implementation.
The owner chose to leave replacement pending. Scene names and numeric states below
are preserved. Following session 1, the owner confirmed that both chapter-1 home
visits must occur during **Day**; those entry restrictions are now implemented.

## Saved state and entry dependencies

`sophiaphase1interaction1` starts at 0 and advances through 1, 2, 3, 4, 5.
`sophiaphase1interaction2` starts at 0, advances through 1 and 2 in chapter 1,
and becomes 3 in later progression or the chapter-2 skip preset.
`sophiaphase1interaction3` and `Sophia_endchapter1_trigger` are initialized but
have no further references in the current .rpy sources; retain until reviewed.

Mia's first school conversation sets `sophiaquesticon` to the active icon.
Classroom visibility also depends on Mia's progress: the normal Sophia button
appears in the morning when `miaphase1interaction1 >= 1` and Sophia's chapter 2
interaction has not started. Do not make her initial event automatically
available at every location merely because her state is 0.

## Main progression

| Proposed descriptive step | Existing state | Actual entry / restrictions | Scene and resulting state |
| --- | --- | --- | --- |
| Meet at school | interaction1 = 0 | Click Sophia via her available school screen; `sophiaPivot` itself has no location/time guard on this branch | `sophiaphase1interaction1part1` sets interaction1 = 1, suggests visiting her home, returns to classroom1 |
| Visit her home | interaction1 = 1 | Day only, enforced at the house router and scene entry. Clicking her in classroom1 instead enters `sophianottalkingtome` without advancement | `sophiaphase1interaction1part2` sets interaction1 = 2, suggests classroom, then `passtime` |
| Meet in class / park conversation | interaction1 = 2 | Enter classroom1 outside Night; automatic trigger comes after the Mia lost-phone classroom blocker | `sophiaphase1interaction1part3` sets interaction1 = 3, suggests sleep, then `passtime` |
| Sleep / wakeup scene | interaction1 = 3 | `gotosleep` at Night, after earlier Katie and Emily sleep events. This is separate from `specialwakeup` | `sophiaphase1interaction1part4` sets interaction1 = 4 and jumps back to `gotosleep`, which performs normal sleep advancement |
| Ask about visiting | interaction1 = 4 | Click Sophia when her screen is available; pivot resets interaction2 = 0 and sets interaction1 = 5 before entering the scene | `sophiaphase1interaction2part1` sets interaction2 = 1, suggests a home visit, returns to current location |
| Visit for lunch | interaction1 = 5, interaction2 = 1 | Day only, enforced at the house router and scene entry. Clicking in classroom1 only enters `cantwaitforvisitsophia` | `sophiaphase1interaction2part2` sets interaction2 = 2, waits for other activities in chapter 1, then `passtime` |
| Ready for track-meet choice | interaction2 = 2 | Sleep reaches dayNumber = 10 and triggers `phase1ending`. Sophia is one option alongside other eligible characters; Nobody remains available | Menu writes `esch1_choice = "sophia"`, shared routing jumps to `gohomesophia` |
| Chapter-ending choice | `esch1_choice = "sophia"` | `gohomesophia` leads to Romantic / Naughty choices; no inventory or money gate is present | `sophiachapter1rom` or `sophiachapter1naughty` writes `endchapter1_trigger = "1 sophia romantic"` or `"1 sophia naughty"`, then `startofchapter2` |

The descriptive step column is vocabulary for the future pilot, not saved keys.

## Shared routing and clock details

- `startofchapter2` sets chapter = 2, adds one to dayNumber, performs other
  characters' updates, and enters `continuegamechapter2`.
- Choosing somebody else at the track meet does not erase Sophia's completed
  interactions. Her chapter 2 home/classroom trigger requires chapter = 2,
  interaction2 > 1, and chapter 2 interaction1 = 0.
- `skiptochapter2` sets Sophia's interaction1 = 5 and interaction2 = 3, activates
  her icon and hint, and sets dayNumber = 10. The Sophia preset offers both ending
  choices. Nobody routes through the shared `esch1_check`.
- `passtime` advances Morning -> Day -> Night -> Morning and advances weekday at
  night, but normally does **not** increment dayNumber. `gotosleep` increments
  dayNumber at night and checks the chapter boundaries. There is a special
  day-24 exception in `passtime`. This difference affects waits across the game.
- The classroom lost-phone branch (`miaphase1interaction3 == 4`) runs before the
  automatic Sophia state-2 scene. Future blocker hints must reflect its priority.
- Sophia's first sleep scene can be delayed by earlier Katie/Emily events. The
  pilot must retain event priority and test re-entry instead of silently skipping
  those scenes.

## Questions to resolve before replacing routing

1. First home visit: resolved by the owner in session 1 — **Day only**, implemented.
2. Invited home visit: resolved by the owner in session 1 — **Day only**, implemented.
   Some existing dialogue still describes evening/night; review that wording later
   without changing the agreed entry rule.
3. `sophiaPivot` can send state 2 directly to part4 from classroom1, bypassing
   part3. The automatic classroom entry usually preempts this, but the branch is
   still present. Remove or reroute only after deciding whether a bypass is intended.
4. Decide whether the two clock helpers intentionally count days differently.
5. Decide whether day-10 endings should remain time-limited even when a route is
   incomplete. Do not make every route mandatory without a story decision.

Questions 3–5 remain preserved behavior questions; the two visit restrictions
are the explicit changes made after session 1.

## Future objective and blocker contract

After compatibility and timing decisions, Sophia is the first pilot. Quest
definitions describe steps, conditions, scene labels and objective text; saved
progress uses named steps in a Ren'Py rollback-compatible store. There must be
one authority for advancement, not two independently maintained progress sets.

The screen should show the next objective plus known blockers: available time,
location, earlier shared event, or relevant character/activity. It should not
reveal future scenes. Scene availability and blocker text must share conditions.
Existing choices and routing priority remain intact unless the owner explicitly
changes the behavior questions above.

## Save-compatibility assessment (decision pending)

- Sophia's main progress can mostly be inferred from the two interaction flags;
  the ending choice must also read `endchapter1_trigger`. The chapter-2 preset
  uses a different completed value than natural chapter-1 completion.
- Mid-scene saves may contain a state written before the scene finished (the
  pivot writes interaction1 = 5 before the invitation). Migration must distinguish
  persisted progress from the current saved execution position.
- Existing saves also carry choices, day/time, inventory, other routes, return
  stacks and statement positions. Moving source files does not prove these saves
  load correctly. Engine-managed compiled statement identities need real tests.
- A fresh-save requirement simplifies replacement, but still needs fresh-start,
  chapter-skip and rollback checks. Preservation requires fixture saves at each
  step, mid-scene and chapter boundary, migration that does not run repeatedly,
  and testing of load/rollback plus unaffected routes.
- No migration is implemented and no existing-save compatibility is claimed.

See [the acceptance checklist](../playtest.md) before implementing the pilot.
