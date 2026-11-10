# PayPal moves the compliance gate onto the paved road with MCP

Conf42 Blog, 2026-10-25, updated 2026-11-09. https://www.conf42.com/platform2026/paypal-puts-compliance-gate-on-paved-road

In short: Sumeet L. Ram (PayPal) at Conf42 Platform Engineering 2026 on exposing a geo-expansion platform to agents over MCP while people keep approving the rules.

On most paved roads the compliance check sits at the very end, where it's most expensive to fail. At Conf42 Platform Engineering 2026, Sumeet L. Ram, Senior Technical Product Manager at PayPal who owns the geo-expansion platform teams use to launch in new markets, showed how to move that gate into the road itself by exposing the platform to AI agents through a Model Context Protocol server, with people still approving every rule.

His closing line is the whole talk in six words: agents find and flag, people decide.

## The platform had the answer; nobody asked

Sumeet opens with a story most platform owners will recognise. A team integrates through the platform SDK; it works. Compliance adds a new data-handling rule for some markets; the platform ships support, with release notes. The team's integration still works, so nobody looks. Weeks later an audit asks, and the scramble begins.

More than 150 product teams use his platform to launch in a new market by configuration rather than rebuilding. Yet teams build for their home market first, discover market rules late in the sprint, file a ticket and wait, each reading the docs their own way. The same five failures repeat: teams stuck on old versions, one requirement built five ways, compliance gaps found after code is written, a single missed rule holding up a launch, and real exposure in regulated flows. Regulators and payment networks change rules on their own calendars, which never match sprint plans. End-of-life notices meet the eternal promise to upgrade next quarter.

Now add agents. A team's agent working off a PRD and Figma files will figure out market rules on its own, confidently, sometimes even correctly, and ungoverned.

## Three tools any platform can offer an agent

The fix is an MCP server in front of the platform, so rules show up at design time instead of at release. Sumeet's core slide, and the one he asks you to remember, is three kinds of tools:

1. **Adopt**: how do I build on this, or move to the current version?
2. **Update**: what changed that affects my flow?
3. **Verify**: is my work still valid, checked before launch and long after?

His example is address layout. Some markets write addresses from the largest administrative unit down; the West goes street first. With the platform reachable by agents, the integration gets it right from day one and nothing surprises QA during KYC or KYB checks. He notes the pattern fits any rule-heavy platform: security, accessibility, data handling.

## When agents become your customers

Once the platform speaks MCP, other agents start asking it first. A design tool's agent can ask which layouts change by market, so designs match what production will really render, and QA stops comparing a home-market mock to a localised screen. A policy agent can watch the compliance system of record, compare it to what's live, notify the owning team and open a pull request with the fix, which a person reviews before anything ships.

Governance runs in two loops that meet in the platform's rule set. Teams read it at design time. Custodians maintain it: a recurring research loop scans standards bodies and regulators, scores how well current rules still match, and proposes updates when the score drops, and a platform custodian approves every change. That approval is what makes the audit trail credible: each answer carries the rule version, its source, its effective date and who approved it, so you can answer an auditor asking why the platform said what it said on a given day.

## Numbers, with honest caveats

Sumeet says he has seen up to a 96% reduction in upgrade time, and gives a directional range of roughly 50 to 80% less effort across finding rules, upgrading and keeping rules current, while telling you to measure your own. His five moves to copy: find your late loop, expose the platform where work starts, offer adopt/update/verify tools, make upgrades the platform's job, and keep people owning the rules. Start with the rule that changed most recently.

## Who should watch

Owners of any platform with rules attached (payments, privacy, security, accessibility) who are watching agents start to consume their APIs. It's a product-manager talk about operating model rather than MCP server code.

## Related Conf42 talks

- [Enhancing Security and Compliance with Policy as Code (PaC) in Jenkins for DevOps Pipelines](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sarathe_Krisshnan_Jutoo_Vijayaraghavan_enhancing_security_comp) by Sarathe Krisshnan Jutoo Vijayaraghavan (CGI Technologies)
- [SRE for National-Scale Regulatory Reporting: HA, DR, and Audit-Ready Design](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Bhargavaram_Potharaju_national_scale_regulatory) by Bhargavaram Potharaju (Wells Fargo)
- [From Prompt to Production Dashboard: Agentic AI with MCP Servers and Live Data](https://www.conf42.com/AI_Agents_2026_Rohit_Deshpande_Scott_Young_mcp_dashboards_live) by Rohit Deshpande and Scott Young (SAP)

[Watch Sumeet's talk](https://www.conf42.com/Platform_Engineering_2026_Sumeet_L_Ram_compliance_gate_paved)

[Watch the talk on YouTube](https://youtu.be/SlNLDiAkxyI).

## Watch the talk

[The Paved Road Had a Compliance Gate](https://www.conf42.com/Platform_Engineering_2026_Sumeet_L_Ram_compliance_gate_paved) at Conf42 Platform Engineering 2026.
