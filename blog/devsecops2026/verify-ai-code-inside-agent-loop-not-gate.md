# Verify AI-written code inside the agent's loop, not at the gate

Conf42 Blog, 2026-09-29, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/verify-ai-code-inside-agent-loop-not-gate

In short: At Conf42 DevSecOps 2026, TestSprite co-founder Yunhao Jiao argues coding agents need runtime checks while they work, using the CoderCup experiment.

Security and quality gates were built for code arriving at human typing speed. At Conf42 DevSecOps 2026, Yunhao Jiao, CEO and co-founder of TestSprite and a former AWS software engineer, argued that coding agents broke that assumption, and that the useful question is no longer whether to verify AI-written code but when. His answer: inside the agent's own loop, while it works, not at the pull request.

Honest scope first. TestSprite builds a testing agent, and the evidence in the talk comes from CoderCup, an experiment his company ran and open-sourced. Read it as a vendor's argument backed by its own data, which is still more data than most opinions on this topic arrive with.

## The gate cannot read what arrives

Jiao's starting point is volume. An agent can run for hours and produce thousands of lines at a time. He shows one PR from his own company with roughly 40,000 lines added and more than 50,000 removed, and asks the room whether anyone really reviews that by hand. Agents are also not reliably correct, and they lose track of requirements as long tasks overflow the context window, so constraints quietly drop out mid-build.

The industry response is to let machines check machines, and he walks through the weaknesses of each option. AI code review reads the code but usually does not run the app, so it misses runtime issues. Agent-written unit tests tend to reflect the code rather than the spec, so a wrong assumption gets tested as correct. Integration tests catch more, but only if something keeps running them.

## What CoderCup measured

In the experiment, several frontier coding agents built the same ten-phase application from the same requirements: a web app predicting World Cup results, timed to the tournament. A separate testing agent acted as referee, checking after each phase which features actually worked and feeding failures back.

Three findings carry the talk. First, the loop lifts every agent: according to the abstract, agents got tasks right on the first attempt about 80% of the time and reached 94% once the verification loop caught failures and drove fixes. Second, the loop matters more than the model: the agent with the best final score started near the bottom on first tries, and in their run it was also the cheapest. Third, every agent breaks its own working features. The abstract puts it at between 31 and 57 times per build, and those regressions stayed invisible until something actually ran the application.

That third number is the one to show your team. A gate at the end sees the final state; it does not see the forty-odd times a feature worked, broke, and maybe got fixed by accident.

## Build the loop, keep the tests

His practical advice is to design the loop deliberately: how the agent reads requirements, writes code, and verifies its own work against a running app. And keep every test the loop generates in the workspace. Each iteration's UI and backend integration tests become assets for the next one, so the suite grows with the code base and old edge cases keep getting checked as the agent adds features.

He also pushes back on the cost objection. In the enterprises his team works with, he says a cloud run of hundreds of test cases usually takes around ten minutes, and the loop can be wired in through a CLI, MCP or GitHub Actions on every PR without a human in it. Ten minutes per iteration is cheap next to a regression found by a customer.

## Who should watch

Engineering leads whose PRs have quietly tripled in size since agents arrived, and platform teams deciding where verification sits in an agent-driven pipeline. It is short and argument-led rather than a deep technical demo, and it is clearly a pitch for agentic testing as a category. Bring your own scepticism about the benchmark, then go look at the open-source CoderCup data.

## Related Conf42 talks

- [Ruben Marcus Luz Paschoarelli on running AI coding loops without shipping fiction](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence).
- [Liran Yushinsky on LLM-as-judge for testing non-deterministic code generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen).
- [Sylvain Kalache on what happens when AI writes the code you debug](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sylvain_Kalache_vibes_outages_writes).

[Watch Yunhao Jiao's talk](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates)

[Watch the talk on YouTube](https://youtu.be/FKRzJSMkLe8).

## Watch the talk

[Verification Timing: Why Checking AI-Written Code at the Gate Is Already Too Late](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates) at Conf42 DevSecOps 2026.
