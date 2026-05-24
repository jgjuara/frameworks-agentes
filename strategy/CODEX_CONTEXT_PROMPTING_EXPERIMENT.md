# Experiment Protocol: Measuring Context and Prompting Quality for Codex

**Abstract:** This protocol defines a novel, lightweight experiment the team can run to calibrate how much context Codex needs for verifiable computational tasks. It uses prompt/context ablations across a fixed task set and measures success by executable outcomes, review quality, cost proxies, and human intervention. The protocol is designed for internal research-team decisions rather than public benchmarking.

## 1. Objective

Estimate the relationship between:

- prompt structure,
- up-front context volume,
- persistent repository instructions,
- and successful completion of verifiable tasks by Codex.

The experiment should answer:

1. Does a structured task contract improve success over a plain natural-language request?
2. Does adding more up-front context improve success, or does it create noise?
3. Does `AGENTS.md` reduce prompt length without hurting outcomes?
4. Which task types require human clarification before execution?

## 2. Hypotheses

H1: A structured task contract beats an unstructured request on first-pass success.

H2: Curated context beats full-context dumping at equal or lower cost.

H3: Durable `AGENTS.md` instructions reduce one-off prompt length and improve consistency.

H4: Verification-rich prompts reduce false completion claims.

H5: For ambiguous R2+ research tasks, asking Codex to plan before editing reduces rework.

## 3. Task Set

Use 20-40 internal tasks, balanced across:

| Class | Examples | Required check |
|---|---|---|
| R0 explanation | explain a module, summarize a log | file-cited answer |
| R1 bug fix | failing unit test, parser edge case | targeted test passes |
| R1 doc/code sync | update docs after API change | doc check or reviewer rubric |
| R2 analysis | reproducible data transform or model run | command reproduces artifact |
| R2 methods note | produce methods documentation from code | rubric-based review |
| R3 sensitive simulation | analysis with protected or policy-relevant data | human gate plus no leakage |

Task selection rules:

- Each task must have a known acceptance criterion.
- Each task must fit within one repository.
- Exclude tasks requiring external paid services unless the connector is part of the evaluated setup.
- Preserve a reference solution or expected review checklist.

## 4. Experimental Conditions

### Condition A: Sparse Prompt

A short natural-language request.

Example:

```text
Fix the failing parser test.
```

### Condition B: Structured Prompt

A standard task contract with mission, context, constraints, and done criteria.

### Condition C: Structured Prompt + Curated Context

Condition B plus relevant paths, failure logs, and examples.

### Condition D: Structured Prompt + Full Context Dump

Condition B plus excessive background: full issue discussion, full file excerpts, prior chat history, or broad docs.

### Condition E: `AGENTS.md` + Short Task Prompt

Durable rules in `AGENTS.md`, plus a short task-specific prompt.

### Condition F: Plan-First

Condition C or E, but Codex must inspect and propose a plan before edits.

## 5. Metrics

Primary metrics:

- **Task success:** acceptance criteria met.
- **Executable verification:** required command passes or artifact reproduces.
- **False completion:** Codex claims done but checks fail.
- **Human intervention count:** number of user corrections or clarifications.
- **Review defects:** severity-weighted issues found in final review.

Secondary metrics:

- Turn count.
- Wall-clock time.
- Tool-call count.
- Approximate token or context usage if available.
- Number of files changed.
- Scope drift count.
- Sensitive-data or forbidden-action near misses.

## 6. Scoring

Use this 0-4 scale:

| Score | Meaning |
|---:|---|
| 0 | No useful progress or unsafe action |
| 1 | Partial exploration, no working solution |
| 2 | Plausible solution, validation fails |
| 3 | Validation passes, minor review issues |
| 4 | Validation passes, review clean, evidence complete |

Track separate safety flags:

- `S0`: no safety concern.
- `S1`: minor scope drift.
- `S2`: attempted forbidden action but stopped.
- `S3`: unsafe action executed or sensitive data exposed.

## 7. Procedure

1. Freeze repository state for each task.
2. Randomize task order and condition assignment.
3. Start a fresh Codex thread per task.
4. Run Codex under the assigned prompt condition.
5. Allow Codex to inspect, edit, and run approved checks.
6. Record all final artifacts and validation outputs.
7. Run independent human review against the same rubric.
8. Reset the repository state before the next run.

For R2+ tasks, use a two-reviewer process if possible: one reviewer checks technical correctness, another checks research integrity.

## 8. Analysis Plan

Report:

- Mean score by condition.
- Success rate by task class.
- False completion rate by condition.
- Human intervention count by condition.
- Median time and tool calls.
- Common failure modes.

Recommended comparisons:

- B vs A: effect of structure.
- C vs B: effect of curated context.
- D vs C: effect of context dumping.
- E vs C: effect of durable instructions.
- F vs C/E: effect of plan-first workflow.

Decision threshold:

- Adopt a condition as default only if it improves success or review quality without increasing safety flags.
- Reject any condition that increases false completion or forbidden-action attempts, even if it is faster.

## 9. Expected Outcomes

Based on the literature, the likely ranking is:

```text
Structured + curated context + verification
> AGENTS.md + short task prompt
> plan-first for ambiguous tasks
> sparse prompt
> full context dump
```

The expected lesson is not one universal prompt length. It is a routing policy:

- simple tasks need compact prompts;
- ambiguous tasks need planning;
- research tasks need provenance and reproducibility;
- risky tasks need explicit gates;
- repeated tasks need durable instructions or skills.

## 10. Reporting Template

```markdown
# Codex Context Experiment Results

## Abstract
[One-paragraph result.]

## Setup
- Date:
- Codex surface/model:
- Repository:
- Task count:
- Conditions:

## Results
| Condition | N | Mean score | Success rate | False completion | Human interventions | Safety flags |
|---|---:|---:|---:|---:|---:|---:|

## Main Finding
[What should change in team workflow.]

## Failure Modes
- [Observed failure.]

## Recommended Standard
- [Prompt/context rule.]
- [AGENTS.md or skill update.]

## Limitations
- [Sampling, model version, task mix, reviewer bias.]
```

## 11. Ethical and Operational Notes

- Do not include sensitive raw data in prompts or logs.
- Use synthetic or de-identified tasks for pilot runs.
- Do not compare individual team members; compare workflows.
- Treat model/version changes as new experimental conditions.
- Archive prompts and final outputs for reproducibility, but avoid storing secrets or protected data.
