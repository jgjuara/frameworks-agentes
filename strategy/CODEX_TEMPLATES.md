# Templates for Codex Start-Gates and Final Reviews

**Abstract:** This file provides reusable Markdown templates for research teams using Codex. The templates are designed to reduce unstructured prompting, improve initial context quality, and make final review consistent across users and projects.

## Template 1: Codex Task Brief

```markdown
# Codex Task Brief

## Mission
[Describe the concrete deliverable.]

## Background
[Only include context needed to complete the task.]

## Authoritative Sources
1. [Highest-priority source.]
2. [Second-priority source.]
3. [Existing code/docs conventions.]

## Relevant Files
- `[path]`: [why relevant]
- `[path]`: [why relevant]

## Allowed Actions
- [Allowed action.]
- [Allowed action.]

## Forbidden Actions Without Approval
- [Forbidden action.]
- [Forbidden action.]

## Risk Class
[R0/R1/R2/R3/R4] because [reason].

## Acceptance Criteria
- [ ] [Checkable criterion.]
- [ ] [Checkable criterion.]
- [ ] [Checkable criterion.]

## Required Validation
- [Command or manual check.]
- [Command or manual check.]

## Escalation Triggers
Codex must stop and ask before continuing if:
- [Trigger.]
- [Trigger.]

## Final Response Requirements
Include:
- Changed files.
- Validation run.
- Acceptance criteria status.
- Assumptions.
- Residual risks.
- Recommended next step.
```

## Template 2: Research Analysis Brief

```markdown
# Research Analysis Brief

## Research Question
[Question.]

## Hypothesis
[Hypothesis. State whether Codex should try to falsify it.]

## Dataset
- Source:
- Version/date:
- Location:
- Data-use restrictions:
- Sensitive fields:

## Methods Constraints
- Required method:
- Forbidden method:
- Required robustness checks:
- Required reporting format:

## Reproducibility Requirements
- Environment:
- Commands:
- Random seed:
- Output location:

## Interpretation Rules
- Distinguish association from causation.
- Report limitations.
- Do not make policy claims beyond evidence.
- Flag contradictory evidence.

## Acceptance Criteria
- [ ] Analysis runs end to end.
- [ ] Outputs are reproducible.
- [ ] Methods note explains data, sample, model, and limitations.
- [ ] Findings are supported by tables/figures/logs.
- [ ] No sensitive data is exposed in generated artifacts.
```

## Template 3: Literature Review Brief

```markdown
# Literature Review Brief

## Objective
[Decision this review should inform.]

## Scope
- Topic:
- Date range:
- Disciplines:
- Geographies:
- Include:
- Exclude:

## Source Priority
1. Peer-reviewed papers.
2. Official standards or government sources.
3. Top enterprise engineering/research publications.
4. High-quality technical blogs only if primary sources are unavailable.

## Required Treatment of Evidence
- Separate empirical findings from expert opinion.
- State uncertainty.
- Identify contradictions.
- Prefer systematic reviews and benchmarks where available.
- Include links and dates.

## Output
- Executive summary.
- Evidence table.
- Implications for our team.
- Open questions.
- Source list.
```

## Template 4: Final Review Request

```markdown
# Final Review Request

Review the completed Codex work against the original task brief.

## Review Priorities
1. Bugs, regressions, and incorrect behavior.
2. Missing or weak validation.
3. Data leakage or research-integrity risks.
4. Scope creep.
5. Documentation gaps.

## Required Output
- Findings first, ordered by severity.
- File and line references where possible.
- Acceptance criteria status table.
- Tests/checks reviewed.
- Residual risks.
- Decision recommendation: accept, accept with notes, revise, or escalate.
```

## Template 5: `AGENTS.md` Addendum for Research Repositories

```markdown
## Research Integrity
- Preserve raw data. Do not modify files under `data/raw/` unless explicitly requested.
- Make analysis reproducible with documented commands.
- Distinguish findings, interpretation, and speculation.
- State assumptions and limitations.
- Do not expose sensitive data in examples, logs, generated docs, or commits.

## Codex Workflow
- For non-trivial tasks, inspect context first and present a short plan.
- Before editing, identify target files and validation commands.
- Keep changes scoped to the user's request.
- Run relevant checks when feasible.
- End with changed files, validation results, assumptions, and residual risks.

## Review
- Use `code_review.md` for code review standards.
- Lead reviews with defects and risks, not summaries.
- For research outputs, check data provenance, methods, reproducibility, and claim strength.
```

## Template 6: `code_review.md` for Research Code

```markdown
# Code Review Rubric

## Correctness
- Does the code implement the requested behavior?
- Are edge cases handled?
- Are errors explicit and actionable?

## Reproducibility
- Are commands documented?
- Are inputs and outputs stable?
- Are random seeds controlled where relevant?

## Research Integrity
- Is raw data preserved?
- Are transformations traceable?
- Are statistical claims supported?
- Are limitations documented?

## Security and Privacy
- Are secrets excluded?
- Is sensitive data protected?
- Are external calls approved?

## Maintainability
- Does the code follow local patterns?
- Is complexity justified?
- Are comments useful and sparse?

## Tests
- Are tests or checks proportional to risk?
- Are failures reported honestly?
```

