# Friendly fraud happens weeks after checkout, so model the graph and time

Conf42 Blog, 2026-04-13. https://www.conf42.com/blog/cloud2026/friendly-fraud-graph-attention-transformers

In short: Gautham Paspala of ServiceNow at Conf42 Cloud Native 2026 on catching friendly fraud with temporal graph attention, transformers and human review.

Friendly fraud is the one where nothing looks wrong at checkout: a real customer, a valid card, an authorised transaction, delivered goods, and then a dispute weeks later. At Conf42 Cloud Native 2026, [Gautham Paspala](https://www.conf42.com/Cloud_Native_2026_Gautham_Paspala_data_warehousing_analytics), Staff Software Engineer at ServiceNow working on dispute operations for banks, proposed catching it with two attention models working together: a temporal graph attention network over the payment ecosystem and a transformer over each cardholder's history.

It's a short talk, around 15 minutes, that moves from problem framing to architecture to deployment concerns.

## Point-of-sale controls look at the wrong moment

The difficulty is the time gap. Traditional fraud controls try to stop a bad transaction before it clears. With friendly fraud the bad act, filing the dispute, happens long after the sale, when the merchant has already shipped. His abstract puts friendly fraud at 60 to 75% of chargeback volume and more than $48B in annual global losses, as industry estimates.

The baselines he cites are rule-based systems catching 23 to 31% of confirmed friendly fraud, with rigid thresholds fraudsters learn to step around, and traditional machine learning reaching roughly 38 to 47%. The ML ceiling, in his framing, comes from hand-crafted features and a weak grip on relationships between cardholders, merchants and devices, and on how those relationships change over time.

## The payment ecosystem is a graph with timestamps

The first model treats payments as a heterogeneous graph: accounts, devices and merchants, then transactions and IP addresses, then physical and digital addresses. The scale in the talk is issuer-sized: 50 to 100 million cardholder accounts, 15 to 25 million merchants, 10 to 50 billion edges, and 100 to 500 million new edges a day.

Every edge carries a timestamp: when a purchase happened, when a device was used, when an address was linked to an account. That's what lets the model see patterns that develop over weeks. Graph attention then learns which relationships deserve weight. Several accounts sharing one device or IP points to a coordinated ring. One cardholder disputing across many unrelated merchants is a cross-merchant pattern. Nobody writes a rule for either; the attention scores surface them.

## A transformer reads the cardholder's history

The second model processes each cardholder's transactions as a sequence, using self-attention to find which earlier transactions matter most when predicting whether a new one will be disputed. Combined, he argues, the two catch patterns neither finds alone: the graph sees structure, the sequence sees behaviour over time.

## The numbers, and how they were measured

He evaluates with precision, recall, AUC, and cost-sensitive threshold tuning that weighs annoying a real customer against missing a real loss. Against traditional ML, he reports the combined approach reaching 67 to 78% detection, a 40 to 65% relative improvement, and 35 to 45% fewer false positives than rule-based systems. The talk presents these as benchmark results without detailing the dataset, so read them as the framework's claim rather than a production report.

## Deploying it is the hard part

Keeping a graph with tens of billions of edges fresh while hundreds of millions arrive daily, and running transformer inference in near real time, is where the cloud-native part comes in. Three principles: distributed graph databases with partitioned storage and compute; segment-level calibration, with separate thresholds per merchant category and transaction type instead of one global cut-off, which he says sharply reduces false positives; and Kubernetes autoscaling for traffic spikes.

The last piece is human review. Fraud teams decide whether flagged cases really were fraud, and that feedback goes back into training. It keeps false positives falling and helps the model follow fraudsters to new tactics.

## Who should watch

Engineers and data scientists in payments or dispute operations who are past rules and gradient-boosted features and wondering whether graph models are worth the infrastructure. It's a framework talk, not a code walkthrough.

## Related Conf42 talks

- [Cloud-Native Observability for Financial Systems: Implementing Graph-Based Monitoring and Behavioral Analytics for 99% Anomaly Detection Accuracy](https://www.conf42.com/Observability_2025_Siva_Prakash_financial_anomaly_graph) by Siva Prakash at Conf42 Observability 2025.
- [AI-Driven Fraud Detection & Personalization in Scalable Go Fintech Systems](https://www.conf42.com/Golang_2026_Sridhar_Muthineni_driven_fraud_detection) by Sridhar Muthineni at Conf42 Golang 2026.
- [Impact of AI in detecting and monitoring fraudulent payments from social engineering](https://www.conf42.com/Incident_Management_2024_Ndubuisi_Obirije_30_ai_fraudulent_payments) by Ndubuisi Obirije at Conf42 Incident Management 2024.

[Watch Gautham Paspala's talk](https://www.conf42.com/Cloud_Native_2026_Gautham_Paspala_data_warehousing_analytics) or the [YouTube recording](https://youtu.be/VMLef2kDRwc).

## Watch the talk

[Cloud-Native Friendly Fraud Detection with Temporal Graph Attention and Transformers](https://www.conf42.com/Cloud_Native_2026_Gautham_Paspala_data_warehousing_analytics) at Conf42 Cloud Native 2026.
