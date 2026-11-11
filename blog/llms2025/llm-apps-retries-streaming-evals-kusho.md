# Building LLM apps means retries, streaming, queues and evals

Conf42 Blog, 2025-03-20. https://www.conf42.com/blog/llms2025/llm-apps-retries-streaming-evals-kusho

In short: Sourabh Gawande of Kusho AI at Conf42 LLMs 2025 on the plumbing every LLM app needs, from retries and schema checks to background jobs and evals.

Treat an LLM API like any other API and your app will break in production. That is the opening claim from Sourabh Gawande, co-founder and CTO of Kusho AI, at Conf42 Large Language Models 2025. Drawing on 18 months of building Kusho's AI agent for API testing, he walked through the unglamorous engineering that sits between a working prompt and a working product: retries, schema validation, streaming, background jobs and evals, with the specific libraries his team runs in production.

## Plan for the model to be wrong a few percent of the time

The root cause is simple: "LLMs are inherently non-deterministic." A stable REST API might fail around 0.1% of the time in his experience; even the most mature LLMs come in at roughly one to five percent depending on the task. Chain calls, feeding one response into the next prompt, and the error rate compounds. Sourabh's point is that this won't be fixed by waiting for better models. It's the application's job.

So retries and timeouts go in on day one, not after the first incident. In Python his team uses tenacity: a decorator on the function, with stop conditions (three attempts, ten seconds), fixed or random waits, and timeout decorators in the same package. LangChain users get a retry output parser that resends the prompt along with the failed output so the model knows what went wrong.

## Validate structure, then fix the prompt

Structured output is where most failures show up: extra fields, missing fields, a lost bracket. The fix is a schema library rather than hand-rolled checks. Pydantic on Python, Yup on JavaScript, with failed validation triggering a retry. Usually one or two retries clear it.

The useful nuance is cost in time. A call that should take five seconds can take 15 to 20 after retries, and users notice. If the same mistake keeps coming back (single quotes in JSON, say), put that rule in the prompt so the first answer is right. He also mentioned OpenAI's structured output mode, but prefers validation in the app: rely on one vendor's feature and switching to Claude or another provider gets harder.

## Stream short tasks, queue long ones

Users drop off well before ten seconds, and many LLM calls take five to ten. Streaming tokens as they arrive hides most of that. WebSockets work but mean a rewrite and possibly a different language; Server-Sent Events reuse your existing HTTP stack, and in Flask or FastAPI amount to a generator and a couple of headers. His recommendation: SSE, unless you truly need two-way traffic.

Streaming stops making sense when a task takes minutes. His example is an essay generator fed a hundred topics: do it in the request path and you tie up the backend for everyone else. Store the task, process it in the background, and notify the user by email or Slack, because they've left the tab. Start with a cron job polling the database. When you need more workers, move to a task queue. Kusho uses RQ (Redis Queue), which he says takes about 15 minutes to set up; they found Celery more than they needed.

## Evals are unit tests for prompts

The evals section is short and practical. Think of it, in his words, as "unit testing for your prompts": take a prompt template, run it against many inputs and several models, assert on the outputs, and compare cost. Hook it into CI so every build checks the prompts still behave. His team's pick is promptfoo, configured in YAML and available as open source or hosted.

## A provider tour with a timestamp on it

The talk closes with a quick tour of model APIs as they stood in early 2025: OpenAI as the versatile, reliable default; Anthropic's Claude for coding; Groq's custom chips for low latency; AWS Bedrock for keeping sensitive data inside AWS; Azure OpenAI, which was slightly faster in their tests but gated behind forms; and DeepSeek's open weights. The specific models have moved on since. The way of choosing (task fit, latency, data residency, reliability) still applies.

## Who should watch

Developers shipping their first LLM feature into an existing product, especially in Python. Experienced backend engineers will recognise every pattern; the value is in seeing which ones matter more with LLMs, and which libraries a small team found good enough. It is a talk by a vendor's CTO, but it's about engineering practice, not Kusho's product.

[Watch Sourabh Gawande's talk](https://www.conf42.com/Large_Language_Models_LLMs_2025_Sourabh_Gawande_applications_practices_tradeoffs) ([YouTube](https://youtu.be/aZo37Cyaprk)).

## Related Conf42 talks

- [Shipping AI Features That Don't Break in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Andrii_Veremiienko_shipping_ai_features) by Andrii Veremiienko (Revolut), LLMs 2026.
- [Scaling AI: Fault-Tolerant GenAI Solutions for Millions](https://www.conf42.com/MLOps_2025_Dennis_Nerush_scaling_ai_fault) by Dennis Nerush (Elementor), on switching between AI vendors, MLOps 2025.
- [AI-Driven Testing for Conversational AI: LLM-as-Judge, Generative QA, and Scalable Automation](https://www.conf42.com/Prompt_Engineering_2025_Yash_Panjari_testing_conversational_automation) by Yash Panjari (Apple), Prompt Engineering 2025.

## From Kusho AI

Kusho AI builds an AI agent for API testing; per the talk's abstract, it is used by more than 5,000 engineers to make API testing autonomous.

- [kusho.ai](https://kusho.ai/?kusho_ref=conf42)

## Watch the talk

[Practical tips for building AI applications using LLMs - Best practices and trade-offs](https://www.conf42.com/Large_Language_Models_LLMs_2025_Sourabh_Gawande_applications_practices_tradeoffs) at Conf42 Large Language Models (LLMs) 2025.
