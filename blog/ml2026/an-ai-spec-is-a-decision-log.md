# An AI product spec should be a decision log, not a manuscript

Conf42 Blog, 2026-02-03, updated 2026-11-09. https://www.conf42.com/blog/ml2026/an-ai-spec-is-a-decision-log

In short: Rohan Mitra of PhonePe at Conf42 Machine Learning 2026 rewrites a vague smart-reply spec live with a five-pillar AI spec framework.

"Generate helpful replies" is not a requirement; it is a wish with a Jira ticket attached. At Conf42 Machine Learning 2026, Rohan Mitra, Product Manager at PhonePe, a Walmart company, made the case that the 40-page PRD is dead but vibe coding straight to production is chaos, and offered a middle path: a short AI spec built to force decisions. Then he rewrote a bad spec in front of the audience.

## The PRD died, the ambiguity did not

Rohan opened with the build-first debate: when you can prototype in the time it takes to write the doc, why write the doc? He agrees the long PRD that nobody reads after the first email should go. But a self-described vibe coder, he also sees the feature-factory trap: shipping fast, shipping the wrong thing, and shipping things nobody can measure.

His examples of the vibe-based spec are painfully familiar. Problem: returns are a big problem. Goal: improve the returns experience. Behaviour: generate helpful replies. Plan: start small, then run. Plenty of words, zero decisions, and, he argued, the biggest single source of wasted sprints for data science teams.

## Five pillars, two that are unique to AI

The modern AI spec has five parts: opportunity framing (why are we doing this), a behaviour contract (what good looks like), evaluation (how we prove it before shipping), boundaries and scope (trade-offs and non-goals), and risks and recovery (including the kill switch).

Two pillars carry the AI-specific weight. The **behaviour contract** replaces logic you cannot write with examples you can: a good smart reply (*Yes. Sending by 4:00 PM*), a bad one (technically correct, robotic and vague) and a forbidden one (anything mentioning confidential projects or PII). The **evaluation ladder** moves a feature from idea to production in steps: an offline golden set of 500 agreed examples, human review for hallucinations and tone, then online guardrails. His line: "A prototype has vibes, a product has a passing bar."

## The live rewrite

The demo is the best part. Starting from a blank five-pillar template, Rohan filled in the smart-reply spec:

- **Opportunity:** a measured baseline for reply times and a hypothesis that three context-aware suggestions cut p50 reply time by at least 10%.
- **Behaviour contract:** a proxy metric of at least 25% smart-reply adoption, a guardrail that the block rate may not rise more than 0.3 percentage points against control, and the good, bad and forbidden examples.
- **V0 plan:** hard-code the ten most common replies as buttons and see whether anyone clicks. Buildable in a day without touching a GPU.
- **Boundaries:** accept 300 ms of extra latency for better suggestions, written down as a leadership decision.
- **Kill switch:** a feature toggle in the admin panel that on-call engineers can flip in seconds.

Five minutes, and the word helpful has numbers, limits and an off switch.

## Who should watch

Product managers on AI features, and engineers who keep receiving specs that just say to make it smart. It is a tutorial, so expect a framework and a worked example rather than ML internals.

## Related Conf42 talks

- [Responsible AI Product Management for Production LLM Lifecycles](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vijayalakshmi_Narasimhan_governance_lifecycle_products) by Vijayalakshmi Narasimhan, the governance layer on top of the spec.
- [Unleashing Innovation: Mastering AI Product Management for Enterprises](https://www.conf42.com/Machine_Learning_2024_Pramod_Nammi_unleashing_innovation_mastering) by Pramod Nammi.
- [AI-Powered Digital Product Management: The Smart Shortcut from Idea to Market-Ready Solution](https://www.conf42.com/Prompt_Engineering_2024_Sabarinath_Viji_Selvam_productmanagement_ai_solutions) by Sabarinath Viji Selvam.

[Watch Rohan Mitra's talk](https://www.conf42.com/Machine_Learning_2026_Rohan_Mitra_experimentation_reproducibility_science) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/gmtRjqJbQkE).

## Watch the talk

[The AI Product Spec: A Hands-On Tutorial for Defining and Scoping Recommendation Systems](https://www.conf42.com/Machine_Learning_2026_Rohan_Mitra_experimentation_reproducibility_science) at Conf42 Machine Learning 2026.
