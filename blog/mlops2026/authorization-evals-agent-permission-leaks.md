# Test your agents for permission leaks like any other regression

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/authorization-evals-agent-permission-leaks

In short: Ajay Munjuluru (JPMorgan Chase) at Conf42 MLOps 2026 on authorization evals: personas, canaries and join tests that can block an agent release.

An agent can write a perfect summary of a client relationship for someone who is not supposed to know half of what is in it, and every eval metric will come back green. At Conf42 MLOps 2026, Ajay Munjuluru, senior lead software engineer at JPMorgan Chase, shows how to turn "who is asking" into a test suite that runs in the delivery pipeline and can stop a release. He is clear that every example on his slides is made up for the talk and the opinions are his own.

## The agent is one front door to many rule sets

Users used to visit each system separately. The CRM had profiles, permission sets, field-level security and sharing rules. The warehouse had its own policies. Documents had ACLs. Now people ask one question in one place and the agent fetches from everywhere, so it has to combine all those rule sets per request and then describe the result in plain language. Ajay's uncomfortable observation is that a better model makes this harder, because it gets better at putting two and two together.

He groups leaks into five places: the response (the only one most suites check), summaries and memory, tool calls, context and retrieval, and joins. A call note written back to a record that more people can see than its sources is restricted data moved into a shared place. A tool that pulls 50 fields when the task needed five leaves the restricted ones sitting in context. Retrieval is the one he would worry about most: if chunks the user is not entitled to come back, the facts are in the prompt before the model writes a word.

## Personas need real logins, canaries need odd numbers

The property he tests: for each persona and each task, everything the agent produces stays inside what that persona may see. That covers responses, summaries, tool arguments and handoffs to other agents.

His banking CRM example has six personas, among them a coverage banker, a deal team member wall-crossed on exactly one deal, a public-side analyst, and a platform admin with lots of configuration access and no business reason to see client financials. The condition that makes them useful is that they are real test users with real permission sets, roles and sharing. "If the persona only exists in the prompt, you're testing whether the model follows instructions, which is a different question from whether your access model holds," Ajay Munjuluru said at Conf42 MLOps 2026.

To detect a leak he plants canaries: fake restricted facts that are unique and easy to spot, such as a deal codename or an exposure number with odd precision. They go on records, in free-text notes, inside PDF attachments and in email threads, because the leak usually comes from the note someone pasted, not the field you were watching. The expected results are not written by hand. He logs in as each test user, queries the source system with that user's token and saves what comes back. When someone changes a sharing rule next quarter, the expected sets change with it.

Three kinds of checks sit on top. Exact canary matches in responses, summaries or tool arguments block the release. A judge model answers one narrow question about paraphrased hints, and those hits go to a human reviewer. Behaviour checks ask what the agent did: a service credential used in place of the user's own, fields requested outside the expected set, restricted text written to a shared record. In multi-turn conversations the checks run after every turn.

## The hardest leak is built from allowed facts

Ajay calls it permission aggregation disclosure. His definition of the join problem is short: "Two facts the user is allowed to see that add up to the one they aren't." A banker can see a dashboard count of one live sell-side mandate in a sector and region, and an activity feed showing a colleague met one company's CFO three times this month. Ask the agent what is going on with that company and a helpful one connects the dots into material non-public information. No source system did anything wrong and no canary appears in the sentence.

His test is to build scenarios where joining allowed results narrows to a single record, then check the agent does not take the last step: no naming, no ranking of likelihood, no speculation. He would start with three of these.

## A pass rate is the wrong gate

The suite runs on more than code changes: model upgrades, prompt edits, new tools or MCP servers (in his experience the most common way a leak arrives), permission changes in the source system and rebuilt retrieval indexes. Tool-level tests run on every pull request, the persona suite nightly, join scenarios before a release, and a few canaries stay in production as tripwires.

The gate is binary. Any exact canary match or wrong credential blocks promotion. "A 99% pass rate here means, one answer in 100 leaked something," he said. When a test fails, the harness walks the trace backwards from the leaked sentence to the context, the tool call, the credential and the rule that should have stopped it, so the right team gets the ticket.

## Who should watch

Teams shipping agents over CRM, warehouse or document data in regulated businesses, and anyone who owns an eval suite that has never been run as a second user. No new platform is required: test data, test users, a trace and agreement that authorization is part of release readiness. If your agent only reads public data, you can skip this one.

## Related Conf42 talks

- [Who Is Calling Your Model? Identity and Authorization for AI Agents and ML Pipelines](https://www.conf42.com/MLOps_2026_Bhavik_Thakkar_identity_authorization_agents) by Bhavik Thakkar at Conf42 MLOps 2026.
- [Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) by Sajal Garg at Conf42 MLOps 2026.
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar at Conf42 LLMs 2026.

[Watch Ajay Munjuluru's talk](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) at Conf42 MLOps 2026.
