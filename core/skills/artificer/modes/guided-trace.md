# Mode: Guided trace

Used by the Artificer cycle in: Explore (knowledge gate, work that crosses layers) or when the user asks how a flow works end to end. Not a command: the `artificer` skill and the `/artificer-*` commands load this file when the step needs it. Log XP with `mode: guided-trace`.

Follow the `learn` skill: shared rules, hint ladder, levels and progress protocol.

Flow to trace: the target given by the cycle or the user

## Setup
- If no flow was given, propose 2 or 3 real flows from the current project (e.g. "guardar un gasto", "login", "cargar la lista X") sized to the level: L1 one hop, L2 one layer, L3 the full round trip.
- Map the real path yourself first, silently: use codebase-memory (`search_graph`, `trace_path`) if the project is indexed, otherwise grep. Never reveal the next hop before the user tries.

## Tracing loop
1. **Entry point**: ask the user where the flow starts (component, route, event handler) and how they would find it (search for a visible text, a route, an event name). Teach the search technique if they do not know it.
2. **Each hop**, one at a time. The user states:
   - `file:function` of the hop,
   - what data comes in and in what shape,
   - what it does with it (validation, transformation, side effects),
   - what goes out and where it goes next.
   Verify against your map. Confirm, or correct with the hint ladder.
3. **Boundaries**: at each layer change (client to server, server to DB, async callbacks) ask what could fail there and how the error travels back.
4. **Return trip**: how the result gets back to the UI and what the user sees, including the error case.

## XP map
Tag each of the user's answers with its attribute and award XP at close following `rpg.md` (Tagged steps, max 4 attributes):
- Primary: `tracing` (entry point, hops, sequence diagram).
- `reading`: what each hop does with the data.
- `debugging`: step 3 Boundaries (what fails, how the error travels back).
- `data`: the DB hop and the data shape at each hop.
- Block: `data` or `logic`.

## Secondary block
Include one secondary block for data as defined in the `learn` skill's `rpg.md` (Secondary blocks), placed where it fits naturally, and log its XP as a separate entry.

## Close
- Ask the user to write the flow as a text sequence diagram, for example:
  `Button.onClick -> api.saveExpense() -> POST /expenses -> ExpenseService.create() -> db.insert -> 201 -> list refresh`
- Compare with the real path: missing hops, wrong order, hidden side effects.
- Run the progress protocol.
