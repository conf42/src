# An LLM that estimates delivery time from your Git history

Conf42 Blog, 2026-02-18, updated 2026-11-09. https://www.conf42.com/blog/ml2026/llm-delivery-estimates-and-pr-risk-scores

In short: Tim Markin (GiftHorse) at Conf42 Machine Learning 2026 demos a pipeline that estimates feature delivery time from past work and scores every commit for risk.

Every product manager has asked "how long will this take?" and every engineer has guessed. At Conf42 Machine Learning 2026, Tim Markin, Technical Product Manager at GiftHorse, showed a pipeline that answers with an estimate built from the team's own Git history, then reviews each commit and pull request for risk before a human reviewer has to.

It is a demo-driven talk from a former game developer turned PM. The demo is a from-scratch rebuild, not the internal tool, and Markin says plainly that it is not production ready, so treat it as a blueprint.

## Estimates come from what the team actually shipped

The problem he has fought his whole career is wrong delivery estimates. Before, his team relied on engineers' judgement corrected by past Jira sprints. Now, when the discovery team brings a feature to the delivery team, the tool produces an estimate first.

The pipeline has three steps. Feature extraction reads the Git history. Retrieval-augmented generation looks up similar past work, which is what makes the estimate better than a cold guess. An LLM analysis step then reasons about complexity and risk and returns a time estimate with a confidence level, risk scores and recommendations.

To show it, he points the tool at a three-repository Web3 hackathon project: a NestJS and Postgres backend, a frontend in the Cocos game engine, and a smart contract. Static analysis reports files, lines of code, complexity and a risk score per repository. The well-structured backend scores low risk; the Cocos frontend scores higher because so much of it is wiring UI to scripts in the editor, which the model struggles to read. Markin's aside that a React frontend would likely have scored lower is a quiet reminder that these tools reward code they have seen a lot of.

## A risk score on every commit

The second half is review. Each commit and PR gets an AI review, and if the feedback is useful the engineer can act on it immediately instead of waiting for a colleague. In his team's production setup, a risk score above 50% or quality below 50% notifies team leads and stakeholders, who will ask about it at the feature demo. If an engineer shows the AI got it wrong, they carry on and the model gets tuned.

The demo makes the point with a deliberately bad commit: a hardcoded secret key, no input validation, command injection. The tool rates it maximum risk and unsafe for production, which is the right call and also the easy one. The more interesting case is the AI-written NFT service commit that also comes back high risk and low quality.

## Closing the loop on estimates

The tool also compares estimates with what actually happened. In the demo it filters out overnight gaps of eight hours, counts the rest as working time, and uses commit timing to see when work stopped. The estimates line up except for backend setup, which went faster because it was done with AI help.

Markin reports that after adoption his team's delivery estimate accuracy rose from 60% to up to 80%, security issues were caught before merge, PMs could prioritise without long meetings, and PRs arriving for human review were noticeably better. The demo stack is Python with FastAPI, ChromaDB and the Claude API, which he says matches production apart from hardening. The repository is linked at the end of the talk; you will need a Claude or OpenRouter API key to run it.

## Who should watch

Engineering managers and PMs tired of estimates that drift, and platform teams thinking about AI review as a CI gate. Watch it for the RAG-over-past-work idea and the feedback loop on estimates; bring your own skepticism about any model's confidence on unfamiliar codebases.

## Related Conf42 talks

- [From Prompts to Review Harnesses: Scaling AI Code Reviews Across 70+ Software Projects](https://www.conf42.com/AI_Agents_2026_Guido_Scheffler_code_review_harness) by Guido Scheffler (CGI) is what AI review looks like across many repos.
- [Not Just Syntax: How AI is Changing Code Review](https://www.conf42.com/Python_2025_Shubham_Singh_ai_code_review) by Shubham Singh gives a broader view of the review side.
- [Test estimation - how did I become a fortune-teller](https://www.conf42.com/Chaos_Engineering_2023_Grzegorz_Niczyporuk_test_estimation_fortuneteller) by Grzegorz Niczyporuk (Swing Development) is the human craft this tool tries to augment.

[Watch Tim Markin's talk](https://www.conf42.com/Machine_Learning_2026_Tim_Markin_feature_stores_management)

[Watch the talk on YouTube](https://youtu.be/cRKS3K1bOTo).

## Watch the talk

[AI-Driven Engineering Quality: How We Use Machine Learning to Predict Delivery Time and Improve Code Reliability](https://www.conf42.com/Machine_Learning_2026_Tim_Markin_feature_stores_management) at Conf42 Machine Learning 2026.
