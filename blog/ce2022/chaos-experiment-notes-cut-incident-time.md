# The chaos experiment doc that held the safe delete command

Conf42 Blog, 2022-03-11. https://www.conf42.com/blog/ce2022/chaos-experiment-notes-cut-incident-time

In short: Paul Marsicovetere (Formidable) at Conf42 Chaos Engineering 2022 on how a documented Kubernetes chaos experiment cut a later production incident short

The most useful output of a chaos experiment might be the boring document you write afterwards. At [Conf42 Chaos Engineering 2022](https://www.conf42.com/ce2022), Paul Marsicovetere, Senior Cloud Infrastructure Engineer at Formidable in Toronto, told the story of one small Kubernetes experiment whose notes, weeks later, held the exact command his team needed in the middle of a production incident. The takeaway: write down every command you ran to inject the failure, including the dangerous ones.

It is a short talk, under ten minutes, built around a single real incident. No vendor tooling, no framework, just a team that broke something on purpose and kept good notes.

## Why break things at all?

Paul borrows Kolton Andrus's definition of chaos engineering, thoughtful, planned experiments designed to reveal the weakness in a system, and gives three reasons to bother. We depend more and more on cloud providers, and new kinds of outages keep appearing. Tests only check how code is supposed to behave. And there is a freedom in running an experiment with no expectations at all.

"Unit and integration testing can only really take us so far," Paul Marsicovetere said at Conf42 Chaos Engineering 2022. Chaos experiments show how an application actually responds, whether you remove a network file share or delete a database table.

## What was the experiment?

Deliberately modest. Take a Kubernetes cluster in a non-production environment, kill pods, and record how the service responds. The service under test had a parent-child design: a parent orchestrator pod spun up child pods for job requests, and the child pod logs streamed to a web page outside Kubernetes where clients watched their jobs.

The team terminated child pods, the parent pod and the underlying node while simulated scheduled jobs ran, wrote every error into a document, and watched the logs page to see what clients would see. The headline finding at the time was drift between the logs web page and the actual pod logs on the cluster, plus a few small bugs and failure modes nobody had mapped before. The document went to a team meeting and then, presumably, into a folder.

## How did it pay off in production?

Some weeks later the parent pod went into an error state in production with many child pods still running. Deleting it the wrong way risked taking those children, and services downstream, offline. Mid-incident, someone opened the chaos experiment document.

It held a safe command for deleting the parent pod without touching the running children, recorded because the team had logged how they injected each failure. It also held a very unsafe one. "I'm sure you can all guess which command was chosen to resolve this issue," he said.

## The lessons he draws

Paul's favourite part was not the lower MTTR. It was that the experiment was never designed to speed up incident response; it was designed to understand resilience, and the faster recovery came for free, along with bugs that became fixes and feature requests. Without the notes, the team would have been guessing at commands during an outage.

He also reframes non-production: not only a place to test features, resource changes and patches, but a safe place to inject failures and carry the learnings upward, before graduating experiments to production once confidence is built. Getting a new service to work at all is an underrated milestone, he says, but trying to break it in creative or esoteric ways is where the interesting results show up.

## Who should watch

Teams that have never run a chaos experiment and want a low-stakes first one, and anyone who needs a short, concrete story to convince a manager that game-day notes are worth the time. If you already run chaos in production, this one is a quick reminder rather than new material.

## Related Conf42 talks

- Vishnu Vardhan Chikoti on [utilising results from chaos experiments](https://www.conf42.com/Chaos_Engineering_2022_Vishnu_Vardhan_Chikoti_utilising_results_from_chaos_experiments), from the same event.
- Ayelet Sachto on [reliable systems that minimize incident impact](https://www.conf42.com/Chaos_Engineering_2022_Ayelet_Sachto_reliable_systems_minimize_incidents_impact).
- Kyle Shelton on [disaster recovery preparedness](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness).

[Watch Paul Marsicovetere's talk](https://www.conf42.com/Chaos_Engineering_2022_Paul_Marsicovetere_optimizing_incident_response) from [Conf42 Chaos Engineering 2022](https://www.conf42.com/ce2022).

## From Formidable

Formidable is a consultancy that partners with companies to build for the modern web and to design solutions to complex technical problems.

- Formidable: [formidable.com](https://formidable.com/?utm_source=Conf42&utm_medium=logo&utm_campaign=conf42)

[Watch the talk on YouTube](https://youtu.be/UbugZS4eK4s).

## Watch the talk

[Optimizing incident response thanks to Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2022_Paul_Marsicovetere_optimizing_incident_response) at Conf42 Chaos Engineering 2022.
