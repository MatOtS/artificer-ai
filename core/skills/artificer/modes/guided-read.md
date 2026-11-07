# Mode: Guided read

Used by the Artificer cycle in: Explore (knowledge gate) or when the user asks what some code does. Not a command: the `artificer` skill and the `/artificer-*` commands load this file when the step needs it. Log XP with `mode: guided-read`.

Follow the `learn` skill: shared rules, hint ladder, levels and progress protocol.

Target: the target given by the cycle or the user

## Setup
- If no target was given, propose 2 or 3 real candidates from the current project that fit the user's level (L1: a short pure function; L2: a whole file or module; L3: a feature spread across files). Let them pick.
- Read the target yourself first so you know the right answers. Never paste the whole code back: point to `file:line` ranges and let the user open them.
- If the code uses a construct the user may not know, wait for them to ask; do not lecture up front.

## Reading loop
Go step by step, one question per turn:
1. **Skim (top-down)**: give the user the file and line range. Ask them to look only at names, signatures, imports and tests first (beacons), then: "En una frase, ¿para qué existe este código?"
2. **Contract**: inputs (params, props, request, env), output (return, render, response) and side effects (state, DB, network, storage, logs).
3. **Flow**: ask them to describe the main path in order, then one error or edge path.
4. **Predict**: give a concrete input and ask what happens or what it returns. Choose inputs that hit a branch, a loop boundary or an error path. Confirm with the code, or with a test if one exists.
5. **Names and structure** (L2+): why is it split this way? What would they rename? What responsibility does each piece have?
6. **Change impact** (L3): "si cambiamos X, ¿qué más se rompe?". Let them search for callers; then verify with grep or codebase-memory `trace_path`.

After each answer: say what was right, what was wrong and why (with `file:line`), then move on. Use the hint ladder when they are stuck.

## XP map
Tag each of the user's answers with its attribute and award XP at close following `rpg.md` (Tagged steps, max 4 attributes):
- Primary: `reading` (skim, contract, final summary).
- `logic`: step 4 Predict.
- `tracing`: step 3 Flow (L2+) and step 6 Change impact (finding callers).
- `reviewing`: step 5 Names and structure.
- `debugging`: step 3b **How would it fail**: after the flow, ask "¿qué input o estado haría fallar esto y qué vería el usuario?".
- Block: `logic` or `data`.

## Secondary block
Include one secondary block for logic or data as defined in the `learn` skill's `rpg.md` (Secondary blocks), placed where it fits naturally, and log its XP as a separate entry.

## Close
- Ask the user to write a 3 to 5 line summary of the code as if explaining it to a teammate. Grade it: correct, missing, wrong.
- Run the progress protocol.
