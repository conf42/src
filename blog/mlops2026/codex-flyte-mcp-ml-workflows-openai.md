# How OpenAI connects Codex to Flyte through MCP for ML training runs

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/codex-flyte-mcp-ml-workflows-openai

In short: Phoebe Wang (OpenAI) at Conf42 MLOps 2026 on a read-only Flyte MCP tool that lets Codex turn a failed training run link into a first fix to test.

OpenAI hosts Flyte for its internal traditional ML training jobs, and the unit that moves between people, the orchestrator and the coding agent is a run link. At Conf42 MLOps 2026, Phoebe Wang, Member of Technical Staff at OpenAI working on ML infrastructure, shows how a small Flyte MCP server lets Codex look up a failed execution, report what Flyte recorded and suggest the first thing to test. It is a short talk with one clear pattern in it.

## A failed run is three questions

Phoebe starts with a scene every ML engineer knows. You change a model, submit the full training job, go back to other work, and later receive a link to a failed run. In her fictional example, loading the data worked, training failed, and evaluation never started because it needs the trained model. What she wants to know at that point is which step failed, what error was reported and what to test next.

The three pieces each have one job. Flyte, the open-source ML orchestration layer, runs the steps of a workflow and records the state of every run. MCP, the Model Context Protocol, lets an AI application use tools, so a Flyte MCP server can expose a tool that looks up a run and returns its task states and recorded errors. Codex is where the question gets asked.

"The useful handoff is the link," Phoebe Wang said at Conf42 MLOps 2026. The same link can go to a teammate, and both people start from the same run.

## The run record is what makes the next run a fair comparison

A workflow defines the steps; a run is one attempt at them. Her example is an image classifier where run 41 finished all three steps and run 42 stopped in training, both from the same workflow.

That history matters the next morning, when the editor holds three more changes. Which version of the code did the failed job run? Was it the same dataset as the last good run? Did the batch size or the GPU type change? She keeps the run link and records the workflow version, the software environment, the dataset and the inputs, which for this classifier include the evaluation split and the batch size. Change one thing in the next run and those records make the comparison fair. They also let you trace a model you want to serve back to the run that produced it.

## Give the tool a narrow, read-only job

The integration answers one small question: given a link, can Codex tell which step failed and what Flyte recorded? Phoebe's summary of the design: "That gives the tool a narrow read-only job."

For run 42 the tool returns the run state, the failed task and the error details. Flyte says the training step ran out of GPU memory and that evaluation was skipped, so the place to look is training. Her advice for teams building something similar comes as four principles:

- Start with the information someone would normally open the workflow UI to find.
- Give the tool a way to identify the exact run.
- Return the task and the error in a form the agent can refer to.
- Keep access scoped to the runs the caller is allowed to see.

## Evidence first, then a suggestion you still review

In the Codex CLI, the first part of the answer is the evidence: the error trace Flyte returned. The suggestion follows from it. An out-of-memory error in training points to a smaller batch, because a smaller batch keeps fewer things in GPU memory at once. Codex can update the local training code and environment so the modified run can start.

Phoebe keeps the human in two places. She reviews the change before submitting a run, and she checks the evaluation score afterwards, because a smaller batch can change training behaviour. A run that finishes and a model worth keeping are two separate things to verify.

The talk ends with the step after training. Her team built a GPU deploy skill in Codex so experimental models can be put on GPUs quickly and tested end to end for latency and availability. The example request is to prepare a test deployment of version three of the classifier and show the change for review, which gives Codex a model, a version, a target and a clear point to hand back.

## Who should watch

Platform engineers who run Flyte, or any workflow orchestrator, and are deciding what to expose to coding agents first. The session is brief and uses a fictional run on slides; it does not go into how the MCP server is implemented, and the checklist promised in the abstract arrives as the four design principles above. As a pattern for a first, low-risk agent integration, it is easy to copy.

## Related Conf42 talks

- [Less Theater, More Engineering: A Production Claude Code + MCP Agent Pipeline at 80% Accuracy](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) by Suneet Malhotra (Motorola Solutions) at Conf42 AI Agents 2026.
- [Building an MCP Server in Go for a Real B2B Workflow](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow) by Shadi Elyafi at Conf42 Golang 2026.
- [From Agents to Systems: Orchestration, Recovery, and Economics](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics) by Rajesh Gupta at Conf42 MLOps 2026.

[Watch Phoebe Wang's talk](https://www.conf42.com/MLOps_2026_Phoebe_Wang_codex_flyte_mcp) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Build ML Workflows with Codex, Flyte, and MCP](https://www.conf42.com/MLOps_2026_Phoebe_Wang_codex_flyte_mcp) at Conf42 MLOps 2026.
