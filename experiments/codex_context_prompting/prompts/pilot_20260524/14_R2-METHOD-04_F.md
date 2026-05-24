# Codex Task

Inspect the repository and produce a short implementation plan before editing. Do not edit files until the plan is accepted, unless the task brief explicitly allows continuation.

## Mission
Document sample exclusion criteria from analysis code.

## Context
- `scripts/filter_sample.py`: relevant to the task.
- `docs/sample.md`: relevant to the task.

## Known Signal
Filter order changes the counts.

## Constraints
- Keep changes scoped to the task.
- Preserve raw data and do not expose sensitive records.
- Use existing repository patterns.

## Allowed Actions
- Read relevant repository files.
- Edit only files needed for the task.
- Run the validation command or rubric.

## Forbidden Without Approval
- Delete files or reset repository state.
- Install dependencies, publish outputs, or call external services.
- Use protected or unidentified raw data.

## Done When
- [ ] Each exclusion is listed.
- [ ] The order of filters is preserved.
- [ ] Verification passes: `Human rubric review.`

## Escalate If
- Requirements conflict or acceptance criteria are not verifiable.
- The task requires a forbidden action.
- Data provenance or privacy status is unclear.

## Final Response
Report changed files, validation commands/results, assumptions, limitations, and residual risks.
