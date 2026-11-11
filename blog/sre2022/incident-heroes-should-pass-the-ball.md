# Your incident hero is hiding the need for incident management

Conf42 Blog, 2022-06-09. https://www.conf42.com/blog/sre2022/incident-heroes-should-pass-the-ball

In short: Malcolm Preston (FireHydrant) at Conf42 Site Reliability Engineering 2022 on why the 2am incident hero should pass the ball, and three steps to start

Every company has one: the engineer who answers the 2am page first, finds the problem, wakes the VP, drafts the customer message and is back at their normal job by 9am. At Conf42 Site Reliability Engineering 2022, Malcolm Preston, Staff Software Engineer at [FireHydrant](https://firehydrant.io), compared that person to Shaquille O'Neal and argued that the team keeps winning games while the organisation loses the season. His fix comes in three small steps, none of which needs a budget.

It's a culture talk with no product demo until a closing slide, and the basketball metaphor carries further than you'd expect.

## Why is the hero a problem if incidents get resolved?

Malcolm frames it in three layers: individuals bring talent, teams try to win this season, organisations try to win year after year. The hero optimises the middle layer. Because Shaq makes dunking look easy, nobody else feels the pain, so the company doesn't see a problem, so there's no system, so the hero keeps doing it. A self-fulfilling prophecy, in his words.

He tells it from experience. A VP once said that seeing Malcolm's name in the incident Slack channel was a relief, a reputation that started on his first day, when he fixed an internal system during new hire orientation. At another job he became the go-to person for a self-hosted NoSQL database that had spread into almost every microservice. When he pushed for a database monitoring tool so other teams could self-serve, he met scepticism: nobody else thought there was a problem, because every time there was one, he solved it.

## Remote work took away the water cooler

The part that ages well is his point about where the hero's knowledge came from. Malcolm estimates that most of the service dependency map in his head at past companies came from water cooler talk: someone asking advice about a new component, a casual mention of an upcoming change. With people rarely in the same room after Covid, that channel thinned out, which means what incident responders know has to be written down rather than absorbed. And heroes get tired, get hurt and burn out.

## Step one: think out loud during the incident

Don't block out a day to write a runbook. Next time you respond, open a thread in the incident channel and narrate. What's the first thing I do when paged? Where do I check service status? How do I find who owns the broken service? How do I revert the last deploy? What's the customer and internal impact? What would I fix going forward? These are the answers you give yourself silently; written down, they become the raw material for a runbook or a wiki page.

## Step two: play point guard, not centre

Take the incident commander role and resist the urge to dunk during non-critical incidents. Hang back, give assists, help teammates find information rather than handing it over. Then skip being on call for a rotation or two, for your own health and so others step up, and spend the time turning your notes into documentation. Malcolm's sharpest line: nothing flags a weakness up the chain of command like showing what happens when you're not there.

## Step three: question the status quo

His checklist for the two big Os, on-call and observability: do you alert on every down instance or only what affects customers? Are you using SLOs, and if not, what's in the way? With noisy alerts, is a week on call even reasonable? Can teammates find the data they need to triage? How are incidents declared, do you run retrospectives, and do they influence the product roadmap? And who picked your tools, when, and do they fit how the team works?

"If you're playing the hero role at your organization, you might be unintentionally masking the need for better incident management practices," Malcolm Preston said at Conf42 Site Reliability Engineering 2022.

## Who should watch

The person everyone pings during incidents, and the manager who relies on them. It's short, and step one costs nothing but typing.

Related Conf42 talks: Einat Mahat on [on-call heroes and effective practices](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices), Sylvain Kalache on [burnout and on-call for SREs](https://www.conf42.com/Observability_2026_Sylvain_Kalache_burnout_oncall_sre), and Lisa Karlin Curtis on [incidents that level up teams](https://www.conf42.com/Site_Reliability_Engineering_2022_Lisa_Karlin_Curtis_incidents_levelup_teams) from the same event.

[Watch Malcolm Preston's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Malcolm_Preston_We_cant_all_be_shaq_pass_the_ball_make_it_happen) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From FireHydrant

The talk closes on FireHydrant's view of incident management, covering an incident from the moment it starts through to the retrospective. FireHydrant offers service catalogs, incident response, status pages and retrospectives.

- FireHydrant: [firehydrant.io](https://firehydrant.io)
- [How FireHydrant works](https://firehydrant.com/how-it-works)
- [Watch a demo](https://firehydrant.com/demo)
- [Create a free account](https://app.firehydrant.io/registrations/new)

[Watch the talk on YouTube](https://youtu.be/FDHQJrtShM4).

## Watch the talk

[We can’t all be Shaq: why it’s time for the SRE hero to pass the ball and how to make it happen](https://www.conf42.com/Site_Reliability_Engineering_2022_Malcolm_Preston_We_cant_all_be_shaq_pass_the_ball_make_it_happen) at Conf42 Site Reliability Engineering 2022.
