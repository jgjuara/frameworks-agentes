# Templates: Codex Prompts for Verifiable Research Tasks

**Abstract:** This file provides reusable prompt templates for research teams using Codex on computable tasks. The templates operationalize the report's recommendation: keep prompts compact, make context explicit, define verification before execution, and require a final evidence package.

## 1. Standard Verifiable Task

~~~markdown
# Codex Task

## Mission
[Build/fix/analyze exactly what?]

## Context
- `[path]`: [why relevant]
- `[path]`: [why relevant]
- Known failure or symptom: [command/output/behavior]

## Constraints
- [Scope rule.]
- [Architecture/data/dependency rule.]

## Allowed Actions
- Read relevant repository files.
- Edit files under `[paths]`.
- Run `[commands]`.

## Forbidden Without Approval
- Modify raw data.
- Install new dependencies.
- Push commits, publish outputs, or call external services.
- Delete files or run destructive commands.

## Done When
- [ ] `[validation command]` passes.
- [ ] [Expected artifact exists or behavior changes.]
- [ ] [Assumptions and limitations are documented.]

## Escalate If
- Requirements conflict.
- Validation cannot be run.
- The task requires a forbidden action.
- Data provenance or interpretation is unclear.

## Final Response
Include changed files, validation commands/results, assumptions, limitations, and residual risks.
~~~

## 2. Research Analysis Task

~~~markdown
# Research Analysis Task

## Research Question
[Question.]

## Computable Deliverable
[Script, notebook, table, figure, model output, report section.]

## Data
- Source:
- Version/date:
- Location:
- Raw data is immutable: yes/no
- Sensitive fields:

## Methods Constraints
- Required method:
- Forbidden method:
- Robustness checks:
- Random seed:

## Relevant Files
- `[path]`: [why relevant]

## Reproducibility
Run:

```bash
[command]
```

Expected outputs:
- `[path]`

## Done When
- [ ] The analysis runs end to end.
- [ ] Outputs are reproducible from documented commands.
- [ ] The methods note states data, sample, model, exclusions, assumptions, and limitations.
- [ ] Claims are supported by generated artifacts.
- [ ] No sensitive data is copied into generated docs.

## Final Response
Map each finding to evidence, distinguish findings from interpretation, and list unresolved assumptions.
~~~

## 3. Bug Fix With Failing Test

~~~markdown
# Bug Fix

## Mission
Fix the failure in `[test file or command]`.

## Failure
Command:

```bash
[failing command]
```

Observed output:

```text
[short failure excerpt]
```

## Constraints
- Keep the public API unchanged unless the test proves it is wrong.
- Prefer the smallest maintainable change.
- Add or update tests only if needed to capture the behavior.

## Done When
- [ ] The failing command passes.
- [ ] Related tests pass: `[command]`.
- [ ] The final response explains root cause and fix.
~~~

## 4. Literature Review For A Technical Decision

~~~markdown
# Literature Review Task

## Decision This Should Inform
[Decision.]

## Scope
- Topic:
- Include:
- Exclude:
- Date range:

## Source Priority
1. Peer-reviewed papers.
2. Official standards/government sources.
3. Top enterprise engineering or research publications.
4. Other sources only if primary sources are unavailable.

## Evidence Requirements
- Search current sources.
- Separate empirical findings from expert opinion.
- Identify contradictions and limitations.
- Provide source links.

## Output
Create Markdown with:
- Abstract.
- Executive summary.
- Evidence table.
- Recommendation.
- Risks and open questions.
- References.
~~~

## 5. Plan-First Prompt

~~~markdown
# Plan First

Inspect the repository and produce a short implementation plan before editing.

Do not edit files yet.

The plan must include:
- Relevant files found.
- Assumptions.
- Proposed changes.
- Validation commands.
- Risks or questions.

Proceed to implementation only after the plan is accepted or if the task instructions explicitly allow you to continue after presenting the plan.
~~~

## 6. Final Review Prompt

~~~markdown
# Final Review

Review the completed work against the original task brief.

Prioritize:
1. Incorrect behavior or failed acceptance criteria.
2. Weak or missing validation.
3. Data leakage, reproducibility, or research-integrity risks.
4. Scope drift.
5. Maintainability issues.

Output findings first. For each finding, include severity, file/line if applicable, evidence, and recommended fix.

Then include:
- Acceptance criteria status.
- Commands reviewed.
- Residual risks.
- Decision: accept, accept with notes, revise, or escalate.
~~~

## 7. Compact One-Line Prompts

Use these only when `AGENTS.md` already contains team standards.

```text
Fix `[failing command]`; keep changes minimal; run the targeted test; report root cause, changed files, and residual risks.
```

```text
Inspect `[path]` and explain how it works with file references; do not edit files.
```

```text
Make `[artifact]` reproducible from `[command]`; preserve raw data; document assumptions and validation results.
```

```text
Review the uncommitted diff for bugs, missing tests, scope drift, and research-integrity risks; findings first.
```
