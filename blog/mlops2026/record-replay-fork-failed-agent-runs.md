# Record, replay, fork: debugging an agent that failed mid-run

Conf42 Blog, 2026-11-09, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/record-replay-fork-failed-agent-runs

In short: Reza Amini (Flashback) at Conf42 MLOps 2026 on saving agent runs as cassettes, replaying them offline and forking a fix from the first wrong call.

A customer ordered three cartons and the warehouse agent reserved three pallets. Nothing crashed, every tool call returned success, and the logs were clean. At Conf42 MLOps 2026, Reza Amini, senior engineer and founder of Flashback, uses that made-up order to show a debugging habit for agents: save every model and tool call of a run to a local file, replay the run offline, then fork from the first wrong call with a fix. His summary is four words long: "Reproduce first, change second."

## Why running the agent again is a different test

With ordinary software you reproduce the bug on your machine, change something, test and ship, as often as you like. An agent asks a model what to do and then calls live APIs and databases. Logs and traces tell you what happened, but they cannot play the run back.

So most teams run the whole agent again, and Reza walks through what that does to his five-step warehouse agent. Step one calls the customer system again. Step two reads stock again, and the count may now include the reservation from the failed run. Step three asks the model again, and it may decide differently. By step four the inputs have changed. If the request now says cartons, was it your fix or the model taking another path? If it says pallets, the warehouse has a duplicate request. Either way you paid for more model calls and have not tested a fix.

Retries do not help here either. They are for timeouts and crashes. This request went through. It was just wrong.

## A cassette is the run, saved call by call

Recording means wrapping your LLM client and your tools once, with a few lines of code. Every call that passes through them is saved in order: input, output, any error, how long it took. Reza calls the resulting local file a cassette. He stresses that this is no proxy and no middleman, and the agent's own code does not change.

The demo agent's five steps become six calls: two tool calls that read the customer and the order, a model call that decides what can ship, a model call that writes the warehouse request, a tool call that sends it, and a model call that drafts the reply. In the cassette, call three says three cartons. Call four says three pallets. The model's unit slip was planted on purpose for the demo. The real bug is in the code, which sends the model's proposal to the warehouse when it should send the decision.

Replay runs the agent again locally, with each model and tool call answered from the cassette. No tokens, no live systems, no second reservation, and the same result every time. Reza is upfront about the limit: replay only covers the calls you recorded. Code that reads the clock, uses random numbers or talks to something unrecorded can still change the run.

## Replay refuses to lie after you change the code

The best moment of the demo comes after the fix. Reza changes two fields so the outgoing request uses the decision, then replays the old cassette. Replay stops at the warehouse call and says so, because the new request no longer matches the recording. It will not hand back an old result that does not fit.

That is the cue to fork. Like a branch in Git, a fork picks a call, reuses everything before it from the cassette and runs live from there. He forks at call four: calls one to three are frozen, calls four to six hit the model and the warehouse tool, and the reservation and customer reply now say three cartons. Only those three calls cost anything. The fork is written to a new cassette that records its parent and fork point, and a compare command shows the two runs side by side. The CLI in the demo is Flashback's, with commands to list and show cassettes.

## A fork does not cancel the three pallets

Reza closes with three cautions. Fork from the earliest wrong call, since everything after it is suspect. Record every model and tool call, because a skipped one goes live on each replay. And remember the world outside the debugger: "a fork alone doesn't really undo what already happened," Reza Amini said at Conf42 MLOps 2026. The pallets from the original run are still reserved and someone has to cancel them.

He places the habit next to existing tools. Traces help you find the failure. Replay and fork reproduce it and test a fix on the same inputs. A fork is like one eval case on that failed run, and a full eval set tells you whether the fix holds elsewhere.

## Who should watch

Anyone running multi-step agents with side effects who has ever fixed a bug by re-running production and hoping. Be aware it is a founder's talk: the demo uses Flashback, which Reza says is in early access, and the last minutes cover its roadmap, including testing a change across many saved runs and safe forks that will not touch real systems unless you choose to. The habit itself is tool-neutral, and most of the 27 minutes are spent teaching it.

## Related Conf42 talks

- [From Agent Trace to Reproducible Regression Test](https://www.conf42.com/MLOps_2026_Raju_Dandigam_trace_regression_agent) by Raju Dandigam at Conf42 MLOps 2026.
- [Your Agent Works. Will It Survive Tomorrow? Operating LangGraph.js with skein-js](https://www.conf42.com/MLOps_2026_Maina_Wycliffe_langgraph_skein_agent) by Maina Wycliffe at Conf42 MLOps 2026.
- [You Can't Debug What You Can't See: Observability for AI Agents](https://www.conf42.com/Observability_2026_Sabith_K_Soopy_agents_debugging_tracing) by Sabith K Soopy at Conf42 Observability 2026.

[Watch Reza Amini's talk](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Your Agent Failed Mid-Run. Logs Won't Replay It.](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) at Conf42 MLOps 2026.
