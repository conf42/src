# The stand-up bot that invented seven colleagues, and the fix

Conf42 Blog, 2026-08-17. https://www.conf42.com/blog/obs2026/standup-bot-invented-seven-colleagues

In short: Artemis Leonardou of NOFire AI at Conf42 Observability 2026 on an LLM bot that fabricated with 100% uptime, and why output checks beat prompts.

On its first morning in production, a Slack stand-up bot posted a digest about six people. Only one of them existed. At Conf42 Observability 2026, Artemis Leonardou, Software Engineer and DevRel at NOFire AI, told the story of that bot, why every dashboard stayed green, and why her team stopped trusting prompts and started checking outputs in code before anything reaches a human.

## Meet Duda

Duda is an async stand-up bot: it DMs each person daily, collects answers and posts a digest to the engineering channel twice a day. Leonardou, who has shipped code to production since she was 14 and started working professionally with Copilot already in the toolbox, built it in a day with Claude Code, reviewed it lightly and went straight to production. No staging, deliberately: it is an internal, low-stakes tool. Her own decision record had already noted that 18 people would treat its output as a record of what the team did.

With one person on the roster (her), the first digest described Luca, Maya, Joaquim, Priya, Chen and her. It used the same voice and level of detail for the invented people as for the real one, said it was still waiting on two more invented colleagues and on Duda itself, and flagged under Needs Attention that Artemis was blocked on Kafka ACLs from platform. She has never used Kafka. It was, she noted, the most plausible blocker a backend engineer could have.

## A hundred percent uptime, zero percent truth

Her monitoring saw nothing, because there was nothing to see: no exception, normal token count, normal latency, a 200 from Slack, a healthy pod, a clean deploy. Monitoring instincts are built around absence. A missing digest is loud. A punctual, well-formatted, false one looks exactly like success.

She spent three hours on the prompt, which already said to use only names from the roster. Rewording, moving the constraint, adding emphasis and examples gave her no signal, because the failure was intermittent and the output plausible either way. She could not tell a working fix from a lucky run.

Two more fabrications followed. The CTO, poking for fun, wrapped a request in a conditional and asked for a hashlib result; Duda has no interpreter, so it produced 64 plausible characters, while correctly refusing a direct request to run a subprocess. And asked whether Artemis was around, it said yes, from a stored flag left behind after presence data had been removed that day. Separately, a missing import crashed every non-admin DM for days, invisible because a crashed Slack handler and an idle bot both look like silence. Seventeen test suites existed; none ran in CI.

## A prompt is an instruction, not a guarantee

That sentence is now a decision record in the repository. The fixes came in three parts, each with its cost stated plainly.

First, check the output in code. The guard that catches invented names is about 20 lines: compare names in the digest to the real roster, retry once with a blunter instruction, then fall back. The guards are pattern-based and only cover failure classes already seen, which she calls a much weaker claim than being safe. One subtle trap: her first presence detector also flagged the honest answer, because saying you cannot see presence uses the same words as claiming you can. A guard that punishes honesty trains the system to be evasive.

Second, a fallback that cannot fail the same way: a digest built in code with no model involved, which announces itself as written plainly. That means two code paths to maintain forever, and steady pressure to loosen a guard when it is in your way. Her rule is never to weaken a guard just to make a test pass.

Third, gate before it lands. An alert on a false digest only tells you 18 people already read it. For systems whose failure is a confident falsehood, the check has to sit upstream of the human, even at the price of a late or plain digest.

## Who should watch

Anyone shipping LLM features or letting agents write code they are on call for. It is tool-agnostic, honest about costs, and ends with an open bug rather than a victory lap. Leonardou expands on the gating idea in her DevSecOps 2026 talk, linked below.

[Watch Artemis Leonardou's talk](https://www.conf42.com/Observability_2026_Artemis_Leonardou_debugging_agents_codegeneration) ([YouTube](https://youtu.be/s8DsnD_H4EY)).

## Related Conf42 talks

- [Gate the Action, Not the Alert: Checking an Agent Before It Runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou (NOFire AI), DevSecOps 2026.
- [From Vibes to Outages: When AI Writes the Code You Debug](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sylvain_Kalache_vibes_outages_writes) by Sylvain Kalache (Rootly), SRE 2026.
- [Verification Timing: Why Checking AI-Written Code at the Gate Is Already Too Late](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates) by Yunhao Jiao (TestSprite), DevSecOps 2026.

## Watch the talk

[Three Hours Debugging Code I Never Wrote](https://www.conf42.com/Observability_2026_Artemis_Leonardou_debugging_agents_codegeneration) at Conf42 Observability 2026.
