# Sometimes the best send time is not sending at all

Conf42 Blog, 2026-02-02, updated 2026-11-09. https://www.conf42.com/blog/ml2026/sometimes-the-best-send-time-is-never

In short: Adobe's Murthy Chandrapaty and Chakravarthy Kalva at Conf42 Machine Learning 2026 on turning send-time prediction into a send, defer or skip decision.

Send-time optimisation can pick the minute you are most likely to open an email and still be wrong, because three other brands, and two other campaigns from the same brand, picked that minute too. At Conf42 Machine Learning 2026, Chakravarthy Kalva, Senior Product Manager, and Murthy Chandrapaty, Principal Engineer, both at Adobe, argued that the question should change from "when do we send?" to "should we send at all?", and showed a decision layer that answers it.

The talk splits cleanly: Chakravarthy makes the product case, Murthy demos and explains the architecture.

## A good prediction can still be a bad decision

Chakravarthy described how classic send-time optimisation (STO) works: train on past opens and clicks, output a personalised best time per person. It worked well when marketing meant weekly newsletters and batch blasts. It works less well when every inbox is crowded and engagement has flatlined.

His summary line: "High probability does not equal high wisdom." A model that says 10:30 AM has no idea whether the customer has already heard from you three times today, whether quiet hours apply, or whether the message fits where they are in their journey.

## Send, defer or skip

The replacement is a decisioning step that treats the STO prediction as one input among several: journey stage, how many messages this person received today or this week, fatigue rules, quiet hours and business priorities. Its output is an action, send now, defer or skip, with the reasoning attached.

Murthy's demo ran five email scenarios through the agent. A fresh user with high engagement and a flash sale gets the send. The same campaign to a user with equally high engagement but a fatigue score of 0.80 gets deferred, which is exactly the case a prediction-only system would have sent. A later product update to that same fatigued user is deferred again, because the state persists across campaigns. Over the run, 60% of messages went out and 40% were deferred. The system is optimising the relationship, not the send count.

## Three layers: predict, decide, protect

The architecture has three layers. An ML prediction layer runs four models that emit scores with confidence. The AI decisioning layer, the agent from the demo, consumes those signals and reasons over constraints. A state manager tracks each user's history and enforces limits.

Murthy's engineering points are the ones worth noting. Decisioning is a first-class system, not a pile of business rules. And it is a distributed-systems problem: he said it runs at millions of decisions per day with sub-100 millisecond latency, and the hard part was state contention, multiple campaigns competing for the same user at the same moment, with the decision layer arbitrating in real time. The demo is channel-agnostic; email just kept it simple. The demo code is on GitHub, linked from the talk.

## Who should watch

Marketing-tech engineers and product managers running engagement models who suspect the next gain is in not sending. Engineers building any agent that arbitrates shared resources will recognise the state problem.

## Related Conf42 talks

- [Intelligent Notification Systems at Scale: Combining Machine Learning with High-Performance Architecture](https://www.conf42.com/Machine_Learning_2025_Ankita_Kamat_intelligent_notification_systems) by Ankita Kamat, the delivery side of the same pipeline.
- [Leveraging AI-Driven Insights for Incident Management: Enhancing Customer Retention through Strategic Personalization](https://www.conf42.com/Incident_Management_2024_Anandakumar_Kumaravelu_4_ai_retention_personalization) by Anandakumar Kumaravelu.

[Watch Murthy Chandrapaty and Chakravarthy Kalva's talk](https://www.conf42.com/Machine_Learning_2026_Murthy_Chandrapaty_Chakravarthy_Kalva_decisioning_b2c_marketing) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/KYXzvCGlfSM?si=_dSvuH73yvhEXBPd).

## Watch the talk

[Beyond Send-Time Optimization: From Prediction to AI-Driven Decisioning in B2C Marketing](https://www.conf42.com/Machine_Learning_2026_Murthy_Chandrapaty_Chakravarthy_Kalva_decisioning_b2c_marketing) at Conf42 Machine Learning 2026.
