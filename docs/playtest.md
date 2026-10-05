# What to playtest next

**Session 1 has been played.** See [the reported results and focused retest](playtest-session-1.md)
for the ten repairs. The original instructions below remain the baseline for
future fresh playthroughs; you do not need to repeat the whole session now.

**For the first pass: start a new game, play chapter 1 with Sophia as your main
focus, and stop after entering chapter 2 and checking her first follow-up
conversation.** You do not need to finish chapters 2 and 3 or complete every
character's route now.

Later sessions cover the remaining changes. Completing this first pass does not
mean all the moved chapter 3 content has been tested.

## Which saves should I use?

| Starting point | Use it for |
| --- | --- |
| **New Game**, without skipping chapter 1 | The main playthrough below. This checks initialization and natural progression. |
| Saves created during that new playthrough | Retrying choices, visit times, and save/load. No need to restart the whole game for every variation. |
| **New Game**, then the built-in chapter-2 skip | The separate skip-menu checks. This does not replace the natural chapter-1 playthrough. |
| Saves from before these changes | Optional later investigation. Old-save compatibility has not been verified, so these are not the baseline for this test. |

Keep your older saves and use separate slots for this run. **A new game means
choosing New Game from the menu**, not loading an old save and saving it again.

## Session 1 — the main test to do now

**Start:** New Game; choose not to skip chapter 1.

**Play:** Chapter 1, focusing on Sophia. Play other characters' scenes when needed
to unlock her conversations or advance the story; do not exhaust all their routes.

**Stop:** Reach chapter 2 and check Sophia's first follow-up conversation. Stop
after that conversation, or report the point where you got stuck.

### Start and navigation

- [x ] Enter a name, finish introductions, and reach normal room/map navigation.
- [x ] Save here: **Start of chapter 1**.
- [ x] Visit available locations as they unlock. Check that you can enter and leave. Note: Start chapter 1 everything works as intented
- [x ] Open and close quests, inventory, and phone. Check the return location and
  that navigation buttons still work.
- [x ] At the gym, open those menus in Morning and Day when possible. The background
  should remain visible without an image error.
- [ x] If an arcade visit has no available event, check that you return to the map
  rather than Charlotte's house. If you cannot reach that situation, mark it
  **not reached** and continue.
- [ x] Visit Charlotte's house when available and check that navigation returns
  you to the expected place.

### Follow Sophia's chapter-1 route

Follow the game's hints through this sequence:

1. Meet Sophia at school after Mia's opening school interaction. Works
2. Visit Sophia at her home. Works, note 1
3. Return to class for the conversation that leads to the park. Works
4. Go to sleep at night for her wakeup scene. Works
5. Talk to her again at school to receive the invitation. Works
6. Visit her home for the invited visit. Works
7. Continue playing until the day-10 track meet.

- [x ] Each scene finishes and returns to a usable location.
- [ x] Hints update after completing each step; reminder conversations do not
  replay an already completed main scene.
- [ ] On an ordinary morning, you stay in the room instead of unexpectedly
  entering Charlotte's breakfast scene. Note: Unknown entry to event
- [ ] If another character's bedtime scene plays before Sophia's, finish it and
  check that Sophia's scene can still happen afterward. Note: Did not have multiple bedtime events in playtest. Should be tested again later.
- [x ] Watch the day number and weekday. Report inconsistencies and the action
  that caused them; you do not need to diagnose the time system. Note: Works as intented
- [ ] If convenient, save before both home visits so their timing can be checked later.

**If a required scene crashes or cannot be reached, report that point. You do not
need to force your way through the rest of the chapter.**

### Test the ending using saves

- [x ] Save before choosing who to spend time with at the track meet:
  **Track meet choice**.
- [x ] Check that Sophia is available after completing her chapter-1 route.
- [x ] Choose Sophia, then save before Romantic/Naughty: **Sophia ending choice**.
- [ x] Play Romantic, reach chapter 2, and check her first follow-up conversation.
- [ x] Reload **Sophia ending choice** and repeat with Naughty.
- [x ] Reload **Track meet choice**, choose Nobody or another available character,
  and check that chapter 2 begins. Stop there for this alternative.

You do not need to replay the entire chapter for these choices.

### Save/load and rollback during the run

- [ ] Reload a save from before a Sophia scene and one from after it. Check
  progress, hints, location, and inventory.
- [ ] Try normal rollback around one conversation or choice where allowed. Check
  that continuing again does not duplicate an event or lose progress.

**Session 1 is finished when both Sophia endings have reached chapter 2, one
alternative track-meet choice has reached chapter 2, and you have reported any
problems.** A blocked step is a reported blocker, not a passed test.

## Session 2 — short variations, after the main run

### Home-visit timing

**Start:** Saves from before Sophia's first home visit and invited visit.
If you did not make those saves, leave this for later; do not replay chapter 1
just to obtain them now.

- [ ] Reload and try the first home visit in Morning, Day, and Night. Record when
  she is available.
- [ ] Repeat for the invited visit. Record whether the hint agrees with the time.

Stop after each visit. These observations help us decide intended timing; a
surprising result is not automatically a new bug caused by extraction.

### Chapter-2 skip menu

**Start:** New Game, choose to skip to chapter 2. Save before choosing a character
if the menu allows it; otherwise start a new game for each variation.

**Stop:** After reaching chapter 2 and checking normal navigation and Sophia's
first available conversation. Do not play the entire chapter.

- [ x] Try Sophia -> Romantic.
- [ x] Reload the skip-choice save, or restart, and try Sophia -> Naughty.
- [ x] Repeat for Nobody; check that chapter 2 starts and the map/menus work.
- [ x] Check the chapter/day display, hints, and phone contacts in each variation.

Other characters' skip presets can be checked in a later batch.

## Later — chapter 2 wakeups and moved chapter 3 scenes

These are needed for a complete review, but **not part of your first chapter-1
test**.

**Start:** Continue saves made on this build, or start with a fresh chapter-2 skip
and progress the relevant routes. The skip menu does not take you straight to
chapter 3; you must progress chapter 2 to reach it.

**Play:** Enough of each route to reach its target event. This may mean substantial
parts of chapters 2 and 3 across several saves. One Sophia-focused run will not
unlock all the scenes.

**Stop:** After the target scene finishes; check its next hint, return location,
and save/load. Do not replay unrelated routes for every individual check.

| Target | What to check |
| --- | --- |
| Charlotte's chapter-2 breakfast/wakeup | It plays when due and does not repeat after completion. |
| Ava's scheduled wakeup | It waits for a later day instead of happening immediately on the day it was arranged. |
| Ashley's spending/watch event | It happens when the spending requirement is met and the watch is missing; it does not repeat after completion. |
| Sophia, Emily, Charlotte, Ava, Mia, Katie, and Olivia's solo chapter-3 scenes | They start through normal gameplay, finish, update their hints, and return correctly. Include Charlotte's continuation scene. |
| Julia's conversations when Mia is unavailable | They return to the house/current location normally. |
| Shared chapter endings and chapter-3 sleepover | Choices still reach the correct scenes after extraction. |

Save before each target so you can reproduce a problem. If a missing scene or
image blocks a route, report it and pause that route. The build still has known
unresolved route and asset issues.

## Developer-assisted checks — not homework for you

Exact spending boundaries, several wakeups pending at once, specific internal
progress flags, the lost-phone blocker at a particular Sophia step, and reaching
day 10 with Sophia incomplete need prepared situations. Do not edit variables
or spend hours arranging these combinations. We can use prepared saves later;
the wakeup selector already has automated checks.

Old-save migration tests remain deferred until we decide compatibility.

## What to send back

A short note per problem is enough:

```text
Session: 1 / Sophia first home visit
Starting point: New game on this build; loaded my "Before home visit" save
Chapter / day / time: Chapter 1 / day 3 / Day
What I did: Visited Sophia's house
What happened: ...
What I expected: ...
Can I reproduce it by loading that save? Yes / No
```

Include error text if there is any. Mark checks you could not reach as **not
reached**, rather than passed. Only outcomes explicitly reported in the session
results count as manually verified; the remaining checks are pending.
