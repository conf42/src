# Claude Code's deny list falls to an absolute path; hooks don't

Conf42 Blog, 2026-09-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/claude-code-deny-list-bypassed-by-absolute-path

In short: Oleksandr Kryvchenko of Keeper Security at Conf42 DevSecOps 2026 bypasses a Claude Code deny list, then closes the gap with a PreToolUse hook and managed settings.

A deny rule for `cat .env` blocks `cat .env`. It doesn't block `/bin/cat .env`, a Python subprocess, or a grep for the variable name. At Conf42 DevSecOps 2026, Oleksandr Kryvchenko, Staff SDET and team lead at Keeper Security, ran 57 secret-reading commands against a reasonable-looking Claude Code `settings.json`, showed which ones slipped through, and then rebuilt the setup around a PreToolUse hook that normalises the command before deciding.

It's a short, practical talk with a terminal on screen most of the time, which is exactly what you want for this topic.

## A sensible policy, a creative agent

The starting point is the kind of `permissions.deny` block most people write: no shell deletions, no outbound `wget` or `curl`, no reading secrets. Oleksandr's version is more careful than most. It catches repeated `rm` invocations, `timeout` used as a wrapper (a common pentest trick), and compound commands.

Then he runs the test suite. Plain reads get denied, as do reads through `cat`. Call `cat` by its absolute path and the policy waves it through. Spawn a subprocess and it's through again. Grep for the variable key without even knowing the file name, and the secret is on screen. His verdict on the result is short: a complete disaster from a security perspective.

The reason is structural. A deny list matches spellings, and a shell offers effectively unlimited ways to spell the same intent. A thousand-line deny policy will still miss a few, and an agent is very good at finding them.

## Normalise first, then decide

The fix is a PreToolUse hook: `settings.json` points at a plain shell script (his is `denyguard.sh`) that runs before every Bash tool call, outside the model. Instead of matching raw strings, it normalises the input, for instance stripping absolute paths, so the core intent is visible before the allow or deny decision. As Oleksandr notes, back-end engineers have been normalising untrusted input for decades; agents are just a new source of it.

Re-running the same 57 commands against the hooked policy, the absolute-path read is denied, subprocess reads are denied, and so are some truncate tricks. He also deliberately leaves useful commands alone: `npm test`, `git status` and running project config scripts with Python still work. The guard should fit your project, he stresses, not someone else's.

## CI is where nobody is watching

On a laptop you can at least watch the agent or approve commands by hand. In CI/CD there's nobody at the keyboard, and his example of a breach on Friday evening that someone discovers on Monday will sound familiar to anyone who has read an incident timeline. Running the test in CI, the plain `settings.json` exposed several secrets straight away, while the hooked version blocked 56 of the read attempts.

## Make the policy immutable

The obvious objection: a user can delete their own hook. Oleksandr walks through the three settings levels (project, user and the org-pushed managed settings). Deny rules from any level always win, so a project deny beats a user allow. Managed `settings.json` lives in a protected path that ordinary users can't overwrite, can be updated centrally, and is the right place for the hook, the deny rules and even a default sandbox requirement.

His layering: a deny list (useful, limited), a PreToolUse hook that reads intent, and managed policy to make both stick.

## Who should watch

Anyone rolling Claude Code out to a team, and especially anyone already running it in a pipeline with real credentials in the environment. The abstract also promises pentest guidance for AI-built apps; the talk itself spends its time on the deny-list gap and the hook, so come for that. Then go and try the absolute-path trick against your own config.

## Related Conf42 talks

- [The Secret to Handling Dynamic Secrets](https://www.conf42.com/Cloud_Native_2025_Rosemary_Wang_secrets_handling_security) by Rosemary Wang at Conf42 Cloud Native 2025.
- [Building Enterprise-ready CI/CD Pipelines using Agentic AI](https://www.conf42.com/DevOps_2026_Chinmay_Gaikwad_cicd_agentic_ai) by Chinmay Gaikwad at Conf42 DevOps 2026.
- [Guardrails First: Designing Safe, Scalable, and Accountable AI Agents for Security Operations](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) by Neal Iyer at Conf42 DevOps 2026.

[Watch Oleksandr Kryvchenko's talk](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/7dBRhCMCYqc).

## Watch the talk

[When AI Ignores the Deny List](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) at Conf42 DevSecOps 2026.
