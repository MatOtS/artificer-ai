# Map NNN: <Work item name>

Spec: `work/NNN-name/spec.md`

## Explored context
<What exists today and is relevant: files, functions, data, conventions. Knowledge gate result.>

## Change map
| File | Action (create / modify) | Functions and signatures | Scenarios |
|---|---|---|---|

## Slices
Each slice: at most 200 changed lines, in dependency order.
- [ ] **S1. <Description>.** Scenarios: <names>. Files: <files>.
  - Done when: <scenario tests green + any extra check>.
- [ ] **S2. <Description>.** Scenarios: <names>. Files: <files>.
  - Done when: <check>.

## Data
<Changes to the data model or storage and compatibility with existing data. "None" if none.>

## Decisions
Every design decision is the user's (artificer skill, Decisions belong to the human). Binding: Build stops on anything not listed here.
| Decision point | Type (one-way / reversible) | Decided | Discarded alternatives | Reason (the user's words) | Decided by |
|---|---|---|---|---|---|

Existing decisions that apply (cite, do not ask again unless the work clashes with one): <principles, ADRs, earlier maps>.
Revisited: <old decision> → `superseded by` <new decision row>, with what it affects.

## Risks
<What can go wrong and how it is mitigated. These feed the risk map in Verify.>
