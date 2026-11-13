# The logs say the transaction worked. An empty catch block disagrees

Conf42 Blog, 2021-03-24. https://www.conf42.com/blog/enterprise2021/swallowed-exception-green-logs-on-call

In short: Tom Granot (Lightrun) at Conf42 Enterprise Software 2021 on what monitoring can't tell an on-call developer, and how to get back to sleep sooner

A customer's purchase fails, the metrics look fine, and the logs show every service in the chain doing its job. At Conf42 Enterprise Software 2021, Tom Granot, Developer Advocate at Lightrun and a former site reliability engineer, walks through that incident from the on-call developer's chair and ends at an auto-generated catch block nobody filled in. His point: the bugs that wake developers up are exactly the ones a standard monitoring stack can't see, so answering a new question shouldn't require shipping new code.

## Who is on call when the playbook runs out?

The story follows Jamie, a Java developer with about five years of experience, on call for the transaction system of an enterprise application. Around Jamie: a DevOps engineer who knows the infrastructure, one or two support engineers who follow playbooks, and a NOC team watching all the systems. The transaction system is about six microservices (inventory, transaction, credit, fraud, external billing, a gateway), each with its own ELK monitoring stack.

On call, he says, always brings something new: a problem nobody has seen, one somebody saw and never documented, or an external system failing. Add the noise of logs, tickets and Slack messages, and a remotely complex application logic problem ends up with the developer once support and DevOps come up empty.

## What do your tools tell you, and what don't they?

Tom lays out the usual toolkit by layer: log lines (a timestamped event log of the application), infrastructure metrics (how the machines underneath feel), service or SLA metrics (the value as the customer sees it), distributed tracers like Zipkin and Jaeger, profilers like JProfiler, debuggers, and error monitoring. Modern stacks are good, he grants.

Then the list of what they miss:

- **Incorrect application state**, from product requests implemented wrong or edge cases nobody tested. Logic errors don't trip alarms.
- **Code-level quantities**, like the data structure growing in memory until an OOM, unless you instrumented it beforehand.
- **Swallowed exceptions**, thrown, caught and never emitted.
- **External APIs** that break their own spec or time out in odd ways.
- **Unexpected user flows**, where the state is correct but the user got there by a path nobody planned; he cites GitHub logging a user into the wrong session.
- **Races**, which need the exact circumstances to reproduce.

Adding a log line to dump the missing object isn't always allowed either, he notes, when PCI or HIPAA data is involved.

## How does the demo end?

Jamie has a user id (2911) and a set of green dashboards. The Kibana log trail for that user shows a clean path through inventory, transaction, credit, fraud and external billing, and back. So Jamie opens IntelliJ and reads the code, following the Feign clients from service to service, then jumps to the end of the chain, then works backwards. In the fraud service the problem is plain: a fraud check throws, and the catch block is the empty one the IDE generated.

Tom Granot said at Conf42 Enterprise Software 2021: "an exception was thrown and caught and we were none the wiser."

His working definition of observability is the ability to understand how your systems work on the inside without shipping new code, and this small app fails it. It cost precious minutes on a tiny codebase; on a large system with many teams it costs far more. The practice he proposes is continuous observability: a streamlined way to ask production a new question and get the answer immediately.

## What can you do before the next page?

Most of his advice is about people, not tools:

- Choose to love it, or at least don't be angry at the room: everyone is on call, including the DevOps engineer and the support engineer on the other end.
- Be prepared. You know how the application should behave, so answer questions fast.
- Document every odd incident in a searchable form; the one you think you'll never see again comes back in three to six months.
- Keep emergency debugging tools, from internal tooling to shell scripts, close at hand.
- Write postmortems that cover why it happened and how to stop it recurring, with input from every team: what the playbooks, dashboards and developer tooling were missing.
- Be humble about infrastructure; ask, and say plainly what is outside your control.

## Who should watch

Developers new to on-call rotations, and teams whose dashboards stay green while customers file tickets. Tom gave the talk at Conf42 Cloud Native 2021 as well.

## Related Conf42 talks

- Einat Mahat on [effective on-call practices](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices) at Conf42 Incident Management 2023.
- Shai Almog on [a polyglot cloud-native debugger beyond APM](https://www.conf42.com/Python_2022_Shai_Almog_polyglot_cloudnative_debugger_beyond_apm) at Conf42 Python 2022.
- Julie Gunderson on [postmortems, continuous learning and blameless culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at Conf42 Chaos Engineering 2021.

[Watch Tom Granot's talk](https://www.conf42.com/Enterprise_Software_2021_Tom_Granot_on_call_developer)

## From Lightrun

Lightrun builds what Tom calls a continuous observability toolbox: a way to explore a running application in real time instead of redeploying with more logging.

- Lightrun: [lightrun.com](https://lightrun.com/)

[Watch the talk on YouTube](https://youtu.be/hbfBvjzPyus).

## Watch the talk

[Getting back to sleep as soon as possible for the on-call developer](https://www.conf42.com/Enterprise_Software_2021_Tom_Granot_on_call_developer) at Conf42 Enterprise Software 2021.
