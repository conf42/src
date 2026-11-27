# AI in police CRM systems needs public dashboards and audits

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/ai-crm-policing-needs-public-dashboards

In short: Chiranjeevi Dubaguntla of PruTech Solutions at Conf42 Machine Learning 2025 weighs AI CRM in policing and proposes a community transparency framework.

A model that learns from historical policing data will learn historical policing habits, including the bad ones. Chiranjeevi Dubaguntla, a Salesforce developer at PruTech Solutions with more than 14 years in CRM systems, used his [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) talk to look at both sides of AI-driven CRM in community policing: real gains in response and engagement, and real risks of bias and surveillance. His proposed fix is a Community Algorithmic Transparency Framework built on public dashboards, citizen-readable logs and quarterly third-party audits.

It is a short talk, closer to a policy brief than an engineering session, and it does not walk through a specific product. That is fine: the questions it raises apply to any team building decision support for the public sector.

## What the systems actually do

Dubaguntla describes CRM platforms that ingest 911 calls, case management records and citizen complaints, then run sentiment analysis to flag rising community tensions, predictive alerts to direct resources to high-risk areas, and officer engagement scorecards. He reports departments seeing shorter emergency response times, more positive citizen interactions, and higher community satisfaction where the systems are transparent. That last qualifier carries much of the talk.

## The feedback loop nobody asked for

The "shadow side" section is the part to watch. Documented cases show minority communities flagged more often by algorithms despite similar incident rates. Systems trained on historical data tend to perpetuate the patterns in that data, so more flags lead to more enforcement, which leads to more data that justifies more flags. Most predictive tools offer little auditability, and citizens rarely know what data is collected about them or how it shapes decisions. In communities with a history of over-policing, he points out, that opacity makes trust almost impossible to build.

Anyone who has watched a recommender system amplify its own early guesses will recognise the shape of the problem. The difference is that here the output is a patrol car, not a playlist.

## Four principles: visibility, documentation, participation, review

The framework has four parts. Visibility: public-facing dashboards that show how algorithms make recommendations. Documentation: engagement logs that citizens can access, so they can see how their case was routed, who resolved it and on what basis. Participation: community involvement in system design, through public workshops and town halls. Review: mandatory quarterly third-party algorithm audits, which he compares to the independent financial audits companies already accept.

He reports pilot results from Boston, Oakland and Denver, including higher trust in police technology after dashboards launched, a community oversight committee that reviews algorithm changes, and more engagement with a police portal after transparency measures. The implementation path runs from auditing existing AI systems, to technical changes that make algorithms explainable, to formal channels for citizen feedback, to independent audits that repeat.

## Engineering recommendations

The technical asks are specific enough to act on: open-source the critical algorithms for public review while protecting security-sensitive parts, collect only necessary data with clear retention rules, test regularly against diverse datasets to find and correct bias, and let individuals view and manage their data within reasonable limits.

## Who should watch

Engineers and product managers building analytics or CRM tools for government, and anyone designing a model whose decisions land on people who never opted in. If you want technical depth on bias testing methods, pair it with the talks below.

## Related Conf42 talks

- [AI's hidden history: unpacking bias, power and the builders who shaped it](https://www.conf42.com/Machine_Learning_2025_Lianne_Potter_bias_builders_history), Lianne Potter, Conf42 Machine Learning 2025
- [Ethical data engineering: addressing privacy, bias and fairness in AI systems](https://www.conf42.com/Machine_Learning_2025_Arun_Vivek_Supramanian_privacy_engineering_ethical), Arun Vivek Supramanian, Conf42 Machine Learning 2025
- [Public sector operations with Salesforce Government Cloud](https://www.conf42.com/Golang_2025_Anirudh_Peri_salesforce_cloud_government), Anirudh Peri, Conf42 Golang 2025

[Watch Chiranjeevi Dubaguntla's talk](https://www.conf42.com/Machine_Learning_2025_Chiranjeevi_Dubaguntla_crm_policing)

[Watch the talk on YouTube](https://youtu.be/Z41ycCBg0CA).

## Watch the talk

[AI-Powered CRM in Policing: Innovation and Surveillance](https://www.conf42.com/Machine_Learning_2025_Chiranjeevi_Dubaguntla_crm_policing) at Conf42 Machine Learning 2025.
