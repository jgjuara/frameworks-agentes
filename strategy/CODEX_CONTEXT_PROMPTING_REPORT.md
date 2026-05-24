# Report: Context and Prompting for Verifiable Codex Tasks

**Abstract:** This report answers how much context and prompting a research team should give Codex when the task is verifiable, computable, and expected to produce a concrete solution. The evidence supports a context-minimal but verification-rich workflow: give Codex enough curated context to identify the target, constraints, and success criteria; move durable rules into `AGENTS.md` or skills; let the agent retrieve more repository context as needed; and require executable validation. More context is not automatically better. Long-context research, SWE-bench results, and enterprise agent guidance all point to the same operating principle: Codex works best when the prompt defines the problem contract and the environment supplies tests, tools, and reviewable artifacts.

## 1. Research Question

For a research team using Codex on tasks such as computational analysis, reproducible notebooks, research-code fixes, simulations, data pipelines, and technical reports:

> How much context and prompting should be provided up front for a verifiable task whose expected output is a computable solution?

The practical answer is:

- Use a **short task contract** as the prompt, normally 200-800 words for ordinary tasks and 800-1,500 words for high-risk or cross-file tasks.
- Include **high-signal context**, not background dumps: goal, files, constraints, commands, known failures, acceptance criteria, and escalation triggers.
- Put persistent team rules in `AGENTS.md`, not in every prompt. OpenAI documents that Codex loads `AGENTS.md` automatically and that the default combined project-instruction cap is 32 KiB unless configured otherwise.
- Use **one thread per coherent task**. OpenAI explicitly warns that using one thread per project causes bloated context and worse results over time.
- Make the task **verifiable before execution**: tests, reproducibility commands, expected artifacts, issue reproduction steps, or a review rubric.
- Ask Codex to inspect, plan, implement, run checks, and report evidence. Do not ask for uninterrupted free-form generation on non-trivial research work.

## 2. Evidence Base

This report uses three source classes:

1. Official OpenAI Codex documentation and product notes.
2. Scholarly papers and benchmarks on coding agents, long context, retrieval, and reasoning/action loops.
3. Enterprise guidance from GitHub and Anthropic on coding agents, custom instructions, context, and validation.

The most important sources are listed in `CODEX_CONTEXT_PROMPTING_EVIDENCE.md`.

## 3. Core Finding

The central pattern is not "give the model everything." The central pattern is:

```text
small durable instructions
+ curated task prompt
+ agent-driven context retrieval
+ executable verification
+ final human review
```

This fits the strongest evidence:

- OpenAI Codex best practices recommend prompts with goal, context, constraints, and "done when" criteria, and recommend tests, checks, and review before acceptance.
- OpenAI Codex `AGENTS.md` guidance treats durable repository guidance as automatically loaded context, with closer files overriding broader ones.
- SWE-bench frames real software work as codebase + issue + patch + executable test evaluation. The benchmark shows that real tasks require multi-file reasoning, execution environments, and complex context use, not just isolated code completion.
- "Lost in the Middle" shows that long context windows do not guarantee robust use of all context; relevant information can be underused when buried in the middle.
- SWE-agent shows that interface and tool design improve coding-agent performance.
- Agentless shows that simple localization, repair, and validation can compete with complex autonomous scaffolds, which argues against unnecessary orchestration.
- GitHub Copilot guidance says agent tasks should be clear, well-scoped, include acceptance criteria, and identify files when known.
- Anthropic Claude Code guidance makes the same operational point: context windows fill with irrelevant content, persistent instruction files should be pruned and tested, and permissions/sandboxing reduce approval fatigue.

## 4. Context Budget Recommendation

Use these starting budgets for Codex tasks in research repositories.

| Task class | Up-front prompt | Up-front context | Let Codex discover? | Required verification |
|---|---:|---|---|---|
| R0 read-only explanation | 100-300 words | 0-3 files or paths | Yes | source citations or file references |
| R1 local code/doc fix | 200-600 words | failing command, relevant file paths, expected behavior | Yes | targeted tests/lint/type checks |
| R2 research computation | 500-1,200 words | data source, methods constraints, relevant scripts/notebooks, output format | Yes, within allowed data scope | reproducible command and artifact review |
| R3 sensitive or externally consequential work | 800-1,500 words | explicit risk boundaries, data rules, approval gates, validation rubric | Limited | human review plus automated checks |
| R4 safety/legal/medical/financial/public policy release | Codex can assist only inside a governed workflow | governance packet required | Restricted | domain expert sign-off outside Codex |

The important variable is not word count. The important variable is **context density**: each paragraph should change what Codex will do.

## 5. Prompt Contract

Every non-trivial computable task should include these fields:

1. **Mission:** the concrete artifact or behavior that must exist.
2. **Authoritative context:** files, datasets, issue links, standards, or examples.
3. **Constraints:** architecture, data handling, dependency, security, and scope limits.
4. **Allowed actions:** what Codex may read, edit, run, and install.
5. **Forbidden actions:** destructive, external, sensitive, or high-cost actions requiring approval.
6. **Acceptance criteria:** tests, metrics, output files, reproducibility criteria, and review checklist.
7. **Escalation triggers:** contradictions, missing data, test ambiguity, privacy risk, or irreversible action.
8. **Final evidence package:** changed files, commands run, validation result, assumptions, and residual risks.

For a verifiable task, the acceptance criteria matter more than prose detail. A short prompt with a runnable failing test is better than a long prompt with no test.

## 6. What Not To Put In The Prompt

Avoid putting these into one-off prompts:

- Stable repository conventions that belong in `AGENTS.md`.
- Repeated workflow instructions that should become a skill.
- Full documents when a specific section or claim is relevant.
- Large data excerpts when Codex can inspect files locally.
- Long histories of prior discussion unless a decision must be preserved.
- Vague preferences such as "high quality" without an observable criterion.

The prompt should not become a second repository. It should point Codex to the right repository evidence.

## 7. Verifiable Task Pattern

For tasks that should create a computable solution, use this cycle:

```text
Brief -> inspect -> plan -> implement -> run checks -> repair -> summarize evidence -> human review
```

The user provides the first and last gates. Codex handles the middle loop, but only within defined boundaries.

For research work, this means:

- Specify raw data locations and whether they are immutable.
- Require reproducibility commands.
- Require methods notes that separate data, model, findings, interpretation, and limitations.
- Require no sensitive data in generated documentation.
- Require exact test or validation commands where feasible.

## 8. Answer To "How Much Context?"

Give **the minimum context needed to make the first plan correct**, plus enough verification information to let Codex detect failure.

That usually means:

- **Always include:** goal, done criteria, validation commands, and constraints.
- **Usually include:** relevant paths, failure logs, examples of expected output, and source priority.
- **Sometimes include:** design rationale, domain definitions, prior decisions, and risk gates.
- **Rarely include:** complete documents, whole data dumps, entire chat histories, or broad background reading.

If Codex needs more, instruct it to inspect the repository and ask only when the missing information cannot be discovered safely.

## 9. Recommended Team Standard

Adopt this operating standard for the research team:

1. Keep a concise repo-level `AGENTS.md` with setup, validation, data-handling, and review rules.
2. Use a task brief for all R1+ tasks.
3. Keep one Codex thread per coherent task.
4. Promote repeated workflows into skills.
5. Require executable verification for any computable artifact.
6. Track failures and update `AGENTS.md`, skills, or templates only after repeated friction.
7. Run a monthly prompt/context ablation experiment using `CODEX_CONTEXT_PROMPTING_EXPERIMENT.md`.

## 10. References

- OpenAI, Codex best practices: https://developers.openai.com/codex/learn/best-practices
- OpenAI, Codex prompting: https://developers.openai.com/codex/prompting
- OpenAI, custom instructions with `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md
- OpenAI, Introducing SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- OpenAI, Introducing GPT-5.3-Codex: https://openai.com/index/introducing-gpt-5-3-codex/
- Jimenez et al., SWE-bench: https://arxiv.org/abs/2310.06770
- Yang et al., SWE-agent: https://arxiv.org/abs/2405.15793
- Xia et al., Agentless: https://arxiv.org/abs/2407.01489
- Liu et al., Lost in the Middle: https://arxiv.org/abs/2307.03172
- Chen et al., Evaluating Large Language Models Trained on Code: https://arxiv.org/abs/2107.03374
- Wei et al., Chain-of-Thought Prompting: https://arxiv.org/abs/2201.11903
- Lewis et al., Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- Yao et al., ReAct: https://arxiv.org/abs/2210.03629
- Shinn et al., Reflexion: https://arxiv.org/abs/2303.11366
- Galster et al., Configuring Agentic AI Coding Tools: https://arxiv.org/abs/2602.14690
- GitHub Docs, Best practices for using Copilot to work on tasks: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
- GitHub Docs, Prompt engineering for Copilot: https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
- Anthropic, Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic, Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
