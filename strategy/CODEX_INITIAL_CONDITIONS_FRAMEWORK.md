# Framework: Setting the Initial Conditions for Codex Agentic Work

**Abstract:** This framework defines the start-gate for research-team Codex work. Its purpose is to make the agent's mission, context, constraints, success criteria, tools, and review rubric explicit before execution begins. The goal is to concentrate human judgment at the highest-leverage moment: before Codex starts acting.

## Principle

The first prompt should not be a request. It should be a **task contract**.

A high-quality Codex start-gate answers seven questions:

1. What outcome must exist when the task is done?
2. What sources are authoritative?
3. What constraints cannot be violated?
4. What tools and files are allowed?
5. What counts as evidence of success?
6. What should trigger a stop-and-ask escalation?
7. What should the final review package contain?

## The Start-Gate Artifact

Each non-trivial Codex task should start with a structured brief containing these sections.

### 1. Mission

Define the deliverable, not just the activity.

Bad:

```text
Analyze this dataset and improve the report.
```

Better:

```text
Produce a reproducible analysis notebook and a 2-page methods note explaining whether variable X predicts outcome Y, using only the approved dataset and existing project conventions.
```

### 2. Context Packet

Provide only context Codex needs to act correctly.

Recommended ordering:

1. Repository or project purpose.
2. Current task objective.
3. Relevant files or folders.
4. Domain definitions.
5. Known constraints.
6. Prior decisions that must not be reopened.
7. Examples of acceptable output.

Avoid:

- Large undifferentiated document dumps.
- Contradictory instructions without priority.
- Background that is interesting but not action-relevant.

### 3. Authority Hierarchy

State which source wins if instructions conflict.

Recommended hierarchy:

1. System and security policies.
2. Repository `AGENTS.md`.
3. Task brief.
4. Linked issue or research protocol.
5. Existing code conventions.
6. User preferences stated during the session.

For research teams, add:

- Ethics protocol beats convenience.
- Data-use agreement beats analysis speed.
- Reproducibility beats clever shortcuts.

### 4. Allowed and Forbidden Actions

Define autonomy boundaries before work starts.

Example:

```text
Allowed:
- Read repository files.
- Modify files under `analysis/` and `docs/`.
- Add focused tests or reproducibility checks.
- Run local tests and linters.

Forbidden without explicit approval:
- Deleting source data.
- Changing raw data files.
- Installing new dependencies.
- Pushing commits or opening PRs.
- Calling external APIs with project data.
- Publishing or emailing outputs.
```

### 5. Success Criteria

Make "done" checkable.

A useful acceptance criterion is observable, not aspirational.

Examples:

- `uv run pytest` passes.
- The methods note includes data source, sample exclusions, model specification, limitations, and reproducibility steps.
- The final answer lists changed files, commands run, unresolved assumptions, and residual risks.
- No raw personally identifiable information is copied into generated docs.

### 6. Risk Class

Assign a task risk class at intake.

| Class | Description | Default human involvement |
|---|---|---|
| R0 | Read-only exploration, summarization, planning | Start and end only |
| R1 | Local code/docs edits with tests, no sensitive data | Start and end only |
| R2 | Research analysis that can affect published findings | Start, automated checks, final review |
| R3 | Sensitive data, external systems, irreversible changes, policy impact | Start, predefined mid-run gates, final review |
| R4 | Legal, medical, financial, safety-critical, or public release | Human governance outside Codex required |

### 7. Escalation Triggers

Escalation should be rare, explicit, and tied to risk.

Codex must stop and ask if:

- Requirements conflict.
- The task requires a forbidden action.
- A test failure cannot be explained after reasonable debugging.
- Results materially contradict the user's hypothesis.
- Data provenance is unclear.
- Sensitive data appears in a file that may be committed or shared.
- The agent needs to choose between incompatible research interpretations.
- The next action is irreversible or externally visible.

### 8. Final Review Requirements

Define the review package before work begins.

Minimum final package:

- Changed files.
- Summary of behavioral or analytical changes.
- Commands run and results.
- Evidence mapped to acceptance criteria.
- Known limitations.
- Residual risks.
- Recommended next checks.

## Persistent Team Assets

### `AGENTS.md`

Use `AGENTS.md` for stable repository policy:

- Role and tone.
- Project architecture.
- Testing and validation commands.
- Data handling rules.
- Dependency policy.
- Documentation language.
- Review expectations.

### `code_review.md`

Use `code_review.md` for final review standards:

- Correctness.
- Reproducibility.
- Data leakage.
- Security.
- Performance.
- Statistical validity.
- Documentation clarity.

Reference it from `AGENTS.md` so Codex can apply it during `/review`.

### Skills

Promote repeated workflows into Skills:

- Literature review synthesis.
- Dataset audit.
- Reproducible notebook cleanup.
- PR review against research-code checklist.
- Methods note drafting.
- Survey instrument QA.
- Statistical robustness review.

Each skill should have narrow triggers, clear inputs, and explicit outputs.

## Intake Quality Rubric

Score each task brief from 0 to 2.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Mission clarity | Vague activity | Output named | Output and use named |
| Context relevance | Dumped or missing | Partially curated | Prioritized and linked |
| Constraints | Missing | Some constraints | Explicit allowed/forbidden actions |
| Success criteria | Subjective | Partly checkable | Fully checkable |
| Risk class | Missing | Implied | Explicit with gates |
| Verification | Missing | Generic | Concrete commands/rubric |
| Final review | Missing | Summary requested | Review package specified |

Recommended rule: do not start R2+ work below 10/14.

## Core Prompt Pattern

```text
You are working as a senior research software engineer in this repository.

Mission:
[Concrete deliverable.]

Authoritative context:
[Files, docs, assumptions, source priority.]

Allowed actions:
[Read/edit/run permissions.]

Forbidden actions:
[Actions requiring explicit approval.]

Risk class:
[R0-R4 plus reason.]

Acceptance criteria:
[Checkable criteria.]

Escalate before continuing if:
[Triggers.]

Execution requirements:
- Inspect context before editing.
- Present a short plan for non-trivial work.
- Make focused changes only.
- Run relevant validation.
- Keep an assumptions log.
- End with a final review package mapped to the acceptance criteria.
```

