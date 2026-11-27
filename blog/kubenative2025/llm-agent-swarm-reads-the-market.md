# A swarm of specialist LLM agents reads the market on Kubernetes

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/llm-agent-swarm-reads-the-market

In short: Kiran Purushotham of JPMorgan Chase presents SAFSO at Conf42 Kube Native 2025, a swarm of specialist LLM agents with a consensus oracle and federated learning.

One generalist model reading every headline, tweet and SEC filing is a bottleneck with a good vocabulary. At Conf42 Kube Native 2025, Kiran Purushotham, Executive Director and Head of Architecture at JPMorgan Chase, presented a different shape: a swarm of specialist LLM agents on Kubernetes, each reading one kind of source, with a consensus layer deciding what the market is telling you.

The system is called the Self-Adapting Financial Sentiment Oracle (SAFSO). The talk is short and dense, closer to an architecture briefing than a tutorial, and it leans on results the speaker reports from the system.

## Most market data is text, and text is slow

Purushotham starts with the scale problem: he puts the daily volume of market data at 2.5 quintillion bytes, around 80% of it unstructured (news, social chatter, analyst reports, filings). Traditional models can't keep up with the volume or the variety, and in trading the latency of analysis is the cost: a signal you find after the move is trivia.

## Specialists plus a referee

SAFSO pairs two models. FinBERT extracts domain-specific sentiment from financial texts such as earnings calls; RoBERTa-large adds broader context from news and social media. Around them sit specialist agents: news agents on breaking stories and press releases, social media agents on investor conversations, regulatory agents parsing filings, and market data agents tying sentiment to price action and order flow.

The interesting piece is the referee. A consensus oracle uses a 16-head attention mechanism to weigh the agents' predictions, scores its own confidence and recalibrates as conditions shift. Think of it as an ensemble that learns which expert to trust this week.

He reports the swarm handling about 1,200 documents a second with end-to-end latency from ingestion to insight measured in milliseconds, even during volatile markets.

## Federated learning so banks can share without sharing

Data privacy is the other half of the design. Institutions train locally on private data and send only encrypted model weights to a central orchestrator, using homomorphic encryption. Purushotham says the setup ran across 47 financial institutions and improved accuracy by almost 15% compared with isolated models, while keeping raw data where regulators want it.

The reported performance numbers are bold: about 95% directional accuracy, 87% magnitude accuracy, 21% annualised returns over five years of backtesting and a Sharpe ratio of 1.67. Treat them as the speaker's results; the talk doesn't go into the backtest methodology. He also describes an early-warning use, flagging market stress events up to 36 hours ahead and spotting coordinated manipulation campaigns on social media.

## Kubernetes is the boring, essential part

The platform layer is deliberately standard: each agent in a lightweight container, HPA for surges, Istio for service-to-service traffic, Prometheus for health and performance. The challenges he lists will sound familiar to anyone running ML in production: latency versus model complexity, GDPR and CCPA compliance, model drift, and tuning clusters for cost.

## Who should watch

Architects designing multi-agent LLM systems who want a reference shape (specialists, consensus, federation), and fintech engineers curious how a large bank frames the problem. If you want code or a reproducible benchmark, this talk doesn't carry one.

## Related talks

- Ganesh Marimuthu covers the monitoring side of fast markets in [Observability in Modern Treasury Trading Platforms](https://www.conf42.com/Observability_2025_Ganesh_Marimuthu_trading_treasury_platforms).
- Sunny Guntuka's [Algorithmic Trading with Python](https://www.conf42.com/Python_2025_Sunny_Guntuka_trading_algorithmic_python) is the hands-on counterpart.
- Sentiment analysis outside finance: Vishal Khadake on [Leveraging NLP for Enhanced Incident Management](https://www.conf42.com/Incident_Management_2024_Vishal_Khadake_49_nlp_sentiment_language).

[Watch Kiran Purushotham's talk](https://www.conf42.com/Kube_Native_2025_Kiran_Purushotham_trading_llm_insight)

[Watch the talk on YouTube](https://youtu.be/drry36s-cu4).

## Watch the talk

[Swarming LLM Agents for Real-Time Market Insight in Cloud-Native Trading Systems](https://www.conf42.com/Kube_Native_2025_Kiran_Purushotham_trading_llm_insight) at Conf42 Kube Native 2025.
