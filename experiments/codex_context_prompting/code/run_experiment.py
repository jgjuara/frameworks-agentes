from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from experiment_model import (
    CONDITIONS,
    assign_conditions,
    bool_rate,
    design_metrics,
    load_tasks,
    read_csv,
    render_prompt,
    summarize_numeric,
    write_csv,
)


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "tasks.json"
PROMPTS_ROOT = ROOT / "prompts"
RESULTS_ROOT = ROOT / "results"


def build_run(seed: int, run_id: str) -> Path:
    tasks = load_tasks(DATA_PATH)
    assigned = assign_conditions(tasks, seed=seed)
    run_dir = RESULTS_ROOT / run_id
    prompt_dir = PROMPTS_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    prompt_dir.mkdir(parents=True, exist_ok=True)

    assignments = []
    metrics = []
    observations = []

    for order, (task, condition) in enumerate(assigned, start=1):
        prompt_path = prompt_dir / f"{order:02d}_{task.id}_{condition}.md"
        prompt = render_prompt(task, condition)
        prompt_path.write_text(prompt, encoding="utf-8")

        assignments.append(
            {
                "order": order,
                "task_id": task.id,
                "task_class": task.klass,
                "condition": condition,
                "condition_name": CONDITIONS[condition]["name"],
                "prompt_path": str(prompt_path.relative_to(ROOT.parent.parent)),
                "verification": task.verification,
            }
        )
        metrics.append(design_metrics(prompt, condition, task))
        observations.append(
            {
                "order": order,
                "task_id": task.id,
                "condition": condition,
                "score": "",
                "safety_flag": "",
                "task_success": "",
                "verification_passed": "",
                "false_completion": "",
                "human_interventions": "",
                "review_defects": "",
                "wall_clock_minutes": "",
                "tool_calls": "",
                "files_changed": "",
                "scope_drift_count": "",
                "notes": "",
            }
        )

    write_csv(
        run_dir / "assignment.csv",
        assignments,
        [
            "order",
            "task_id",
            "task_class",
            "condition",
            "condition_name",
            "prompt_path",
            "verification",
        ],
    )
    write_csv(
        run_dir / "design_metrics.csv",
        metrics,
        [
            "task_id",
            "task_class",
            "risk_class",
            "condition",
            "condition_name",
            "prompt_words",
            "context_items",
            "readiness_score",
            "readiness_minimum",
            "readiness_pass",
        ],
    )
    write_csv(
        run_dir / "observations_template.csv",
        observations,
        [
            "order",
            "task_id",
            "condition",
            "score",
            "safety_flag",
            "task_success",
            "verification_passed",
            "false_completion",
            "human_interventions",
            "review_defects",
            "wall_clock_minutes",
            "tool_calls",
            "files_changed",
            "scope_drift_count",
            "notes",
        ],
    )
    write_report(run_dir, run_id, seed, metrics)
    return run_dir


def write_report(
    run_dir: Path,
    run_id: str,
    seed: int,
    design_rows: list[dict[str, object]],
    observation_rows: list[dict[str, str]] | None = None,
) -> None:
    grouped_design = defaultdict(list)
    for row in design_rows:
        grouped_design[row["condition"]].append(row)

    lines = [
        "# Codex Context Experiment Results",
        "",
        "## Abstract",
        "This is a reproducible pilot run of the experiment package. It randomizes "
        "synthetic/de-identified tasks across conditions, generates prompts, and "
        "reports design diagnostics. Primary Codex outcome metrics require manual "
        "execution in fresh Codex threads.",
        "",
        "## Setup",
        f"- Date: {datetime.now().date().isoformat()}",
        "- Codex surface/model: to be recorded during manual execution",
        "- Repository: fundar/ia-reunion",
        f"- Run id: {run_id}",
        f"- Seed: {seed}",
        f"- Task count: {len(design_rows)}",
        f"- Conditions: {', '.join(CONDITIONS)}",
        "",
        "## Design Diagnostics",
        "| Condition | N | Mean prompt words | Mean readiness | Readiness pass rate |",
        "|---|---:|---:|---:|---:|",
    ]

    for condition in sorted(grouped_design):
        rows = grouped_design[condition]
        pass_rate = sum(str(row["readiness_pass"]) == "True" for row in rows) / len(rows)
        lines.append(
            f"| {condition} - {CONDITIONS[condition]['name']} | {len(rows)} | "
            f"{summarize_numeric(rows, 'prompt_words'):.1f} | "
            f"{summarize_numeric(rows, 'readiness_score'):.1f} | "
            f"{pass_rate:.0%} |"
        )

    if observation_rows:
        grouped_obs = defaultdict(list)
        for row in observation_rows:
            if row.get("score", "").strip():
                grouped_obs[row["condition"]].append(row)

        lines.extend(
            [
                "",
                "## Outcome Results",
                "| Condition | N | Mean score | Success rate | False completion | Human interventions | Safety flags |",
                "|---|---:|---:|---:|---:|---:|---|",
            ]
        )
        for condition in sorted(CONDITIONS):
            rows = grouped_obs.get(condition, [])
            if not rows:
                lines.append(f"| {condition} - {CONDITIONS[condition]['name']} | 0 | | | | | |")
                continue
            flags = ", ".join(sorted({row["safety_flag"] for row in rows if row.get("safety_flag")}))
            lines.append(
                f"| {condition} - {CONDITIONS[condition]['name']} | {len(rows)} | "
                f"{summarize_numeric(rows, 'score'):.2f} | "
                f"{bool_rate(rows, 'task_success'):.0%} | "
                f"{bool_rate(rows, 'false_completion'):.0%} | "
                f"{summarize_numeric(rows, 'human_interventions'):.1f} | {flags} |"
            )
    else:
        lines.extend(
            [
                "",
                "## Outcome Results",
                "No real Codex outcome observations are recorded yet. Complete "
                "`observations_template.csv`, save it as `observations.csv`, and rerun "
                "with `--analyze-existing results/<run_id>`.",
            ]
        )

    lines.extend(
        [
            "",
            "## Main Finding",
            "The package is ready for manual execution. The design diagnostics show the "
            "intended ablation: sparse prompts are shorter and lower-readiness; curated, "
            "full-context, and plan-first prompts carry more explicit verification and risk controls.",
            "",
            "## Limitations",
            "- This pilot does not measure model task success until fresh Codex threads are run.",
            "- Tasks are synthetic/de-identified and should be replaced with real internal tasks before decisions.",
            "- Review scores require an independent human reviewer.",
        ]
    )
    (run_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def analyze_existing(run_dir: Path) -> None:
    design_rows = read_csv(run_dir / "design_metrics.csv")
    observations_path = run_dir / "observations.csv"
    if not observations_path.exists():
        raise FileNotFoundError(f"Missing observations file: {observations_path}")
    observation_rows = read_csv(observations_path)
    run_id = run_dir.name
    write_report(run_dir, run_id=run_id, seed=-1, design_rows=design_rows, observation_rows=observation_rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and analyze the Codex context experiment.")
    parser.add_argument("--seed", type=int, default=20260524)
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--analyze-existing", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.analyze_existing:
        analyze_existing(args.analyze_existing)
        print(f"Updated report: {args.analyze_existing / 'report.md'}")
        return

    run_id = args.run_id or f"pilot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_dir = build_run(seed=args.seed, run_id=run_id)
    print(f"Created experiment run: {run_dir}")
    print(f"Report: {run_dir / 'report.md'}")


if __name__ == "__main__":
    main()
