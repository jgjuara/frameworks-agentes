# Final Review Playbook for Codex Work

**Abstract:** This playbook defines how a research team should review Codex outputs at the end of agentic work. It assumes the human reviewer should not inspect every intermediate step. Instead, the final review must be evidence-based, rubric-driven, and supported by reproducible commands, diffs, logs, and risk notes.

## Purpose

The final review is where the human decides whether to accept, reject, revise, or escalate the work. It is not a vibe check. It is an adjudication against the start-gate contract.

## Required Final Review Package

Codex should provide:

1. **Changed artifacts:** files created, modified, or deleted.
2. **Intent summary:** what was changed and why.
3. **Acceptance mapping:** each acceptance criterion and whether it was met.
4. **Validation evidence:** commands run, tests passed/failed, lint/type checks, screenshots if relevant.
5. **Assumptions log:** assumptions made because the brief was incomplete.
6. **Risk log:** data, security, statistical, publication, or operational risks.
7. **Residual uncertainty:** what remains unverified.
8. **Human decisions needed:** only concrete yes/no or choose-one decisions.

## Review Sequence

### 1. Scope Review

Ask:

- Did Codex solve the requested task and nothing materially unrelated?
- Are changes limited to expected files?
- Did it avoid forbidden actions?
- Did it preserve user or team work already in the repo?

Reject or revise if the output includes unsolicited features, broad refactors, hidden dependency changes, or unexplained data changes.

### 2. Evidence Review

Ask:

- Are claims backed by files, tests, outputs, or cited sources?
- Are commands reproducible?
- Are results traceable to raw inputs?
- Are failures reported plainly?

For research work, require:

- Data provenance.
- Sample definition.
- Exclusion criteria.
- Model or method specification.
- Sensitivity or robustness checks where relevant.
- Clear distinction between findings and interpretation.

### 3. Code Review

Use a code-review stance:

- Correctness before style.
- Reproducibility before convenience.
- Explicitness before cleverness.
- Minimality before abstraction.

Check:

- Edge cases.
- Error handling.
- File paths and OS assumptions.
- Dependency changes.
- Determinism and random seeds.
- Test coverage proportional to risk.
- Whether generated code follows existing project patterns.

### 4. Data and Research Integrity Review

Check:

- No raw sensitive data leaked into logs, docs, prompts, generated examples, or commits.
- No accidental mutation of raw data.
- No unapproved external API use with protected data.
- No claims stronger than the evidence supports.
- No p-hacking, silent filtering, or undisclosed analytic degrees of freedom.
- Limitations are explicit.

### 5. Risk Review

Map final output against the intake risk class.

| Risk | Review action |
|---|---|
| R0 | Read final output; verify source references. |
| R1 | Inspect diff and tests. |
| R2 | Inspect methods, reproducibility, and interpretation. |
| R3 | Require second reviewer or domain owner approval. |
| R4 | Do not accept through Codex-only review; use formal governance. |

### 6. Decision

Use one of four outcomes:

- **Accept:** all material criteria met, residual risk acceptable.
- **Accept with notes:** minor limitations documented and not blocking.
- **Revise:** concrete defects or missing validation.
- **Escalate:** decision requires domain, ethics, legal, security, or publication authority.

## Final Review Checklist

```text
[ ] The final output matches the original mission.
[ ] All changed files are expected.
[ ] No forbidden action was taken.
[ ] Acceptance criteria are mapped one by one.
[ ] Tests/checks were run or the reason they were not run is explicit.
[ ] Claims are supported by evidence.
[ ] Assumptions are listed.
[ ] Residual risks are listed.
[ ] Sensitive data handling is acceptable.
[ ] Research interpretation is not overstated.
[ ] The reviewer can reproduce the core result.
[ ] The decision is recorded: accept, accept with notes, revise, or escalate.
```

## Codex-Assisted Final Review

Use Codex itself as a second-pass reviewer, but do not make it the accountable approver.

Recommended prompts:

```text
Review the working tree against `code_review.md` and the original task brief.
Lead with bugs, regressions, missing tests, and research-integrity risks.
Do not summarize until after findings.
```

```text
Map this final output to the acceptance criteria.
Return a table with criterion, evidence, status, and residual uncertainty.
```

```text
Search the diff for accidental data leakage, hidden dependency changes, broad refactors, and claims not supported by tests or citations.
```

## Metrics for the Team

Track review quality over time:

- Acceptance rate without revision.
- Defects found after acceptance.
- Average number of back-and-forth turns per task.
- Percent of tasks with complete intake briefs.
- Percent of tasks with reproducible validation.
- Escalation frequency by risk class.
- Common missing context categories.
- Time from start-gate to final-gate.

The goal is not zero escalations. The goal is fewer unnecessary interruptions and better detection of the few decisions that genuinely need human authority.

