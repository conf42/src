# Repository-scale code changes are a planning problem, not a prompt

Conf42 Blog, 2025-10-14, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/repo-scale-code-changes-are-planning-problems

In short: Janak Bhalla (Microsoft) at Conf42 Prompt Engineering 2025 on CodePlan, which pairs LLM planning with AST chunking, RAG and static analysis for migrations at scale.

Split a source file every 500 characters and hand the pieces to an LLM, and you'll get confident edits to half a function. At Conf42 Prompt Engineering 2025, Janak Bhalla of Microsoft explained how CodePlan approaches repository-wide changes such as package migrations, build fixes and static-analysis repairs: treat the job as planning, chunk code along its syntax tree, ground the model with retrieval, and verify every step with static analysis.

It's a well-structured architecture talk. No live demo, but the three building blocks are explained clearly enough to apply in your own tooling.

## Three reasons a bare LLM can't migrate your repo

Janak names the obstacles first. Context windows: real repositories don't fit in one API call, so the work has to be split and orchestrated. Knowledge cutoff: if a library changed yesterday, the model doesn't know, and APIs change constantly. Hallucination: models write syntactically pretty code that calls APIs that don't exist or skips edge cases, which is unacceptable for a change touching hundreds of files.

His conclusion: an LLM alone, however capable, can't reliably do repository-scale transformation without a human at every step. Something has to wrap it.

## Plan first, then generate

CodePlan, as he describes it, is a neuro-symbolic framework that pairs LLMs with symbolic reasoning and static analysis. The input is the repository, a knowledge base of transformation instructions and examples, and static-analysis reports or logs. The engine does four things: contextualises prompts with the most relevant code, plans and orchestrates the steps, analyses dependencies using abstract syntax trees, and validates the output with static analysis. Did this edit break the build? Will it break downstream dependents?

The key idea is the reframing. Instead of asking the model to solve the whole change in one shot, ask it to break the task into structured steps, choose tools and order, then execute with feedback. Typical jobs: C# package migrations across a repo, Python dependency updates spanning services, adding type annotations at scale.

## Chunk along the syntax tree

The most memorable section compares character-based chunking with AST-based chunking. Character splits cut through functions, strand an include statement on its own, and leave the closing semicolon in the next chunk: the fragments are syntactically invalid and the model gets confused. AST chunks follow real boundaries (includes, using declarations, whole functions, control structures), so each chunk is valid code with intact meaning.

He walks through a tiny Python greet function and its AST (a function node, its name and argument, a return containing a string concatenation) to show why a structured view helps. The model stops guessing whether it's looking at a loop or a call.

## Retrieval for what the model doesn't know

RAG covers the knowledge-cutoff and hallucination problems. The retriever searches the instruction knowledge base, documentation, examples and existing code for what the transformation needs; the generator feeds that alongside the AST chunks to the LLM. The model then works from your current APIs and patterns, not from whatever it remembered in training.

## Honest about the limits

Janak cited organisations doing mainframe migrations reporting large reductions in modernisation timelines, and fewer manual errors thanks to the validation loop. He's equally clear on the limits: very large codebases still strain context, hallucinations are reduced but not gone, repository-scale analysis is computationally heavy, and dynamic languages like Python and JavaScript are harder because static analysis has less to grip. What's next, in his view: multi-agent systems, learning from developer edits, and integration into IDEs and CI/CD.

## Who should watch

Developers and platform teams building or buying AI tooling for migrations, dependency upgrades or lint-driven fixes, and anyone whose AI coding experiments fall apart beyond a single file. If you already run AST-aware retrieval in production, this is a tidy confirmation rather than news.

## Related Conf42 talks

- [From Prompts to Review Harnesses: Scaling AI Code Reviews Across 70+ Software Projects](https://www.conf42.com/AI_Agents_2026_Guido_Scheffler_code_review_harness) by Guido Scheffler at Conf42 AI Agents 2026.
- [From Patchwork to Picasso: Refactoring 80+ Angular projects and what went wrong](https://www.conf42.com/DevOps_2025_Muhammad_Ahsan_Ayaz_angular_refactoring_projects) by Muhammad Ahsan Ayaz at Conf42 DevOps 2025.
- [Who Judges the AI Agent? LLM-as-Judge for Testing Non-Deterministic Code Generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen) by Liran Yushinsky at Conf42 AI Agents 2026.

[Watch Janak Bhalla's talk](https://www.conf42.com/Prompt_Engineering_2025_Janak_Bhalla_code_developers_scale) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/EWbgZYC_JsI).

## Watch the talk

[AI-Powered Code Transformations at Scale: Empowering Developers](https://www.conf42.com/Prompt_Engineering_2025_Janak_Bhalla_code_developers_scale) at Conf42 Prompt Engineering 2025.
