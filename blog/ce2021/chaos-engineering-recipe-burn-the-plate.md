# Burn the plate on purpose, then taste and adjust

Conf42 Blog, 2021-02-26. https://www.conf42.com/blog/ce2021/chaos-engineering-recipe-burn-the-plate

In short: Ana Margarita Medina (Gremlin) at Conf42 Chaos Engineering 2021 on chaos engineering as a learning loop, with blast radius, magnitude and abort conditions

Most cooks learn by tasting as they go, and most of them have burned a pan or two before a recipe works. At Conf42 Chaos Engineering 2021, [Ana Margarita Medina](https://www.conf42.com/Chaos_Engineering_2021_Ana_Margarita_Medina_fire_chaos), Senior Chaos Engineer at Gremlin, used the kitchen to make the case that chaos engineering is first a way of learning: small, planned experiments with clear limits, run until the system and the team stop surprising you.

It is a good first talk on chaos engineering, built around one metaphor and the vocabulary you need to run an experiment safely.

## What does cooking have to do with production?

Medina opens with a question to the audience: how did you learn to cook? Watching others, following tutorials, hands-on attempts, early feedback, or a fire extinguisher? Her own answer is building and breaking. She cooks for other people, mixes four or five recipes together, and tastes constantly.

Ana Margarita Medina said at Conf42 Chaos Engineering 2021: "I actually need to burn my plate in order for me to learn."

The mapping to software is direct. Tasting as you go is observability and gradual rollouts. Cooking for others is focusing on the end user. Burning the plate on purpose is replaying past incidents to practise.

## Why bother: downtime and complexity

She splits the cost of downtime into what you can count (lost revenue, engineers pulled off feature work, SLA chargebacks) and what you cannot (brand damage, and attrition from teams stuck firefighting). She puts the average at around $300,000 per hour of downtime, before any high-traffic event. Meanwhile complexity keeps climbing: one waterfall release became daily deploys, one monolith became hundreds of interdependent services, hundreds of servers became hundreds of thousands of Kubernetes resources.

## The vocabulary that keeps it thoughtful

Her definition of chaos engineering stresses three words: thoughtful, planned experiments designed to reveal weakness. Breaking production for fun is not it. The safeguards:

- **Blast radius**: the surface area of the experiment, from one server or one service out of 100 to 10% of the infrastructure.
- **Magnitude**: the intensity, such as CPU raised in 10% steps, or latency injected at 100 ms, then 300, up to 800 ms.
- **Abort conditions**: the signals in monitoring or user experience that tell you to stop and roll back.

The method follows the scientific one: observe the system and its architecture diagrams, baseline the metrics (a good moment to set SLOs and SLIs), form a hypothesis with abort conditions, set blast radius and magnitude, run, analyse, then expand or fix and rerun. The last step is the one she calls among the most important: share the results with leadership, the organisation and the wider community.

## Two experiments to start with

The first targets autoscaling. Raise CPU to 60% across the hosts, with abort conditions on HTTP 400 and 500 errors or anything that feels wrong for customers, and test a hypothesis such as a new node being up within two minutes and traffic being rerouted while it joins.

The second targets dependencies, including the ones your diagram treats as minor. Her example is a Redis cart service used as a cache in a Kubernetes app, with the hypothesis that latency on a mere caching layer should not affect the application. She leaves the result for her bootcamps, which is a fair tease.

## The recipe

Her closing recipe is availability, reliability and practice. Assume things will break, battle test new tools before rolling them out, keep asking what happens when X fails for every box on the diagram, and check that you are not about to relive the incident from five months ago. As she puts it, chaos engineering builds reliable systems, "but you also build reliable people and organizations with that."

## Who should watch

Teams new to chaos engineering, and anyone who needs a friendly way to explain blast radius and abort conditions to colleagues. Experienced practitioners will know the method already.

Related Conf42 talks:

- Tammy Bryant Butow, also of Gremlin, on [breaking the network](https://www.conf42.com/Chaos_Engineering_2021_Tammy_Bryant_Butow_breaking_network) at the same event.
- Karolina Rachwał on [onboarding chaos engineering](https://www.conf42.com/Chaos_Engineering_2021_Karolina_Rachwa_onboarding_chaos_engineering), Conf42 Chaos Engineering 2021.
- Mandi Walls on [game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering), Conf42 Incident Management 2022.

## From Gremlin

Gremlin builds a chaos engineering platform; Medina pointed viewers to it to try the full suite of Gremlin attacks.

- [Gremlin](https://www.gremlin.com)

[Watch the talk on YouTube](https://youtu.be/EEDE7YzWjCU).

## Watch the talk

[In the kitchen: A sprinkle of fire and chaos](https://www.conf42.com/Chaos_Engineering_2021_Ana_Margarita_Medina_fire_chaos) at Conf42 Chaos Engineering 2021.
