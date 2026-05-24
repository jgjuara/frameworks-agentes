# Experiment Protocol: Measuring Codex Prompting for Open-Ended Reports

**Abstract:** This protocol defines a small, novel experiment a research team can run to compare Codex prompting strategies for non-verifiable report-generation tasks. It is designed to measure whether structured context and staged evidence workflows outperform short prompts or large context dumps on source quality, factuality, citation accuracy, and review effort.

## Purpose

The literature review supports structured context and verification workflows, but the exact best prompt size and process will vary by team. This experiment lets the research team measure performance on its own report tasks.

## Research Question

For open-ended research-report tasks without an exhaustive source index, which Codex prompting strategy produces the best balance of factuality, source quality, synthesis usefulness, and reviewer effort?

## Hypotheses

H1: A structured task brief plus staged source inventory and claim ledger will outperform a short one-shot prompt.

H2: A large undifferentiated context dump will not reliably outperform a compact structured brief plus source-gathering workflow.

H3: Requiring claim-level verification will reduce unsupported claims and citation errors, but increase runtime.

## Experimental Conditions

Use the same report topic across four conditions.

| Condition | Description |
|---|---|
| A: Minimal Prompt | "Write a report on X using reliable sources." |
| B: Structured Brief | Goal, audience, scope, source hierarchy, output schema, done-when criteria. |
| C: Large Context Dump | Structured brief plus many unscreened documents or long notes. |
| D: Staged Workflow | Structured brief plus required source inventory, evidence matrix, outline, draft, claim ledger, final report. |

## Suggested Topics

Choose 3-5 real topics relevant to the team. Each topic should be broad enough to require source selection but narrow enough to review.

Examples:

- AI use in public-sector policy analysis.
- Evaluation methods for LLM-assisted literature reviews.
- Automation bias in expert decision support.
- Retrieval-augmented generation for institutional knowledge systems.
- Governance of AI agents in research organizations.

## Prompt Template for Condition D

```markdown
# Task
Create a research report on [topic] for [audience] to inform [decision].

## Scope
Include [boundaries]. Exclude [boundaries].

## Source Hierarchy
1. Peer-reviewed scholarship.
2. Official government or standards sources.
3. Primary enterprise research/engineering publications.
4. Other sources only as background and clearly labeled.

## Workflow
1. Search trusted sources and create a source inventory.
2. Create an evidence matrix.
3. Draft an outline.
4. Write the report with inline citations.
5. Create a claim ledger.
6. Revise unsupported claims before finalizing.

## Rules
- Do not cite sources unless opened or supplied.
- Mark missing evidence as not found.
- Separate empirical evidence, official guidance, enterprise practice, and inference.
- Report contradictions.

## Output
Markdown report with header, abstract, methods, synthesis, recommendations, limitations, and source list.
```

## Evaluation Rubric

Score each report from 1 to 5.

| Dimension | Definition |
|---|---|
| Source quality | Uses peer-reviewed, official, or primary enterprise sources appropriate to the claim. |
| Citation accuracy | Citations are real, correctly described, and support nearby claims. |
| Claim support | Major claims are backed by evidence or clearly qualified. |
| Coverage | Covers the important subtopics within the stated scope. |
| Synthesis quality | Compares, resolves, or explains evidence rather than listing sources. |
| Uncertainty handling | States limits, contradictions, and evidence gaps. |
| Usefulness | Helps the intended audience make the target decision. |
| Review effort | Time required for a human reviewer to verify and improve the report. Lower effort scores higher. |

## Measurement Procedure

1. Pick 3-5 topics.
2. Run each topic under all four prompt conditions.
3. Save each Codex transcript and output.
4. Assign blinded reviewers if possible.
5. Reviewers score each output using the rubric.
6. Record review time in minutes.
7. Audit citations:
   - source exists;
   - source was opened or supplied;
   - bibliographic details are correct enough to retrieve;
   - cited source supports the claim.
8. Count unsupported claims:
   - unsupported factual claim;
   - overgeneralized claim;
   - citation mismatch;
   - fabricated or unverifiable citation.

## Output Metrics

| Metric | Calculation |
|---|---|
| Citation error rate | erroneous citations / total citations |
| Unsupported claim rate | unsupported major claims / total major claims |
| Mean rubric score | average across dimensions except review effort |
| Reviewer minutes | median minutes to acceptable final draft |
| Revision burden | number of claims removed, qualified, or replaced |
| Source trust share | high-trust sources / total sources |

## Acceptance Thresholds

A prompting strategy is acceptable for team default use if:

- citation error rate is below 5%;
- no fabricated citations survive final review;
- unsupported major claim rate is below 10%;
- mean rubric score is at least 4;
- reviewers agree the output is usable after normal editing.

For external publication or high-stakes decisions, thresholds should be stricter and include expert review.

## Analysis Plan

Compare conditions using:

- average rubric score by condition;
- citation error rate by condition;
- unsupported claim rate by condition;
- review time by condition;
- qualitative reviewer notes.

Expected result:

- Condition D should perform best on factuality and reviewability.
- Condition B should be the best low-cost default for low-risk internal memos.
- Condition C may underperform if the extra context is not structured.
- Condition A should be fastest but riskiest.

## Limitations

- Results will be model-version dependent.
- Reviewers may disagree about synthesis quality.
- Some topics have easier source ecosystems than others.
- Citation checking is time-consuming but necessary for trustworthy reports.
- The experiment measures report quality, not all possible Codex workflows.

## Recommended Next Step

Run the experiment with at least three topics from the team's actual work. If Condition D wins as expected, turn it into a Codex skill and keep Condition B as a lighter template for low-risk internal memos.
