# Some of the fires we fight in production we set ourselves

Conf42 Blog, 2023-03-29. https://www.conf42.com/blog/cloud2023/arsonist-firefighter-prevent-incidents

In short: Einat Mahat (Skai) at Conf42 Cloud Native 2023 on seven ways developers can prevent production incidents instead of heroically putting them out

The arsonist firefighter is a real thing: a firefighter who starts fires so he can be the one to put them out. At Conf42 Cloud Native 2023, [Einat Mahat](https://www.conf42.com/Cloud_Native_2023_Einat_Mahat_legend_arsonist_firefighter), R&D Group Lead at Skai, borrows the image for software teams. Nobody sets production on fire on purpose, she says, but after more than a decade of leading production-heavy dev teams she noticed that many of the incidents her heroes were fighting started in their own code. Her answer is seven habits that prevent fires, plus one that matters most once a fire has started anyway.

It is a short, practical talk aimed at developers, not a tooling session. Skai's stack never comes up.

## Why bother, if the team is good at firefighting?

Because firefighting for a living burns people out. She describes a former group with too many major incidents, where one engineer still gets anxious every time his phone rings. Being great at the rescue is not the goal; needing fewer rescues is.

## The seven ways to prevent the next fire

**Invest in monitoring.** She calls monitoring an art: dashboards with enough data to give visibility without drowning anyone, built so issues show up before they become incidents and so the team can find the cause fast when one does.

**Place alerts.** Problems should come to you, push not pull. Route by severity, so some alerts go to the owning team and the serious ones to whoever is on call, even in the middle of the night, and make each one carry enough information to act on. Balance matters here too, because too many false alerts make it harder to take the real ones seriously.

**Run postmortems.** Gather the data and timeline, find the root cause, create action items and follow up on them, in a culture of facts rather than finger pointing. She adds a tip for people who are not on call: read other teams' debriefs anyway, since incidents can still land on you.

**Run premortems.** Before a critical change, imagine it has already failed in production. "The technique is to imagine that a project has already failed and then identify the reasons for the failure," Einat Mahat said at Conf42 Cloud Native 2023. Then rank the risks by impact and agree mitigations before anything ships.

**Write the rollback plan, not just the rollout plan.** Teams debate whether everything needs a gradual rollout, but the rollback plan is the part that gets skipped. For critical changes she wants an exit strategy: the steps to revert to the previous version and clear criteria for when to pull the trigger.

**Keep runbooks.** Step-by-step procedures for the things that commonly break, usable by developers and operations alike, so the work is done consistently under pressure. Writing them also forces you to think through failure modes before they happen.

**Improve continuously.** Regular retrospectives, runbook reviews, incident trend analysis to spot patterns and recurring root causes, and feedback from users and stakeholders.

## What to do when the fire starts anyway

Not every fire can be prevented, so her closing section is communication. Have an incident communication plan that covers every stakeholder, from engineers to management to customers, and names who communicates what. Assign clear roles so everyone knows what is expected of them. Give regular updates, in plain language without jargon for non-technical audiences, and be transparent. Her sign-off: "Don't be an arsonist firefighter, be a true hero."

## Who should watch

Developers who are new to on-call, and team leads who want a compact checklist to hand to a team that keeps meeting the same incidents. Experienced SREs will know every item; the premortem and rollback sections are the ones most teams still skip.

Related Conf42 talks:

- Laurent Parenteau on [hacking the premortem](https://www.conf42.com/Platform_Engineering_2024_Laurent_Parenteau_hack_premortem_success), Conf42 Platform Engineering 2024.
- Ramon Medrano Llamas on [postmortem culture at Google](https://www.conf42.com/Site_Reliability_Engineering_2022_Ramon_Medrano_Llamas_postmortem_culture_google), Conf42 SRE 2022.
- Mandi Walls on [tackling alert fatigue](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue), Conf42 SRE 2025.

## From Skai

Skai is the company where Einat Mahat leads an R&D group and where the production lessons in this talk were learned.

- [Skai](https://skai.io/)

[Watch the talk on YouTube](https://youtu.be/ipwX39e6xMc).

## Watch the talk

[The Legend of the Arsonist Firefighter](https://www.conf42.com/Cloud_Native_2023_Einat_Mahat_legend_arsonist_firefighter) at Conf42 Cloud Native 2023.
