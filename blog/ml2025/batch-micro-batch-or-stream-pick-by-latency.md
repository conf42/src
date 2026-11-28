# Batch, micro-batch or stream? Let the latency budget decide

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/batch-micro-batch-or-stream-pick-by-latency

In short: Meta engineer Sai Kaushik Ponnekanti walked through real-time ML pipelines at Conf42 Machine Learning 2025: Kafka, Flink, event time and drift.

A fraud alert for a card swipe that happened two hours ago is a history lesson, not a defence. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Sai Kaushik Ponnekanti, a senior software engineer at Meta with earlier stints at Google and Walmart Labs, explained how to build sub-second analytics pipelines for machine learning, and, just as usefully, when you shouldn't bother.

## Not every business needs a stream

The talk's best section is the honest one. Ponnekanti lines up three options. Batch runs hourly or daily and is perfectly fine for the ad-tech team that wants last week's campaign performance; building a heavy streaming pipeline for that is engineering for its own sake. Micro-batching sits in the middle. Real-time streaming pushes latency under 10 milliseconds for things like live stock trading, real-time gaming and dynamic content.

His micro-batching example is pleasingly specific. When an Amazon purchase event for diapers arrives, you want the user's path that led there: homepage, product page, add to cart. So you look back a few windows to reconstruct the session. That is a micro-batch problem, not a sub-10ms one.

## Fraud, carts and factory floors

The use cases span three industries. In banking, he describes his own card being used in Tennessee an hour after a transaction in California, which an hourly batch would spot only after the thief had finished shopping. In e-commerce, real-time pipelines update recommendations within a session and warn shoppers before a Black Friday iPad deal sells out under them, a scenario he knows from Walmart's Thanksgiving traffic. In manufacturing, machines stream temperature, vibration and speed so models can flag a failing line before your kid's birthday toy ships five weeks late.

The abstract carries headline figures, such as fraud losses cut by $15M and conversions up 18%; treat those as the talk's cited industry numbers rather than Meta production data.

## Event time is where streaming gets hard

The technical core is the gap between when an event happens and when it is recorded. Click add-to-cart, the backend gets it minutes later, and the event still happened when you clicked. Ponnekanti puts out-of-order arrival at around 15% of streaming data and walks through the standard defences: sliding windows that wait a minute or two for the homepage and product-page events, and watermarking. If an add-to-cart shows up before the homepage visit, your pipeline needs to wait, not panic.

Model drift gets the same treatment. Summer clothes sell in summer, winter clothes in winter, and a model trained on one season quietly degrades in the next. Real-time systems should detect distribution shifts and retrain automatically.

## Kafka in, Flink through, and pick hybrid on purpose

On frameworks he compares Apache Kafka, Apache Flink, AWS Kinesis and Azure Event Hubs, noting that the managed cloud services integrate more easily but add latency. His own career has mostly meant hybrids: Kafka for ingestion, Flink for processing, then a real-time feature store feeding an optimised model-serving layer that retrains when accuracy drops. The fastest framework is not automatically the right one; team count, tolerated latency, integration effort and learning curve all count.

## Who should watch

Data and ML engineers deciding whether a use case needs streaming at all will get the most from it. It's an architecture overview with personal examples rather than a code walkthrough. Start, as he suggests, with your most latency-sensitive application and grow from there.

## Related Conf42 talks

- [Building a real-time analytics dashboard with Streamlit, Apache Pinot, and Apache Kafka](https://www.conf42.com/Python_2022_Mark_Needham_realtime_analytics_dashboard_streamlit_apache_pinot_apache_kafka) by Mark Needham is the hands-on build.
- [Designing streaming data pipelines: Best Practices and Considerations](https://www.conf42.com/Cloud_Native_2024_Ankit_Virmani_streaming_data_pipelines) by Ankit Virmani goes deeper on pipeline design.
- [Cloud-Native Analytics: Transforming Big Data into Real-Time Product Insights](https://www.conf42.com/Cloud_Native_2025_Nimit_Bhardwaj_big_data_analytics_realtime_insights) by Nimit Bhardwaj takes the product-analytics angle.

[Watch Sai Kaushik Ponnekanti's talk](https://www.conf42.com/Machine_Learning_2025_Sai_Kaushik_Ponnekanti_motion_analytics_realtime)

[Watch the talk on YouTube](https://youtu.be/Fv7tv1fs6sM).

## Watch the talk

[Real-Time ML in Motion: Architecting Sub-Second Analytics Pipelines for Predictive Business Value](https://www.conf42.com/Machine_Learning_2025_Sai_Kaushik_Ponnekanti_motion_analytics_realtime) at Conf42 Machine Learning 2025.
