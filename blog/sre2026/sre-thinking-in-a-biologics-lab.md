# SRE habits in a biologics lab cut manual work 40% per AMBR run

Conf42 Blog, 2026-02-24, updated 2026-11-09. https://www.conf42.com/blog/sre2026/sre-thinking-in-a-biologics-lab

In short: Amogha Tenneti of Eurofins PSS at Conf42 SRE 2026 on automating AMBR250 lab analytics with FLEX2 via phase gates, equivalency tests and super users.

Toil, single points of failure and controlled migrations are not only software problems. At Conf42 Site Reliability Engineering 2026, Amogha Tenneti, Senior Associate Scientist at Eurofins PSS supporting Janssen, a Johnson & Johnson company, showed how SRE-style thinking guided the move of a regulated upstream biologics lab from manual analytics to an automated analyzer, cutting manual labour per AMBR250 run by about 40%.

This is one of the more unusual talks at the event: no Kubernetes, no pager, and a very familiar shape anyway.

## High toil and a big error surface

The setting is upstream biologics process development at Janssen's Malvern, Pennsylvania site. The Sartorius AMBR250 runs many parallel 250 ml microbioreactors for rapid process screening, which means lots of small samples and dense data. The analytics behind it were still manual: each sample went through several instruments by hand.

Tenneti lists three resulting problems: reliability risk from operator-dependent sampling variability, operational overhead that capped throughput, and a compliance burden that widened audit and data integrity exposure. In her words, from an SRE perspective the system had high toil and a large error surface area.

The fix was the BioProfile FLEX2 analyzer, which measures metabolites, blood gases, electrolytes, osmolality and cell health metrics from a single small sample in one automated run, with structured, audit-ready output suited to GxP requirements. One instrument replacing several also removed the throughput mismatch between the bioreactor and its analytics.

## A phase-gated rollout that looks like a production migration

What makes it an SRE talk is how the change was made. From December 2022 to August 2024 the integration followed a phase-gated model: independent analytical evaluation, instrument qualification through IQ, OQ and PQ (installation, operational and performance qualification), equivalency studies, validation, super user deployment, and full operational implementation in August 2024. Tenneti draws the parallel herself: it mirrors a controlled production migration in software.

The equivalency studies are the lab's version of running old and new systems side by side before cutting over. Four structured comparability experiments tested each AMBR-derived sample on both the FLEX2 and the existing standard analyzers, across pH, pCO2, glucose, lactate, glutamine, glutamate, ammonium, osmolality, viable cell density and viability. Acceptance criteria were set in advance from internal validation and regulatory standards. All four studies met them, and only then were the old analyzers decommissioned. Picture a canary release where the canary has to pass a regulatory review.

## Removing the human single point of failure

Automation also changed the day. Instead of someone coming into the lab to sample and walk each sample across several instruments, sampling could be scheduled sensibly, with a full analytical panel from one run per sampling event. Fewer touch points meant fewer handling errors and data that could be reviewed and trended.

The scale-out plan is the part most engineering orgs could copy. Twelve super users were trained: eight at Malvern and four at Spring House, Pennsylvania, so both sites could troubleshoot independently without relying on one subject-matter expert. That is distributed ownership aimed squarely at knowledge silos.

## Who should watch

Engineers working in regulated industries (pharma, medical devices, anything with GxP or audit trails) will find a rare worked example of SRE principles outside software. SREs who want a fresh way to explain toil, change management and bus factor to non-software colleagues will also get something from it. It is a short case study from a lab scientist, so expect process and validation detail rather than code. Her summary: eliminate toil, protect reliability through controlled change, improve observability with structured data, and distribute ownership.

## Related Conf42 talks

- [Reduce Toil by Improving Your Automation](https://www.conf42.com/DevOps_2024_Mandi_Walls_improve_automation_reduce_toil) by Mandi Walls.
- [AI-Powered Clinical Trials: Transforming Statistical Programming for Speed, Compliance, and Precision](https://www.conf42.com/Cloud_Native_2025_Vamsi_Upputuri_biotech_analysis_compliance) by Vamsi Upputuri.
- [Engineering the Future of Pharma: AI-Driven Platforms for Drug Discovery](https://www.conf42.com/Platform_Engineering_2024_Amit_Taneja_pharma_aidriven_discovery) by Amit Taneja.

[Watch Amogha Tenneti's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Amogha_Tenneti_driven_automation_flex) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/fPrFV5qi9U4).

## Watch the talk

[SRE-Driven Automation of FLEX2 Analytics in AMBR250 Upstream Biologics Workflows](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Amogha_Tenneti_driven_automation_flex) at Conf42 Site Reliability Engineering (SRE) 2026.
