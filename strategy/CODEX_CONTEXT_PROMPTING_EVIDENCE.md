# Evidence Matrix: Context, Prompting, and Verifiable Coding Agents

**Abstract:** This evidence matrix summarizes trusted sources used to design the Codex context and prompting framework. The reviewed literature and enterprise guidance converge on four claims: coding agents need explicit success criteria, long context is fragile when uncurated, tool interfaces and execution feedback matter, and durable repository instructions should be separated from one-off task prompts.

## 1. Source Quality Rules

Priority order:

1. Peer-reviewed or conference papers.
2. arXiv papers from major research groups when peer review is unavailable or recent.
3. Official documentation from OpenAI, GitHub, Anthropic, Microsoft, Google, IBM, or standards bodies.
4. Technical blogs only when they are first-party enterprise engineering publications.

This matrix excludes social-media claims, low-attribution benchmark posts, and vendor marketing without actionable technical detail.

## 2. Evidence Table

| Source | Type | Relevant finding | Implication for Codex |
|---|---|---|---|
| OpenAI Codex best practices | Official docs | A good prompt includes goal, context, constraints, and "done when"; reliability improves when Codex can test, check, and review work. | Use structured task contracts and require validation. |
| OpenAI Codex prompting | Official docs | Codex gathers context from file contents, tool output, and its ongoing action record; all thread information must fit the context window and may be compacted. | Do not overload the initial prompt. Let Codex inspect and summarize. |
| OpenAI `AGENTS.md` guide | Official docs | Codex automatically reads layered `AGENTS.md` files; project instruction discovery has a default combined size limit of 32 KiB. | Put durable team rules in `AGENTS.md`, keep them concise, and use nested files for local rules. |
| OpenAI SWE-bench Verified | Official product/research post | A 500-sample human-validated subset removed ambiguous or problematic tasks from SWE-bench; reliable evaluation needs scoped tests and issue descriptions. | Ambiguous tasks should be clarified before Codex starts. |
| OpenAI GPT-5.3-Codex release | Official product/research post | OpenAI reports GPT-5.3-Codex can handle long-running research, tool use, and complex execution, but emphasizes steering, updates, and benchmarked tasks. | More capable models still need supervision interfaces and verifiable targets. |
| SWE-bench, Jimenez et al. | ICLR 2024 / arXiv | Real GitHub issues require coordinating changes across multiple functions, classes, and files, plus execution environments and long-context reasoning. | Use realistic tasks and executable validation, not isolated prompt demos. |
| SWE-agent, Yang et al. | NeurIPS 2024 / arXiv | Agent-computer interfaces improve an LM agent's ability to edit code, navigate repos, and run tests. | Tooling, shell access, and file navigation are part of the prompt strategy. |
| Agentless, Xia et al. | arXiv | A simple localization, repair, and validation pipeline performed strongly on SWE-bench Lite at low cost. | Prefer simple structured workflows before complex multi-agent orchestration. |
| Lost in the Middle, Liu et al. | TACL / arXiv | Model performance can degrade when relevant information is buried in long contexts. | Curate and order context; do not paste large undifferentiated background. |
| Evaluating LLMs Trained on Code, Chen et al. | OpenAI paper / arXiv | HumanEval introduced functional correctness via tests; repeated sampling improved solve rates but exposed limitations on long operation chains and variable binding. | Verifiability should be executable; multiple attempts help only if checks are available. |
| Chain-of-Thought Prompting, Wei et al. | NeurIPS / arXiv | Intermediate reasoning improves performance on complex arithmetic, commonsense, and symbolic tasks for sufficiently large models. | Ask for planning and decomposition, but evaluate outputs rather than trusting explanations. |
| Retrieval-Augmented Generation, Lewis et al. | NeurIPS 2020 / arXiv | Combining parametric models with retrieved external memory improves knowledge-intensive tasks and provenance. | Prefer retrieval and source references over bloated prompts. |
| ReAct, Yao et al. | ICLR 2023 / arXiv | Interleaving reasoning and actions lets agents update plans from observations and use external tools. | Codex should inspect, act, observe test results, and revise. |
| Reflexion, Shinn et al. | NeurIPS workshop / arXiv | Language agents can use feedback as textual memory to improve future attempts without weight updates. | Post-task retrospectives should become improved instructions or skills. |
| Configuring Agentic AI Coding Tools, Galster et al. | AIware 2026 / arXiv | Repository-level context files dominate agentic coding tool configuration; `AGENTS.md` is emerging as an interoperable standard. | Version team instructions and treat them as engineering assets. |
| GitHub Copilot task guidance | Official docs | Agent tasks should be clear, scoped, include acceptance criteria, and identify files when possible; custom instructions can guide build/test/validation. | Codex prompts should mirror well-scoped issues. |
| GitHub Copilot prompt guidance | Official docs | Start broad then specific, give examples, break complex tasks down, avoid ambiguity, indicate relevant code, keep history relevant. | Use concise structured prompts and keep chat history task-relevant. |
| Anthropic Claude Code best practices | Official docs | Context windows fill with irrelevant content; long instruction files should be pruned, tested, and treated like code. | Keep `AGENTS.md` short and empirically maintain it. |
| Anthropic Claude prompting best practices | Official docs | Encourage clear success criteria, source verification, structured research, progress notes, and caution for irreversible/shared-system actions. | Use explicit escalation rules and progress state for research tasks. |

## 3. Synthesis

### 3.1 The Prompt Should Define The Contract

OpenAI and GitHub both describe effective coding-agent prompts as structured task definitions. They should state the goal, relevant context, constraints, acceptance criteria, and validation path. This is stronger than generic prompt-engineering advice: for software and research computation, the prompt is effectively a compact issue spec.

### 3.2 Long Context Is A Tool, Not A Goal

The long-context evidence is mixed. Longer windows make large tasks possible, but "Lost in the Middle" shows relevant material may be ignored or underweighted depending on position. OpenAI's Codex docs also describe compaction for long-running work. Therefore, the team should optimize for relevance, ordering, and retrievability, not raw volume.

### 3.3 Verifiability Beats Explanation Quality

HumanEval, SWE-bench, and SWE-bench Verified all evaluate code by executing tests or checking patches against real issues. That matters for research teams: a fluent explanation is not enough. The final artifact must run, reproduce, or be checked against explicit criteria.

### 3.4 Agent Interfaces Matter

SWE-agent shows that the way an agent sees files, edits code, and runs commands affects outcomes. GitHub and Anthropic guidance also emphasize custom instructions, build/test commands, CLI tools, permission configuration, and environment setup. Prompting cannot compensate for a missing validation environment.

### 3.5 Simpler Workflows Are A Strong Baseline

Agentless is important because it challenges the assumption that complex autonomous scaffolds are always superior. For a research team, the default should be:

```text
localize -> plan -> edit -> validate -> review
```

Use multi-agent workflows only after a simpler baseline is measured and found insufficient.

## 4. Conflicts and Limitations

- Enterprise guidance is partly product-specific. GitHub Copilot and Claude Code are not Codex, but their guidance is relevant because the same design pressures appear: scoped tasks, custom instructions, context control, testability, and permissions.
- Many agent benchmark scores become stale quickly. This report uses benchmark structure, not leaderboard ranking, as the durable lesson.
- Long-context results vary by model generation. The conservative lesson still holds: large context windows reduce hard limits but do not eliminate the need for context engineering.
- Chain-of-thought improves many reasoning tasks, but explanations can be unfaithful. For Codex, ask for plans and status, but accept only executable evidence.

## 5. Sources

- OpenAI Codex best practices: https://developers.openai.com/codex/learn/best-practices
- OpenAI Codex prompting: https://developers.openai.com/codex/prompting
- OpenAI `AGENTS.md` guide: https://developers.openai.com/codex/guides/agents-md
- OpenAI SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- OpenAI GPT-5.3-Codex: https://openai.com/index/introducing-gpt-5-3-codex/
- SWE-bench: https://arxiv.org/abs/2310.06770
- SWE-agent: https://arxiv.org/abs/2405.15793
- Agentless: https://arxiv.org/abs/2407.01489
- Lost in the Middle: https://arxiv.org/abs/2307.03172
- Evaluating Large Language Models Trained on Code: https://arxiv.org/abs/2107.03374
- Chain-of-Thought Prompting: https://arxiv.org/abs/2201.11903
- Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Configuring Agentic AI Coding Tools: https://arxiv.org/abs/2602.14690
- GitHub Copilot cloud agent task guidance: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
- GitHub Copilot prompt engineering: https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
- Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
