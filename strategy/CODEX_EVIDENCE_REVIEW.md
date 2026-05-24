# Evidence Review: Context, Oversight, and Agentic Reliability

**Abstract:** This file reviews trusted evidence relevant to Codex adoption by a research team. The evidence rejects two extremes: fully manual human-in-the-loop supervision is too slow and often weak, while unchecked autonomy is unsafe when tasks are ambiguous, irreversible, or externally consequential. The most defensible pattern is bounded autonomy: strong initial task framing, automated checks during execution, and rigorous final review with selective escalation.

## 1. Codex-specific evidence

OpenAI's Codex best-practices documentation states that Codex reliability improves when the user asks it to create or update tests, run checks, confirm behavior, and review work before acceptance. Crucially, the documentation says Codex can do that loop only if it knows what "good" looks like, and that guidance can come from the prompt or `AGENTS.md`.

Implication: the initial prompt and persistent repo instructions are not cosmetic. They define the agent's evaluation target.

Source: OpenAI Codex best practices, "Improve reliability with testing and review"  
https://developers.openai.com/codex/learn/best-practices#improve-reliability-with-testing-and-review

OpenAI also recommends turning repeatable work into Skills rather than relying on long prompts or repeated back-and-forth. Skills package instructions, context, and supporting logic so Codex applies them consistently across surfaces.

Implication: for a research team, scaling Codex means productizing repeated interaction patterns as team assets.

Source: OpenAI Codex best practices, "Turn repeatable work into skills"  
https://developers.openai.com/codex/learn/best-practices#turn-repeatable-work-into-skills

Codex slash commands also support this operating model: `/init` creates persistent `AGENTS.md` instructions, `/mention` attaches specific files, `/plan` asks for a plan before implementation, `/goal` sets a persistent task target, `/diff` supports review before tests or commit, and `/review` asks Codex to review uncommitted changes, commits, or PR-like diffs.

Source: OpenAI Codex CLI slash commands  
https://developers.openai.com/codex/cli/slash-commands#built-in-slash-commands

Codex configuration supports project-local `.codex/config.toml`, approval policies, sandbox modes, review model settings, AGENTS-related limits, and project trust. This indicates that scalable Codex use is a configuration and governance problem, not only a prompting problem.

Source: OpenAI Codex configuration reference  
https://developers.openai.com/codex/config-reference#configtoml

## 2. Evidence that continuous human-in-the-loop is weak at scale

Automation-bias research shows that people can over-rely on automated recommendations, especially in time-pressured or complex environments. This undermines the idea that frequent human approvals automatically create meaningful control.

Source: Goddard, Roudsari, Wyatt, "Automation bias: a systematic review..."  
https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/

Parasuraman, Sheridan, and Wickens' classic model of automation describes levels and types of human interaction with automation. The practical lesson is that "human involvement" is not a binary control. Oversight quality depends on the function being automated, the authority allocated to the machine, and the human's real ability to intervene.

Source: Parasuraman, Sheridan, Wickens, "A model for types and levels of human interaction with automation"  
https://dblp.org/rec/journals/tsmc/ParasuramanSW00.html

Recent public-sector and governance work echoes this point: human oversight can fail when reviewers lack context, authority, time, or observability. This supports replacing ad hoc approvals with designed control points, logs, and escalation rules.

Source: Human-AI interactions in public-sector decision making, automation bias and selective adherence  
https://academic.oup.com/jpart/article/33/1/153/6524536

## 3. Human-AI design guidance favors calibrated control, not constant interruption

Microsoft Research's 18 Guidelines for Human-AI Interaction, validated with practitioners, emphasize making clear what the system can do, showing contextually relevant information, supporting efficient correction, and handling failure gracefully. The pattern is not "ask the human constantly"; it is "make the system observable and controllable."

Source: Microsoft Research, Amershi et al., CHI 2019  
https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/

Google's People + AI Guidebook recommends defining success, setting user expectations, designing feedback and control mechanisms, explaining AI behavior, and planning for errors and graceful failure. This reinforces the need for up-front framing and end-stage evaluation.

Source: Google PAIR, People + AI Guidebook  
https://pair.withgoogle.com/old-gb/

## 4. Agentic enterprise guidance favors boundaries, evals, and oversight

Anthropic's "Building Effective Agents" distinguishes workflows from agents and argues that effective agentic systems need clear success criteria, feedback loops, meaningful human oversight, and good agent-computer interfaces. It also recommends simple patterns before complex autonomy.

Source: Anthropic, Building Effective Agents  
https://www.anthropic.com/engineering/building-effective-agents

Anthropic's agent eval guidance frames evaluation as a multi-turn, environment-aware problem. For research teams, the important point is that final outcomes alone are insufficient; teams need logs, rubrics, and calibrated review against expert judgment.

Source: Anthropic, Demystifying Evals for AI Agents  
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

IBM's agentic governance guidance argues that scaling is not "more autonomous agents"; it is embedding autonomy with defined control, visibility, accountability, lifecycle governance, monitoring, and prompt optimization. IBM's context-engineering guidance also stresses governed, machine-callable interfaces rather than informal context dumps.

Sources:  
https://www.ibm.com/think/insights/agentic-ai-governance-playbook  
https://www.ibm.com/think/insights/context-engineering-foundation-trusted-ai

NIST's AI Risk Management Framework treats AI risk management as a lifecycle process: mapping context, measuring risk, managing risk, and governing the overall system. For Codex use, this implies that initial context must include risk context and final review must check whether risk controls operated.

Source: NIST AI RMF  
https://www.nist.gov/itl/ai-risk-management-framework

## 5. LLM and agent research supports structured decomposition and review

Long-context research shows that larger context windows do not guarantee reliable use of all supplied information. "Lost in the Middle" found that model performance can degrade when relevant information is buried in long contexts.

Implication: a good Codex intake should prioritize, rank, and summarize context instead of dumping documents indiscriminately.

Source: Liu et al., "Lost in the Middle"  
https://arxiv.org/abs/2307.03172

ReAct showed that interleaving reasoning and action can improve task solving and interpretability by allowing the model to update plans from observations.

Implication: the initial prompt should ask Codex to plan, act, observe, revise, and verify, but the user should review the final artifact rather than every intermediate step.

Source: Yao et al., ReAct  
https://openreview.net/forum?id=WE_vluYUL-X

AI Chains found that decomposing LLM work into chained subtasks improved transparency, controllability, collaboration, and enabled users to "unit-test" subcomponents.

Implication: the scalable alternative to human-in-every-loop is workflow decomposition with checkable intermediate artifacts.

Source: Wu et al., AI Chains  
https://arxiv.org/abs/2110.01691

Reflexion showed that language agents can improve by incorporating feedback into future attempts. For teams, this argues for a structured post-task review record that can become future context, skills, or `AGENTS.md` updates.

Source: Shinn et al., Reflexion  
https://arxiv.org/abs/2303.11366

SWE-bench Verified emphasizes human-validated, real-world software tasks for more reliable evaluation of coding agents. It reinforces that agent performance must be measured against realistic tasks and trusted evaluation sets, not just demos.

Sources:  
https://www.swebench.com/verified.html  
https://openai.com/index/introducing-swe-bench-verified/

## 6. Conclusion from evidence

The evidence supports a strong version of your position for the research-team setting:

- Put the main human cognitive work at task intake and final acceptance.
- Replace mid-run manual approval with automated checks, logs, and predefined escalation rules.
- Do not rely on context-window size as a substitute for context engineering.
- Do not rely on a human checkbox as a substitute for observability, authority, and review quality.

The evidence does not support eliminating all mid-run human intervention. It supports **risk-triggered intervention**, not default intervention.

