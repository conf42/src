# Your LLM writes good Terraform but cannot see your infrastructure

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/infrastructure-as-a-graph-for-llms

In short: Roxane Fischer of Anyshift at Conf42 DevOps 2026 on why AI fails at infrastructure without context, and how a live knowledge graph of cloud, code and state fixes it.

Ask a coding assistant for a Terraform VPC peering connection and you get clean, idiomatic code that references a VPC that does not exist. At Conf42 DevOps 2026, Roxane Fischer, co-founder of Anyshift, used that small example to make a large point: LLMs are now good at writing infrastructure code, and they still fail at infrastructure because they cannot see the live dependencies around it. Her fix is to model infrastructure as a graph and give the AI that graph as context.

Anyshift builds AI on-call engineers for root cause analysis, but Roxane says up front that the talk is about the technology underneath, the graph, and not a product tour. That makes it useful whether or not you ever touch their tool.

## Three ways to write one peering connection

The opening example is the best part of the talk, because it shows the failure mode step by step.

First, a developer with no AI writes the peering by copying VPC IDs out of the AWS console and hardcoding them. It works today, and it quietly breaks dependencies as the estate grows.

Second, GitHub Copilot does better on style. It knows hardcoded values are bad practice and reaches for references instead. But it does not know where your VPC is defined, so it creates a new one, which is complete as code and completely unrealistic as infrastructure.

Third, an AI IDE like Cursor that can read several repositories should, in principle, wire the reference to the VPC in another repo through remote state. Except that the junior developer's hardcoded ID from the first step only points at a cloud resource, not at any code. Cursor cannot reconcile cloud data with code, so the dependency link never gets made. The missing ingredient each time is the same: context about what actually exists.

## Infrastructure already is a graph

Roxane's argument is that a graph database is the natural shape for this context. Nodes are VPCs, IAM roles, pods, containers and accounts; edges are relationships such as an IAM role attached to an EC2 instance, or an instance belonging to a VPC. Layer on metadata (where a resource is defined in code, who owns it, who last committed to it, its timeline) and you can ask questions like which instances or pods have run hot on CPU over the last 24 hours and what depends on them.

She notes that at Anyshift, once versioning is included, such a graph can reach tens of millions of nodes. Every answer depends on that density.

## Building one is mostly ontology and plumbing

The recipe she gives is honest about where the effort goes:

- **Pick a graph database.** Anyshift uses Neo4j internally; she mentions Amazon Neptune as an option.
- **Define the ontology.** Decide what nodes and edges exist, with a common model across AWS, GCP and Azure so the AI treats equivalent resources as equivalent despite different definitions.
- **Populate and keep it fresh.** Each integration differs: scan AWS APIs for resources, and use CloudTrail for live updates.

Clean, structured data is the slow, expensive part, she says, and also what makes the context good.

## Where MCP servers are enough, and where they stop

For smaller estates, Roxane suggests a lighter route: connect MCP servers for your cloud providers to your AI tools and query live data directly. It is quick to set up and useful. The limit is that each MCP call is an API call returning a bounded slice of data, so a question that needs every dependency, relationship and bit of history in one go needs a prebuilt graph behind it.

## Drift detection as the worked example

She closes with a concrete subset: reconcile AWS resources, Terraform state and Terraform files into one graph. Parse all three, match entities by their IDs across cloud, state and code, then load the links into the graph and keep it updated. The result shows what is correctly defined in code, what has drifted, and what is shadow IT.

The abstract also promises natural language to Cypher querying and measuring context quality; the recorded talk runs to its 15-minute limit before getting there, so expect the graph-building half rather than the evaluation half.

## Who should watch

Platform and DevOps engineers evaluating AI assistants for infrastructure work, and anyone wondering why their copilot keeps inventing resources. If you already run a CMDB or asset graph, the ontology section will feel familiar and the AI angle gives it new reasons to exist.

## Related Conf42 talks

- [Shipping with Context: Knowledge Graphs as the Backbone of AI-First Software Delivery](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prateek_Mittal_knowledge_graphs_delivery) by Prateek Mittal makes the same case for graphs one level up, across the delivery process.
- [Stop AI Agents from Making Up Facts: Graph-RAG for Reliable Data Retrieval](https://www.conf42.com/MLOps_2026_Elizabeth_Fuentes_Leone_graph_rag_retrieval) by Elizabeth Fuentes Leone covers the Graph RAG side the abstract mentions.
- [From Ghost Assets to Infrastructure Drift - Don't Get Spooked](https://www.conf42.com/Cloud_Native_2022_Naor_Paz_ghost_assets_infrastructure_drift) by Naor Paz is a good pairing for the drift and shadow IT example.

[Watch Roxane Fischer's talk](https://www.conf42.com/DevOps_2026_Roxane_Fischer_context_reasoning_infrastructure)

[Watch the talk on YouTube](https://youtu.be/_v1oPl0oBjY).

## Watch the talk

[Context Engineering for DevOps: Turning Your Infrastructure into a Reasoning Graph](https://www.conf42.com/DevOps_2026_Roxane_Fischer_context_reasoning_infrastructure) at Conf42 DevOps 2026.
