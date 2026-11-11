# OpenTelemetry already sees your code in prod. Nobody looks

Conf42 Blog, 2022-12-01. https://www.conf42.com/devsecops2022/opentelemetry-feedback-loop-developers-skip

In short: Roni Dover (Digma) at Conf42 DevSecOps 2022 on turning free OpenTelemetry data into continuous feedback developers actually use while coding

Most teams already collect enough telemetry to tell a developer whether their last feature works, who calls it and where it is slow. At Conf42 DevSecOps 2022, Roni Dover, CTO and Co-Founder of Digma, argued that the missing piece is not more data but a feedback loop: OpenTelemetry gives you the traces almost for free, and the hard part is getting them in front of the person who wrote the code.

It's a sponsor talk, and Roni says so when he gets to Digma. The first two-thirds are a practical case for OpenTelemetry tracing that works with any backend.

## What happens after Bill ships?

Roni builds the talk around Bill, a solid developer with a great CI/CD pipeline who has just released a feature. Roni's instinct after a release is to ask questions: did the code run at all, is anyone using it, did that data access change make things better or worse? He has seen carefully written code sit a few bad if statements away from ever executing in production.

What Bill actually does, most of the time, is pick up the next ticket. Roni went looking for why, and found it in the overused DevOps infinity loop. Every stage has a crowd of tools except one: continuous feedback, which in the diagram he pulled had a single tool attached to it, Salesforce. Developers get rich feedback locally, some red/green feedback from tests, and next to nothing from production.

## Why OpenTelemetry matters: everyone agrees on it

Roni's take on OpenTelemetry is refreshingly unromantic. It is a spec with implementations for many languages, and its value is consensus rather than novelty.

"it is important first and foremost because everyone agrees on it," Roni Dover said at Conf42 DevSecOps 2022. Library and framework maintainers no longer have to pick which vendor agent to support; they support OpenTelemetry, and an ecosystem of tools grows on top. He notes that .NET went as far as putting it in the standard library.

To test the claim he built a deliberately non-trivial demo: a Gringotts vault API (he was watching Harry Potter with his kids at the time) on FastAPI, RabbitMQ through the Pika client, PostgreSQL via SQLAlchemy and psycopg, plus an external mock API. Every one of those libraries had ready-made instrumentation. The setup code amounts to calling each instrumentor's instrument method, and including the right packages can make even that automatic. Manual spans, which he calls logging on steroids, cover the business steps, such as authenticating a vault owner with a key.

## Traces and spans, in one demo

A trace is one flow through the system: an appraisal request hits the FastAPI service, becomes a message on the queue, and gets picked up by a goblin worker. A span is a piece of that flow, such as checking permissions or enqueueing the job, with its caller, duration, errors and logs. Exported to Jaeger, the trace shows both services, the HTTP call, each database statement and the custom spans, all from instrumentation he didn't write by hand.

The same data is useful before a change, too. Who uses this code? Who breaks if I change it? What is the baseline to compare against, and where does concurrency happen?

## So why doesn't Bill look?

Roni lists the small reasons first. Expertise: making the numbers mean something takes outlier removal, medians and p99s, and not everyone has brushed up on Statistics 101. Context switching: a new tool and constant hops between IDE and dashboard.

The big reason is that it isn't continuous. Nobody decides to run the tests or deploy; the pipeline does it on every merge. Feedback needs the same treatment.

## What continuous feedback looks like in the IDE

This is where Digma comes in, framed as Roni's vision rather than a feature tour. With the plugin switched on, the vault service code gets annotations from its production traces: the area sees low traffic, there is an N+1 query that repeats over 101 times in each trace, here are the callers affected. It also shows code that runs only in production and not in local tests, and code that is never reached at all. The trace view then starts from the issue instead of from a dashboard search.

## The culture part

His closing point is not about tools. Developers once argued that testing was QA's job; owning code all the way to production is the same shift. He has seen observability dashboards that might as well have been pictures on the wall. "If we don't use and harvest the observability data we already have, then why are we collecting it?" he asks. His practical fix: put feedback on the agenda, with at least a biweekly meeting on what the shipped features are doing.

## Who should watch

Developers who own services in production but rarely open the tracing UI, and leads wondering why their observability spend never reaches the code review. If you already live in Jaeger, the culture section is the part to hear.

More OpenTelemetry at Conf42: [Nicolas Frankel on OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) at DevOps 2023, [Nočnica Mellifera on open source observability with OpenTelemetry](https://www.conf42.com/DevOps_2023_Nocnica_Mellifera_open_source_observability_opentelemetry), and [Yosef Arbiv on OpenTelemetry](https://www.conf42.com/Cloud_Native_2022_Yosef_Arbiv_opentelemetry_epsagon) at Cloud Native 2022.

[Watch Roni Dover's talk](https://www.conf42.com/DevSecOps_2022_Roni_Dover_observant_developer_opentelemetry_from_code_to_prod) from [Conf42 DevSecOps 2022](https://www.conf42.com/devsecops2022).

## From Digma

In the talk, Roni shows Digma as an IDE plugin that reads OpenTelemetry data and surfaces insights such as N+1 queries, bottlenecks and usage next to the code. He also points to continuousfeedback.org for getting-started links, including OpenTelemetry, Jaeger and the Gringotts demo project, which runs with Docker Compose.

- Digma: [digma.ai](https://digma.ai/)

[Watch the talk on YouTube](https://youtu.be/pD1Wl0LfB_g).

## Watch the talk

[The Observant Developer - OpenTelemetry from code to prod](https://www.conf42.com/DevSecOps_2022_Roni_Dover_observant_developer_opentelemetry_from_code_to_prod) at Conf42 DevSecOps 2022.
