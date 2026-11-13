# Two teams owning one service means nobody owns it

Conf42 Blog, 2021-02-25. https://www.conf42.com/blog/ce2021/no-unowned-services-ever

In short: Joey Parsons (effx.com) at Conf42 Chaos Engineering 2021 on service ownership rules to settle before any game day - one owner, real contacts, reorged services

You cannot run a game day on a shared database if nobody can tell you who owns the services that depend on it. That is the starting point of [Joey Parsons](https://www.conf42.com/Chaos_Engineering_2021_Joey_Parsons_service_ownership_organizational_chaos), CEO of effx and previously in charge of site reliability at Airbnb, at Conf42 Chaos Engineering 2021: before failure injection, fix service ownership, or the organisation supplies the chaos for free.

The talk is short and opinionated, a list of rules from his career and from effx customers, whose platform helps engineering teams operate microservices.

## What does service ownership actually cover?

Parsons rejects the "you code it, you own it" shorthand as too thin. His definition: a team is fully autonomous and responsible for delivering its service, component or piece of functionality, and the freedom comes with the responsibility. That responsibility spans more than on-call:

- incident response, plus the observability and monitoring that make it possible;
- performance and efficiency tuning;
- features and bugs, meaning who the Jira tickets land with;
- capacity planning and cost, which in a low-margin business can show up on the P&L;
- failure injection and chaos: who runs the game days and makes sure the service is fault tolerant.

## What does it look like when ownership is missing?

His catalogue of organisational chaos will feel familiar. Unowned services, the worst case. No easy way to reach an owner: which Slack channel, which email, how to page them. Poor documentation and runbooks. Bus factors of one, usually paired with a hero complex. Broken on-call rotations; he recalls being paged by a startup he had left years earlier because something esoteric broke.

## The recipes

**No unowned services, ever.** The critical service that teams have played hot potato with for years is the one nobody can be found for during a security issue. Every service needs an owner, recorded somewhere easy to read and kept current.

**One service, one team.** He flags it as possibly controversial. Joey Parsons said at Conf42 Chaos Engineering 2021: "When two teams own it, nobody does." Two owners add a decision point during an incident that should not exist.

**Never toss it over the fence, even inside a team.** Embedded SREs are fine, but if they become the only ones doing the hard parts, that is the pre-DevOps split again. Every engineer on the team should be on the rotation, and the SREs should raise everyone's ability to handle it.

**Track operational readiness constantly.** Runbooks, API specs, docs and dashboards, checked continuously rather than once on a launch checklist. Measure what matters to your organisation: in-depth runbooks for one company, a daily security scan for a regulated one.

**Make contact details obvious.** His example: a team called User Growth whose Slack channel is named after scaling and whose email alias says growth. Nobody will find them. Keep names simple and consistent.

**Tie on-call rotations to the user directory** (Google, LDAP, Active Directory), or you end up paging people who left the team.

**Reorg the services too.** Reorgs tend to be hasty, and "the people get reorgs, but the microservices don't." Every reorg should end with every service reassigned, so nobody shrugs and says they used to own that.

## Who should watch

Engineering managers mid-reorg, platform teams building a service catalogue, and anyone about to schedule a first game day. It is a quick watch with no tooling demo.

Related Conf42 talks:

- Jay Hankins on [service ownership in the enterprise](https://www.conf42.com/Chaos_Engineering_2024_Jay_Hankins_service_ownership_enterprise), Conf42 Chaos Engineering 2024.
- Daniel Spoonhower on [service ownership and distributed tracing](https://www.conf42.com/Site_Reliability_Engineering_2020_Daniel_Spoons_Spoonhower_service_ownership_distributed_tracing), Conf42 SRE 2020.
- Cristina Buenahora Bustamante on [evangelising a culture of ownership](https://www.conf42.com/Site_Reliability_Engineering_2021_Cristina_Buenahora_Bustamante_evangelizing_culture_ownership), Conf42 SRE 2021.

## From effx

effx builds a platform to help engineering teams operate microservices, including keeping track of who owns what.

- [effx](https://www.effx.com)

[Watch the talk on YouTube](https://youtu.be/iUYdO2ZNgms).

## Watch the talk

[Organizational Chaos and recipes for Service Ownership](https://www.conf42.com/Chaos_Engineering_2021_Joey_Parsons_service_ownership_organizational_chaos) at Conf42 Chaos Engineering 2021.
