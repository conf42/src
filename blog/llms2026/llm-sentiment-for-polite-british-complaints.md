# Catching churn hidden inside polite British emails with an LLM

Conf42 Blog, 2026-05-19, updated 2026-11-09. https://www.conf42.com/blog/llms2026/llm-sentiment-for-polite-british-complaints

In short: Anton Denisov (Dwelly) at Conf42 LLMs 2026 on an LLM pipeline that spots unhappy landlords in polite emails and calls before they leave.

"Whenever you get a chance to look in the boiler, that would be great. Thank you so much for all your help." Every off-the-shelf sentiment model scores that as a happy customer. At Conf42 Large Language Models (LLMs) 2026, Anton Denisov, who leads revenue at the UK property manager Dwelly, explains why that landlord moved to a competitor about two weeks later, and how his team built an LLM system that would have flagged it.

Dwelly manages rental properties end to end for thousands of landlords on its own software. The system in the talk runs in production, reading landlord emails and phone calls and flagging dissatisfaction early enough to act on it.

## Complaints arrive with the emotion removed

Classic sentiment tools assume that stronger words mean stronger feelings. British professional politeness inverts that. "A little disappointed" usually means quite a lot. "When you get a chance" often means overdue. A note that someone would have expected a callback by now is a complaint, minus the exclamation marks. Keyword models read all of these as neutral.

NPS doesn't save you either. The people most likely to quietly leave are the ones too polite to give a low score: they give you a seven and then don't renew.

The harder half is silence. A lot of dissatisfaction came from what Dwelly didn't do: the unanswered email, the voicemail nobody returned. The triggering event is an absence, and the only trace in the data is a follow-up that is slightly shorter and cooler than the last one.

Anton is also honest about the target. Part of churn is unpreventable (landlords sell, or move back in), so the real question was narrower: can you spot the preventable, service-driven kind early, inside tens of thousands of ordinary, polite interactions?

## Read first, prompt later

The dataset was around eleven thousand interactions from roughly two thousand landlords over about seven weeks, across four channels: CRM email, direct email, outbound calls and inbound calls. About eleven hundred calls were transcribed with Voximplant. Calls were the most candid and the messiest.

Before any prompting, the team hand-labelled around two hundred borderline negative cases and wrote the label definitions as mechanical rules. Severity had four levels: amber needed one explicit signal, orange two independent strong signals, red literal termination language. Topic and intent sat on separate axes. The same set served as the evaluation benchmark and as the source of few-shot examples.

## Two cheap questions beat one expensive one

The model was Claude Sonnet, in a two-step pipeline. Step one asks only whether a message is positive, neutral or negative. Step two runs on the six or seven percent that come back negative and extracts severity, topic, intent and routing. The whole pipeline came in around a third of a cent per message.

Cost was the minor benefit. Splitting the steps let the team tune the detector for recall and the classifier for precision separately; one prompt doing both did both worse.

Three prompt fixes did most of the work. Treat courtesy as wrapping and classify the substance, anchored with polite-but-negative examples (the single biggest improvement). Put the severity rules into the prompt verbatim, so orange stopped being the default. And add an "external issue" intent, because a landlord annoyed about a contractor who says it's not your fault needs a different response from one blaming you.

## What the data said

Calls ran around 50% more negative than email. A landlord who switches from email to phone is a leading indicator of escalation. Communication failure was the largest category, about 36% of negative interactions. And one agency that looked like the top performer turned out to have most of its calls missing from the feed: coverage bounds quality.

Each intent maps to an owner and a response time, so the output is a to-do list rather than a dashboard. The communication-failure number also justified the next build: an agentic voice assistant for inbound landlord calls.

## Who should watch

Anyone classifying messy human text with an LLM, sentiment or otherwise. The British sarcasm hook is fun, but the lessons are about labelling, splitting the problem and closing the loop with action.

## Related Conf42 talks

- [Building Intelligent Retention Engines: Real-Time Churn Detection with AI on Kubernetes](https://www.conf42.com/Kube_Native_2025_Gaurav_Sunkar_retention_churn_ai) by Gaurav Sunkar, on the churn problem from the platform side.
- [Detecting 70 Kinds of Bias with a Model You Own](https://www.conf42.com/Prompt_Engineering_2026_Aleem_Khan_bias_news_llm) by Aleem Khan, another production text classifier with a strong opinion on labels.
- [Optimizing Subscription Services with Uplift Modeling](https://www.conf42.com/Large_Language_Models_LLMs_2025_Dmitriy_Zolotukhin_subscription_uplift_modeling) by Dmitriy Zolotukhin, for what to do once you know who is at risk of leaving.

[Watch Anton Denisov's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Anton_Denisov_british_sarcasm)

[Watch the talk on YouTube](https://youtu.be/FTQTsFjrweY).

## Watch the talk

[Teaching and LLM to Catch British Sarcasm](https://www.conf42.com/Large_Language_Models_LLMs_2026_Anton_Denisov_british_sarcasm) at Conf42 Large Language Models (LLMs) 2026.
