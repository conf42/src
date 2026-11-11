# An incident drill where your teammates are language models

Conf42 Blog, 2023-10-19. https://www.conf42.com/blog/im2023/incident-drills-with-generative-ai-teammates

In short: Mahdi Jelodari (Uptime Labs) at Conf42 Incident Management 2023 on training incident managers in a simulated outage run by generative AI characters.

Most incident training stops at the runbook, and the hard part of a real outage is the people: the CEO asking for an update, the support manager forwarding angry customers, the developer who answers in five minutes instead of five seconds. At Conf42 Incident Management 2023, Mahdi Jelodari, ML / IoT Specialist at Uptime Labs, showed a drill environment where those people are generative AI characters, and an incident manager has to size up, triage and fix a broken shop while they talk over each other in Slack.

It is a short, demo-heavy vendor talk about the Uptime Labs product, and it says so. The interesting part is the framing: incident skills are trainable the way muscle memory is, if you have somewhere safe to break things.

## What is missing from the textbook definition?

Mahdi opens by asking ChatGPT to define incident management. The short answer is correct, he says, but it leaves out everything about people: coordination under time pressure, communication, managing stressed colleagues, time management and understanding incident mechanics. That gap is the product's whole pitch.

"Unlike many other solutions out there, our focus at the moment is people and processes," Mahdi Jelodari said at Conf42 Incident Management 2023. Monitoring tools tell you what is broken; they do not teach you how to run a bridge call while three people ask you different questions.

## What does the simulated company look like?

The drill runs against a full e-commerce company: an online boutique where you can actually place orders, a microservice stack on Kubernetes, Grafana dashboards with orders per minute, logs and change records, and a company hierarchy from the CEO down to development, platform and escalation teams. Drills are configurable, and customers can have them tailored to the skills they want to practise.

The characters are the point. Each has a personality and a role, they respond at human speed, and some are deliberately difficult. "Of course, they can be stubborn," Mahdi said, which anyone who has paged a database owner at 2am will recognise as realism, not a bug.

Communication is text-only for now, in Slack, with audio and video on the roadmap. Each drill opens two channels automatically: an incident bridge and a business communication channel.

## How does the drill play out?

The demo drill is fully driven by generative AI. The team introduces itself (the CEO sets the tone), then the customer services manager reports that customers can't place orders. The dashboards confirm it: user activity drops, messages pile up, and the first job is to declare who the incident manager is so the team knows who has command.

Mahdi then works with a developer character, an AI agent with access to logs and the history of previous incidents. He asks about recent changes and whether the current outage resembles anything from the last week. The agent lines it up against past database capacity, ISP and front-end cache incidents, shares the matching logs, and points to requests per minute climbing unexpectedly.

That is the size-up stage of the incident mechanics Mahdi uses: size-up, triage, action, review. With enough information gathered, he decides to revert a front-end change, tells the agent to do it, and watches Grafana until orders start flowing again. Then he reports back to the business channel. The whole loop takes about five minutes on screen.

Along the way the platform hands out hints and rewards, and everything lands in a performance report at the end, which is where the training value is meant to show up: what you did well, what you skipped, where you hesitated.

## Where does generative AI help beyond the characters?

Mahdi lists drill design (personalised drills), automating control of the platform, the pros-and-cons performance reports, and mining insights from drill data. The skills he wants people to practise one by one: scoping the problem, coordinating under time pressure, structured troubleshooting, forming hypotheses and step-by-step reasoning.

## Who should watch

Incident managers and SRE leads who run game days and want to train the human side, not only the failover. It is about ten minutes, mostly demo; if you want data on whether simulated drills improve real incident outcomes, the talk doesn't cover it.

For the other side of the same idea, pair it with [Austin King on games that improve incident response](https://www.conf42.com/Site_Reliability_Engineering_2021_Austin_King_games_improve_incident_response) from SRE 2021, [Mandi Walls on game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering) from Incident Management 2022, and [Einat Mahat on effective on-call practices](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices) from the same event.

[Watch Mahdi Jelodari's talk](https://www.conf42.com/Incident_Management_2023_Mahdi_Jelodari_it_training_generative_ai) from [Conf42 Incident Management 2023](https://www.conf42.com/im2023).

## From Uptime Labs

In the talk, Uptime Labs is a London-based startup building an immersive, gamified environment for incident response practice: a simulated company with AI-powered characters, realistic dashboards and Slack-based drills, plus performance reports after each session.

- Uptime Labs: [uptimelabs.io](https://uptimelabs.io/)

[Watch the talk on YouTube](https://youtu.be/RQejDeQdj60).

## Watch the talk

[IT incident management training and assessment using generative AI](https://www.conf42.com/Incident_Management_2023_Mahdi_Jelodari_it_training_generative_ai) at Conf42 Incident Management 2023.
