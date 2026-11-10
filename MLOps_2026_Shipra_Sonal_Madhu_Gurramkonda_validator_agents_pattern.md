# Agents That Check Their Own Work: The Validator Pattern

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Shipra Sonal](https://www.conf42.com/speaker_Shipra_Sonal) (Data Engineering Manager @ Amazon) and [Madhu Gurramkonda](https://www.conf42.com/speaker_Madhu_Gurramkonda) (Head of Data Analytics @ Amazon). Page: https://www.conf42.com/MLOps_2026_Shipra_Sonal_Madhu_Gurramkonda_validator_agents_pattern

## Abstract

An analytics agent that is right most of the time still can't be trusted with business questions, because nobody knows which answers are the wrong ones. This talk covers a simple pattern that changes that. Specialist agents can only read data, and a separate validator checks every claim in a draft answer against its live source before the answer goes out. We'll look at how to split the work between specialists and validator, what the validator should check and what it shouldn't, and how to handle answers it rejects. We'll also cover the failures that showed up in practice, including outages nobody noticed at first, and the operating rules that came out of them.
