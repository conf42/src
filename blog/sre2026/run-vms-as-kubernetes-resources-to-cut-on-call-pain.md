# Run VMs as Kubernetes resources to cut hybrid on-call pain

Conf42 Blog, 2026-03-03, updated 2026-11-09. https://www.conf42.com/blog/sre2026/run-vms-as-kubernetes-resources-to-cut-on-call-pain

In short: Shruthi Rajashekar (Broadcom) at Conf42 SRE 2026 on VM Service in VCF, which manages virtual machines and containers through one Kubernetes control plane.

If your on-call rotation covers containers in Kubernetes and VMs in a separate virtualization stack, you are on call for two platforms with two sets of alerts, dashboards and runbooks. At Conf42 Site Reliability Engineering (SRE) 2026, Shruthi Rajashekar, Engineering Manager at Broadcom who leads VM Service in VMware Cloud Foundation (VCF), argued for managing both through one Kubernetes control plane, with VMs declared and reconciled like any other resource.

To be clear about scope: this is a talk about a Broadcom product, VM Service in VCF, from the team that builds it. Shruthi has spent a decade at VMware and Broadcom and worked on vMotion, so the hybrid problem is home turf.

## Two worlds, one pager

The pain she describes is operational fragmentation. Containers live in Kubernetes-native tooling; VMs live in another stack with different APIs and consoles. During an incident, SREs correlate alerts from different systems and switch context to troubleshoot, and automation is hard to standardize when every workload type has its own lifecycle model. Most enterprises still run critical workloads on VMs while newer services run in containers, so this split isn't going away on its own.

## A VM as a first-class Kubernetes resource

VM Service makes a virtual machine something you declare, deploy, scale and manage with the same Kubernetes primitives as a pod or a deployment. You write the desired state in a manifest; the platform provisions it and keeps reconciling. That brings the usual Kubernetes benefits to VMs:

- VM specs can live in Git next to application code, so GitOps workflows apply to them too.
- Provisioning becomes repeatable and auditable instead of a console click or a one-off script.
- Engineers stop asking which system owns a workload during an incident; they interact with Kubernetes either way.

The same automation, policies and playbooks then apply across both workload types.

## Where reliability actually improves

Shruthi's list of reliability gains is concrete enough to test against your own setup:

- **Consistent alerts and metrics.** When VMs and containers sit under the same orchestration layer, alerts are generated the same way and metrics follow the same patterns, so incident response becomes predictable.
- **Capacity planning as one pool.** Instead of reasoning about separate resource pools for VMs and containers, teams can plan holistically.
- **Policy-driven rollouts and isolation.** Rollout safety, resource isolation and security policies can be enforced programmatically for VMs, and Kubernetes scheduling and policy help limit blast radius.
- **Unified telemetry.** Correlating CPU pressure, network anomalies or latency spikes across VMs and containers in one view, rather than across two monitoring pipelines.

## Modernize without rewriting

Her closing point is the most persuasive for teams with real legacy estates: you don't have to containerize everything to adopt cloud-native operations. Bring existing VM workloads under Kubernetes governance, keep newer services in containers, and modernize incrementally. The legacy application that nobody wants to rewrite gets declarative management and safer rollouts without a migration project.

## Who should watch

Platform and SRE teams on VMware or VCF who run mixed VM and container estates and are tired of two operational models. If you're not in the VMware world, the talk still frames the case for unifying control planes, but the mechanics are specific to VM Service. It is an overview talk; expect architecture and benefits rather than a demo or incident numbers.

## Related Conf42 talks

- [KubeVirt Alchemy: Transforming VMs into Kubernetes Workloads](https://www.conf42.com/Kube_Native_2024_Koray_Oksay_Batuhan_Apaydin_kubevirt_vms_kubernetes_workloads) by Koray Oksay and Batuhan Apaydin (Kubermatic), the open-source route to the same idea.
- [Debugging cluster issues as an on-call SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pravar_Agrawal_debugging_cluster_oncall) by Pravar Agrawal (IBM).
- [Compliance-Aware Platform Engineering: Scaling Hybrid Cloud Automation](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid) by Satish Manchana (UBS).

[Watch Shruthi Rajashekar's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Shruthi_Rajashekar_reducing_call_pain)

[Watch the talk on YouTube](https://youtu.be/Vv8bHcqVXKU).

## Watch the talk

[Reducing On-Call Pain in Hybrid Platforms: Operating VMs and Containers Reliably on Kubernetes](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Shruthi_Rajashekar_reducing_call_pain) at Conf42 Site Reliability Engineering (SRE) 2026.
