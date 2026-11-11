# Conf42 Feature Flags 2026: kill switches, migrations and model gates

Conf42 Blog, 2026-10-16. https://www.conf42.com/blog/featureflags2026/conf42-feature-flags-2026-roundup

In short: Conf42 Feature Flags 2026 roundup: 16 talks from Harness, Capital One, Adobe, Bank of America, Confluent and more on flags for AI agents, migrations and models.

The first Conf42 Feature Flags conference ran on October 15, 2026, under the tagline *Flip features, not tables!*, and it quickly became clear that nobody on the lineup thinks of a flag as a boolean any more. Across 16 talks, engineers from Harness, Capital One, Walmart, Adobe, Bank of America, Confluent, PayPal and Amazon used flags as kill switches for AI agents, routers for migrations, gates for model releases and runtime controls for production diagnostics. Everything is on the [event page](https://www.conf42.com/featureflags2026).

Four themes carried the day.

## A flag stops new work, not running work

The most memorable opening of the event belonged to [Parthiban Rajasekaran](https://www.conf42.com/Feature_Flags_2026_Parthiban_Rajasekaran_ai_kill_switch) of Capital One, in "Your AI Kill Switch Is Probably Broken". In a simulated drill he disables an agent, the dashboard turns red, and a new request is rejected a second later. Fifteen seconds after that, a job that was already queued sends a customer email anyway. His point: most feature flags are admission controls, and a real kill switch for autonomous systems also needs cancellation semantics for work that's already in flight.

The rest of the agents track built on the same worry. [Girish Konda](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) of Microsoft, tech lead for capacity management in Microsoft Fabric, talked about a year of running agents against his real job (incident triage, telemetry, code review, runbooks) and the failure modes demos never show, like numbers with no source and citations to documents that don't exist. [Pavan Boppidi](https://www.conf42.com/Feature_Flags_2026_Pavan_Boppidi_autonomy_ai_logistics) of Walmart presented confidence-gated human-in-the-loop routing for autonomous logistics, with flags deciding how much autonomy each decision gets. And [Ishan Shah](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) of PayPal treated flag changes as incident evidence in Beacon, a governed workflow for AI-assisted root cause analysis that puts an explicit operator decision between hypothesis and action.

## Migrations as a series of reversible steps

Harness's keynote set the frame. [Ryan Vila](https://www.conf42.com/Feature_Flags_2026_Ryan_Vila_feature_flags_migration) walked through the strangler fig pattern with a flag doing the routing, a ramp from internal users to general availability, and the advice to step back a stage instead of killing a rollout. His closing section on flag hygiene (stale flags, untested defaults, drift between environments, clear ownership) is the part to share with your team.

Two talks applied that thinking to heavy, regulated systems. [Jaya Chand Bandi](https://www.conf42.com/Feature_Flags_2026_Jaya_Chand_Bandi_migration_payment_platforms) showed flags as the engine for domain-driven decomposition of monolithic payment platforms, carving out business capabilities one at a time. [Jaymin Sutarwala](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) of United Therapeutics described retiring a legacy patient CRM for a Salesforce stack spanning Marketing Cloud, Data Cloud and Health Cloud, with identity resolution, segmentation and activation each gated behind flags because a big-bang cutover wasn't an option with patient data involved.

[Pratham Yadav](https://www.conf42.com/Feature_Flags_2026_Pratham_Yadav_flag_kpi_analytics) of the College of Southern Nevada raised a migration most teams forget: the one in the analytics layer. When a flagged change alters the logic behind a KPI, dashboards and executive reports change too, so he argued for metric versioning and reconciliation against the old definition before switching.

## Gating models on quality, not just exposure

A flag decides who sees a feature. Three speakers asked what else it should check before widening. [Pavan Rupanguntla](https://www.conf42.com/Feature_Flags_2026_Pavan_Rupanguntla_credit_model_rollouts) of Bank of America separated model deployment from model activation for machine learning credit decisions, so a credit line strategy can ship dark and be released gradually with regulatory risk in mind.

[Rajesh Lingam](https://www.conf42.com/Feature_Flags_2026_Rajesh_Lingam_quality_gates_genai) of Adobe pointed out that a GenAI feature can be technically healthy while its answers get less accurate, grounded or safe. His answer is continuous automated evaluation feeding quality gates that inform rollout decisions. And [Rakshay Pawar](https://www.conf42.com/Feature_Flags_2026_Rakshay_Pawar_guardrails_rollout_risk) of Codeflow Capital asked whether guardrail metrics stay valid when targeting changes mid-rollout, stress-testing static, rolling and adaptive conformal bounds on decades of U.S. Treasury yield data. Probably the only feature flag talk this year with a bond market in it.

## Flags as runtime controls for operations

The reliability track used flags for things no product manager will ever see. [Fuad Laguda](https://www.conf42.com/Feature_Flags_2026_Fuad_Laguda_flag_diagnostics_runtime), an independent engineer in Stirling who runs two production apps alone, keeps his diagnostics behind a Cloudflare KV flag with three states (off, admin only, everyone), because shipping a build with extra logging at 11pm is too slow and leaving detailed traces on all the time would store users' personal data. The same flag shape reports when his app fails over to a second language-model provider after four consecutive failures, and he forced that failover in production on purpose to prove it works.

At the other end of the scale, [Naveen Goel](https://www.conf42.com/Feature_Flags_2026_Naveen_Goel_infrastructure_ai_sdlc) of Amazon made the case for AI as an operator inside the SDLC for a connected-device fleet serving more than 200,000 requests per second, with performance-aware review, payload replay in CI and phased canary, cell and region rollouts. [Prateek Jindal](https://www.conf42.com/Feature_Flags_2026_Prateek_Jindal_cloud_infrastructure_flags) of Confluent covered self-healing cloud infrastructure, using flags to limit blast radius and disable unstable behaviour automatically. [Anil Kumar](https://www.conf42.com/Feature_Flags_2026_Anil_Kumar_api_resilience_monitoring) of Allstate combined API health monitoring and auto-healing with flag-driven traffic controls, and [Emmanuela Opurum](https://www.conf42.com/Feature_Flags_2026_Emmanuela_Opurum_flags_cloud_deployments) of SoftNet Technologies gave an accessible tour of progressive rollouts, canaries and the common mistakes teams make with flags.

## Sponsors

Thanks to [Harness](https://www.harness.io/) and [SREday](https://www.sreday.com/), the diamond sponsors of the event, and to [HockeyStick](https://www.hockeystick.show/) for the podcast partnership.

## What's next

Every talk is linked from the [Conf42 Feature Flags 2026 page](https://www.conf42.com/featureflags2026). The second edition, [Conf42 Feature Flags 2027](https://www.conf42.com/featureflags2027), is scheduled for June 24, 2027. If your kill switch has never been tested with work in flight, you have until then.
