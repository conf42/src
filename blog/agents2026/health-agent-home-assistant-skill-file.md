# A health agent that acts, built on Home Assistant and a skill file

Conf42 Blog, 2026-09-08, updated 2026-11-09. https://www.conf42.com/blog/agents2026/health-agent-home-assistant-skill-file

In short: Nick Rezaee of Harvard at Conf42 AI Agents 2026 wires wearable, phone and smart home data through Home Assistant so an AI skill can send personal nudges.

Uploading your Fitbit export to a chatbot and asking for insights is old news; getting an agent to notice a pattern and nudge you at the right moment is the open problem. At Conf42 AI Agents 2026, Nick Rezaee, technical research staff at a Harvard lab and a computational biology master's student at Harvard, showed a home setup that does the second part, and the surprising answer to the hardest piece is not a swarm of agents but Home Assistant.

It is a short, introductory talk with a clear architecture you can rebuild on a spare Linux box.

## Most health tech stops at the dashboard

The abstract states the problem well: most personal health technology collects data, computes a few metrics and tells you what already happened. Nick's goal is the next step, an agent that reads your data and your goal (say, walking more) and sends an intervention personalised to your patterns, so your notification differs from someone else's.

That needs something always on. Your laptop sleeps, so he puts a Linux server at home that syncs data, runs the AI on a schedule, sends phone notifications and keeps the history of what it sent for later improvement.

## The hard part is plumbing, and Home Assistant already did it

Once you add more context than the wearable (phone data, then smart home data), you can look for associations: less activity when you're on the phone, a higher heart rate with music. But every device has its own API and data format. Nick tried the obvious move first, top models running as a swarm of agents to do the integration, and found it needed a lot of steering and context, still tripped over data formats, and kept warning him that personal data might not be safe to handle.

His fix is Home Assistant, the popular open source home automation project. It pulls all those sources into a unified SQL database, sends phone notifications, runs automations, installs on Linux or Windows and is configured in the browser, so you don't need to be technical to set it up. It's a nice reminder that the agent doesn't have to do the boring integration work if a mature project already does it.

## The skill file is the product

With data in one place, the agent is a daily loop driven by a skill file, and Nick stresses that the details in that file matter. It decides which data streams to read (reading everything costs time and tokens, so you can prioritise), how messages are designed, and how to judge whether past notifications worked so the next ones improve. The flow becomes: personal data, Home Assistant, the daily skill, an intervention decision, a phone notification.

He runs this at home himself and reports that it works relatively well. Because Home Assistant also reaches speakers and computers, interventions don't have to be phone pings, and changing the goal (sleep, meditation, diet, other habits) is a matter of editing text in the skill file rather than writing software.

## What the abstract adds

The abstract goes further than the talk has time for: memory of what the agent has seen and tried, keeping analysis separate from action, limiting what the agent is allowed to do, evaluating whether interventions help, and the real risk of an annoying notification generator that thinks every pattern means something. Its example question (does staying on the computer late lead to worse sleep, and does a wind-down reminder change that?) is the right shape for a first experiment. Nick is explicit that the goal is not an AI doctor.

## Who should watch

Builders interested in agents that act on real-world feedback, quantified-self tinkerers, and anyone who already runs Home Assistant and wants to add an AI layer. If you are looking for clinical validation or an evaluation framework, this is not that talk; it's a working pattern and a starting point.

## Related Conf42 talks

- [DevOps Pipelines for Clinical AI: Deploying Real-Time Sepsis Detection at Scale](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) by Swapna Chimanchodkar at Conf42 DevOps 2026.
- [When Bad Data Reaches the Model: Engineering Data Quality Into MLOps at Healthcare Scale](https://www.conf42.com/MLOps_2026_Saiteja_Jonnalagadda_healthcare_quality_data) by Saiteja Jonnalagadda at Conf42 MLOps 2026.
- [Building Real-Time AI Decision Systems with Large Language Models](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mohanraj_Varatharaj_realtime_decisions_llms) by Mohanraj Varatharaj at Conf42 Large Language Models 2026.

[Watch Nick Rezaee's talk](https://www.conf42.com/AI_Agents_2026_Nick_Rezaee_health_wearables_intervene) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/tyLJAIzIH5c).

## Watch the talk

[From Health Data to Action: Building AI Agents That Observe, Reason, and Intervene](https://www.conf42.com/AI_Agents_2026_Nick_Rezaee_health_wearables_intervene) at Conf42 AI Agents 2026.
