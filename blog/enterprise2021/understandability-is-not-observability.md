# Understandability is the metric your team isn't tracking

Conf42 Blog, 2021-03-24. https://www.conf42.com/blog/enterprise2021/understandability-is-not-observability

In short: Liran Haimovitch (Rookout) at Conf42 Enterprise Software 2021 on software understandability, how it differs from observability, and five ways to improve it

Liran Haimovitch, CTO and co-founder of Rookout, argued at Conf42 Enterprise Software 2021 that the reason a trivial task such as sorting a data structure takes days in a big system is rarely the task. It is the time spent working out how, where and with what side effects to do it. He calls that property understandability, defines it with four criteria borrowed from finance, and gives five ways to improve it, only one of which is a debugger.

## Flying slow or flying blind

Haimovitch spent about a decade in cybersecurity before Rookout and is an advocate of agile, DevOps and lean. He frames the cost with a report finding that 68% of organisations experience the trade-off between flying slow and flying blind: you either move carefully, trying to understand each change, or move fast and ship potentially dangerous changes without knowing their impact. The abstract adds that in surveys most developers say they spend at least a day a week troubleshooting their own code.

## What does understandable software mean?

The term comes from finance, where insurers and pension funds have to make reports their customers can actually read. Applied to software, a system is understandable when it is presented so that an engineer can easily comprehend it. And a system is more than source code. Haimovitch lists five parts: the code, configuration and state, the runtime environment (Spring Boot, Micronaut, WebLogic, a cloud runtime), service dependencies from open source libraries to other microservices to Stripe, and the hardest to predict, inputs and outputs. A function that takes JSON only makes sense once you know what JSON it really gets.

The finance criteria carry over too. The information must be complete, concise, clear and organised, so you can move from a short summary down to the source and across to sample inputs and production configuration.

## How is it different from complexity, readability and observability?

Complexity is related but not the same: hand someone a bare JAR and ask what it does, then hand them the same JAR with source, docs and input examples. Same complexity, very different understandability. Readability helps clarity, but readable code can still be incomplete or disorganised. Observability tells you whether a system is up and serving customers; understandability goes a step back to how and why it works. Improving any of the three usually helps, but isn't always possible.

## What can you do about it?

His five levers:

- **Minimise complexity.** Cut functional and non-functional requirements, hire the best developers, use the highest-level building blocks (cloud, open source), apply encapsulation and abstraction, and build step by step with agile and DevOps to avoid over-engineering.
- **Create and curate knowledge.** Learn the system from colleagues and from whoever used to work on it ("Buy them a cup of coffee"), document what you find, then share it through talks, tutorials and internal meetups, and fold the corrections back in.
- **Build development environments that match production.** The same Java version (Java 11, not 14 or 8, which behave differently), the same database and operating system, ideally the same scale, with high-quality test data. Environments drift, so this is ongoing work, and compliance makes production data hard to use.
- **Get access to observability tools.** Logs, traces, metrics and error tracking won't tell you everything, but they make guesses better educated.
- **Use debuggers, which he calls understandability tools.** Classic debuggers let you step, rewind and change values, but they don't reach Kubernetes, serverless or production. Next-generation debuggers such as Rookout use non-breaking breakpoints to give that experience anywhere.

The first lever comes with an honest caveat. All of it is easy on a new system and hard on one that is 10 or 20 years old. "I mean, you can't cut back on requirements on a system that has been written for 20 years, and you can't change the engineering team who originally wrote it," Liran Haimovitch said at Conf42 Enterprise Software 2021. That is why the knowledge and tooling levers matter most for legacy code.

## Who should watch?

Engineering leads looking for words to explain why their team is slow on a mature codebase, and developers who have just inherited one. It is a conceptual talk with no demo; Rookout comes in at the end as one example of the last lever.

## Related Conf42 talks

- Tom Granot on [getting the on-call developer back to sleep](https://www.conf42.com/Cloud_Native_2021_Tom_Granot_on_call_developer) at Conf42 Cloud Native 2021.
- Elinor Sapir on [debugging differently](https://www.conf42.com/Cloud_Native_2023_Elinor_Sapir_debugging_debugging_differently) at Conf42 Cloud Native 2023.
- Finbar Fleming on [debugging errors in production](https://www.conf42.com/JavaScript_2022_Finbar_Fleming_debugging_errors_in_production) at Conf42 JavaScript 2022.

[Watch Liran Haimovitch's talk](https://www.conf42.com/Enterprise_Software_2021_Liran_Haimovitch_understandability_wrong), part of [Conf42 Enterprise Software 2021](https://www.conf42.com/enterprise2021).

## From Rookout

Rookout is a live data collection and debugging platform: it collects data from running applications on the fly, with no extra coding, redeployments or restarts. Liran Haimovitch is its CTO and co-founder.

- [Rookout website](https://www.rookout.com)

[Watch the talk on YouTube](https://youtu.be/htiICUhTmH8).

## Watch the talk

[Why you’re getting understandability wrong](https://www.conf42.com/Enterprise_Software_2021_Liran_Haimovitch_understandability_wrong) at Conf42 Enterprise Software 2021.
