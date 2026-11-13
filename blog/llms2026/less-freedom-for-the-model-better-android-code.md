# The more experience you gain, the less freedom you give the model

Conf42 Blog, 2026-05-29, updated 2026-11-09. https://www.conf42.com/blog/llms2026/less-freedom-for-the-model-better-android-code

In short: Andrii Veremiienko (Revolut) at Conf42 LLMs 2026 on AI-assisted Android work: rules files, a core UI module and no code you cannot explain.

"The more experience I gain, the less freedom I gave to the model." Andrii Veremiienko, an Android engineer at Revolut, calls that sentence the main lesson of his talk at Conf42 Large Language Models (LLMs) 2026. He reached it by using AI coding tools in two very different places: a large fintech Android codebase, and his own indie apps, Loggia and Padel Coach.

The comparison is the interesting part. The symptoms in each world were different, but the root cause was the same: a model that is allowed to make architectural decisions will make a lot of them.

Note on scope: the abstract frames the session around LLM features inside mobile apps. The talk itself is mostly about building apps with AI assistance, and how to stay in charge of the code while doing it.

## Fast code, slower understanding

The speed-up was real. Andrii estimates each indie app would have taken around six months the traditional way; with AI the first production version took roughly two, on weekends and evenings. Custom animations and canvas components that once took days got easy, and basic tests became cheap enough to write early.

But the bottleneck moved. He shipped more code than before, which meant more code to read, review and own. In his words, AI did not make engineering discipline less important; it made it more important.

## Freedom shows up as anarchy

His early prompts were "build a feature" plus a few screenshots. It worked, which was the trap. The happy path ran, and weeks later the bill arrived: the model had invented its own abstractions and managers, and solved local problems without the global picture. In the indie apps, where nobody else enforced an architecture, every task got its own little design. He calls the result solid suffering: single responsibilities split so finely that several pieces did the same job.

The UI suffered the same way. Treated as separate tasks, screens got different back buttons, different navigation animations, and errors shown as a toast on one screen, a snackbar on another and a dialog on a third.

At Revolut the failure looked different. The architecture already exists, and the model's code often made sense in isolation but wouldn't survive a serious review, because a big codebase has several ways to do the same thing and only some are current. He also saw over-testing: valid but fragile, implementation-specific tests that cost time to review and to run.

## The fixes are boring on purpose

- **Context before code.** Study how similar problems were solved, note what's legacy or deprecated, and store it in project notes or the model's memory. His workflow is notes, understanding, plan, then the smallest reasonable change.
- **Rules files early.** Pick the architecture, package structure, core libraries, error handling, navigation, offline behaviour and dark theme up front. Adding offline support later with AI, he warns, is close to impossible.
- **A strict testing prompt.** Ask for behaviour-focused tests, then turn the preferences into a reusable skill. A useless test generated quickly is still useless, so delete it.
- **A core UI module first.** Colours, typography, spacing, buttons, sheets, error pop-ups. A screenshot tells the model what to build; a design system tells it how the product behaves everywhere.

The rule underneath all of it: don't merge code you can't explain. If a library call or decision is unfamiliar, stop and ask the model to explain it, and write the lesson down.

## Who should watch

Mobile developers using Claude, Codex or similar tools day to day, especially anyone running a side project where they are the only architect. Engineering leads deciding how much autonomy to give coding agents will find a useful counterweight to the more-autonomy-is-better pitch.

## Related Conf42 talks

- [From Vibes to Outages: When AI Writes the Code You Debug](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sylvain_Kalache_vibes_outages_writes) by Sylvain Kalache (Rootly), on what AI-written code does to reliability.
- [From Prompts to Review Harnesses](https://www.conf42.com/AI_Agents_2026_Guido_Scheffler_code_review_harness) by Guido Scheffler (CGI), on scaling AI code review across 70+ projects.
- [Not Just Syntax: How AI is Changing Code Review](https://www.conf42.com/Python_2025_Shubham_Singh_ai_code_review) by Shubham Singh, on the reviewer's side of the same problem.

[Watch Andrii Veremiienko's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Andrii_Veremiienko_shipping_ai_features)

[Watch the talk on YouTube](https://youtu.be/WM_oOe5yMoA).

## Watch the talk

[Shipping AI Features That Don’t Break in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Andrii_Veremiienko_shipping_ai_features) at Conf42 Large Language Models (LLMs) 2026.
