# Scaling a biopharma data platform from 15 TB to 140 TB a month

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/healthcare-data-platform-15tb-to-140tb

In short: Ritesh Kumar Sinha at Conf42 Platform Engineering 2025 on a platform-as-a-product rebuild of biopharma analytics on AWS, with compliance written as code.

A Fortune 500 biopharma company could reach only 15% of its available healthcare data sources, and its researchers were waiting hours for queries. At Conf42 Platform Engineering 2025, Ritesh Kumar Sinha, Associate Vice President at Kotak Mahindra Bank with two decades in technology and engineering, showed how a platform-as-a-product rebuild took that analytics stack from 15 TB to 140 TB of monthly processing on AWS, with HIPAA and GDPR controls built into the infrastructure code.

It is a compact talk (under eight minutes) and mostly a case study with the numbers up front, so it suits a quick watch between meetings.

## Why healthcare data platforms are their own kind of hard

Ritesh lists the constraints: hundreds of terabytes of sensitive data a month, HIPAA and GDPR on top, legacy systems that will not scale, researchers who want self-service analytics, and very different data domains to join. The legacy setup was a monolith that could not grow with demand, which in this industry means slower research, not just slower reports.

## Researchers are the customers

The shift he puts at the centre is treating infrastructure as a product, with research and clinical teams as its customers. In practice that meant self-service capabilities and automation so teams could get resources without waiting for an engineer, and compliance requirements written directly into infrastructure code instead of checked afterwards.

The platform runs on AWS, with automated ETL pipelines, a multi-zone data architecture and dynamic scaling. A metadata-driven framework keeps data quality consistent. Data lands in Amazon S3 and loads into Amazon Redshift with the COPY command, which is about as plain as a data platform gets and is probably why it scaled.

## The numbers he reports

Ritesh puts the outcomes in a list, and they are worth quoting as reported:

- monthly processing capacity from 15 TB to 140 TB;
- an 80% reduction in processing time;
- 67% faster developer velocity through self-service;
- $2.3 million in annual cost savings;
- drug discovery timelines shortened by 4.2 months per compound;
- a 23% higher clinical trial success rate through better data access.

The abstract frames the query change as 12 hours to 2.4 hours. Since the talk does not show the measurement method behind the research outcomes, read those as the team's own assessment.

## How the migration was run

The legacy-to-cloud-native move came in five phases: assessment of current capabilities and target architecture; a foundation of cloud environment plus compliance frameworks; migration using blue-green deployments; optimisation of the architecture and self-service; and then innovation with advanced analytics and ML.

The challenges were mostly human: organisational resistance, skill gaps, legacy integration, compliance worries, and the tension between standardisation and flexibility. The fixes Ritesh lists are the ones that tend to work: executive champions, platform engineers embedded with the teams, phased migration with clear metrics, compliance as code, and golden paths with escape hatches for edge cases. That last pairing is the detail to take home; a golden path with no escape hatch is just a wall.

His four strategies for anyone repeating this: start small with a high-value use case and scale fast, put compliance into automation and CI/CD, measure platform value with KPIs such as developer velocity and resource utilisation, and build an internal community through feedback forums and training.

## Who should watch

Data platform engineers in regulated industries, and platform teams whose customers are scientists or analysts rather than application developers. It is a results-first case study with an AWS reference shape, not a deep architecture walkthrough.

## Related Conf42 talks

- [Amit Taneja (UMB Bank) on AI-driven platforms for drug discovery](https://www.conf42.com/Platform_Engineering_2024_Amit_Taneja_pharma_aidriven_discovery), the research workload on the other end of a platform like this.
- [Santhosh Kumar Rai on cloud-native data engineering for precision medicine](https://www.conf42.com/Cloud_Native_2025_Santhosh_Kumar_Rai_data_engineering_healthcare_precision), a parallel healthcare data stack.
- [Shiva Kumar Chinnam (Rialtic) on healthcare data processing with Kubernetes](https://www.conf42.com/Kube_Native_2024_Shiva_Kumar_Chinnam_healthcare_kubernetes_data_processing), the same domain on a different substrate.

[Watch Ritesh Kumar Sinha's talk](https://www.conf42.com/Platform_Engineering_2025_Ritesh_Kumar_Sinha_monthly_analytics_healthcare)

[Watch the talk on YouTube](https://youtu.be/ZbLYt21GGWA).

## Watch the talk

[Platform Engineering at Scale: Building Cloud-Native Data Infrastructure for 140TB Monthly Healthcare Analytics](https://www.conf42.com/Platform_Engineering_2025_Ritesh_Kumar_Sinha_monthly_analytics_healthcare) at Conf42 Platform Engineering 2025.
