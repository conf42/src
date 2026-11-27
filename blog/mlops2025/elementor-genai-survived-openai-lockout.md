# How Elementor's GenAI stack shrugged off an OpenAI account lockout

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/elementor-genai-survived-openai-lockout

In short: Dennis Nerush of Elementor at Conf42 MLOps 2025 on multi-org rate limits, circuit breakers, a one-switch Claude fallback and the insert-rate metric.

Two days before Elementor launched its AI Site Planner, OpenAI locked the company's account and every call stopped. At Conf42 MLOps 2025, Dennis Nerush, Director of AI Engineering at Elementor, explained why that turned out to be a minor event instead of a war room: a GenAI infrastructure built for rate limits, sick vendors and switching providers with a single key.

Elementor powers more than 19 million websites, and Dennis put its AI footprint at over 2 million users, more than 40 AI features, around 10 billion tokens a month and about a million AI requests a day. This is one of the most practical talks of the event: real incidents, real design decisions, and an honest list of what still hurts.

## Rate limits shape the architecture first

Elementor shipped its first AI features roughly four months after ChatGPT launched, when GPT-3.5 Turbo allowed 60 requests per minute. That pushed them to Microsoft Azure for higher limits and better support, which worked for about a year until the Elementor Copilot arrived. Like GitHub Copilot for layouts, it predicts the next section of a page and fires events on almost every user interaction.

Azure's limits weren't enough, and its developer experience got heavy: models available only in some regions, a dedicated resource and deployment per region, quotas shared across deployments, and a portal form to request more. So they moved back to OpenAI, where switching models is a line of code. To go beyond one organisation's limits without committing to an enterprise tier, they created several OpenAI organisations and extended the SDK so a call first fetches the next organisation from a round-robin pool. Developers don't know or care which org serves them.

## Sick organisations get benched automatically

Identical organisations do not behave identically. Dennis showed that latency and error rates mostly track each other and then diverge, with one org slowing or failing while others are fine, and provider status pages are rarely as green as you'd hope. Users don't care; they expect the product to work.

The fix is a circuit breaker on top of the pool. If an organisation crosses a threshold, such as hitting its rate limit or returning errors three times within a window, it is marked unhealthy and removed; after a while the system tries it again and restores it if it behaves. State lives in Redis so every Kubernetes pod sees the same pool rather than each pod rediscovering the failure, and every open and close posts to Slack. Nobody deploys a hotfix to remove a resource and sets a reminder to add it back the next morning.

## The fallback vendor needs its own prompts, and drills

The lockout is where the second vendor paid off. From day one Elementor also built on Anthropic's Claude, and Dennis was frank that migrating is harder than it sounds: structured output and validation features differ, and the same system prompt gives different results on different models. They keep provider-specific prompts and instructions so a single configuration key moves the whole system to Claude and back. It is deliberately manual, since the scenario is rare. His extra tip: practise the switch regularly, because fallbacks quietly rot while the main path keeps improving. He also mentioned the team was working on open-sourcing the framework.

## Insert rate beats vibes for evaluating images and layouts

Text evals are fairly direct; Dennis's example was the AI writing a whole paragraph for a button, fixed by evals on length per widget type. Images and full page structures need taste, so Elementor defined a success metric it calls insert rate: did the user actually insert the result, or regenerate or close the page? Every interaction is stored with the raw input, the enhanced prompt, the full prompt, the output and the inserted flag.

They started by reading failures manually, then built AI-powered offline clustering jobs that post weekly findings to Slack. One cluster found that requests mentioning transparent backgrounds were almost always rejected because the image model couldn't produce them; the fix was a hint telling users so. Others surfaced the long button text and weaker Japanese understanding than they had assumed.

## Who should watch

Anyone shipping LLM features to real users at volume, especially if your whole product sits on a single provider key. Platform engineers will want the circuit-breaker section; product teams, the insert-rate one. Smaller products can skip the multi-org gymnastics, and Dennis said as much: size the resilience to the need.

## Related Conf42 talks

- Hima Bindu Yanala (eBay) on [Designing Resilient Self-Service Search in Go: From Failure Modes to Intelligent Fallback](https://www.conf42.com/Golang_2026_Hima_Bindu_Yanala_designing_resilient_self).
- Mandi Walls (PagerDuty) on [Managing Vendor Incidents](https://www.conf42.com/Incident_Management_2024_Mandi_Walls_25_vendor_incidents_management), for when the outage belongs to someone else.
- Hilik Paz (Arato.ai) on [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals)

[Watch Dennis Nerush's talk](https://www.conf42.com/MLOps_2025_Dennis_Nerush_scaling_ai_fault)

[Watch the talk on YouTube](https://youtu.be/CRWCevLsi7w).

## Watch the talk

[Scaling AI: Fault-Tolerant GenAI Solutions for Millions](https://www.conf42.com/MLOps_2025_Dennis_Nerush_scaling_ai_fault) at Conf42 MLOps 2025.
