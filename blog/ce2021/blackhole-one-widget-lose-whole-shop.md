# Blackhole one widget, lose the whole shop

Conf42 Blog, 2021-02-25. https://www.conf42.com/blog/ce2021/blackhole-one-widget-lose-whole-shop

In short: Tammy Bryant (Butow) (Gremlin) at Conf42 Chaos Engineering 2021 on live blackhole and packet-loss attacks against a Kubernetes demo store

The recommendations box at the bottom of a product page is not in anyone's critical path, until you blackhole it and the whole store stops working. At Conf42 Chaos Engineering 2021, Tammy Bryant (Butow), Principal SRE at Gremlin, runs three live network attacks against a Kubernetes demo shop, with a hypothesis written down before each. One degrades gracefully. Two take the site down. That ratio is the argument for running the experiments.

Before Gremlin she was an SRE manager at Dropbox for databases, block storage and code workflows, where she credits chaos engineering with a 10x reduction in incidents in three months.

## Where do you start?

Not with low-hanging fruit, she says: in SRE that isn't impactful. Start with your top five critical services, and expect different people in the same company to give different answers when you ask what those are. Typical picks: monitoring and alerting, caches like Redis or Memcached, payments, databases.

Her recipe from there: whiteboard the service with the team, pick a scenario (validate alerting, validate autoscaling, make a dependency unavailable, shut down a host or container), set the magnitude in servers and duration, form a hypothesis, baseline your metrics (ideally with SLOs and SLIs per service), mind the blast radius, run, measure, then fix or widen the blast radius.

## Why is detection her favourite metric?

She co-wrote an O'Reilly book on mean time to detection with friends from LinkedIn, Twitter and Amazon, and gives the reason in one line. Tammy Bryant (Butow) said at Conf42 Chaos Engineering 2021: "if it takes you a week to detect an incident and five minutes to resolve it, it still means that it took you a week and five minutes to fix the issue."

Among the other benefits she lists: finding monitoring gaps, validating upstream and downstream dependencies, fire drills that trigger real alerts to real teams, and fewer 2am pages. She also argues for chaos before big automation projects, since automation takes years and uncovers its own failures.

## What happened in the demo?

The target is the twelve-service hipster shop demo. On the whiteboard she trims it to seven services in the critical path (checkout, payment, shipping, cart, product catalogue, the cache and the frontend), leaving email, currency and recommendations out. Being off the critical path is good, she notes; critical-path teams get more checks and more compliance. One concern straight away: the cart seems to live only in a Redis cache, so where are the backups?

1. **Blackhole the ad service, 60 seconds.** Hypothesis: the ads disappear, nothing else breaks. Result: exactly that. Products load, the cart works, orders go through. Graceful, like Netflix hiding a broken hero banner. Along the way the Gremlin UI shows the ad service runs a single pod across two hosts, so there is nothing to fail over to, which is the next experiment.
2. **Blackhole recommended products, 60 seconds.** Same hypothesis. Result: a full outage. Product pages hang, the cart won't open, only the home page loads. Some hard-coded dependency turns a nice-to-have into a single point of failure.
3. **Packet loss on the cart service.** Hypothesis: no cart items lost. Result: the site is unusable and returns a 500 error with logs visible to every user. Gremlin aborts the attack once it detects the problem. The good news afterwards: all 22 items are still in the cart, so no data was lost.

Each result goes into the scenario record (passed, or failed with an incident uncovered and not mitigated), error message included.

## What do you do with the results?

Her closing questions: was it expected, was it detected, was it mitigated, did we fix it (code, config or process), and can we automate it so past failures run regularly and the system doesn't drift back. Then write it up as an executive summary of what you learned and fixed, schedule attacks, run game days as a team, and wire chaos into CI/CD as a shift-left practice.

## Who should watch

Teams that have read about chaos engineering and want to see what a first network experiment looks like on Kubernetes, start to finish, including the parts that fail.

## Related Conf42 talks

- Tanveer Gill on [graceful degradation when everything goes wrong](https://www.conf42.com/Chaos_Engineering_2023_Tanveer_Gill_graceful_degradation_everything_goes_wrong) at Conf42 Chaos Engineering 2023.
- Henrik Rexed on [Kubernetes chaos engineering in production](https://www.conf42.com/Site_Reliability_Engineering_2022_Henrik_Rexed_kubernetes_chaos_engineering_production) at Conf42 SRE 2022.
- Sakshyam Shah on [steady states and developing hypotheses](https://www.conf42.com/Chaos_Engineering_2022_Sakshyam_Shah_steady_states_developing_hypotheses) at Conf42 Chaos Engineering 2022.

[Watch Tammy Bryant (Butow)'s talk](https://www.conf42.com/Chaos_Engineering_2021_Tammy_Bryant_Butow_breaking_network)

## From Gremlin

All three attacks run from Gremlin's chaos engineering platform, targeting Kubernetes deployments, with options to narrow a blackhole to specific IPs, ports or providers. Tammy also points to Gremlin's free bootcamps (101 introduction, 201 automation and CI/CD), its Chaos Champion program and the chaos engineering Slack community.

- Gremlin: [gremlin.com](https://www.gremlin.com)
- Gremlin bootcamps: [gremlin.com/bootcamps](https://www.gremlin.com/bootcamps)

[Watch the talk on YouTube](https://youtu.be/vslg-W-ox-k).

## Watch the talk

[Chaos Engineering: When The Network Breaks](https://www.conf42.com/Chaos_Engineering_2021_Tammy_Bryant_Butow_breaking_network) at Conf42 Chaos Engineering 2021.
