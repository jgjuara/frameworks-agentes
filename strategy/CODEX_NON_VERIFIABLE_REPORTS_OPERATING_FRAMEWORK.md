# Operating Framework: Codex for Open-Ended Research Reports

**Abstract:** This framework translates the literature review into an operational process for a research team using Codex to draft reports without a fixed source list. It defines context layers, task classes, source rules, review gates, and reusable prompt patterns.

## Operating Principle

Codex should not be asked to produce a final research report in one step unless the task is low stakes and the user already supplied trusted source material.

For open-ended reports, Codex should produce intermediate artifacts:

1. source inventory;
2. evidence matrix;
3. report outline;
4. draft;
5. claim ledger;
6. final markdown.

## Task Classes

| Class | Example | Codex Autonomy | Required Controls |
|---|---|---:|---|
| R0: Style-only | Rewrite an existing report. | High | Preserve claims; no new sources. |
| R1: Source-bound summary | Summarize 3 supplied papers. | High | Cite only supplied sources; extract quotes first. |
| R2: Bounded research memo | Report using peer-reviewed and official sources. | Medium | Source inventory and evidence matrix. |
| R3: Decision report | Report informs strategy, policy, funding, or publication. | Medium-low | Claim ledger, contradiction log, reviewer signoff. |
| R4: High-stakes domain | Medical, legal, financial, safety, sensitive population. | Low | Human expert review, strict source index, no unsupervised final claims. |

## Context Layers

### Layer 1: Durable Team Context

Put in `AGENTS.md` or a task-specific strategy file:

- preferred language and documentation standards;
- source hierarchy by domain;
- citation policy;
- privacy and data restrictions;
- definition of "done";
- review expectations.

Keep this short. If it grows, move detailed workflows into separate markdown files or Codex skills.

### Layer 2: Task Brief

Every non-trivial report request should specify:

- objective;
- research question;
- audience;
- scope;
- exclusions;
- source hierarchy;
- output format;
- acceptance criteria;
- risk class;
- validation method.

### Layer 3: Evidence Context

Codex should build this during the task:

- source title, author, year, organization, URL/DOI;
- source type and trust level;
- reason for inclusion;
- key findings;
- limitations;
- contradictions;
- claims supported by the source.

## Source Policy

Default source hierarchy:

1. peer-reviewed papers, systematic reviews, and major conference papers;
2. official government, statistical, standards, or institutional sources;
3. primary enterprise research and engineering publications from major labs;
4. high-quality technical blogs only when primary sources are unavailable;
5. news and commentary only for recent events or ecosystem context.

Rules:

- Do not cite a source unless opened or provided.
- Prefer original papers over blog summaries.
- Use official documentation for current product behavior.
- Separate empirical results from expert opinion.
- Record source date and access date when the topic is time-sensitive.
- For contradictory evidence, report the contradiction instead of forcing consensus.

## Required Intermediate Artifacts

### Source Inventory

| Source | Type | Why Included | Trust Level | Notes |
|---|---|---|---:|---|

### Evidence Matrix

| Claim/Theme | Supporting Source | Evidence Type | Limitations |
|---|---|---|---|

### Claim Ledger

| Report Claim | Citation | Support Status | Action |
|---|---|---|---|
| [Claim] | [Source] | supported / partial / unsupported | keep / qualify / remove |

## Prompt Pattern

```markdown
You are helping a research team produce a report. Treat this as a literature-review workflow, not a one-shot writing task.

First, build a source inventory from trusted sources. Prioritize peer-reviewed work, official sources, and primary enterprise research. Do not cite a source unless you opened it or it was provided.

Second, create an evidence matrix. Separate empirical findings, official guidance, enterprise practice, and inference.

Third, propose an outline. State assumptions and unresolved contradictions.

Fourth, draft the report with inline citations near the claims they support.

Fifth, create a claim ledger for major claims. Remove or qualify unsupported claims before finalizing.
```

## Review Gate Checklist

Before accepting a Codex-generated report:

- [ ] Does the abstract match the actual findings?
- [ ] Are source types appropriate for the claim strength?
- [ ] Are citations real and opened/provided?
- [ ] Are citations near the claims they support?
- [ ] Are unsupported claims removed or qualified?
- [ ] Are source limitations stated?
- [ ] Are contradictions reported?
- [ ] Does the report distinguish evidence from recommendation?
- [ ] Does the final section state what was not verified?

## Recommended Team Assets

Create these reusable files:

- `AGENTS.md`: durable Codex rules.
- `strategy/RESEARCH_SOURCE_POLICY.md`: domain-specific source hierarchy.
- `strategy/RESEARCH_REPORT_TEMPLATE.md`: report format.
- `strategy/CLAIM_LEDGER_TEMPLATE.md`: verification table.
- `.codex/skills/research-report/SKILL.md`: optional skill once the workflow stabilizes.

## Practical Defaults

| Situation | Prompting Default |
|---|---|
| User has no source list | Require source inventory before drafting. |
| User supplies many sources | Ask Codex to extract source notes before synthesis. |
| Topic is current | Browse; include publication dates and access date. |
| Topic is scholarly | Prefer systematic reviews and primary papers. |
| Report is for publication | Require manual citation audit. |
| Report is for internal strategy | Require evidence matrix and limitations. |
| Source evidence is weak | State uncertainty; do not upgrade claim strength. |

## Failure Modes and Controls

| Failure Mode | Control |
|---|---|
| Fabricated citations | Cite only opened/provided sources; run citation audit. |
| Source laundering | Track whether source is primary, secondary, or commentary. |
| Context burial | Use evidence matrix instead of bulk source dumps. |
| Overconfident synthesis | Require uncertainty and contradiction sections. |
| Hidden source gaps | Include search terms and exclusion notes. |
| Prompt bloat | Move durable rules to `AGENTS.md` or skills. |
| Vague acceptance | Define "done when" before drafting. |

## Final Recommendation

Use Codex as a research workflow agent, not as an isolated report generator. The best framework is a staged, evidence-grounded process with compact initial context and explicit review artifacts.
