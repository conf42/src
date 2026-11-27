# Rate limits that watch behaviour instead of counting requests

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/ai-rate-limiting-watches-behaviour-not-counts

In short: Rehana Sultana Khan (Versa Networks) at Conf42 Incident Management 2025 on ML rate limiting that lets real traffic spikes in and slows the bots down.

A fixed rate limit fails twice: it slams the door on the crowd your marketing team worked hard to attract, and it waves through the patient bot that spreads its requests across a hundred IP addresses. At Conf42 Incident Management 2025, Rehana Sultana Khan, Software Engineer at Versa Networks, made the case for rate limiting that classifies behaviour rather than counting requests, and walked through how to build it on the big three clouds.

She tells it as a story, which is unusual for a talk this close to security engineering, and it works. A shop door with a "five people per hour" rule, and a friend called Sarah who runs a travel app with the same kind of static threshold.

## The static threshold is wrong in both directions

Sarah's first bad day: an influencer writes about her app, real users flood in, the limit kicks in and blocks them for an hour. No revenue, lots of angry people. Her second bad day: a scraper comes in from many IP addresses, each one politely staying under the limit, and walks off with all the flight and hotel data. The threshold saw nothing wrong.

Khan names the two failure modes plainly. False positives turn into abandoned transactions and damaged customer relationships. Sophisticated attackers who distribute traffic across IPs and time never trip the rule in the first place, so there is nothing to respond to.

## Hire a committee, not a bouncer

The fix is to replace the counter with something closer to a security guard who watches how people behave. Instead of a single number, the model looks at request timing patterns, payload characteristics, geographic distribution, user agent diversity and response code sequences, plus the temporal dimension: what a session does over time. A real shopper logs in, browses and adds to a cart. A scraper hits the same endpoints with perfect spacing and never buys anything.

Her "committee of experts" is a friendly description of decision tree ensembles such as random forests and gradient boosting: one tree is good at geography, another at timing, another at browsers, and the majority vote wins. She picks them because they handle mixed data types, capture non-linear relationships and stay relatively interpretable. Class imbalance (legitimate traffic vastly outnumbers attacks) is handled with sampling techniques and cost-sensitive learning, and the models keep learning through online updates and periodic retraining.

## Slow them down before you block them

The most practical idea is progressive throttling. Rather than a binary allow or deny, the system applies subtle delays, then rate reductions, and only blocks outright when confidence is high. Users are grouped into behavioural cohorts that they can move between, earning more headroom with legitimate use or losing it with suspicious activity.

She maps three attack types onto this: credential stuffing (rapid failures from many IPs, followed by forced password resets for affected accounts), API scraping (robotic browse patterns with no purchases) and low-and-slow account takeover (a valid account that only ever views personal and payment details).

For the build, she lists the cloud pieces: API Gateway, Lambda and SageMaker on AWS; API Management with Azure Machine Learning; API Gateway with Vertex AI on Google Cloud. Multi-cloud setups get one central policy source pushed to every region, with Kubernetes helping keep deployments consistent.

## The numbers, with a caveat

Khan cites figures for organisations that adopt this approach, including 30% lower infrastructure costs from not serving junk traffic, and an e-commerce case study with a 92% drop in false positives while handling 300% traffic spikes during flash sales. The case study is not named, so read these as the shape of the payoff rather than a benchmark. Her measurement advice holds regardless: track detection accuracy and adaptation rates next to business metrics like blocked legitimate users and support tickets, because security metrics alone tell half the story.

## Who should watch

Platform and API teams who own gateway configuration, and anyone who has had to explain why the launch-day spike got a wall of 429s. It is an accessible, analogy-heavy introduction, so security specialists will want to pair it with something more hands-on.

## Related Conf42 talks

- [API Security in DevSecOps: Built-In, Not Bolted On](https://www.conf42.com/DevSecOps_2024_Anirudha_Karandikar_api_security) by Anirudha Karandikar covers the rest of the API defence stack.
- [Navigating the World of API Gateways](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison) by Roman Rastiehaiev compares the open-source gateways you would hang this on.
- [Enhancing API Security in Modern Enterprise Platforms](https://www.conf42.com/Incident_Management_2024_Pavan_Vovveti_32_api_security_enterprise) by Pavan Vovveti, from the previous Incident Management edition.

[Watch Rehana Sultana Khan's talk](https://www.conf42.com/Incident_Management_2025_Rehana_Sultana_Khan_ratelimiting_api_protection)

[Watch the talk on YouTube](https://youtu.be/7tRgh5Yyvec).

## Watch the talk

[AI-Driven Rate Limiting for Resilient and Cost-Efficient Cloud API Protection](https://www.conf42.com/Incident_Management_2025_Rehana_Sultana_Khan_ratelimiting_api_protection) at Conf42 Incident Management 2025.
