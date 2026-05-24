# Codex Context Experiment Results

## Abstract
This is a reproducible pilot run of the experiment package. It randomizes synthetic/de-identified tasks across conditions, generates prompts, and reports design diagnostics. Primary Codex outcome metrics require manual execution in fresh Codex threads.

## Setup
- Date: 2026-05-24
- Codex surface/model: to be recorded during manual execution
- Repository: fundar/ia-reunion
- Run id: pilot_20260524
- Seed: 20260524
- Task count: 36
- Conditions: A, B, C, D, E, F

## Design Diagnostics
| Condition | N | Mean prompt words | Mean readiness | Readiness pass rate |
|---|---:|---:|---:|---:|
| A - Sparse Prompt | 6 | 20.8 | 2.3 | 0% |
| B - Structured Prompt | 6 | 165.8 | 14.0 | 100% |
| C - Structured Prompt + Curated Context | 6 | 183.2 | 14.0 | 100% |
| D - Structured Prompt + Full Context Dump | 6 | 260.2 | 14.0 | 100% |
| E - AGENTS.md + Short Task Prompt | 6 | 46.3 | 13.0 | 100% |
| F - Plan-First | 6 | 209.5 | 14.0 | 100% |

## Outcome Results
No real Codex outcome observations are recorded yet. Complete `observations_template.csv`, save it as `observations.csv`, and rerun with `--analyze-existing results/<run_id>`.

## Main Finding
The package is ready for manual execution. The design diagnostics show the intended ablation: sparse prompts are shorter and lower-readiness; curated, full-context, and plan-first prompts carry more explicit verification and risk controls.

## Limitations
- This pilot does not measure model task success until fresh Codex threads are run.
- Tasks are synthetic/de-identified and should be replaced with real internal tasks before decisions.
- Review scores require an independent human reviewer.
