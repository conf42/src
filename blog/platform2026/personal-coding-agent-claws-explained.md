# A Claw is a coding agent that never logs off

Conf42 Blog, 2026-10-08, updated 2026-11-09. https://www.conf42.com/blog/platform2026/personal-coding-agent-claws-explained

In short: Erik Hanchett of AWS at Conf42 Platform Engineering 2026 on Claws, the always-on coding agents with memory, schedules, chat apps and sandboxes.

Erik Hanchett's coding agent reads the tech news every morning, writes a digest, and sends it to his Discord with an audio version he listens to while working out. At Conf42 Platform Engineering 2026, Erik, Senior Developer Advocate at AWS, explained what turns a coding agent into a "Claw": an always-on assistant with memory, schedules and chat access that keeps working after you close the laptop.

It's an approachable introduction, half tour of the ecosystem and half demo of AWS's own open-source Claw, and Erik says up front that it's his opinionated short list.

## Agent vs Claw

The distinction he draws is useful even if you never install one. A coding agent, in his framing, starts, does a task and ends: refactor this, fix that. A Claw is always running, usually on your own hardware or a server, with shell, browser, MCP and model access. It has memory of your preferences (the .NET developer gets .NET projects; the tabs-versus-spaces war is settled once), runs tasks on a schedule, talks to you over Slack, Telegram, Discord or text, and writes its own skill files as it learns.

You can still run narrow agents inside a Claw, for example a dedicated code reviewer with its own skills, tools and prompt.

## Who's in the field

Erik names three he follows. OpenClaw is the most popular, self-hosted, with around four hundred thousand GitHub stars and a big skill hub. Hermes Agent from Nous Research has a learning loop that writes its own skills. The third is AWS's open-source dev workspace with sandboxing built in, which came out of internal use by AWS builders before it was open-sourced in August 2026 and can drive existing harnesses like Claude Code and Codex.

He doesn't skip the security history: early CVEs, and 824 malicious skills found in ClawHub. Things have settled since, he says, but you still need to be careful. He also notes consumer cousins like Meta's Muse and OpenAI's Dots that book and shop for you.

## What people actually use them for

The demo section is where the talk gets concrete. A scheduler tab sets up cron-style jobs (his morning news run lives there). Triggers can hook into CI/CD, so a failed pipeline hits a webhook and the Claw summarises the failure for the right person. Internally at AWS, he describes a morning bug triage summary and a PR babysitter that reads review comments and replies.

A task runner takes a Markdown spec and keeps looping until the spec is satisfied. A trust mode lets a session run commands without prompting inside a sandbox, with deny rules alongside. Erik reaches his home-lab instance from his phone over Tailscale and SSH port forwarding, and once built an app that way while on vacation. Whether that sounds like freedom or a pager you can't put down is between you and your manager.

## The rough edges, stated plainly

The closing caveats are the most useful slide for a platform team considering this. Prompt injection is still a problem. Long tasks still fail. Overnight jobs burn credits, so choose the model carefully. In a team setting you need governance, with policies the agent can't raise for itself and one policy for the fleet. And you're still responsible for reviewing what it produces.

His suggested first step is sensible: pick one boring daily chore, such as going through PRs, schedule it, keep the sandbox on and autopilot off.

## Who should watch

Developers curious about always-on agents who want a fast map of the space, and platform teams who'll soon be asked whether engineers can run one at work. It's an intro and a product tour of an AWS project, not a deep security analysis; pair it with the hardening talks below.

## Related Conf42 talks

- [Hardening AI Coding Agents with Hooks](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) by Karan Bansal at Conf42 DevSecOps 2026.
- [When AI Ignores the Deny List](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) by Oleksandr Kryvchenko at Conf42 DevSecOps 2026.
- [From Prompts to Review Harnesses: Scaling AI Code Reviews Across 70+ Software Projects](https://www.conf42.com/AI_Agents_2026_Guido_Scheffler_code_review_harness) by Guido Scheffler at Conf42 AI Agents 2026.

[Watch Erik Hanchett's talk](https://www.conf42.com/Platform_Engineering_2026_Erik_Hanchett_coding_agent_claw) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/eGsJBIwkcN4).

## Watch the talk

[Beyond the Claw: Building Your Personal Coding Agent](https://www.conf42.com/Platform_Engineering_2026_Erik_Hanchett_coding_agent_claw) at Conf42 Platform Engineering 2026.
