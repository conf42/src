# A solo dev forced his LLM failover live and found four ladders

Conf42 Blog, 2026-10-03, updated 2026-11-09. https://www.conf42.com/featureflags2026/forced-llm-failover-one-kv-flag

In short: Fuad Laguda at Conf42 Feature Flags 2026 on a three-state Cloudflare KV trace flag and a deliberately forced failover from Claude Sonnet to Qwen on Nebius.

If you've never forced your backup to run, you've never seen it work. At Conf42 Feature Flags 2026, Fuad Laguda, an independent infrastructure engineer in Stirling, Scotland, who runs two production web apps alone, showed the one-key Cloudflare Workers KV flag behind his diagnostics and LLM provider failover, then pulled the plug on his own production app on camera and found a bug in his failover that he'd never have caught otherwise.

The scale is honest from the first minute: no team, no rota, and if something breaks at 11 at night the person who gets up is him. The app under test is Postbarrel, which turns people's stories into social video scripts and has paying customers.

## A trace flag with three states, read on every request

The constraint behind everything: he can't ship a build with more logging and wait, and he can't leave detailed tracing on, because the trace holds users' own scripts. Keeping personal data at rest because it might be useful one day, he says, isn't a decision, it's laziness with somebody else's personal data.

So one KV key, traceMode, has three states. Off is the default, and also what you get if the key is missing, holds something unknown or the read fails. Admin stores full traces only for his own account. All stores them for everyone, and he almost never uses it. A Boolean would leave two bad options, logging off or logging on for everybody mid-incident. The middle state lets him reproduce a user's wrong-but-not-broken output on his own account without reading anyone else's writing.

The details are the good part. The flag is read on every request, because a flag read at startup is just a deploy with extra steps. KV is built for hot reads and his requests wait seconds on a language model anyway, so the read is noise; the cost is eventual consistency, with changes taking up to a minute or so to reach other locations. A read failure logs one line and means off: losing a diagnostic is fine, losing the request is not. Traces expire after 24 hours, so a forgotten switch costs a day. And cheap operational lines (which provider answered, token counts, retries) carry no user content and are always on. If your flag is hiding your operational logs, it's on the wrong door.

## Four attempts, then a different company on a different cloud

The writer is Claude Sonnet. Each call gets four attempts with waits of one, three and eight seconds plus jitter, because rate limits, timeouts and overloads are often transient. A definite 400 is never retried, since that's his bug. After four failures the request is translated and sent to Qwen on Nebius: a different model and company on another cloud, because a fallback in another region of the same provider only covers a data centre problem. He picked Qwen by sending the same captured prompts to five candidates, and is candid about how it's worse: it parrots example phrases, sharpens loose numbers and writes soft endings.

Handoffs log the provider, model, tokens and reason, send at most one email an hour, and tag the response for the cost report. A nightly 40-token ping exercises the exact failover path, which proves the door is open but not that anything works on the other side.

## The forced outage, and what it found

Faking the outage was its own design problem. A bad API key returns 401, which is on the never-retry list, so the failover would never fire. Editing the code would mean testing a system that doesn't exist. So he added a second KV key, off by default, that makes every Anthropic attempt behave as an overload without sending the request. Everything after that is real, and the log says FORCED so a future reader can tell a caused outage from a suffered one.

The run took 78 seconds end to end. The logs showed why: the probe, the writer, a correction pass and a director each made their own model call, and each climbed the full four-attempt ladder before handing off. The fix is that one failover should count for the whole script, which he estimates brings it closer to 40 seconds. The throttle held (one email, three suppressed), and a downstream punctuation check caught Qwen breaking a no-em-dash rule that Sonnet follows. On Qwen the whole script cost under half a cent against six cents on Sonnet.

## Who should watch

Anyone running an LLM feature with a single provider, and every solo or small-team engineer who thinks feature flags are a platform-team luxury. It's funny, specific and ends with five rules worth stealing, starting with letting a failed flag read mean off. His own verdict: none of this makes the system reliable, it makes it legible.

## Related Conf42 talks

- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty of AWS and Karthik Akula at Conf42 AI Agents 2026.
- [The Multi‑Workload Challenge: Predictable Failover Across the Stack](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads) by Akshay Pratinav of Intuit at Conf42 DevOps 2026.

[Watch Fuad Laguda's talk](https://www.conf42.com/Feature_Flags_2026_Fuad_Laguda_flag_diagnostics_runtime) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/eHhQaCSaqqY).

## Watch the talk

[One flag, no deploy: switching diagnostics and providers at runtime in a one-person production app](https://www.conf42.com/Feature_Flags_2026_Fuad_Laguda_flag_diagnostics_runtime) at Conf42 Feature Flags 2026.
