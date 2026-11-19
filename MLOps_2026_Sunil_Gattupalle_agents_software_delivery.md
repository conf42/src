# What Your Agents Need to Know About Software Delivery

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Sunil Gattupalle](https://www.conf42.com/speaker_Sunil_Gattupalle) (Engineering Architect @ Harness). Page: https://www.conf42.com/MLOps_2026_Sunil_Gattupalle_agents_software_delivery

## Abstract

**[Harness free plan - sign up here!](https://app.harness.io/auth/#/signup?utm_source=webinar&utm_medium=webinar&utm_campaign=2026q4-conf42-mlops)**

Before a coding agent changes a service, it helps to know who owns it, where it runs, and what shipped last week. A pipeline agent preparing to promote that same service needs a different answer. Are there open incidents? Does the artifact it’s about to deploy have a critical vulnerability? Both agents need to know how the code, the artifact, and the running service relate to one another.

We’ll show how Harness models those relationships in a software delivery knowledge graph and makes them available to agents through the Model Context Protocol (MCP). We’ll follow a plain-language question from prompt to answer, showing how the graph checks that the requested relationships exist and returns only the records the user has permission to see.


In the demo, we’ll ask a coding agent the same question with and without the graph. You’ll see which details it can establish from the repository alone and what it can verify once it can follow a change into production.


Thanks!
