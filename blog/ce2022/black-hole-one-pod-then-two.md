# Black-hole one pod and the bank app shows an engineer error

Conf42 Blog, 2022-03-11. https://www.conf42.com/blog/ce2022/black-hole-one-pod-then-two

In short: Julie Gunderson (Gremlin) at Conf42 Chaos Engineering 2022 on chaos engineering and game days as the Accelerate path to tempo and stability

A single-replica service is a single point of failure that looks fine right up until you unplug it. At Conf42 Chaos Engineering 2022, Julie Gunderson, Senior Reliability Advocate at Gremlin and previously a DevOps advocate at PagerDuty, tied chaos engineering and game days to the tempo and stability metrics from *Accelerate*, then proved the point on Google's open source Bank of Anthos: black-hole the one pod behind a service and customers get a cryptic error; run two replicas and the same attack goes unnoticed.

## Why measure reliability with Accelerate?

People ask how to prove chaos engineering is worth it, and Julie's answer is the research by Nicole Forsgren, Jez Humble and Gene Kim. Tempo is deployment frequency and change lead time; stability is mean time to recover and change failure rate. *Accelerate* treats reliability as the foundation for tempo, and her reasoning is human: engineers who trust the system ship new code with more confidence. The book asks for systems that can detect and tolerate failures, and the most direct way to check that, she argues, is to inject real failures.

## Chaos is the wrong word for it

"Chaos engineering is a misnomer," Julie Gunderson said at Conf42 Chaos Engineering 2022. The practice is methodical: a baseline of metrics under normal load, a hypothesis, the smallest experiment that yields a signal, a customer-facing metric such as orders per minute that halts the experiment if it moves, a known way to roll back, then a slowly widening blast radius from one host to the fleet and from dev to staging to production. Both outcomes are wins: either you gain confidence or you find the bug before your customers do. And share what you learn, internally and, if allowed, outside.

## What happened to Bank of Anthos?

Bank of Anthos is a multi-language banking demo (Python and Java services, two Postgres databases for accounts and the ledger) that you can spin up for free in Google Cloud Shell. Her hypothesis: black-holing the balance reader, a critical-path service, should degrade gracefully. The Gremlin UI immediately showed only one pod in the replica set, so the experiment would take out the whole service.

It did not degrade gracefully. The balance turned into a confusing placeholder, a $1,000 deposit still succeeded and showed in the transaction history while the balance stayed broken, and payments failed with an error message written for engineers. She points out who reads those messages: "my mom calls me to see if I can figure out what's wrong, even though I have repeatedly told her that I do not work at these organizations."

Black-holing the transaction history service was kinder, a plain cannot-load message while deposits still worked. Then the fix: `kubectl scale` the transaction history deployment to two replicas and black-hole 50% of them. The failover blip was too short to see, and users still got their data.

## How do you run a game day?

Game days are the second practice, and she sells them as relationship-building as much as testing. Her recipe: four or more people from at least two teams, 30 minutes to an hour (not a lost day), a chosen comms channel, two or three planned scenarios, and roles such as commander, observer and scribe. Spike load with JMeter or Gatling and attack CPU to see autoscaling kick in and back down, test dependencies, and test capacity plans; she recalls outages where teams tried to scale on peak day and hit limits or missing permissions. Gremlin publishes a scenario template covering attack target, type, expected behaviour, risk and impact.

Then automate: codify experiments, version them, and gate production readiness in CI/CD on passing a set of reliability experiments.

## Who should watch

Teams starting chaos engineering who want a measured method and a business case, and Kubernetes folks who want a tidy single-replica demonstration to show their team. The demo uses Gremlin, though she notes any chaos tool works.

## Related Conf42 talks

- Mandi Walls on [game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering) at Conf42 Incident Management 2022.
- Sakshyam Shah on [steady states and developing hypotheses](https://www.conf42.com/Chaos_Engineering_2022_Sakshyam_Shah_steady_states_developing_hypotheses), from the same event.
- Ana Margarita Medina on [continuous reliability](https://www.conf42.com/Chaos_Engineering_2022_Ana_Margarita_Medina_continuous_reliability).

[Watch Julie Gunderson's talk](https://www.conf42.com/Chaos_Engineering_2022_Julie_Gunderson_the_road_to_reliability) from [Conf42 Chaos Engineering 2022](https://www.conf42.com/ce2022).

## From Gremlin

Gremlin builds a chaos engineering platform for running fault-injection experiments, including black hole and resource attacks, on hosts and Kubernetes.

- Gremlin: [gremlin.com](https://www.gremlin.com)
- Game day guides and scenario template: [gremlin.com/gamedays](https://www.gremlin.com/gamedays)
- Chaos engineering certification: [gremlin.com/certification](https://www.gremlin.com/certification)

[Watch the talk on YouTube](https://youtu.be/BKsxJRzuxTI).

## Watch the talk

[The Road to Reliability](https://www.conf42.com/Chaos_Engineering_2022_Julie_Gunderson_the_road_to_reliability) at Conf42 Chaos Engineering 2022.
