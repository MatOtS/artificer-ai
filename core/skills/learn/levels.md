# Learn levels

| Level | Scope | Reading | Tracing | Reviewing |
|---|---|---|---|---|
| L1 | One function or component | Purpose, inputs, output, one prediction | One hop: caller to callee | Spot naming and obvious bugs in a small diff |
| L2 | One file or module | Responsibilities, dependencies, side effects, error paths | One feature inside one layer (e.g. UI only, API only) | Correctness, edge cases, tests in a medium diff |
| L3 | One feature across files and layers | Design intent, trade-offs, what would break if changed | Full request: UI, API, service, DB and back | Architecture, coupling, security, missing tests |

Which scope to use comes from the attribute level in `character.json`: Lv 1-3 → L1, Lv 4-6 → L2, Lv 7-10 → L3. Attribute levels only change through trials (see `rpg.md`).

## Faded guidance
| Level | Worked examples |
|---|---|
| L1 | Before the exercise you may show a worked example of **similar** code (never the code of the exercise), then ask the user to apply the same reasoning. |
| L2 | No example up front. A partial example only after hint step 2. |
| L3 | No examples. Hints only. |

## Reading strategy (all levels)
Top-down first: names, signatures, imports, types and tests as beacons to form a hypothesis of what the code does. Then bottom-up, line by line, to confirm or correct the hypothesis.
