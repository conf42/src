# A timeout is not a failed action: chaos-testing agent tool calls

Conf42 Blog, 2026-11-25. https://www.conf42.com/blog/chaos2026/agent-timeout-is-not-a-failed-action

In short: Arjun Garg (Intuit) at Conf42 Chaos Engineering 2026 on injecting a lost reply after an agent's tool call commits, and how retries stay safe.

An agent places an order, the service creates it, and the reply never arrives. The agent sees a timeout, retries, and now there are two orders. At Conf42 Chaos Engineering 2026, Arjun Garg of Intuit shows how to make that failure observable with a small public MCP reproduction, then turns it into a chaos test plan for any agent tool that mutates something.

He is explicit that the experiment uses synthetic effects, that it is not evidence of an incident at an employer or a vendor, and that he speaks in a personal capacity. What he offers is a familiar distributed-systems boundary, replayed with an MCP client and server.

## Why can't a better prompt fix a lost reply?

The service knows it appended a record. The caller knows a response didn't arrive before its deadline. "Neither observation cancels the other," Arjun says, and a handler that turns every timeout into a new business operation is making a consequential policy choice with incomplete evidence.

That is why longer timeouts, better prompts or telling the model to be careful don't close the gap. They may change how often it happens. They don't establish what happened during one particular ambiguous attempt. The question he wants you to keep in mind is what new evidence would make the next mutation justified.

## What does the reproduction show?

The setup uses a real SDK client and server over in-memory streams. A relay watches the first tool response and drops it after the handler has returned, so the effect is already recorded when the reply disappears. The client's read timeout then raises an MCP error, and the script does exactly one application-level retry. The SDK doesn't retry on its own. No sleeps coordinate the fault.

Two runs are compared. The baseline ends with two effects. The positive control carries a logical operation ID and returns the earlier effect identifier on the repeat. The fault stays identical and only duplicate suppression changes, so the property being tested is isolated. Arjun is careful about the limits: it is an in-memory, sequential illustration, and it does not show durability across restarts, concurrent exclusion or safe integration with a separate downstream service.

## Four identifiers, four different meanings

A big part of the talk is vocabulary. An RPC identifier correlates messages. An attempt identifier explains a dispatch. A logical operation identifier says "this is the same intent". An effect reference points at what actually happened. They can all sit in one trace and still mean different things.

This is why hashing the whole argument object misleads, since attempt metadata changes between tries. Even a hash of only the business arguments can't tell retrying one order from deliberately buying the same items twice. The caller or a trusted workflow has to make that call, and the receiver needs a scope and a contract for honouring it.

## Where reserving a key goes wrong

If a gateway reserves a key, calls an external service, then stores the receipt, a crash after the external commit but before the receipt write leaves an intent record with no completion evidence. Reserve first and you can stop a second worker but leave the operation unresolved. Write only afterwards and a crash leaves no local record even though the effect happened. A local transaction can't atomically include an arbitrary remote API, so recovery needs the provider's cooperation: idempotency, lookup by operation reference, or a documented reconciliation procedure.

The fault-injection matrix changes the fault location in each row, and so changes what you know afterwards: before dispatch, after reservation, after remote commit, after receipt persistence, after retention expiry. A test harness should record which barrier it reached before injecting the fault, and the assertion isn't always a successful retry. Sometimes the right result is a bounded unresolved state with an owner and a reconciliation route.

Arjun also lists four assertion types that aren't interchangeable: effect count (catches duplicates), result integrity, progress (is anyone able to resolve unfinished work), and freshness (a stale worker waking up after a takeover). Refunds make the point: a system can block the second refund and still leave support unable to tell whether the first one happened.

## The recovery decision tree

His rule of thumb for a mutating agent tool: look for evidence of completion first, and return the original result if you can. If you have reliable proof of non-execution and stale workers are fenced out, a new dispatch may be appropriate. If the provider supports idempotent retry with the same key, use that contract even when the first outcome is ambiguous. Otherwise preserve the ambiguity and reconcile. A human clicking approve doesn't prove the first effect never happened.

Cancellation and backoff don't help here. MCP cancellation lets the recipient ignore the notification if work already completed, so it isn't a rollback, and waiting longer doesn't tell you whether the first order exists. Keep an oracle independent of the system under test, include the deliberately unprotected baseline to prove the oracle can see duplicates, and log the operation key, effect evidence and final caller status together.

The line he closes on: "The timeout tells us that the caller lacks a response. It does not tell us that the service lacks an order."

## Who should watch

Anyone giving an agent tools that charge, refund, create, send or delete. It is a careful, qualified talk with slides about boundaries rather than a product demo, and it will be most useful to people who already own retry logic. If you only need the one-sentence takeaway, it is above; the matrix and the decision tree are the reason to watch.

Related Conf42 talks: [Surviving a 300% Flash Crowd: State-Safe Autoscaling With Zero Split-Brain Events](https://www.conf42.com/Chaos_Engineering_2026_Amit_Singh_Negi_autoscaling_crowd_brain) by Amit Singh Negi of T-Mobile, [Your Backup Is Not Your Recovery](https://www.conf42.com/Chaos_Engineering_2026_Praveen_Kumar_Gopalakrishnan_backup_api_recovery) by Praveen Kumar Gopalakrishnan of Salesforce, and [Your Agent Failed Mid-Run. Logs Won't Replay It.](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) by Reza Amini of Flashback at MLOps 2026.

[Watch Arjun Garg's talk](https://www.conf42.com/Chaos_Engineering_2026_Arjun_Garg_timeout_agent_tool) from [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026).

[Watch the talk on YouTube](https://youtu.be/xfzPswIwSsA).

## Watch the talk

[A Timeout Is Not a Failed Action: Chaos Testing AI Agent Tool Calls](https://www.conf42.com/Chaos_Engineering_2026_Arjun_Garg_timeout_agent_tool) at Conf42 Chaos Engineering 2026.
