# When the LLM writes the code, reading it becomes the job

Conf42 Blog, 2026-05-22, updated 2026-11-09. https://www.conf42.com/blog/llms2026/reading-code-is-the-new-writing

In short: Petras Bazdaras at Conf42 LLMs 2026 argues AI-generated code makes reading and CS fundamentals the core engineering skill, not typing speed.

If a model can produce in seconds what used to take you an afternoon, the afternoon didn't disappear. It moved to after the model stops typing. That is the argument Petras Bazdaras, an aspiring cloud engineer, makes at Conf42 Large Language Models (LLMs) 2026: reading and critically auditing code is now the primary engineering act, and that raises the bar on fundamentals instead of lowering it.

It's a short, opinionated talk with no benchmarks or case study. What it offers is a clear vocabulary for a problem most teams using coding assistants already feel.

## Compiled and working is not the same as good

Before AI, output was a decent proxy for skill: hours of boilerplate, scaffolding and repeated patterns. Now output is cheap, and Petras names the delusion that follows: mistaking code that compiles and runs for good engineering. Shipping code you didn't write and don't understand is a liability.

He sees it in two forms. Cargo-culting AI output means accepting code that looks right but embeds anti-patterns, security gaps or inefficient logic. Blind trust at scale means every accepted suggestion quietly adds technical debt you didn't choose and may not see until production.

His estimate is that developers now spend roughly ninety percent of their time auditing, debugging and maintaining what the model generated. Teams split into two habits: skim and accept, or read and verify, which means tracing logic line by line, testing behaviour and questioning trade-offs. Hidden assumptions and edge cases slip through the first and get caught by the second.

## The autopsy problem

The sharpest idea in the talk is what Petras calls the autopsy problem. When a system fails under load, you're performing an autopsy on logic you didn't write. Because you never built a mental model of it, the debugging intuition simply isn't there. Race conditions, resource leaks and odd edge cases tend to surface only in production, and the on-call pager doesn't care who or what wrote the code. The incident report has your name on it.

LLMs, in his framing, are pattern matchers rather than engineers. They introduce deprecated APIs and outdated library versions, write logic that scales poorly, and know nothing about your team's architectural constraints. Human review matters most on three fronts: security, performance and context.

## The basics, redefined

The fundamentals he means aren't syntax. They are the parts of computer science that let you evaluate any code regardless of who wrote it:

- data structures and algorithmic complexity, including memory layout and why trade-offs matter at scale;
- concurrency and memory management, to catch the race conditions, deadlocks and garbage collection issues that LLMs readily introduce;
- system design and secure coding, including threat modelling.

Using AI to skip learning these doesn't make you faster, Petras argues; it makes you dependent. Problem-solving is a muscle, and an unexercised one weakens. The career shift he describes runs from code typist to system reviewer, with the engineer as a managing editor who audits, secures and scales what the model drafts.

## Who should watch

Junior engineers deciding what to learn while their assistant writes the boilerplate, and leads who need words for why "it passed CI" isn't a review. Senior engineers will agree with most of it; the autopsy framing is the part worth borrowing for your next team discussion.

## Related Conf42 talks

- [Low-Level Computing in a Cloud Native World](https://www.conf42.com/Cloud_Native_2021_Rob_Zuber_cs_fundamentals_fail_us) by Rob Zuber, a pre-LLM case for fundamentals that holds up well.
- [Verification Timing: Why Checking AI-Written Code at the Gate Is Already Too Late](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates) by Yunhao Jiao, on when the reading should happen.
- [Why You Don't Need That New Library: Sticking to Fundamentals](https://www.conf42.com/Chaos_Engineering_2025_Denis_Ermakov_library_fundamentals_need) by Denis Ermakov, the same instinct applied to dependencies.

[Watch Petras Bazdaras's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Petras_Bazdaras_reading_new_writing)

[Watch the talk on YouTube](https://youtu.be/RHsgnNjkiLE).

## Watch the talk

[Reading is the New Writing: Why the AI Era Demands Absolute Mastery of the Basics](https://www.conf42.com/Large_Language_Models_LLMs_2026_Petras_Bazdaras_reading_new_writing) at Conf42 Large Language Models (LLMs) 2026.
