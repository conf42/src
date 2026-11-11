# Cloud Custodian turns cloud compliance into YAML instead of glue functions

Conf42 Blog, 2021-12-02. https://www.conf42.com/blog/devsecops2021/cloud-custodian-yaml-instead-of-glue-functions

In short: Ismael Hommani and Tanguy Combe (WeScale) at Conf42 DevSecOps 2021 on policy as code with Cloud Custodian across AWS, Azure and GCP, with a live GCP demo

Every team that wants its dev databases stopped at night ends up writing the same scheduler, the same two cloud functions and the same Terraform to wire them, each with its own bugs. At Conf42 DevSecOps 2021, Ismael Hommani, Cloud Native Developer, and Tanguy Combe, Cloud Builder, both at French consultancy WeScale, showed how Cloud Custodian replaces that hand-made plumbing with declarative YAML policies, and demoed a policy chain on Google Cloud that stops any VM exposing a public IP.

## Why treat compliance as code?

"Compliance is all about managing the risk," Ismael Hommani said at Conf42 DevSecOps 2021.

In his framing, that means rules you follow, usually for legal reasons such as GDPR or PCI DSS, sometimes internal ones such as HR, environmental or budget policies. The cloud's shared responsibility model covers the provider's hardware and managed services; your data and workloads are your part. The aim is to bake compliance into the platform, continuously and automatically, so an audit becomes a non-event.

He splits the platform into three layers. Identity and access management is about trust. Passive platform policies are the provider's own settings, like forbidding buckets in a region, but they cannot follow every business rule. Reactive platform policies fill the gap: consume the platform's events and trigger actions.

## What's wrong with doing it by hand?

The hand-rolled version of stop-SQL-at-night on GCP is two Cloud Scheduler entries, a stop function, a start function and Terraform to reproduce it. Ismael lists three drawbacks: the architecture is subjective (everyone designs it differently), the function code is yours to get wrong, and teams that do not talk to each other duplicate it.

Cloud Custodian flips that to declarative. You describe the policy in YAML in business terms; Custodian deploys the triggers and serverless functions itself. One file can be shared across teams.

## How does a Cloud Custodian policy work?

Tanguy covers the internals. Cloud Custodian is an open source project launched by Capital One: a Python library driven by YAML, in the CNCF sandbox, with a monthly release cadence, supporting AWS, Azure and GCP (GCP still alpha at the time). Each policy names a resource, filters and actions. His shortcut is SQL: the resource is the FROM, the filters are the WHERE, the action is the SELECT. The example policy finds Azure disks attached to nothing and deletes them.

Policies run locally, periodically or on events. On AWS, Custodian wires CloudWatch Events from CloudTrail or schedules to Lambda; on GCP, audit logs, Security Command Center or Cloud Scheduler to Cloud Functions; on Azure, Event Grid and Azure Functions. Filters come in three flavours: value filters that query the API, event filters that inspect the incoming event, and resource-specific filters.

## What about resources you can't fix at creation time?

Some resources cannot be modified until they finish provisioning. The answer is a mark-for-op workflow. His example enforces a 35-day backup retention period, the maximum, on every RDS DB cluster. Policy one reacts to the create and modify CloudTrail events, filters clusters below 35 days, tags them for a delayed operation and sends a notification. Policy two runs every two minutes, finds tagged clusters that are now available, and sets retention to 35 days. Policy three removes the tag from clusters that are now compliant. Then, in Tanguy's words, you can take a coffee.

The same engine covers FinOps (start and stop dev instances), alerting on suspicious actions through Slack, Splunk or Datadog, and GitOps for compliance, with the repository as the source of truth for auditors.

## Contributing back

When they found Cloud Custodian had no start action for GCP Cloud SQL instances, they wrote one. The test pattern is worth knowing: record real API responses once with record flight data, then replay them in tests with replay flight data, so the suite never touches the cloud again.

## The demo: no public IPs on GCP

Ismael's live demo in Cloud Shell starts with zero Cloud Functions and zero scheduler jobs, to prove Custodian creates the architecture. Terraform only enables the APIs and creates a least-privilege identity for Custodian. The policy chain has four parts: label every new compute instance from the audit log; every minute, mark labelled instances that expose a public IP for a stop and notify via Pub/Sub; every minute, stop marked instances; and an exception that restarts instances named unstoppable plus five digits and removes the labels so the chain does not loop forever. A test VM gets stopped; the unstoppable one comes back. A bonus policy batch-deletes instances by label, the kind of job usually done with a throwaway script.

## Who should watch

Cloud and platform engineers who own guardrails across accounts or projects, and anyone maintaining a drawer of compliance Lambda functions. Expect YAML and a real demo.

## Related Conf42 talks

- Travis Gary on [passing compliance audits with Terraform instead of Jira tickets](https://www.conf42.com/DevSecOps_2021_Travis_Gary_Infraascode_Jira_tickets) at Conf42 DevSecOps 2021.
- David Melamed on [Open Policy Agent as a control engine](https://www.conf42.com/Cloud_Native_2022_David_Melamed_open_policy_agent_control_engine) at Conf42 Cloud Native 2022.
- Peter O'Neill on [securing terraform apply with Open Policy Agent](https://www.conf42.com/Site_Reliability_Engineering_2022_Peter_ONeill_terraform_apply_secured_open_policy_agent) at Conf42 SRE 2022.

[Watch Ismael Hommani and Tanguy Combe's talk](https://www.conf42.com/DevSecOps_2021_Ismael_Hommani_Tanguy_Combe_compliance_as_code_cloud_custodian) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From WeScale

WeScale, founded in 2015 with a community of about 50 cloud experts in Paris, Nantes and remote, helps clients design, build and run cloud native architectures, and runs training on GCP, AWS, Kubernetes, Vault and Terraform.

- WeScale: [wescale.fr](https://www.wescale.fr/)

[Watch the talk on YouTube](https://youtu.be/H3hLVALwkqc).

## Watch the talk

[Compliance As Code with Cloud Custodian](https://www.conf42.com/DevSecOps_2021_Ismael_Hommani_Tanguy_Combe_compliance_as_code_cloud_custodian) at Conf42 DevSecOps 2021.
