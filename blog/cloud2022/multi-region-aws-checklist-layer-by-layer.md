# High availability survives a zone; fault tolerance survives the region

Conf42 Blog, 2022-04-29. https://www.conf42.com/blog/cloud2022/multi-region-aws-checklist-layer-by-layer

In short: Ana Van Straaten (Globant) at Conf42 Cloud Native 2022 on taking a single-region AWS service multi-region, layer by layer

Spreading a cluster across availability zones protects you from a dead server, not from a dead region. Ana Van Straaten, DevOps Engineer at Globant, spent her Conf42 Cloud Native 2022 talk on the step after high availability: making a service fault tolerant across AWS regions, with a checklist that walks from security through networking, compute and data to the CI/CD that deploys it all twice.

It is a compact field guide drawn from projects that needed zero downtime, and it is very AWS-specific. She says so herself, and adds that other clouds have equivalents for each piece.

## High availability or fault tolerance?

She draws the line clearly. High availability spreads workloads across a cluster of instances, usually across availability zones in one region, with a load balancer moving traffic away from failures. It is easier to maintain and scale, but it doubles components, risks losing data in flight while authority changes hands, and still allows some disruption. And if the region goes, the whole service goes.

Fault tolerance aims for zero interruption, not only during failures but during upgrades and maintenance, with redundancy that avoids the active-passive crossover. Done well, there should be no data loss. The price is a costlier, more complex setup, so the choice depends on how much disruption you can tolerate and how much operational effort you can afford.

## What has to be replicated first?

Security, before anything else. Authorization, encryption, auditing and observability all need cross-region (and cross-account) replication:

- IAM is multi-region with no configuration on your side.
- Secrets Manager secrets, encrypted with KMS, can be replicated to secondary regions so they are read from the closest available one, and KMS multi-region keys simplify encryption for apps running in both.
- Logs go into an S3 bucket with multi-region replication, and Security Hub can collect findings from both regions into one pane.

## How do the regions talk, and how do users find them?

Networking comes next. VPC peering lets resources communicate over private IP addresses without an internet gateway, VPN or extra appliances, and she notes it is the cheaper option. Transit Gateway, with inter-region peering, connects VPCs and on-premises networks into a global private network. Route 53 routes users to the distributed endpoints, CloudFront can fail over to a secondary origin when the primary is down or returns a failure status code, and Global Accelerator gives internet-facing apps two static anycast IPs as one entry point, redirecting traffic within 6 seconds. She likes traffic weights in Global Accelerator for testing deployments: developers shift weights, no cloud engineer required.

## What about compute and data?

For EC2, Data Lifecycle Manager replicates EBS volumes to another region and EC2 Image Builder replicates AMIs. For containers, ECR does cross-region and cross-account image replication.

Data is where the CAP theorem bites: you pick two of consistency, availability and partition tolerance, and across long distances consistency is the hardest to keep. Her map of the options:

- **S3**: one-way or two-way continuous replication, optionally for a subset of objects.
- **DynamoDB**: global tables with multi-writer replication.
- **ElastiCache for Redis**: a global datastore with cross-region replicas.
- **Aurora**: one writer region and read replicas elsewhere. Aurora MySQL's write forwarding sends writes from a secondary endpoint to the primary, which keeps application code simple. A cross-region read replica can be promoted to a standalone instance in a disaster.

## Who deploys all of this twice?

The last layer is application management. Whether it is CodePipeline, GitLab CI or Jenkins, the pipeline has to deploy to both regions, one after the other while the primary keeps serving, with variable files per region and environment. She mostly uses Terraform for its review-before-apply step; CloudFormation can create, update and delete stacks across multiple regions and accounts from one template. Decoupled apps can route events across regions with EventBridge, and Systems Manager Explorer gives one operations dashboard across regions and accounts.

"Each cloud has similar resources and alternatives to build a fault tolerant multiregion service. It's hard, but it's possible," Ana Van Straaten said at Conf42 Cloud Native 2022.

## Who should watch

Engineers inheriting a legacy service that runs in one region with no failover, and anyone who wants a checklist before the planning meeting. It is a survey, not a migration story with numbers, so pair it with your own RTO and RPO targets.

## Related Conf42 talks

- Christian Elsen and Lerna Ekmekcioglu on [reliable multi-region architecture](https://www.conf42.com/Site_Reliability_Engineering_2022_Christian_Elsen_Lerna_Ekmekcioglu_reliable_multiregion_arch) at Conf42 SRE 2022.
- Lerna Ekmekcioglu and Jack Iu on [multi-region deployments with Terraform](https://www.conf42.com/Chaos_Engineering_2022_Lerna_Ekmekcioglu_Jack_Iu_multi_region_terraform_deployments_with_terraform_b) at Conf42 Chaos Engineering 2022.
- Kyle Shelton on [disaster recovery preparedness](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness) at Conf42 Chaos Engineering 2022.

[Watch Ana Van Straaten's talk](https://www.conf42.com/Cloud_Native_2022_Ana_Van_Straaten_going_multi_region)

## From Globant

Globant is a digitally native technology services company; Van Straaten works there as a DevOps engineer on cloud projects like the ones behind this talk.

- [Globant](https://bit.ly/3pYFWRA)

[Watch the talk on YouTube](https://youtu.be/T4yw0Unc-wQ).

## Watch the talk

[Preparing for disaster: going Multi-Region](https://www.conf42.com/Cloud_Native_2022_Ana_Van_Straaten_going_multi_region) at Conf42 Cloud Native 2022.
