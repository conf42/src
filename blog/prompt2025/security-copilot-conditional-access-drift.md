# Security Copilot finds the users your Conditional Access forgot

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/security-copilot-conditional-access-drift

In short: Cynthia Akiotu at Conf42 Prompt Engineering 2025 demos Microsoft Security Copilot fixing Conditional Access drift and summarising DLP alerts with prompts.

The most dangerous gap in a Microsoft tenant is often a policy nobody remembers writing, or a user nobody added to it. At Conf42 Prompt Engineering 2025, Cynthia Akiotu, a cybersecurity architect who works on identity and access management and data security, showed how Microsoft Security Copilot turns plain-language prompts into fixes for exactly that kind of quiet drift, with two live demos in Entra and Purview.

It's a Microsoft-stack talk, and an honest one: the product on screen is Security Copilot, and the case is that defenders should use AI at least as fluently as attackers already do.

## The pressure cooker

Cynthia opens with the defender's problem as she sees it. Attackers use AI to write better phishing emails and probe faster; analysts drown in alerts, false positives and real ones alike; and employees paste sensitive data into AI tools, which keeps executives up at night. Her framing is that defenders don't lose for lack of skill so much as lack of context and speed. Nobody reads every alert, and nobody eyeballs every policy.

Her answer is what she calls augmentation rather than automation: the analyst stays in charge, but asks questions in natural language (who are the riskiest users in this tenant?) instead of hunting through consoles.

## Drift is the silent hole

The sharpest part of the talk is about Conditional Access drift. In a large organisation, people join, change roles and leave, picking up admin rights on the way. New applications get deployed without Conditional Access coverage. Policies pile up: duplicates, obsolete ones, conflicting ones. Each of these is a door an attacker can walk through, and she points out they're hard for the human eye to spot.

The demo shows the Conditional Access Optimization agent in a Microsoft Entra tenant. It scans for users not covered by policies such as MFA, applications outside policy coverage, and policies that could be merged. The concrete moment: a suggestion that two users were missing from an existing policy requiring MFA for a financial application. One click applies it, with an explanation of what the policy does. That's the whole pitch in miniature: the agent spots the gap, the analyst approves the fix.

## DLP alerts you can actually read

The second demo moves to Microsoft Purview and data loss prevention. Cynthia asks Copilot for insight into existing DLP policies by location (endpoint devices in her example), then opens an alert about a sensitive document being downloaded to a device and asks for a summary of the user's activity.

What comes back reads like an insider-risk timeline: the same user emailed attachments outside the organisation, uploaded sensitive files to cloud storage, collected an unusual volume of sensitive files, then deleted files. She reads it, plausibly, as a disgruntled employee on the way out. The point is the turnaround: a sequence that would take an analyst a while to reconstruct arrives as a paragraph.

## The prompt is now a perimeter

She closes with a warning that keeps the talk from being a pure product tour. If prompts can change policies, prompts are an attack surface. Her rules: audit every prompt and action analysts run, treat Security Copilot as a privileged access surface, and cover it with the same policies as any other admin tool. Speed without visibility just moves the risk.

## Who should watch

Security analysts and identity admins in Microsoft 365 shops who want to see what Security Copilot looks like on real tenant screens, and security leads weighing whether an AI assistant earns its privileged access. If you're on another stack, the drift checklist (users, apps, redundant policies) still travels well; the clicks won't.

## Related Conf42 talks

- [Exploring Copilot Capabilities](https://www.conf42.com/Prompt_Engineering_2024_Peter_De_Tender_copilot_capabilities_microsoft) by Peter De Tender at Conf42 Prompt Engineering 2024, for the wider Microsoft Copilot family.
- [From Reactive to Predictive: AI-Powered Cybersecurity in the Age of Advanced Threats](https://www.conf42.com/Machine_Learning_2025_Dinesh_Rajasekharan_cybersecurity_threats_predictive) by Dinesh Rajasekharan at Conf42 Machine Learning 2025.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq at Conf42 AI Agents 2026, on agents as privileged identities, from the other side.

[Watch Cynthia Akiotu's talk](https://www.conf42.com/Prompt_Engineering_2025_Cynthia_Akiotu_security_defense_cyber) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/GRMUiGIMVrM).

## Watch the talk

[From Prompts to Protection: How Security Copilot Reinvents Cyber Defense](https://www.conf42.com/Prompt_Engineering_2025_Cynthia_Akiotu_security_defense_cyber) at Conf42 Prompt Engineering 2025.
