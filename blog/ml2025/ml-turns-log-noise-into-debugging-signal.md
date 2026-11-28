# Your logs already know what broke; ML helps you hear it

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/ml-turns-log-noise-into-debugging-signal

In short: SRE architect Vijaybhasker Pagidoju showed at Conf42 Machine Learning 2025 how clustering, embeddings and LSTMs turn noisy logs into faster debugging.

Most log lines are noise, and the one line that matters tends to show up once, quietly, at the worst possible time. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Vijaybhasker Pagidoju, a Lead Site Reliability Engineer and SRE architect, made the case for machine learning as the thing that reads logs at a scale humans can't, then spent equal time on what it can't do without an engineer next to it.

It's a compact talk, roughly 15 minutes, and a good primer for an SRE team weighing ML-assisted log analysis.

## Logs are the most honest telemetry you have

Pagidoju's framing flips logs from chore to asset. They are raw, authentic records of user activity, system behaviour and failure traces, with no modelling guesswork in between. The problem is volume and mess: a brutal signal-to-noise ratio, JSON next to plain text next to semi-structured lines, timestamps that don't line up so cause and effect drift apart, and rare events that never cluster into a convenient spike. Meanwhile MTTR keeps climbing, and with it pager fatigue. His line for it: finding the right entry is like trying to find a single sentence in a dictionary the size of Australia.

## Four techniques do most of the work

The toolkit is classic and well chosen:

- **Clustering** groups similar log entries so the algorithm can say these events look related.
- **Embeddings** turn unstructured text into numbers that carry meaning.
- **Dimensionality reduction** such as PCA strips noise and keeps the features that matter.
- **Sequence models** such as LSTMs catch patterns across time, which is how you see the slow-building failure.

For anomaly detection he separates statistical baselines (z-scores, moving averages) for known patterns from ML models like isolation forests, autoencoders and one-class SVMs for the hidden ones. In production, his recommendation is a hybrid: rule-based filters first, ML verification on top, and feedback loops so the system improves.

The reference pipeline is four boxes: collect from every service and infrastructure layer, pre-process into a machine-readable shape, run the ML stage, then an insight engine that produces alerts and dashboards people actually act on. He cites Estonia's Health and Welfare Information System Centre reporting a 40% MTTR reduction after adopting Elastic's observability platform.

## The model doesn't know it's Black Friday

The section worth the watch is the one about limits. ML surfaces patterns but lacks context: it can't tell whether a traffic spike is Black Friday or an incident. Engineers validate findings, tune alerts and correct the system, and that loop is what makes it trustworthy. He lists three risks: black-box models nobody can explain (and an alert you can't explain is an alert you won't trust), drift as system behaviour changes, and bias, for example alerting that only cares about revenue-critical services while the rest go dark.

## Who should watch

On-call engineers drowning in alerts, and SRE leads who've been sold an AIOps product and want the vocabulary to question it. It's conceptual rather than a demo. His closing advice is the right one: adopt incrementally, prove value on a small slice, then expand.

## Related Conf42 talks

- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz attacks the same fatigue from the alerting side.
- [Getting the most out of your logs at 3 AM](https://www.conf42.com/Observability_2024_Shyamkumar_Kalariya_logs_3AM) by Shyamkumar Kalariya is the practical, pre-ML version.
- [From Fragmented Logs to Unified Insights](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Alok_Ranjan_fragmented_logs_unified) by Alok Ranjan covers getting the logs into one place first.

[Watch Vijaybhasker Pagidoju's talk](https://www.conf42.com/Machine_Learning_2025_Vijaybhasker_Pagidoju_debugging_analysis_pattern)

[Watch the talk on YouTube](https://youtu.be/h296O-FC_as).

## Watch the talk

[ML-based Log Analysis for Faster Debugging – AI techniques for log pattern recognition and anomaly detection](https://www.conf42.com/Machine_Learning_2025_Vijaybhasker_Pagidoju_debugging_analysis_pattern) at Conf42 Machine Learning 2025.
