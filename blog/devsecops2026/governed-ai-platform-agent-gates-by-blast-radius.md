# One control plane for AI workloads, and approval gates by blast radius

Conf42 Blog, 2026-09-21, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/governed-ai-platform-agent-gates-by-blast-radius

In short: At Conf42 DevSecOps 2026, Peoplefluent's Sonu Kumar maps a five-layer governed AI platform where agents act only after policy says yes.

If your inference service and your payroll service pass through different control planes, you run two platforms that happen to share hardware. That is the core claim from Sonu Kumar, Senior DevOps Engineer at Peoplefluent with about 18 years in build systems, Kubernetes and observability, at Conf42 DevSecOps 2026. His reference architecture puts AI workloads and ordinary services under the same policy, identity and audit, and lets operational agents act only inside tiers defined by blast radius.

## Building for AI and building with AI

Kumar describes two jobs that pull against each other. Building for AI means GPU capacity, vector stores and model registries for RAG assistants, inference and agents. Building with AI means using it inside DevSecOps: validating rollouts, triaging incidents, catching drift. Most teams do one reasonably well. Few do both under the same controls, so an AI platform appears in a corner with its own rules, dashboards and on-call story, and the risk lives in the gap.

## Five layers, governance around all of them

His stack, bottom up: infrastructure (with dedicated, tainted GPU node pools and Cilium network policy between, say, a RAG service and its vector database), platform services (identity, secrets, a registry like Harbor where a model is just another signed and scanned artifact), AI workloads, DevSecOps automation with GitOps via Argo CD, and governance plus observability wrapped around everything.

The reason for the wrapper is the sharpest point in the talk. Governance used to live at the edges: an ingress check, a pipeline scan. An agent inside the cluster can call the Kubernetes API directly and never pass through the edge.

Some details worth stealing. Permission filtering in RAG has to happen at retrieval time, because a vector index that does not carry document permissions leaks across tenants quietly. Changing the embedding model means re-embedding the corpus into a second index and cutting over, a blue-green deploy for vectors. For inference autoscaling, queue depth or tokens in flight beat GPU utilisation as a signal.

## Policy as code, signed models, split roles

Security rests on three things. OPA Gatekeeper (or Kyverno if you prefer YAML) enforces admission, runtime and data access policies that live next to the code and go through pull requests, so "Why was my deployment blocked?" is answered by a commit. Start new policies in audit mode for a week or two; you will find the legitimate workload you forgot about. Models are signed with Sigstore Cosign as OCI artifacts and carry a bill of materials. And RBAC splits deploy, invoke, retrain and override into four roles, starting with the one broad service account most ML pipelines run on.

On observability he warns against labelling token metrics by user or prompt in Prometheus, a cardinality explosion in waiting, and pushes hard for full agent traces using the OpenTelemetry generative AI conventions.

## Check, then act, then record

Agents earn their keep in deployment validation, incident triage that escalates when confidence is low, self-healing inside approved playbooks, and drift correction. Mechanically: the agent has its own narrowly scoped service account, every tool call passes a thin gateway that asks the policy engine first and writes the audit record, and the model never holds broad credentials.

Approval gates come in three tiers. Tier one is small, scoped and reversible, such as aborting a canary in the agent's own namespace. Tier two runs and notifies a human. Tier three, anything touching shared infrastructure, production data or another team's workload, waits for a yes. His sorting question: if this goes wrong, how many people find out, and can we undo it in five minutes? Actions approved over and over become candidates to move down a tier.

## The canary that proved the point

He closes with a scenario he describes as very close to what his team deals with. A new generation model goes out as a 10% canary. P99 latency climbs from around 380 ms to over two seconds and canary pods get OOM-killed. The agent correlates metrics, logs and rollout history, aborts the canary as a tier-one action, and latency recovers. Then it proposes draining three GPU nodes still under memory pressure. Those nodes host another team's production model, so policy blocks it and the on-call engineer gets the evidence bundle. The follow-up fix became an admission policy: registry entries declare the GPU memory a model needs, and deployments requesting less are rejected.

## Who should watch

Platform teams being asked to host RAG and agents next to everything else, and anyone about to give an ops agent cluster credentials. Dense, practical, tool-specific.

## Related Conf42 talks

- [Ralph Bird asks who owns code that AI wrote and shipped](https://www.conf42.com/Observability_2026_Ralph_Bird_sre_agents_incidentresponse).
- [Neeraj Kumar Singh Beshane on GenOps, governance for AI in CI/CD](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity).
- [Bhaskar Bharat Sawant on SBOMs, SLSA and provenance in CI/CD](https://www.conf42.com/DevSecOps_2025_Bhaskar_Bharat_Sawant_supply_chain_ci), the supply chain habits Kumar wants applied to models.

[Watch Sonu Kumar's talk](https://www.conf42.com/DevSecOps_2026_Sonu_Kumar_platformengineering_governance_ai)

[Watch the talk on YouTube](https://youtu.be/8g8y3kXhBvU).

## Watch the talk

[Building AI-Native DevSecOps Platforms with Governed Platform Engineering](https://www.conf42.com/DevSecOps_2026_Sonu_Kumar_platformengineering_governance_ai) at Conf42 DevSecOps 2026.
