# Agent reliability is a property of the platform around the model

Conf42 Blog, 2026-11-16, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/self-healing-cloud-infrastructure-agentic-ai

In short: Amit Anand at Conf42 MLOps 2026 on the platform agents need to heal infrastructure: durable runs, a policy gate, run IDs and autonomy per action class.

At 99% success per step and no retries, a 50-step agent run completes about 60% of the time. Amit Anand, who builds distributed systems, payment systems and AI agents, uses that arithmetic at Conf42 MLOps 2026 to argue that agent reliability is decided by the platform, and then runs an architecture review of that platform with one incident threaded through it: latency on an API service creeps up after a deployment, and an agent proposes a rollback.

"The reliability of agentic system is a property of the platform around the model," Amit Anand said at Conf42 MLOps 2026. He opens and closes on that sentence.

## An agent run is a long workflow whose control flow you do not know

Amit reads an agent run as a distributed, long-running workflow where the model picks the control flow at runtime. A trigger starts the run, then it loops: plan through the model gateway, act through the tool gateway, write a checkpoint to a state store, emit telemetry tagged with the run ID. Every arrow is a remote call that can be slow, fail or be retried.

Four forces follow. You do not know a run's length or fan-out when you admit it, so you need admission control and run budgets. Failures compound, so you retry individual steps and each step must be safe to retry. Runs outlive their compute, since a pod or a deploy can end before the run does, so state has to be durable. And one run mixes GPU-bound, CPU-bound and I/O-bound work, which calls for separate pools that scale on work signals.

## The planner never touches production

In the incident, telemetry arrives through OpenTelemetry, detection correlates alerts and traces into one incident, diagnosis finds the deployment, and planning proposes a rollback with a risk score. Then comes the box Amit calls the most important: the policy gate. Policy as code decides whether a rollback is permitted on this service right now and answers allow, deny or ask a human. If allowed, the change is applied, preferably as a Git commit that a controller reconciles.

Verification closes the loop. If latency and error rates recover, done. If the result is unclear or worse, the default is to stop and escalate to the on-call engineer. An automatic compensating action runs only where one has been defined and tested.

The security model is a trust boundary. Everything the agent reads is untrusted: alerts, logs, tickets, tool output. A line injected into a log can steer an agent with broad privileges, the classic confused deputy. So the agent runtime gets a scoped identity that can read telemetry, call the model and write its own state. It emits a typed request, and every infrastructure-changing action goes through a gateway that can refuse. As a side benefit, "Your compliance evidence is the gateway log."

## Retry storms, duplicate actions and 200 OK

Amit walks through three failure modes. In a retry storm, a model endpoint slows, every agent retries together and load peaks when capacity is lowest, which is also how cost runs away. The response is rate limits, jittered backoff and load shedding at the gateway. Duplicate actions happen when a worker crashes after requesting the rollback and before recording the result, so actions need idempotency keys and you verify state before retrying when the outcome is unknown.

The observability gap is the quiet one. Model and tool spans come from different libraries with no shared context. The Kubernetes change carries no run ID, so the audit log shows a service account patched a deployment and cannot say which decision caused it. Nothing records the outcome: every call returns 200 whether or not latency recovered. His rule is to connect run ID, decision, action and outcome, because you should not automate what you cannot evaluate.

## Autonomy is granted per action class

The reference architecture has one logical control plane per organisation holding the model and tool registry with evaluation gates, GitOps and policy, quota and the observability backend, over identical Kubernetes clusters per cloud. Inside a cluster, a KEDA scaler sets the worker count from queue depth and age, and scale-in must respect active runs. The GPU pool scales on waiting requests, queue time and time to first token, because throughput flattens once the pool is saturated.

On multi-cloud he is careful. Routing new inference requests to another cloud is the easy case, though a pairing such as GKE with Vertex AI and EKS with Bedrock is not interchangeable, so prompts and evaluations must pass on both. Resuming a run already in progress is harder. You pay for it in recovery time, data residency constraints, network cost and idle GPUs.

Autonomy is set by reversibility and blast radius. Reversible and narrow actions may become autonomous, wide and irreversible ones need approval, and every class starts as recommend-only and steps up when its evaluation passes and its production record is clean. For run execution he compares LangGraph checkpoints with a workflow engine such as Temporal and notes the two can be used together.

MLOps comes in at release. Version the model, prompt, tools and configuration together, evaluate the version on past incidents, deploy gradually. "A new prompt goes through the same gate as a new model."

## Who should watch

Platform engineers and SREs who have been asked to let an agent act on production and want the design questions in one place. It is a dense architecture review in under fifteen minutes, with no demo and no vendor product. The migration order alone is worth noting down: join the traces, insert the gateway in recommend-only mode, turn runbooks into typed tools, then promote by evidence.

## Related Conf42 talks

- [From Agents to Systems: Orchestration, Recovery, and Economics](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics) by Rajesh Gupta at Conf42 MLOps 2026.
- [Autonomy with Guardrails: Operating Agentic Automation in High-Risk Production Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating) by Ajay Athitya Ramanathan at Conf42 SRE 2026.
- [Gate the Action, Not the Alert](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou at Conf42 DevSecOps 2026.

[Watch Amit Anand's talk](https://www.conf42.com/MLOps_2026_Amit_Anand_agentic_cloud_healing) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Engineering Cloud Infrastructure for Agentic AI: MLOps and Self-Healing Systems](https://www.conf42.com/MLOps_2026_Amit_Anand_agentic_cloud_healing) at Conf42 MLOps 2026.
