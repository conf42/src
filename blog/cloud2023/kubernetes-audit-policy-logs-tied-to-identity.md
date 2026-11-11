# Kubernetes audit logs only help if you scope them and tie them to a person

Conf42 Blog, 2023-03-31. https://www.conf42.com/blog/cloud2023/kubernetes-audit-policy-logs-tied-to-identity

In short: Kenneth DuMez (Teleport) at Conf42 Cloud Native 2023 on scoping the Kubernetes audit policy, centralising logs and tying every event to an identity

Turn on everything in the Kubernetes audit log and you get millions of lines nobody can read and an expensive bucket to keep them in. At Conf42 Cloud Native 2023, Kenneth DuMez, Developer Relations Engineer at Teleport (previously at Pivotal Cloud Foundry and VMware Tanzu), walked through the audit policy settings that keep the signal, the open source tools that watch the logs for you, and why the missing piece is knowing which human or machine ran each command.

The first two thirds are general Kubernetes practice; the last third is a Teleport demo.

## What does Kubernetes give you out of the box?

A built-in audit system that records API requests, resource changes and system events, stored as log files on the nodes or exposed through your hosted provider's console. It is extremely granular and configurable, which is the problem: a large cluster generates so many events that separating the wheat from the chaff gets hard.

The control is the audit policy, a native Kubernetes object written in YAML and passed to the API server. It is the first thing to configure. You can, for example, log only operations on Secrets, only Pod events, or everything on the core APIs but nothing on custom resources. His suggested starting point is the publicly available audit profile for Google's Container-Optimized OS, tailored from there rather than copied.

## Which policy fields matter?

The rules field does the work. Inside it:

- **omitStages** skips event stages you do not care about, such as RequestReceived or ResponseStarted. You do not need every stage.
- **level** sets how much is recorded: metadata, request or request and response.
- **resources**, **verbs**, **users** and **namespaces** narrow what is audited: which objects, which operations (create, update, delete), whose actions and where.

## What are the best practices?

- **Define the scope clearly.** An overly broad policy produces spam that is hard to parse, expensive to store and hides the events that matter, and it can cause performance problems.
- **Name rules meaningfully.** Audit configs age like legacy code; describe the event, resource and verb so future you can read it.
- **Review logs regularly,** with SIEM tools doing the heavy lifting.
- **Use dedicated storage,** separate from the cluster. S3 is a common home, piped on to monitoring and alerting.
- **Aggregate.** One central location is easier to filter and far easier to show an auditor than dozens of resources.

The point of all this is prevention, not blame. "All of the logs in the world are useless if you aren't actively monitoring them," Kenneth DuMez said at Conf42 Cloud Native 2023. Properly monitored, audit logs can catch an attack in progress rather than explain it afterwards.

## Which open source tools watch the logs?

Nobody reads audit logs by hand at scale. He covers three:

- **Falco**, the cloud native runtime security project, which detects and alerts on anomalous behaviour, including in Kubernetes audit logs, and integrates with incident response tooling.
- **Open Raven**, which collects and centralises audit logs across clusters, checks them against prebuilt compliance rules for PCI, HIPAA and GDPR, and alerts in real time. His caveat: it is hard to configure, especially across many clusters.
- **The Elastic Stack**, for centralised collection, real-time analysis and visualisation in Kibana (Grafana gets an honourable mention).

## What do those tools miss?

Access. A useful audit log needs to say exactly who, or what, executed each command, and with shared credentials it cannot. His argument for Teleport is that it ties every Kubernetes event to an identity mapped to a Teleport user and RBAC role, issues short-lived X.509 certificates to machines through Teleport Machine ID instead of long-lived secrets, and centralises audit logging for SSH, databases, Windows RDP and applications as well as Kubernetes. Fluentd handles formatting and exporting the logs.

The demo shows two paths into a cluster. First an SSH session to the node hosting the cluster from Teleport's web terminal, running kubectl get pods and describe; the session recording that results is not a video but a structured JSON log of every command, which can be shipped to a SIEM. Then from his own workstation: tsh login via GitHub SSO, tsh kube ls to see the one cluster his role allows, tsh kube login to fetch a kubeconfig, and the same kubectl commands. The audit log shows the issued certificate, his AWS role ARNs, the Kubernetes user, namespace and every request, all as JSON.

## Who should watch

Platform and security engineers who have to prove compliance (SOC 2, FedRAMP) for Kubernetes, and anyone whose audit policy is still the default or a copy from a blog post. The audit policy section stands on its own; the demo shows one way to add identity. Pair it with Teleport colleague [Travis Rodgers on just-in-time access requests](https://www.conf42.com/Site_Reliability_Engineering_2023_Travis_Rodgers_automated_justintime_access_requests), [Thomas Labarussias on Falco and eBPF](https://www.conf42.com/Observability_2023_Thomas_Labarussias_falco_ebpf_protect_applications) and [Reza Ramezanpour on Kubernetes security policy design](https://www.conf42.com/Cloud_Native_2023_Reza_Ramezanpour_kubernetes_security_policy_design_top10).

[Watch Kenneth DuMez's talk](https://www.conf42.com/Cloud_Native_2023_Kenneth_DuMez_kubernetes_audit_log)

## From Teleport

- [Teleport](https://goteleport.com/): identity-based access for SSH servers, Kubernetes clusters, databases and web applications.
- [About Teleport](https://goteleport.com/about)
- [Teleport blog](https://goteleport.com/blog)
- [Upcoming events](https://goteleport.com/about/events)
- [Teleport on YouTube](https://www.youtube.com/channel/UC1O9RGv3FGJau091DD09ooQ)

[Watch the talk on YouTube](https://youtu.be/lpkjrdSqgSQ).

## Watch the talk

[Kubernetes audit log best practices](https://www.conf42.com/Cloud_Native_2023_Kenneth_DuMez_kubernetes_audit_log) at Conf42 Cloud Native 2023.
