# From Prototype to Millions of Daily Renders: Shipping LLM-Powered Features Reliably at E-commerce Scale

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Artem Zamarajev](https://www.conf42.com/speaker_Artem_Zamarajev) (Senior Software Engineer @ Amazon). Page: https://www.conf42.com/MLOps_2026_Artem_Zamarajev_llm_commerce_renders

## Abstract

Getting an LLM-powered feature to work in a demo is easy. Serving it on a high-traffic e-commerce page millions of times a day, without hurting latency or showing customers a bad answer, is a different job.  Drawing on shipping AI shopping features at Amazon that reached millions of daily page renders with zero faults, this talk covers the operational side of putting generative AI on a critical page:  - Deciding when content should be generated in real time and when it can be precomputed - Latency budgets, timeouts and fallbacks so the page never waits on a model - Quality gates and monitoring that catch bad output before customers see it - Integrating with an existing AI assistant's orchestration without becoming its bottleneck - Launching safely: gradual dial-ups, kill switches and the metrics that matter  Attendees leave with a practical checklist for taking an LLM feature from prototype to production traffic.
