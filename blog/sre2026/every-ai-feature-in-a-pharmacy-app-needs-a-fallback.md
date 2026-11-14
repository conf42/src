# Every AI feature in a pharmacy app needs a tested fallback

Conf42 Blog, 2026-02-27, updated 2026-11-09. https://www.conf42.com/blog/sre2026/every-ai-feature-in-a-pharmacy-app-needs-a-fallback

In short: Dipta Rakshit (Walmart Global Tech) at Conf42 SRE 2026 on running AI-driven healthcare and retail in one mobile platform without missed doses.

When the refill prediction model in a pharmacy app fails and the app sends nothing, a patient misses a dose. At Conf42 Site Reliability Engineering (SRE) 2026, Dipta Rakshit, Staff Software Engineer at Walmart Global Tech, explained how one mobile platform serves prescriptions and retail (eyewear try-on, pet care, promotions) at once, and why every AI feature on it ships with a degraded mode that has already been tested.

## One app, two very different blast radii

The setup is unusual. On one side sit HIPAA-governed prescription lifecycles, insurance integrations and pharmacy partners, each with its own API quirks. On the other sit commerce features where the failure mode is a lost sale, not a health event. Dipta's answer is domain-scoped microservices: pharmacy, retail and user management deploy independently, with circuit breakers and bulkheads so a retail traffic surge can't starve pharmacy services of compute.

He gave a production example. When a pharmacy integration partner's API went down, the system saw the error rate climb within 30 seconds, tripped the circuit breakers and switched to a backup partner. On-call got a notification and had nothing to do. That is the goal state he describes: detection and isolation happen before a human reads the page.

The same split goes all the way down to data. Health and commerce data travel through separate encrypted pipelines with separate audit controls, even on shared cloud infrastructure. When a data access issue came up, the team could show quickly that it was confined to the commerce plane, which turned a compliance investigation of days into hours.

## Failing closed is the worst default

The sharpest lesson came from early in their ML rollout. When the refill prediction model failed, the system returned nothing, so no reminders went out at all. A dumb rule based on fill dates would have been better. Now every AI feature has a defined fallback chain before launch: ML prediction, then rule-based reminders from prescription history, then fixed-interval reminders. The AR eyewear try-on drops from full AR rendering to a 2D overlay to a plain product image.

They don't trust those fallbacks on paper. They break the AR service on purpose with chaos experiments and check that customers can still finish a purchase. With the ML models running, Dipta reported a 40% reduction in missed doses compared with fixed-interval reminders, which is exactly why falling back silently to nothing would hurt.

## Measure the outcome, not just the API

Observability for AI here covers inference latency per request path, feature drift, prediction confidence (low confidence triggers the fallback) and fallback activation rates by service. Tracking those found a surprise: refill predictions slowed down at peak hours because of feature computation, not inference. Fixing the feature pipeline cut that latency by 60%.

The bigger shift is the SLIs. Refill completion rate is a primary SLI; if it drops below 95%, the team investigates even when CPU and latency look fine. Dipta said these outcome SLIs catch problems 30 to 60 minutes earlier than operational metrics alone.

## Accessibility and localization are reliability work

Two examples make the point better than any slogan. A date-format mismatch sent prescription reminders on the wrong day for some users; the fix was ISO 8601 everywhere. A Spanish translation error in prescription instructions could have led to wrong medication timing, so translated content now goes through code review, automated tests and staging like any other change, plus a native speaker review. Screen reader failures are treated as SLO breaches with the same incident response as an API outage. If a user can't complete the task, the service failed, whatever the status page says.

## Who should watch

Engineers running mobile platforms in regulated domains, and anyone shipping ML features to production who hasn't yet decided what happens when the model is down. The patterns (separate data planes, tested fallbacks, outcome SLIs) carry over well beyond pharmacy. It is a broad architecture talk rather than a code walkthrough.

## Related Conf42 talks

- [Engineering Reliable Mobile Applications](https://www.conf42.com/Site_Reliability_Engineering_2021_Pranjal_Deo_reliable_mobile_applications) by Pranjal Deo (Google), the SRE view of the client side.
- [Graceful degradation: keeping the lights on when everything goes wrong](https://www.conf42.com/Chaos_Engineering_2023_Tanveer_Gill_graceful_degradation_everything_goes_wrong) by Tanveer Gill, on designing the degraded modes themselves.
- [Platform Engineering for AI-Powered Healthcare: Native Mobile Architecture](https://www.conf42.com/Platform_Engineering_2025_Srikanth_Puram_mobile_healthcare_powered) by Srikanth Puram (General Motors), another take on healthcare apps at scale.

[Watch Dipta Rakshit's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Dipta_Rakshit_building_reliable_driven)

[Watch the talk on YouTube](https://youtu.be/RLM8fM-aEsU).

## Watch the talk

[Building Reliable AI-Driven Mobile Platforms for Healthcare and Commerce](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Dipta_Rakshit_building_reliable_driven) at Conf42 Site Reliability Engineering (SRE) 2026.
