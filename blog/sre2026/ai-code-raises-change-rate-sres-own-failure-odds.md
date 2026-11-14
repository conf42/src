# AI-written code raises the change rate, so SREs must cut the odds

Conf42 Blog, 2026-03-18, updated 2026-11-09. https://www.conf42.com/blog/sre2026/ai-code-raises-change-rate-sres-own-failure-odds

In short: Sylvain Kalache of Rootly at Conf42 SRE 2026 on how AI coding multiplies changes and incidents, slopsquatting, and using AI back against the failure rate.

If incidents scale with the number of changes times the chance each change breaks something, AI coding tools just turned up the first number. At Conf42 Site Reliability Engineering 2026, Sylvain Kalache, Head of AI Labs at Rootly and a former SRE, built his talk around that simple model: developers now ship far more change, SREs cannot control that, but they can and must drive down the probability of failure per change.

Disclosure he makes himself: Rootly sells on-call and incident management, including an AI SRE, so part of the remedies section is his own product category. The diagnosis stands without it.

## C is going up whether you like it or not

He anchors the talk in a rough formula: a constant baseline failure rate plus C, the number of changes in a time window, times P, the probability that a change causes a failure. Then he stacks the evidence on C: survey data that most engineers already use AI tools, vendors reporting large shares of their code written by AI, Cursor's founder citing a billion accepted lines a day in mid 2025, and research across 5,000 engineers at Microsoft, Accenture and another large company showing more commits and more completed tasks.

His own data point is from Rootly customers: from 2023 to the time of the talk, a three times increase in the average number of incidents per customer. And the help is thinning. Ask the author about a broken service and the honest answer may be that their agent wrote it. Specialists are getting rarer as practitioners become generalists. More incidents, less help, and a manager asking why the AI has not made you faster.

## AI fails like humans do, only faster

The catalogue of failure modes is fun and slightly alarming. Unit tests generated to match broken logic, so they pass. A test for Terraform that technically tests something but not the intent. An agent that hallucinated a GitHub repo and deployed it into a customer environment, a case he attributes to Vercel. Slopsquatting: researchers published a package under a name LLMs tend to hallucinate, a huggingface-cli package, and saw about 30,000 downloads in three months with no promotion at all. And a study where an irrelevant line about cats sleeping most of their lives doubled an LLM's error rate on a maths problem.

A friend at Airbnb gave him the counterpoint: for every AI screw-up there is a human equivalent. Slopsquatting is curl-to-bash; deleted files are a fat-fingered rm. We have also been distracted by cats for a long time. His conclusion is to extend blameless culture to LLMs: the question is still which guardrail was missing, not whose prompt it was.

## P is the SRE's job, and the fundamentals matter more

He does not list new magic. The usual tools for keeping P low (testing, review, progressive delivery, rollback and the rest) matter more than ever, because if they were weak before, more change makes it worse. Then he points AI back at the problem:

- **Mutation testing**, long a nice theory, becomes practical. He cites Meta's automated compliance hardening experiment across Facebook, Instagram and WhatsApp: 9,000 mutants, 500 privacy test cases, and engineers accepting more than 70% of the generated tests.
- **LLMs as code review helpers**, the next step after linters and static analysis, since review is becoming the bottleneck.
- **MCP** to give agents the same data sources you use in an incident, and AI SRE agents that pull from GitHub, telemetry and past postmortems to propose root causes. At Rootly, he says, some lower-severity incidents are now handled fully automatically.
- **Toil**: let the agent write postmortem timelines and give the ugly internal tools some CSS.

## Who should watch

SREs and engineering leads watching change volume climb since the team adopted coding agents, and sceptics of AI in production. His advice to the latter is blunt: try it. The C times P framing alone is worth a slide in your next reliability review.

## Related Conf42 talks

- [Verification Timing: Why Checking AI-Written Code at the Gate Is Already Too Late](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates) by Yunhao Jiao.
- [Not Just Syntax: How AI is Changing Code Review](https://www.conf42.com/Python_2025_Shubham_Singh_ai_code_review) by Shubham Singh.
- [LLM Copilots for SRE: Transforming Incident Response and Auto-Remediation](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation) by Susanta Kumar Sahoo.

[Watch Sylvain Kalache's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sylvain_Kalache_vibes_outages_writes) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/RBtq7WjYOdg).

## Watch the talk

[From Vibes to Outages: When AI Writes the Code You Debug](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sylvain_Kalache_vibes_outages_writes) at Conf42 Site Reliability Engineering (SRE) 2026.
