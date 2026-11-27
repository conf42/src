# Precompute by default: LLM features on a page that cannot wait

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/shipping-llm-features-amazon-scale

In short: Artem Zamarajev (Amazon) at Conf42 MLOps 2026 on four lessons for LLM features on a busy web page: precompute, fallbacks, output checks, one gateway.

The safest model call on a product page is the one that never happens while the shopper is waiting. At Conf42 MLOps 2026, Artem Zamarajev, a senior software engineer at Amazon working on AI shopping features, compresses what he has learned about LLM features on high-traffic pages into four lessons: precompute by default, keep the model off the critical path, check outputs before customers see them, and put one service in front of the assistant.

His scope is narrow on purpose. This is about AI features inside a web page a shopper loads in a browser. Standalone chatbots and background agents get only partial credit.

## Three problems the usual toolkit does not cover

Timeouts, caching, canaries, feature flags and A/B tests still apply. LLM features add three things on top.

Latency: he quotes Google's guidance that a page's main content should appear within 2.5 seconds and the first byte within 0.8 seconds. A fast model starts streaming in a few hundred milliseconds, but a full response takes several seconds and the slow tail runs longer.

Quality: bad output arrives well-formed with a successful status, so the error rate stays flat while customers read something wrong.

Cost: every call costs money, and page-view volume multiplies it.

To keep the lessons concrete he invents a store, Ridgeline Coffee, with three features on each product page. A quick take (three LLM-written highlights from product details and reviews), suggested questions picked for the shopper, and an Ask button that opens the store's assistant.

## Ask three questions before generating anything live

Does the output depend on the shopper or what they typed? How often do the inputs change? Is anyone waiting for it?

The quick take is the same for everyone, changes only when the product or its reviews change, and nobody is waiting. So it is generated in a background job, checked, and stored. The page does a key lookup. Latency becomes a read, and cost follows product changes instead of traffic. One trap: regenerate on every new review and a popular product burns model calls all day for text that barely moves. He uses a threshold, such as a minimum number of new reviews.

The Ask button has to be live, but only runs for shoppers who click. Suggested questions depend on the shopper, so they run live on every page view. Remember that one for lesson four.

## A timeout will not save the page

A timeout short enough to protect the page would cut off most model calls. So the answer depends on the feature type.

For precomputed content he decides the fallback before writing a prompt, as a ladder: fresh content, then the last good version, then a plain non-AI default such as the product's existing bullet points, then hiding the feature. For live features the page renders first and the model is called afterwards. Suggested questions fill in late, and if they fail the space stays empty. The Ask response is streamed, which also keeps long answers from hitting fixed timeouts in proxies and gateways. The worst case is a plainer page.

## Wrong output looks like success

He brings up the 2024 tribunal ruling against Air Canada, whose chatbot told a customer something that contradicted the airline's own policy page. The company owns what the model says.

Before a quick take is stored, it passes four checks: format, grounding (every claim traces to product data or a review), consistency with the rest of the page, and content policy. A highlight saying the coffee ships ground on a page that says whole bean only is his small-scale example. Format and policy are mostly rules. Grounding and consistency often need a second model call, which is affordable because it runs once per product change.

Live responses get layers instead: the model works from the product's own data, cheap rule checks run on the stream, and a sample of real responses is judged afterwards. Both kinds get a fixed eval set rerun on every prompt or model change. And because fallbacks hide failures, the rejection rate is the metric to watch during a rollout. The page looks healthy either way.

## One door in front of the assistant

The Ask button and suggested questions both call the same assistant. Let each call it directly and two things go wrong. Eligibility rules, languages, timeouts and fallbacks get copied and drift apart. And an assistant sized for the small share of shoppers who click Ask suddenly receives a call on every page view.

His fix is a small service between features and the assistant that holds the rules, sets the timeout, returns fallbacks, and gives each feature a traffic budget with rate limits. "I make it a service rather than a shared library because a library can't enforce one budget across every caller," Artem Zamarajev said at Conf42 MLOps 2026.

His one-line summary of the whole talk: "calling the model is easy, and most of the work is just a system around it".

## Who should watch

Backend and full-stack engineers adding generative features to pages that already have latency targets, and the product managers who keep asking why it cannot just call the model. It is a short, tidy talk with no slides of production metrics. The abstract speaks of millions of daily renders with zero faults, while the recording stays with the invented coffee shop, so expect patterns over war stories.

## Related Conf42 talks

- [Harness Engineering for Production LLMs: Eval-as-Code From Day One](https://www.conf42.com/MLOps_2026_Anwar_Khan_eval_llms_harness) by Anwar Khan (John Deere) at Conf42 MLOps 2026.
- [Evals for Generators: Testing an LLM That Writes Clinical Configuration](https://www.conf42.com/MLOps_2026_Ocean_Coldiron_evals_clinical_configuration) by Ocean Coldiron (ModMed) at Conf42 MLOps 2026.
- [Building Real-Time AI Decision Systems with Large Language Models](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mohanraj_Varatharaj_realtime_decisions_llms) by Mohanraj Varatharaj at Conf42 Large Language Models 2026.

[Watch Artem Zamarajev's talk](https://www.conf42.com/MLOps_2026_Artem_Zamarajev_llm_commerce_renders) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[From Prototype to Millions of Daily Renders: Shipping LLM-Powered Features Reliably at E-commerce Scale](https://www.conf42.com/MLOps_2026_Artem_Zamarajev_llm_commerce_renders) at Conf42 MLOps 2026.
