# Framework: Context and Prompting Levels for Codex

**Abstract:** This framework turns the evidence review into an operating model for research teams. It defines five context levels, when to use each level, what to put in the prompt, what belongs in persistent instructions, and how to decide whether a Codex task is ready to run. The main rule is that prompt length should scale with risk and ambiguity, while verification should be mandatory for every computable output.

## 1. Principle

Give Codex the **least prompt context that makes the first plan likely to be correct**, and the **most concrete verification criteria available**.

This separates two concerns:

- **Context sufficiency:** Codex can understand the task, find the relevant files, and avoid forbidden actions.
- **Verification sufficiency:** Codex can know whether the solution works.

When these conflict, prefer stronger verification over longer explanation.

## 2. Context Levels

### Level 0: Command-Only

Use for simple, reversible, local actions.

Prompt size: 1-3 sentences.

Example:

```text
Run the existing test suite and summarize failures. Do not edit files.
```

Required verification: command output.

### Level 1: Minimal Task Contract

Use for small fixes or explanations.

Prompt size: 100-300 words.

Include:

- Goal.
- Relevant path or symptom.
- Done condition.
- Any forbidden action.

Example:

```text
Find why `uv run pytest tests/test_parser.py` fails and fix only the parser code or the test if the test is stale. Keep the public API unchanged. Done when that test file passes and you summarize the cause.
```

### Level 2: Standard Verifiable Task

Use for most research-code work.

Prompt size: 200-800 words.

Include:

- Mission.
- Relevant files or directories.
- Constraints.
- Validation command.
- Expected final response.

Example:

```text
Implement a reproducible CSV cleaning step for the survey pipeline.

Relevant files:
- `src/cleaning/`
- `tests/test_cleaning.py`
- `data/schema/survey_schema.yml`

Constraints:
- Do not modify raw data.
- Keep transformations explicit and logged.
- Use existing project patterns.

Done when:
- `uv run pytest tests/test_cleaning.py` passes.
- The output schema matches `data/schema/survey_schema.yml`.
- The final response lists assumptions and any dropped rows.
```

### Level 3: High-Context Research Task

Use for multi-file changes, method-sensitive analysis, or tasks that can affect findings.

Prompt size: 800-1,500 words.

Include:

- Research question.
- Hypothesis or analysis objective.
- Data provenance.
- Methods constraints.
- Output artifacts.
- Reproducibility requirements.
- Risk class and escalation triggers.

Required verification:

- End-to-end command.
- Artifact inspection.
- Methods note.
- Claim-strength review.

### Level 4: Governed Task Packet

Use for sensitive data, external systems, public release, security, legal, medical, financial, or policy-impact work.

Prompt size: as needed, but split across:

- `AGENTS.md` for stable rules.
- Task brief for mission and acceptance criteria.
- Separate protocol or governance file for policy.
- Human review outside Codex.

Codex should not be the sole decision maker for Level 4.

## 3. What Goes Where

| Information | Put in prompt | Put in `AGENTS.md` | Put in skill | Let Codex discover |
|---|---|---|---|---|
| One-time task goal | Yes | No | No | No |
| Repository setup commands | Usually no | Yes | Maybe | Yes |
| Current failing test output | Yes | No | No | No |
| Stable data-handling rules | No | Yes | Maybe | No |
| Repeated literature-review workflow | No | Maybe | Yes | No |
| Current issue details | Yes | No | No | Maybe |
| File contents | Only if small and critical | No | No | Yes |
| Large docs | Link or cite section | No | Maybe | Yes |
| External live data | No, use connector/tool if approved | No | Maybe | Yes |
| Acceptance criteria | Yes | Maybe, as general standard | Maybe | No |

## 4. Prompt Readiness Rubric

Score each task from 0 to 2.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Goal | vague activity | artifact named | artifact and use named |
| Context | missing or dumped | some relevant paths | curated, prioritized paths/sources |
| Constraints | none | broad | explicit allowed/forbidden actions |
| Verification | absent | generic | executable command or checkable rubric |
| Risk | ignored | implied | explicit class and escalation triggers |
| Scope | open-ended | somewhat bounded | bounded by files, behavior, or artifact |
| Final evidence | not requested | summary requested | evidence package specified |

Minimum score:

- R0: 6/14.
- R1: 8/14.
- R2: 10/14.
- R3: 12/14.
- R4: governed review required.

## 5. Ordering Rules For Context

Order matters because long-context use can be position-sensitive.

Recommended order:

1. Mission.
2. Acceptance criteria.
3. Relevant paths and source priority.
4. Constraints and forbidden actions.
5. Known failures or examples.
6. Escalation triggers.
7. Final response requirements.

If a detail is crucial, do not bury it in the middle of a long paragraph. Put it near the top or in a labeled section.

## 6. Default Prompt Skeleton

```markdown
# Codex Task

## Mission
[Concrete deliverable.]

## Context
- `[path]`: [why it matters]
- `[path]`: [why it matters]

## Constraints
- [Architecture, data, dependency, privacy, or scope rule.]

## Allowed Actions
- [Read/edit/run permissions.]

## Forbidden Without Approval
- [Destructive, external, irreversible, sensitive, or high-cost action.]

## Done When
- [ ] [Executable or observable criterion.]
- [ ] [Executable or observable criterion.]

## Escalate If
- [Conflict, ambiguity, missing data, or unsafe action.]

## Final Response
Report changed files, validation commands and results, assumptions, and residual risks.
```

## 7. Team Defaults

For this research-team setting, use these defaults unless the task brief says otherwise:

- Use `uv` for Python execution and dependency management.
- Preserve raw data.
- Prefer reproducible scripts over manual notebook state.
- State assumptions and limitations.
- Do not introduce new production dependencies without approval.
- Do not publish, email, push, or call external services without approval.
- Use one Codex thread per task.
- Compact or fork when context becomes mostly historical.

## 8. Decision Rule

When deciding whether to add more context, ask:

1. Will this change the implementation plan?
2. Will this prevent a foreseeable mistake?
3. Will this make validation more objective?
4. Can Codex retrieve this safely instead?

Add the context only if the answer to 1, 2, or 3 is yes and 4 is no.

## 9. Source Basis

This framework is based on OpenAI Codex best practices, OpenAI Codex prompting and `AGENTS.md` documentation, SWE-bench/SWE-agent/Agentless evidence, long-context research, and official GitHub and Anthropic coding-agent guidance. Full citations are in `CODEX_CONTEXT_PROMPTING_EVIDENCE.md`.
