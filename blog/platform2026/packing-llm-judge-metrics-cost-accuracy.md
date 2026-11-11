# Pack five metrics into one LLM judge call, but not forty

Conf42 Blog, 2026-10-12, updated 2026-11-09. https://www.conf42.com/blog/platform2026/packing-llm-judge-metrics-cost-accuracy

In short: Scarlett Attensil of LaunchDarkly at Conf42 Platform Engineering 2026 on how many criteria one LLM judge can score before accuracy slips.

Scoring five metrics in one LLM judge call instead of five separate calls cut Scarlett Attensil's evaluation bill by 46% with no measurable loss in accuracy. At Conf42 Platform Engineering 2026, Scarlett, a developer educator at LaunchDarkly and a former data scientist, showed the experiment behind that number, and the second one that found the judge slowly getting worse as the list grows toward 40.

If your platform team runs a shared eval service, this is the most directly useful half hour of the event.

## Where the savings actually come from

Her judge returned evidence, a short reason and a score for every metric. Sent one metric per call, it read the same response five times and reasoned five times. Packed, it reads once and fills out a checklist. Prompt caching helps with the repeated input, she notes, but it can't touch the model's reasoning tokens, and those were the bigger saving.

From her billing records: about 1,000 metric scores cost 59 cents unpacked and about 32 cents packed. The abstract gives the precise figures, $0.593 versus $0.318 per thousand criteria.

## Same prompt, both ways

The first experiment used NVIDIA's public HelpSteer2 dataset, where humans scored responses from zero to four on helpfulness, correctness, coherence, complexity and verbosity. For roughly 150 prompts with a clear human preference, the judge scored both responses, and a match meant it ranked them in the same order as people, even if its numbers were a point harsher.

Everything stayed fixed except packing: same prompts, model and rubric wording, metric order shuffled with a recorded seed, and the output budget grown by the same 220 tokens per metric so a big call never ran out of room. Each prompt was scored both ways, so it served as its own control. Result: the confidence interval ran from about three points worse to four points better and crossed zero. No measurable change.

She also tracked ties, which most people forget. The judge tied about 48% of the time in both setups. If packing had pushed hard cases into ties, accuracy would look fine only because the hard ones dropped out. Her advice: always report the tie rate next to accuracy.

## Breaking answers on purpose

HelpSteer2 has human labels for only five attributes, so to test 10, 20 and 40 metrics she built synthetic corruptions with a known right answer: filler phrases, broken grammar, repeated sentences, shuffled order, truncated endings, a deleted key sentence, wrong numbers. The haiku about a banana that now opens with a line of bureaucratic throat-clearing is a highlight. Each edit targets one metric and declares the direction the score should move.

The measured metric always sat first, and extra metrics piled up behind it, so position couldn't explain any drop.

## A slow bend, not a cliff

At 40 metrics, across more than 7,000 calls, the judge caught the planted change about six points less often, with the whole interval on the negative side. There was no cliff. Every added metric cost roughly 1% in the odds of catching the change, a slow bend you'd miss if you were waiting for something to fall over.

The breakdown is the interesting part. Repetition suffered most: caught about two-thirds of the time with one metric, under a third with 40. Grammar and punctuation also slipped. Truncation and wrong numbers got easier to catch, possibly because extra metrics like completeness nudged the judge to check those.

## What to do on Monday

Start with a small packed rubric; five worked and nearly halved her bill. Retest whenever the rubric grows, look at each metric on its own rather than the average, run detail-oriented metrics like tone and grammar as their own calls, define every point on your scale, and report ties. Her caveats are explicit: one model, one dataset, one rubric. The method is what transfers, and the repo with data, code and calls is linked from the talk.

## Who should watch

Anyone running LLM-as-judge in CI or production, and platform teams pricing a shared evaluation service. It's also a tidy lesson in paired experimental design.

## Related Conf42 talks

- [Who Judges the AI Agent? LLM-as-Judge for Testing Non-Deterministic Code Generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen) by Liran Yushinsky at Conf42 AI Agents 2026.
- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz at Conf42 LLMs 2025.
- [From Benchmarks to Business Impact: Evaluating Generative AI in Production](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) by Srikanth Devarakonda at Conf42 Observability 2026.

[Watch Scarlett Attensil's talk](https://www.conf42.com/Platform_Engineering_2026_Scarlett_Attensil_llm_judgments_fails) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/8kvVDKAAJl8).

## Watch the talk

[How Many Judgments Can One LLM Make Before It Fails?](https://www.conf42.com/Platform_Engineering_2026_Scarlett_Attensil_llm_judgments_fails) at Conf42 Platform Engineering 2026.
