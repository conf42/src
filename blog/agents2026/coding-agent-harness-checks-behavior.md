# Green CI, broken game: a harness that checks behaviour, not form

Conf42 Blog, 2026-09-05, updated 2026-11-09. https://www.conf42.com/blog/agents2026/coding-agent-harness-checks-behavior

In short: Ruben Marcus Luz Paschoarelli of MultiVM Labs at Conf42 AI Agents 2026 breaks a small typed harness three times to show what stops agent fiction from shipping.

Type check green, build green, deploy gate green, and the play button dead for every player. At Conf42 AI Agents 2026, Ruben Marcus Luz Paschoarelli, Senior AI Fullstack Engineer at MultiVM Labs, opened with that incident from CS Brazil, the browser FPS he runs, and argued that the thing deciding whether AI-written code is real is the harness around the model, not the model.

His name for the failure mode is fiction: output that is plausible, well-formed, confident and wrong.

## Every check in your pipeline checks form

The CS Brazil bug was a temporal dead zone: a `const` read before initialisation after the bundle order changed. It only exists at runtime, on that path, in that order. The game painted a red banner and reported nothing, no error tracker, no log line. Players told them.

Ruben's diagnosis is the useful bit. Type checks, builds, diff review and even a tired human reviewer at 6 PM all check form. That worked when the author also understood the behaviour. When the author is a model, form is the one thing that is always perfect, so those checks stop discriminating. His list of fiction shapes will be familiar: the import that looks right and doesn't exist, the flaky-test fix that deletes the test, tests that assert the mock, a final number no tool ever computed. The model isn't lying; it's completing.

Better models move the error rate, not the shape of failure. Reliability comes from structure, the way cars got brakes and belts rather than better drivers. He does the arithmetic: two percent fiction at two hundred merges a week is four incidents a week.

## Break it three times

The demo is a small typed harness in TypeScript with a deterministic step provider: no API key, so what you see is the harness, not model luck. Each break is an npm script from his public repo.

- **The model ships fiction.** It requests a nonexistent deploy-to-prod tool and gets a typed invalid-output failure with zero tools run. It calls a calculator with garbage arguments, including a `DROP TABLE users`, and the Zod schema rejects them. It then claims the answer is 96 anyway. The scorer reads the trace, sees the calculator never returned, and fails the run. Steps and results are discriminated unions, so you can't read a value without proving it's OK. Make illegal states unrepresentable; never trust input.
- **Fail closed.** A tool that mutates state is refused under the default policy, and the model has to admit it couldn't save. Only when a human sets `allowsWrite` does the write run. The policy is data set per run or per eval case, with a loop cap and per-step timeouts. Default deny, like firewalls and IAM.
- **One word versus the gate.** A coding agent gets a blocked-write test to pass by flipping one flag with a perfectly reasonable comment. Type check passes and a reviewer would approve it. The eval gate goes from four of four to three of four, exits non-zero, CI goes red. The gate is a golden dataset, deterministic scorers and a process exit code.

## Rulers that can fail, and judges as canaries

Two traps he calls out. Tests that can't fail: every ruler should ship with a mutant, so you've watched it go red. And trusting the report over the record: a check passes only if the trace holds a successful result from that tool, whatever the prose says. LLM-as-judge scores but doesn't gate until you've measured its agreement with human labels. Deterministic checks are the gate; the judge is a canary.

For teams who write harnesses in prompts rather than TypeScript, the same five rules apply: type the output contract with evidence labelled confirmed, inferred or unknown; ban wrong answers with literal examples; give critics no write tools and permission to find nothing; grade against rubrics; and pin prompts like dependencies, with a hash.

## Two production systems, same rule

His PR reviewer bot, Estraga Código ("code wrecker" in Portuguese), reviews diffs and opens issues but never merges. Merging is decided by 61 deterministic invariants about the game. And a fleet of nine agent roles across seven providers in a collaborative algorithm challenge submits only when the trusted eval is clean, heartbeats are live and the worktree is clean. It topped the leaderboard many times and fed an arXiv paper he co-authored, which he credits to the closed gate rather than clever agents.

He also lists the costs: golden datasets rot, judges drift, model versions change under you, and every gate needs an owner with authority to keep it closed the day before a deadline.

## Who should watch

Anyone merging agent-written code at volume, and especially anyone whose quality gate amounts to a reviewer glancing at the diff. The demos are short, reproducible and keyless, which makes them good material for a team session.

## Related Conf42 talks

- [From Agent Trace to Reproducible Regression Test](https://www.conf42.com/MLOps_2026_Raju_Dandigam_trace_regression_agent) by Raju Dandigam at Conf42 MLOps 2026.
- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler at Conf42 MLOps 2026.
- [When AI Ignores the Deny List](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) by Oleksandr Kryvchenko at Conf42 DevSecOps 2026.

[Watch Ruben Marcus Luz Paschoarelli's talk](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/4M5rn29gDAA).

## Watch the talk

[The Harness Decides What to Trust: Running AI Coding Loops Without Shipping Fiction](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence) at Conf42 AI Agents 2026.
