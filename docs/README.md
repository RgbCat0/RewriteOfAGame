# Rewrite checkpoint

This checkpoint preserves the existing story and implements the extraction review,
remaining solo-scene extraction, and confirmed repairs. The quest replacement is
**pending**, following the owner's decision on 2026-10-05. No save migration or new
quest progress format has been introduced.

## Work completed

- Reviewed the eight original modified files against HEAD: 355 top-level labels
  before and after, seven moved labels, no lost labels or changed executable scene
  content. The only behavior differences were the owner's Charlotte assignment
  and pivot fallback fixes; both are preserved.
- Moved eight additional scene groups without changing their executable-line
  inventory: Sophia, Emily, Charlotte (including `continuebooboconvo`), Ava, Mia,
  Katie, Olivia, and Julia's household conversation helpers.
- Retained shared introductions, skip presets, chapter endings, the chapter 3
  sleepover and its branching scenes, office group events, and the bullies event
  in `gameDialogues.rpy`. These are intentionally shared, not missed extraction.
- Made room entry and special wakeup use one eligibility function. Charlotte
  requires pending state 2; Ava requires a later day; Ashley requires the missing
  watch. Existing router priority is Ashley, chapter 3 Mia, chapter 1 Mia, Ava,
  Charlotte. An idle router returns to the current location.
- Fixed the arcade's unhandled-path fall-through into Charlotte's house; it now
  returns to the overworld map.
- Fixed Ava's comparison used as initialization, the invalid unreachable
  `startgame` jump after character declarations, `uppgui`, seven mismatched text
  tags, invalid `[povname!!!]` interpolation, undefined gym/mall background names,
  and the verified `Sprite/juliatalk.png` directory typo.
- Fixed the missing transition after variable initialization: Start now follows
  `start -> definevariables -> gameIntro` instead of returning to the main menu.
- The owner also moved Mia's remaining `sleepwithmia` ending into her character
  file. Its executable content is preserved and it has one definition. Character
  extraction and the session-1 repair batch are complete; the owner confirmed the
  final dialogue, overlay and routing refinements work.

## Checks and remaining work

- Twenty automated regression tests pass, covering startup, wakeup eligibility
  and priority, travel restrictions, Sophia visit guards and Mia's routing boundary.
- Ren'Py forced compilation and lint run successfully. **Lint still reports
  existing missing route targets and assets**; successful command execution does
  not mean a warning-free or fully playable game.
- Extraction checks establish source preservation, not successful playthroughs.
  The owner completed session 1 and reported successful Romantic, Naughty and
  Nobody transitions into chapter 2. See [the results and focused retest](playtest-session-1.md).
  Save/load and rollback coverage is not yet confirmed.

See [Sophia's progression map](progression/sophia-chapter-1.md),
[open issues](issues.md), [manual acceptance checks](playtest.md), and the current
[static analysis](analysis/current.txt) and [Ren'Py lint](analysis/renpy-lint.txt).
The [progression inventory](analysis/progression.json) records source evidence for
all characters; it is not a verified interpretation of every route.

## Next batches

1. Playtest this checkpoint and resolve the missing Ava/Mia route targets with
   recovered source or confirmed story intent. Do not guess replacements by name.
2. Review the clock differences, Sophia timing and blocker questions in the map.
3. Choose old-save compatibility after reviewing the migration assessment.
4. Implement and playtest Sophia chapter 1 as the first quest-system pilot.
5. Map and convert subsequent routes in reviewed batches; proofread each route
   once its gameplay checks no longer depend on the displayed quest text.

## Reproduce checks

From the repository root:

```powershell
python -m unittest discover -s tests -v
python tools/progression_inventory.py
python tools/progression_inventory.py --check
python renpy_archaeologist_v3.py game --report ../docs/analysis/current.txt --json --json-file ../docs/analysis/current.json
.\lib\py3-windows-x86_64\python.exe MyGirlfriendsFriends.py . lint --compile --compile-python
```

The inventory and archaeology commands write documentation reports. Ren'Py
validation writes compiled caches and may initialize its application-data save
security keys. Neither validation command performs an interactive playtest.
