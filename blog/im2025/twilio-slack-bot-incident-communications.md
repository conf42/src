# Twilio's Slack bot that writes the incident update for you

Conf42 Blog, 2025-09-08, updated 2026-11-09. https://www.conf42.com/blog/im2025/twilio-slack-bot-incident-communications

In short: Gandhi Mathi Nathan Kumar (Twilio) at Conf42 Incident Management 2025 demos a Windmill + OpenAI Slack bot for customer summaries and status page drafts.

Most AI-for-incidents talks are about detection. At Conf42 Incident Management 2025, Gandhi Mathi Nathan Kumar, Principal Incident Commander for Platform Engineering at Twilio, spent his slot on the part customers actually experience: communication. He demoed a Slack bot his team built in a Twilio hackathon that turns the chaos of an incident channel into customer-ready summaries and status page drafts in well under a minute.

It is refreshing to see a talk pick the unglamorous problem. As he points out, there is plenty of content on resiliency and detection and very little on how incident response communication happens.

## Working the tools instead of the incident

Kumar starts by listing what a Twilio incident touches: FireHydrant to declare and run incidents, PagerDuty to alert, Zoom for the bridge, Slack for async chat (where around nine in ten incidents are run), Datadog dashboards, Atlassian Statuspage for customers, Google Docs for retrospectives, Confluence holding 15-plus years of product knowledge, and Slack canvases for action items. You can trim that list, he says, but you can't collapse it into one tool.

The trouble starts, in his words, when you end up "working the tools instead of working the incident". An incident commander's job is to keep people on mitigation, ask the right questions and push back when the discussion drifts. Every tab switch to gather data or draft an update takes attention from that.

He pairs this with the customer's view of the same incident: something is broken, the status page is still green, nobody has said anything, so they file tickets, call account managers and assume the worst. Each poorly communicated incident spends some trust, and trust is slow to earn back.

## Three Slack commands

The bot is a Slack app built on Windmill that calls OpenAI and is wired into the incident tool, Slack and Zoom chat and voice, and the Confluence and wiki knowledge base. Each command carries a persona describing who the answer is for:

- **A technical customer summary** for an incident number, phrased the way you would brief a technical customer.
- **A status page post**, generated as the usual title plus body.
- **An open question command** for anything else, including the questions people hesitate to ask on the triage bridge because interrupting the engineers who are fixing things costs time.

In the demo, he asks what Twilio's core products are and gets an answer drawn from the internal help centre; asks what a customer's 503 errors on all services might mean and gets causes plus pointers to internal troubleshooting articles; then queries a test incident for a technical summary and its start time. During a live incident the bridge audio is transcribed and fed in, so the answers keep up with what is being said. Responses came back in around 20 to 30 seconds in the demo.

## The next step is the risky one

The team is prototyping automatic posting to the status page, which needs the model to reliably separate internal detail from what customers should see. Kumar is clear that this is still being tested. He also mentions generating retrospective drafts from the same context. Both are the right order of operations: let humans review drafts until the filter has earned trust.

## Who should watch

Incident commanders, support leads and anyone who has typed "any update?" into a busy incident channel. It is a practitioner's talk with a real demo and an honest scope: a hackathon tool, a handful of commands and a clear problem. If you run Slack-first incidents, you could prototype the same thing with a workflow engine and an LLM API in a week.

## Related Conf42 talks

- [Building Slack Applications with Bolt.js](https://www.conf42.com/JavaScript_2022_Alba_Rivas_slack_applications_boltjs) by Alba Rivas covers the plumbing for a bot like this.
- [Postmortems, Continuous Learning and Enabling Blameless Culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) by Julie Gunderson picks up where the incident channel ends.
- [Creating On-Call Heroes: Strategies for Effective On-Call Practices](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices) by Einat Mahat looks after the humans on the bridge.

[Watch Gandhi Mathi Nathan Kumar's talk](https://www.conf42.com/Incident_Management_2025_Gandhi_Mathi_Nathan_Kumar_ai_automation_resilience)

[Watch the talk on YouTube](https://youtu.be/nzJHeYA24DM).

## Watch the talk

[AI for Incident Management](https://www.conf42.com/Incident_Management_2025_Gandhi_Mathi_Nathan_Kumar_ai_automation_resilience) at Conf42 Incident Management 2025.
