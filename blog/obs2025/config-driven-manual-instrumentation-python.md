# Wave turned ten years of manual instrumentation into a config file

Conf42 Blog, 2025-05-22, updated 2026-11-09. https://www.conf42.com/blog/obs2025/config-driven-manual-instrumentation-python

In short: Jean-Mark Wright of Wave at Conf42 Observability 2025 on CACI, Python metaclasses that capture span attributes from config instead of hand-written code.

Auto-instrumentation gets you the databases, caches and HTTP calls. The attributes that actually explain your business logic, which plan, which feature group, which customer, have to be added by hand, and at Wave that hand-work added up to about ten years. At Conf42 Observability 2025, Jean-Mark Wright, staff engineer leading observability at Wave, showed how his team replaced most of it with configuration and Python metaclasses. They call it Config-Accelerated Custom Instrumentation, or CACI.

## The 15-minute fix that started it

The talk opens with an incident. An on-call engineer noticed that Wave was giving away Transaction Import, a premium feature that lets small businesses pull bank transactions into the accounting product, to users on the free starter plan.

The service involved had excellent manual instrumentation in Datadog, so the team could interrogate traces directly. Were users being put on the right plan? Graphing traces by plan said yes, the starter plan. Opening a single trace showed a span attribute nobody had thought about: the feature group was the legacy one. Plans point to feature groups, and the starter plan was pointing to the legacy group, which includes Transaction Import. Graphing feature group over time showed exactly when it started. It was data corruption in the database. Jean-Mark says they found it within 12 minutes and had the leak fixed in 15.

## The bad news: one service like that, 40 without

That service had taken roughly three months of engineering effort to instrument this well over its year and a half of development. Wave has about 40 other microservices. Three months times 40 is 120 months, hence the title. Parallelising helps, but it would still take years.

## Instrument the data, not the call sites

CACI starts from two observations. First, requests flow through a predictable stack of components: API, then service with business logic, then repositories for persistence. Second, data passes between them as arguments: business ID, user ID, country, business name. If engineers can say which data they care about, a framework can wrap every component and capture it wherever it appears.

So engineers write a telemetry capture configuration with allowed and disallowed field names and field types, with support for data classes and dictionaries. They do not have to know which component handles which field.

## Metaclasses do the wrapping

The implementation uses a Python metaclass, a class that creates classes. When a component declares the service metaclass, the metaclass loops over its methods, replaces each with a wrapper that inspects the inputs, captures any that match the configuration as span attributes, and then calls the original function. Application code stays untouched. Because the result is a little magical, they also generate a coverage report listing every component, method and input with a tick for whether it is captured.

## What the pilot showed

On a new microservice, CACI took instrumentation coverage from 1% to about 60%, and getting the configuration in place took less than a week instead of months. The captured fields show up in traces, logs and errors alike, so the team can break errors down by event type or latency by Kafka topic, the same kind of slicing that solved the premium leak.

Next on the list: a component-agnostic metaclass beyond services, capturing outputs as well as inputs, using LLMs to speed up rollout across the fleet, and Datadog's dd-trace support for propagating attributes between spans.

## Who should watch

Python teams with good auto-instrumentation and poor answers to the question of which customers are affected. This is one of the most concrete talks of the event: a real incident, a clear design and code you can picture writing. If your stack is not Python, the idea of declaring data of interest once and capturing it at component boundaries still transfers.

## Related Conf42 talks

- [Jesus Espino on struct embedding, instrumentation and code generation in Go](https://www.conf42.com/Golang_2021_Jesus_Espino_struct_embedding_instrumentation_code_generation), a similar wrap-the-components idea in another language, at Conf42 Golang 2021.
- [Sumit Kaul on observability as a platform contract with zero-code instrumentation](https://www.conf42.com/DevOps_2026_Sumit_Kaul_slos_instrumentation_observability) at Conf42 DevOps 2026.
- [Nikolay Sivko on zero-instrumentation observability based on eBPF](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Nikolay_Sivko_zeroinstrumentation_observability_ebpf) at Conf42 SRE 2024.

[Watch Jean-Mark Wright's talk](https://www.conf42.com/Observability_2025_JeanMark_Wright_instrumenting_second_months)

[Watch the talk on YouTube](https://youtu.be/9FOAaGyQX1c).

## Watch the talk

[Instrumenting at 10 years per second](https://www.conf42.com/Observability_2025_JeanMark_Wright_instrumenting_second_months) at Conf42 Observability 2025.
