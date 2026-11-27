# Generative AI can turn a plain-English request into an ETL pipeline

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/plain-english-etl-with-generative-ai

In short: Achyut Kumar Sharma Tandra of Amazon explains at Conf42 Platform Engineering 2025 how LLM-driven ETL parses intent, plans execution and generates pipelines.

The number of pipelines a data team can ship is capped by the number of data engineers it has, and every analyst in the company knows it. At Conf42 Platform Engineering 2025, Achyut Kumar Sharma Tandra, Data Engineer at Amazon, describes how generative AI changes that equation: users describe the data they need in plain English, and a system parses the intent, plans the work and generates, deploys and monitors the pipeline.

It is an architecture and adoption talk, not a product pitch. He does not name a specific tool; he describes the components such a system needs and the results he attributes to organisations that built one.

## Three bottlenecks of traditional ETL

Tandra names the familiar trio. Manual coding means every pipeline needs a specialist, so throughput equals headcount. The learning curve means the analysts and business users who need data most cannot get it themselves, so they file tickets and wait. Operational overhead means pipelines are never done; maintenance and troubleshooting eat the time that should go to new work. If your data team's roadmap is mostly a list of other teams' reports, you have met all three.

## Four components between a sentence and a Spark job

The core of the talk is the architecture, and it is the part worth stealing for a design review:

1. **Natural language interface.** Users type or speak a request, with contextual help to sharpen vague ones.
2. **Semantic parser.** Maps the request to real data entities, relationships and transformations. Ask for sales by product and it knows which tables hold sales and products and how they join.
3. **Execution planner.** Decides how to run it given data size, available resources and governance policies.
4. **Runtime engine.** Emits executable code for the target framework, whether a Spark job or a series of SQL queries.

Intent recognition is the step that separates this from keyword search. His example: a request about sales trends should become a time-series analysis with the right aggregations, not a single query. In a fuller walk-through, a marketing user's request for total sales by product category and the top ten customers turns into a sum, a group-by and a ranking, plus a time comparison, scheduling, output formatting, monitoring and notifications.

## The unglamorous foundation

To get from demo to enterprise, Tandra lists what has to sit underneath: metadata discovery that catalogues every source so the model knows what exists; credential management on zero-trust principles; caching to avoid recomputing frequently run reports; stream support for time-sensitive work such as fraud detection; data lineage tracking for audits and debugging; and API orchestration across systems. Lineage is the one regulated industries will care most about, because a pipeline nobody wrote still needs a paper trail.

## Results, and the caveats he gives

He shares two case studies from unnamed companies. A financial services firm with over 300 data sources went from an average of three weeks per new pipeline to hours, with most common integration tasks done without code and a smaller engineering backlog. An e-commerce company cut customer-behaviour pipeline builds from five days to 30 minutes, and its marketing team built over 75 pipelines on its own. He also cites aggregate benchmarks from a dozen enterprise implementations showing large drops in pipeline creation time and errors.

To his credit, he is realistic about limits. Complex transformations may still need hand-written code extensions, large volumes may need tuning of generated pipelines, and legacy systems without modern APIs need connectors. Governance must adapt to many user-generated pipelines, and data engineers shift from writing code to architecture and oversight. His rollout advice: discovery, a pilot on two or three low-complexity, high-value use cases, validation against the old method, then scale.

## Who should watch

Data platform leads drowning in report requests, and engineers designing an LLM-to-SQL or LLM-to-Spark layer who want a component checklist. If you are sceptical of no-code claims, watch for the limits section; it is more candid than most talks on this topic.

## Related Conf42 talks

- [AI-Driven ETL Evolution: Harnessing Machine Learning for Scalable, Intelligent Data Pipelines](https://www.conf42.com/Golang_2025_Sudhakar_Kandhikonda_etl_ai_pipelines) by Sudhakar Kandhikonda, Conf42 Golang 2025
- [Leveraging AI to Optimize ETL Pipelines](https://www.conf42.com/Large_Language_Models_LLMs_2025_Gaurav_Mittal_etl_pieplines) by Gaurav Mittal, Conf42 Large Language Models 2025
- [Kube-Native ETL at Scale: Optimizing PySpark + Airflow Workflows](https://www.conf42.com/Kube_Native_2025_Sruthi_Erra_Hareram_etl_airflow_optimization) by Sruthi Erra Hareram, Conf42 Kube Native 2025

[Watch Achyut Kumar Sharma Tandra's talk](https://www.conf42.com/Platform_Engineering_2025_Achyut_Kumar_Sharma_Tandra_redefining_generative_free)

[Watch the talk on YouTube](https://youtu.be/e7lLh7kfmYI).

## Watch the talk

[Scalable, Code-Free ETL: How Generative AI is Redefining Data Integration](https://www.conf42.com/Platform_Engineering_2025_Achyut_Kumar_Sharma_Tandra_redefining_generative_free) at Conf42 Platform Engineering 2025.
