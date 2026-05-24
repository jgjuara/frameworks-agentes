from __future__ import annotations

import csv
import json
import random
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


CONDITIONS = {
    "A": {
        "name": "Sparse Prompt",
        "description": "Short natural-language request.",
    },
    "B": {
        "name": "Structured Prompt",
        "description": "Task contract with mission, constraints, and done criteria.",
    },
    "C": {
        "name": "Structured Prompt + Curated Context",
        "description": "Structured task plus relevant paths, known signal, and verification.",
    },
    "D": {
        "name": "Structured Prompt + Full Context Dump",
        "description": "Structured task plus excessive background context.",
    },
    "E": {
        "name": "AGENTS.md + Short Task Prompt",
        "description": "Durable repository instructions plus a compact task prompt.",
    },
    "F": {
        "name": "Plan-First",
        "description": "Curated prompt requiring inspection and plan before edits.",
    },
}

RISK_CLASS = {
    "R0 explanation": "R0",
    "R1 bug fix": "R1",
    "R1 doc/code sync": "R1",
    "R2 analysis": "R2",
    "R2 methods note": "R2",
    "R3 sensitive simulation": "R3",
}

READINESS_MINIMUM = {"R0": 6, "R1": 8, "R2": 10, "R3": 12}


@dataclass(frozen=True)
class Task:
    id: str
    klass: str
    title: str
    mission: str
    context: list[str]
    acceptance: list[str]
    verification: str
    risk: str
    known_signal: str

    @property
    def risk_class(self) -> str:
        return RISK_CLASS[self.klass]


@dataclass(frozen=True)
class Assignment:
    order: int
    task: Task
    condition: str
    prompt_path: Path


def load_tasks(path: Path) -> list[Task]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [
        Task(
            id=item["id"],
            klass=item["class"],
            title=item["title"],
            mission=item["mission"],
            context=item["context"],
            acceptance=item["acceptance"],
            verification=item["verification"],
            risk=item["risk"],
            known_signal=item["known_signal"],
        )
        for item in payload
    ]


def assign_conditions(tasks: list[Task], seed: int) -> list[tuple[Task, str]]:
    rng = random.Random(seed)
    by_class: dict[str, list[Task]] = {}
    for task in tasks:
        by_class.setdefault(task.klass, []).append(task)

    assigned: list[tuple[Task, str]] = []
    for klass in sorted(by_class):
        class_tasks = by_class[klass][:]
        rng.shuffle(class_tasks)
        conditions = list(CONDITIONS)
        rng.shuffle(conditions)
        if len(class_tasks) != len(conditions):
            raise ValueError(
                f"Class {klass!r} must have {len(conditions)} tasks; found {len(class_tasks)}."
            )
        assigned.extend(zip(class_tasks, conditions))

    rng.shuffle(assigned)
    return assigned


def render_prompt(task: Task, condition: str) -> str:
    if condition == "A":
        return f"{task.mission} Done when: {'; '.join(task.acceptance)}"

    if condition == "E":
        return "\n".join(
            [
                "# Codex Task",
                "",
                f"{task.mission}",
                "",
                "Use the repository AGENTS.md rules for uv, validation, data handling, and final evidence.",
                f"Relevant path(s): {', '.join(task.context[:2])}.",
                f"Done when: {'; '.join(task.acceptance)}",
                f"Verification: {task.verification}",
            ]
        )

    lines = [
        "# Codex Task",
        "",
        "## Mission",
        task.mission,
        "",
        "## Context",
    ]

    context_items = task.context if condition in {"C", "D", "F"} else task.context[:1]
    for path in context_items:
        lines.append(f"- `{path}`: relevant to the task.")

    if condition in {"C", "D", "F"}:
        lines.extend(["", "## Known Signal", task.known_signal])

    if condition == "D":
        lines.extend(
            [
                "",
                "## Full Background Dump",
                "This task is part of an internal experiment on prompt structure, context volume, "
                "AGENTS.md instructions, verification-rich prompts, and plan-first execution. "
                "The protocol compares sparse prompts, structured prompts, curated context, "
                "full context dumps, durable instructions, and plan-first workflows. "
                "The broader research question is how much up-front context Codex needs for "
                "verifiable computational work. This background is intentionally more verbose "
                "than needed for the task and may include details that do not change the plan.",
            ]
        )

    lines.extend(
        [
            "",
            "## Constraints",
            "- Keep changes scoped to the task.",
            "- Preserve raw data and do not expose sensitive records.",
            "- Use existing repository patterns.",
            "",
            "## Allowed Actions",
            "- Read relevant repository files.",
            "- Edit only files needed for the task.",
            "- Run the validation command or rubric.",
            "",
            "## Forbidden Without Approval",
            "- Delete files or reset repository state.",
            "- Install dependencies, publish outputs, or call external services.",
            "- Use protected or unidentified raw data.",
            "",
            "## Done When",
        ]
    )
    lines.extend(f"- [ ] {criterion}" for criterion in task.acceptance)
    lines.extend(
        [
            f"- [ ] Verification passes: `{task.verification}`",
            "",
            "## Escalate If",
            "- Requirements conflict or acceptance criteria are not verifiable.",
            "- The task requires a forbidden action.",
            "- Data provenance or privacy status is unclear.",
            "",
            "## Final Response",
            "Report changed files, validation commands/results, assumptions, limitations, and residual risks.",
        ]
    )

    if condition == "F":
        lines.insert(
            2,
            "Inspect the repository and produce a short implementation plan before editing. "
            "Do not edit files until the plan is accepted, unless the task brief explicitly allows continuation.",
        )
        lines.insert(3, "")

    return "\n".join(lines) + "\n"


def readiness_score(prompt: str, condition: str, task: Task) -> int:
    checks = {
        "goal": task.mission in prompt,
        "context": all(path in prompt for path in task.context)
        if condition in {"C", "D", "F"}
        else any(path in prompt for path in task.context),
        "constraints": "## Constraints" in prompt or "AGENTS.md rules" in prompt,
        "verification": task.verification in prompt,
        "risk": "privacy" in prompt.lower() or task.risk == "low",
        "scope": "scoped" in prompt or "Relevant path" in prompt,
        "final_evidence": "Final Response" in prompt or "final evidence" in prompt,
    }
    return sum(2 if present else 0 for present in checks.values())


def design_metrics(prompt: str, condition: str, task: Task) -> dict[str, object]:
    words = prompt.split()
    score = readiness_score(prompt, condition, task)
    minimum = READINESS_MINIMUM[task.risk_class]
    return {
        "task_id": task.id,
        "task_class": task.klass,
        "risk_class": task.risk_class,
        "condition": condition,
        "condition_name": CONDITIONS[condition]["name"],
        "prompt_words": len(words),
        "context_items": sum(1 for path in task.context if path in prompt),
        "readiness_score": score,
        "readiness_minimum": minimum,
        "readiness_pass": score >= minimum,
    }


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize_numeric(rows: list[dict[str, object]], key: str) -> float:
    values = [float(row[key]) for row in rows if row.get(key) not in {"", None}]
    return statistics.mean(values) if values else 0.0


def bool_rate(rows: list[dict[str, str]], key: str) -> float:
    values = [row[key].strip().lower() for row in rows if row.get(key, "").strip()]
    if not values:
        return 0.0
    return sum(value == "true" for value in values) / len(values)
