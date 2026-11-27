# Fluent Bit on EKS, from empty cluster to CloudWatch logs

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/fluent-bit-eks-cloudwatch-demo

In short: Dharmendra Ahuja at Conf42 Observability 2025 demos Fluent Bit as a DaemonSet on AWS EKS, shipping enriched container logs to CloudWatch, plus five use cases.

Fluent Bit is the small log processor that ends up on most Kubernetes nodes, and the setup is easier to learn by watching than by reading the Helm chart. At Conf42 Observability 2025, Dharmendra Ahuja, a DevOps architect and data engineer, built the whole pipeline live on AWS EKS: cluster, IAM, Fluent Bit and a sample app, ending with container logs in CloudWatch.

It is a practical, step-by-step demo, followed by five real-world patterns that reuse the same building blocks.

## What Fluent Bit does in the pipeline

Before the demo, Dharmendra lays out Fluent Bit's four jobs: **collect** logs from containers and endpoints, **enrich** them with Kubernetes metadata and custom tags, **transform** them by structuring, filtering and masking sensitive fields, and **route** them to destinations based on content, namespace or other attributes.

The internals map to a plain pipeline: input plugins read from containers, files or systemd; parsers turn lines into structured JSON; filters enrich or drop data; buffers hold logs in memory or on disk during spikes or network delays; output plugins push to CloudWatch, S3, Kinesis Data Firehose, OpenSearch, Elasticsearch or Kafka.

## The demo, step by step

The demo is the reason to watch, because it shows the parts people get wrong. In order:

1. Create the EKS cluster from an `eksctl` config file and watch the CloudFormation stacks build the VPC pieces, control plane and add-ons.
2. Update the kubeconfig and create a `fluent-bit` namespace.
3. Associate an IAM OIDC provider with the cluster, then create an IAM service account bound to a pre-made policy that grants CloudWatch Logs access. This is how the pods get permissions without node-wide credentials.
4. Add the Fluent Bit Helm repo and install the chart with the existing service account, CloudWatch output, region, log group and a log stream prefix.
5. Edit the Fluent Bit ConfigMap to swap the default Elasticsearch output for CloudWatch, then restart the DaemonSet so it picks up the change. The restart is the step people forget.
6. Deploy an NGINX "log server" in a demo namespace, port-forward it, and hit it with `curl` while tailing logs locally in a second terminal.

The payoff is a new log group in CloudWatch with the expected streams, and a CloudWatch dashboard showing the requests as they arrive. The demo is honest about waiting for CloudFormation, which anyone who has run `eksctl create cluster` will recognise.

## Five patterns from the field

The closing section takes the same DaemonSet and points it at different problems:

- **FinTech audit trail:** tail container logs, enrich with Kubernetes metadata, ship to CloudWatch for centralised logging that satisfies financial audits.
- **SaaS search:** stream to Amazon OpenSearch with Kibana dashboards for near-real-time log queries.
- **Gaming platform to Datadog:** use the HTTP output plugin with filters that trim log volume and ingestion cost without hurting cluster performance.
- **Healthcare compliance:** add Linux audit logs via the systemd input, archive to a dedicated S3 bucket for long retention under HIPAA, and let the security team pull into Splunk for forensics.
- **Multi-tenant isolation:** add tenant labels by namespace and route each tenant to its own Grafana Loki tenant, so one cluster serves several customers without mixing logs.

## Who should watch

Engineers about to put logging on their first EKS cluster, or anyone who has copied a Fluent Bit Helm values file without knowing what the IRSA steps were for. If you already run Fluent Bit in production, skip to the use cases.

## Related Conf42 talks

- [Michael Levan on Kubernetes monitoring and observability](https://www.conf42.com/Observability_2024_Michael_Levan_kubernetes_monitoring_observability) (Observability 2024).
- [Alok Ranjan on going from fragmented logs to unified insights](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Alok_Ranjan_fragmented_logs_unified) (SRE 2025).
- [Leonid Yankulin on anonymizing application logs the DevOps way](https://www.conf42.com/DevSecOps_2022_Leonid_Yankulin_structured_logging_google_cloud) (DevSecOps 2022), for the masking step in practice.

[Watch Dharmendra Ahuja's talk](https://www.conf42.com/Observability_2025_Dharmendra_Ahuja_fluent_eks_aws)

[Watch the talk on YouTube](https://youtu.be/DM4IBQxJzOM).

## Watch the talk

[Unveiling the Power of Observability using FLUENT BIT in AWS EKS environment](https://www.conf42.com/Observability_2025_Dharmendra_Ahuja_fluent_eks_aws) at Conf42 Observability 2025.
