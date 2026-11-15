# Rate limiting that reads behaviour instead of counting requests

Conf42 Blog, 2025-10-21, updated 2026-11-09. https://www.conf42.com/blog/js2025/rate-limiting-that-reads-behaviour-not-request-counts

In short: Rehana Sultana Khan of Versa Networks showed at Conf42 JavaScript 2025 how 27 behavioural features and tree ensembles replace static API limits.

A product launch that goes viral on Hacker News and a DDoS look exactly the same to a static rate limiter: lots of requests, fast. At Conf42 JavaScript 2025, Rehana Sultana Khan, Technical Program Manager and Engineering Manager at Versa Networks, showed how to swap that request counter for a model that reads 27 behavioural features per client, scores the threat, and slows bots down without slamming the door on real users.

## The fixed threshold is wrong both ways

Set the limit low and you block your best customers mid-flash-sale with HTTP 429s; she cited a figure of 41% of legitimate traffic blocked by overly aggressive static rules. Set it high and abuse walks in, while you over-provision infrastructure for the worst case and pay for servers that sit idle most of the time.

She named three flaws: rigid thresholds that can't tell a good spike from an attack, no context (a user who has logged in from the same office for two years looks like a script from a foreign data centre), and the operational cost of not trusting your limiter.

The threat that exploits all three is the low-and-slow application-layer DDoS. A botnet of thousands of devices sends a few requests per minute each, staying just under your limit, aimed at the expensive endpoints: login, search, checkout. Each IP looks like a quiet user. Together they drain database connections and CPU while the rate limiter waves them through.

## Collect, engineer, train, deploy

Her pipeline has four steps. First, instrument API gateways and load balancers to capture what she calls the digital DNA of each interaction: request frequency and burst patterns, the milliseconds between calls (humans are irregular, scripts keep metronome time), the sequence of endpoints, what happened after each request, login success and failure rates, session token behaviour, response times and 5xx rates, geolocation, IP reputation, and device fingerprints.

The outcome signals are the clever part. A run of 404s suggests a scanner. A run of 401s followed by a single 200 could be credential stuffing in progress.

Second, turn those facts into 27 features in four groups:

- **Temporal**: request-rate volatility, a burst score, time-of-day anomalies.
- **Access behaviour**: endpoint entropy (a shopper goes home, search, product, cart; a scanner jumps between login, admin and export) and a flag for known malicious sequences.
- **Network**: a "geographically impossible" score for New York to London between two requests, IP reputation, a source anomaly index.
- **User context**: a session confidence score, and failed-login velocity normalised against the user's own 90-day baseline. A forgetful typist failing three times means less than a user who never fails suddenly failing twenty.

## A committee and an investigator

Third, training. She uses a decision tree ensemble: a random forest as a committee of specialists, each looking at a different slice of features and voting, plus gradient boosting as the investigator for subtle edge cases. She reported 97.5% model accuracy, inference in microseconds, and interpretability good enough to see which features drive a decision. Retraining runs continuously on new labelled production traffic.

Fourth, deployment: the model runs as a serverless function (AWS Lambda or Azure Functions) behind the API gateway, which computes features, asks for a score and enforces the answer. Scale-to-zero billing, automatic fan-out during spikes, multi-zone availability by default, and blue-green deployments for model updates.

## Slow them down instead of blocking

Her strongest idea is progressive throttling. The model assigns a threat score from 0 to 100. Scores from 0 to 30 get full speed. From 31 to 70, small added delays: a 500 millisecond pause cripples a script and a human barely notices. From 71 to 99, much stricter limits. Confirmed threats are blocked. Graceful slowdown is what keeps false positives from turning into angry customers.

Across production deployments on AWS, Azure and Google Cloud she reported 96% detection accuracy, a 68% drop in false positives and over 27% infrastructure cost savings.

## Who should watch

API platform and security teams tired of tuning one number per endpoint, and anyone who has had a marketing launch blocked by their own WAF. You'll want an ML-literate colleague to build the training pipeline, but the feature list alone is worth stealing for rule-based systems.

## Related talks

- [API Security in DevSecOps: Built-In, Not Bolted On](https://www.conf42.com/DevSecOps_2024_Anirudha_Karandikar_api_security) covers the rest of the API security toolkit.
- [Navigating the World of API Gateways: A Comparative Analysis of Open Source Solutions](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison) helps pick the gateway this would plug into.
- [Enhancing API Security in Modern Enterprise Platforms: Strategies, Challenges, and Future Trends](https://www.conf42.com/Incident_Management_2024_Pavan_Vovveti_32_api_security_enterprise) looks at API protection from the enterprise platform side.

[Watch Rehana Sultana Khan's talk](https://www.conf42.com/JavaScript_2025_Rehana_Sultana_Khan_rate_limiting_cost)

[Watch the talk on YouTube](https://youtu.be/PYXt-bflVGc).

## Watch the talk

[AI-Driven Rate Limiting for Scalable, Secure, and Cost-Efficient APIs](https://www.conf42.com/JavaScript_2025_Rehana_Sultana_Khan_rate_limiting_cost) at Conf42 JavaScript 2025.
