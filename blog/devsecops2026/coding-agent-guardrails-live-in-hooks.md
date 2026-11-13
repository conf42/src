# Coding agent guardrails belong in hooks, not in the model

Conf42 Blog, 2026-09-02, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/coding-agent-guardrails-live-in-hooks

In short: Karan Bansal of ArmorCode at Conf42 DevSecOps 2026 shows pre-tool-use hooks that block dangerous commands, secret reads and fake green builds in under 100ms.

The guardrails that hold up around AI coding agents don't live inside the model, they live in the harness around it. That's the one-line pitch Karan Bansal, Head of AI at ArmorCode, opened with at Conf42 DevSecOps 2026, and the rest of the talk is a field report from the MIT-licensed Claude Code hooks repo he maintains: real blocking scripts, OWASP mapping, and latency numbers measured on his own laptop and dated.

## A developer with no judgment, at machine speed

Karan's framing of the problem is blunt: an AI coding agent is a developer with no judgment. On day one it gets your shell, your files, web fetch, MCP servers and `git push`, and it can spawn subagents, so it recurses. Every action is the model's call, dozens per minute.

The textbook answer is a sandbox, and Karan agrees the textbook is right. In practice, people launch with skip-permissions, click Allow All within minutes, and work in their main environment because the sandbox breaks half their tooling. System-prompt rules don't rescue you either: they're suggestions to a model that wants to finish its task.

So security has to sit in the seam of the agent loop, between act and observe, at the exact moment a decision becomes a tool call. If you skip sandboxes, hooks are your enforcement layer. If you don't, they're your second one.

## The boring contract is the point

The mechanism fits on one slide. The harness pipes JSON to your hook on stdin (tool name, arguments, session ID, working directory). The hook answers with a decision and a plain-language reason, or exits with code 2 to block. The reason goes back to the model, so it adapts instead of retrying the same command.

What's missing from that picture matters most: no LLM in the middle. The hook is a separate process the model never sees, so prompt injection can't talk its way past it. Claude Code exposes 31 hook events; Karan says six carry the security load, with pre-tool-use the one to remember.

## Hooks you can run this week

The repo's examples are concrete:

- **Block dangerous commands**: a regex table with IDs and reasons (rm on your home directory, dd to a disk device, fork bombs, curl piped into a shell), three safety levels set by an environment variable, and an ask mode, contributed by the community, that escalates gray-zone commands to the human.
- **Protect secrets**: file patterns for `.env`, SSH keys and cloud credentials, plus Bash patterns for environment dumps and exfiltration via curl, scp, rsync or netcat. `.env.example` stays readable so the agent can still work.
- **Protect tests**: the "fake green" problem, where an agent under pressure deletes, renames or skip-marks a failing test. The build goes green and the evidence disappears.
- **Config guard**: the newest attack surface. Agent config files like `CLAUDE.md`, Cursor rules and `.claude/settings.json` are being used to plant hidden instructions and persistent hooks, so you guard the files that configure your guards.

The demo clips, recorded in a throwaway sandbox with fake credentials, show the agent trying to read `.env`, getting denied with a reason, hunting for another way, and settling for the sanitised template. Which is roughly how a determined intern behaves, minus the Slack message.

## Sync decides, async observes

The performance rule is what makes this deployable. Enforcement hooks sit on the critical path and get a budget under 100 milliseconds; observers like the session logger run async and get no seat on that path. Karan's arithmetic: 60 tool calls through a 200ms synchronous hook is two minutes of waiting, and slow security gets disabled by the people it protects.

His measured numbers: the flagship hook at a median of about 31.7ms end to end on an Apple M3 Pro, most of it Node startup. A guard pack running six checks in one process takes around 38ms, against roughly 199ms when run separately.

He's also honest about scope. Against the OWASP LLM Top 10 for 2026, six of ten risks have a hook-shaped answer and three are out of reach at runtime. Nobody reliably prevents prompt injection; hooks decide what an injected agent still gets to do.

## Who should watch

Security engineers who've been asked to "approve Claude Code" for a team, and developers who already run agents with broad permissions. The patterns port to Codex, Copilot and Cursor, which Karan says converged on the same shape. If you want a theory of agent alignment, look elsewhere; this is plumbing, and that's its strength.

## Related Conf42 talks

- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar at Conf42 Large Language Models 2026.
- [Make your app its own sandbox](https://www.conf42.com/Platform_Engineering_2026_Leanid_Piliptsevich_sandbox_app_make) by Leanid Piliptsevich at Conf42 Platform Engineering 2026.
- [Beyond the Claw: Building Your Personal Coding Agent](https://www.conf42.com/Platform_Engineering_2026_Erik_Hanchett_coding_agent_claw) by Erik Hanchett at Conf42 Platform Engineering 2026.

[Watch Karan Bansal's talk](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/yV_k8zLGuHo).

## Watch the talk

[Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) at Conf42 DevSecOps 2026.
