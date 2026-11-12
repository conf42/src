# A contact centre that knows you are about to churn before you say so

Conf42 Blog, 2021-07-28. https://www.conf42.com/blog/ml2021/amazon-connect-churn-aware-call-routing

In short: Asif Mujawar (AWS) at Conf42 Machine Learning 2021 on Amazon Connect with Lex, Kendra, SageMaker and Neptune for churn-aware routing and agent matching

The worst part of calling customer service is repeating yourself to three systems and two humans. [Asif Mujawar](https://www.conf42.com/Machine_Learning_2021_Asif_Mujawar_Seamless_Customer_Service_Amazon_Connect_Alexa), a Database Specialist Solutions Architect at AWS in London, used his Conf42 Machine Learning 2021 talk to show how Amazon Connect, wired to Lex, Kendra, a SageMaker model and an Amazon Neptune graph, hands a caller from an Alexa skill to the right human agent with the context intact, predicts churn on the way in, and routes on it.

It is an AWS solution walkthrough with recorded demos, set in a telecom customer service scenario, not a build-it-yourself tutorial.

## Why did Amazon build its own contact centre?

Connect started as an internal tool. Amazon's customer service runs over 70,000 associates supporting millions of customers in dozens of languages across 32 countries, and Prime Day means adding thousands of agents for a day and dropping them the next. He says the products Amazon evaluated were either good at scaling or good at customisation, never both. Asif Mujawar said at Conf42 Machine Learning 2021 that "we needed to have something that can be customizable, that can be scaled".

So Amazon built it, used it across more than 50 groups including Zappos and Audible, and, after AWS customers kept asking Andy Jassy what Amazon's contact centre ran on, launched it as Amazon Connect in March 2017. The basics are the usual contact centre kit (skills-based routing, voice and chat recording, real-time and historical analytics) on a multi-tenant service with managed telephony carriers. During the pandemic, the selling point was simpler: an agent needs a broadband connection and a USB headset.

## How does the Alexa-to-agent handoff work?

The first demo starts at home. A customer opens the provider's Alexa skill, verifies with a phone number and PIN, and gets asked whether the Wi-Fi problem from last time is still there, because the backend has looked up the previous interaction and its category. A frequently asked question (how do I top up my phone) is answered by an Amazon Lex bot backed by Amazon Kendra searching the knowledge base. When the customer asks for a person, Connect places an outbound call to them; nobody has to dial in or wait in a queue.

On the agent side, the call arrives with attributes already filled, including the channel, the queue and a churn prediction. When the customer asks what the monthly bill includes, the agent types the question into a Kendra search bar instead of digging through portals.

Under the hood: an Alexa skill calls the Lex bot, a Lambda function uses the Start Outbound Contact API, and Connect contact flows call other AI services through Lambda. A SageMaker model scores sentiment and churn, and the contact flow acts on it. Asif Mujawar said at Conf42 Machine Learning 2021: "Then we predict the customer churn and then we route the call based on whether the customer is about to churn or not churn." A caller with negative sentiment skips the IVR menus and goes straight to an agent who specialises in unhappy customers.

## How do you match a caller to the right agent?

The second half is about routing on more than skills. He lists three things to know: the new customer (captured live in the IVR), the existing customer base (satisfaction and churn, purchase history, purchasing power), and each sales agent. For the agent, he uses three checks before routing a sales call:

- **CSAT score and sentiment.** Higher-rated agents convert and retain more.
- **Product area expertise.** A technical support specialist is the wrong person for a sales call.
- **Sales revenue attainment.** An agent who has already hit this month's quota is, in his reading, less likely to go the extra mile, so new sales enquiries lean towards agents with high CSAT, the right product knowledge and quota still to reach.

Amazon Neptune holds the relationships. Customers link to their package, sentiment and spend; agents link to their revenue, sentiment and the packages they know. In his example, several happy customers share the 75 GB package, and only two of them have the spend pattern that suggests they would move up a tier. Customer data sits in DynamoDB, the graph is built from it and CRM sources, and a SageMaker model predicts churn and calculates offers.

## What do the demos show?

Two recorded calls. In the sales one, a new caller is recognised as interested in the 75 GB package before saying so, and the agent can steer towards a plan that fits a household of remote workers and YouTube-watching kids. In the retention one, a customer calls to cancel after repeated outages; the agent's panel already shows a model-generated offer, a 30% discount for a year, plus the escalation path to the technical team. The discount lands; the outage, fairly, still needs fixing.

## Who should watch?

Teams running or replacing a contact centre on AWS, and ML engineers who want a concrete example of a model's output changing routing decisions in real time rather than sitting on a dashboard. Skip it if you want code: the talk shows architecture and recorded demos, and the Neptune data model is described rather than queried.

## Related Conf42 talks

- Matteo Gabrielli on [getting insights from text with Amazon Comprehend](https://www.conf42.com/Machine_Learning_2021_Matteo_Gabrielli_Empower_business_insights_text) at Conf42 Machine Learning 2021.
- [Real-time churn detection with AI on Kubernetes](https://www.conf42.com/Kube_Native_2025_Gaurav_Sunkar_retention_churn_ai) at Conf42 Kube Native 2025.
- Samuel Baruffi on [Amazon Bedrock agents beyond chatbots](https://www.conf42.com/Machine_Learning_2025_Samuel_Baruffi_chatbots_bedrock_enterprise) at Conf42 Machine Learning 2025.

[Watch the talk on YouTube](https://youtu.be/q4Cgqq5NlbY).

## From AWS

- Amazon Web Services: [aws.amazon.com](https://aws.amazon.com/)
- Amazon Connect: [aws.amazon.com/connect](https://aws.amazon.com/connect/)
- Amazon Neptune: [aws.amazon.com/neptune](https://aws.amazon.com/neptune/)

## Watch the talk

[Seamless Customer Service with Amazon Connect and Alexa, using AI / ML](https://www.conf42.com/Machine_Learning_2021_Asif_Mujawar_Seamless_Customer_Service_Amazon_Connect_Alexa) at Conf42 Machine Learning 2021.
