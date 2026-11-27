# Use AI on your platform to cut the cognitive load nobody needs

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-should-cut-extraneous-cognitive-load

In short: Mia-Platform's Michel Murabito at Conf42 Platform Engineering 2025: cut extraneous cognitive load with self-service, reusable components and RAG over docs and logs.

In 2004 you could deploy a website by dragging a folder onto a server. At Conf42 Platform Engineering 2025, Michel "Mitch" Murabito, developer advocate at Mia-Platform, used that memory to make a sharp point: the job got harder faster than our ability to manage it, and the only kind of cognitive load a platform team can really remove is the unnecessary kind. AI, used well, is one more tool for removing it.

Mitch co-organises Cloud Native Days Italy and co-founded the Developer Life and Green Software Italia communities, so this is a talk from someone who spends his days listening to developers complain.

## Three kinds of load, one you can delete

The framework is cognitive load theory. Intrinsic load is the task itself being hard; you reduce it by learning, not by tooling. Germane load is the effort of learning something new, like figuring out how CI/CD pipelines work, and that is the good kind. Extraneous load is everything else: poor tools, clunky UIs, workflows with too many steps, unclear docs. That third category is the target, because it is the only one you can cut without a trade-off.

His example is painfully familiar. A developer needs a new environment, files a Jira ticket, and waits while an ops colleague configures resources, variables, networking and security, possibly from another building, possibly from a beach. The platform's job is to make that a self-service click.

He also takes a swipe at the idea that Kubernetes is the hard part. It is just a tool; the real complexity is scalability, distribution, data, integration, security, privacy and now AI, plus choosing between twenty API gateways in the CNCF catalogue.

## Platform engineering is more than a portal

Mitch argues that most people picture platform engineering as an internal developer portal plus an infrastructure orchestrator. His picture is wider: application assets such as ready-made API gateways, API and event portals, a software catalog or marketplace of reusable microservices, a data control plane, and AI services.

That catalog enables what he calls a circular economy. Team one builds a payment microservice and documents it well. Team two reuses it and adds PayPal support as a new version. Team three takes the payment service, adds invoicing, and publishes that too. Nobody starts from zero, which is the whole point, and good documentation is the price of entry.

## RAG over your docs and your logs

The AI section is concrete. Put your LLM behind a RAG layer that holds the platform's documentation, the configuration of your services, and the logs. Now a developer can ask whether the logs show any warnings, which errors they are, and how to fix them, and the assistant can answer with your error codes and your docs in context. That only works if configuration and documentation are centralised in the platform first, which is a nice argument for doing platform work before AI work.

## Start with a problem and a metric you already have

The closing advice is the most transferable. Ask why you need a platform at all, pick a couple of problems rather than everyone's problems, and reuse metrics you already have. His favourite: how long a developer waits for a new environment. Track it over the long run, because tools that help in month one can drag in month twelve, and tie it to business value.

## Who should watch

Platform leads making the case for their roadmap, and anyone told to "add AI" to an internal platform without a clear use case. Mitch himself calls it a theoretical talk; the RAG-over-logs idea and the environment-wait metric are what you walk away with.

## Related Conf42 talks

- [Edidiong Asikpo on closing the developer experience gap of Kubernetes development](https://www.conf42.com/Kube_Native_2023_Edidiong_Asikpo_closing_developer_experience_gap) tackles the same friction from the Kubernetes side.
- [George Hantzaras and Dan Mckean on building a self-service DBaaS for your internal developer platform](https://www.conf42.com/Cloud_Native_2023_George_Hantzaras_Dan_Mckean_self_service_dbaas_internal_developer_platform) is the self-service environment idea made real.

[Watch Michel Murabito's talk](https://www.conf42.com/Platform_Engineering_2025_Michel_Murabito_practical_elevate_strategies)

[Watch the talk on YouTube](https://youtu.be/No_GtgnBdRo).

## Watch the talk

[AI for Platform Engineering: Practical Strategies to Elevate Developer Experience](https://www.conf42.com/Platform_Engineering_2025_Michel_Murabito_practical_elevate_strategies) at Conf42 Platform Engineering 2025.
