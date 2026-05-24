# Codex Task

## Mission
Produce a methods note from the coverage model code.

## Context
- `src/models/coverage.py`: relevant to the task.
- `scripts/build_coverage.py`: relevant to the task.

## Known Signal
The note must not invent undocumented statistical claims.

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
- [ ] Note states data, sample, model, exclusions, assumptions, and limitations.
- [ ] Claims are supported by code references.
- [ ] Verification passes: `Human rubric review.`

## Escalate If
- Requirements conflict or acceptance criteria are not verifiable.
- The task requires a forbidden action.
- Data provenance or privacy status is unclear.

## Final Response
Report changed files, validation commands/results, assumptions, limitations, and residual risks.
