# Regional Keycloak hubs keep global SASE logins close to users

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/regional-keycloak-hubs-for-global-sase

In short: Vivek Koodakkara Shanmughan of Aryaka Networks proposes at Conf42 Kube Native 2025 a regional hub model for Keycloak to scale SASE identity worldwide.

In a zero trust world, the login page is part of the network path, and a slow one is an outage with extra steps. At Conf42 Kube Native 2025, Vivek Koodakkara Shanmughan, Senior Engineering Manager at Aryaka Networks, laid out a regional hub model for Keycloak: autonomous identity clusters in each major region, kept in step with each other, so users authenticate near where they are.

The talk is framed as a design proposal ("we could") rather than a production war story, and it is honest about the trade-offs.

## Identity is the new perimeter

Shanmughan starts from the end of the castle-and-moat model. With remote workers, apps spread across cloud and edge, and regional regulation, the network perimeter is gone, and SASE (Secure Access Service Edge) merges networking and security into a cloud-delivered service built on zero trust. In that model, identity is the passport: every access decision hangs on who you are, on what device, under what conditions.

His analogy is airports. Instead of routing every traveller through one central hub, you check in and clear security locally.

## Why one central IdP hurts

Centralised identity looks tidy on a diagram and causes four problems in practice. Latency: he puts a Singapore user authenticating against a US-based identity provider at 200 to 300 milliseconds of delay per request. Availability: one outage locks out users worldwide. Data sovereignty: GDPR and CCPA can require identity data to be processed and stored locally. And throughput: a central IAM system may simply not be built for global traffic.

## A hub per region, synchronised

The proposal is one autonomous Keycloak cluster per major region (for example the Americas, EMEA and APAC), each authenticating local users on its own. A hub has a standard shape: the Keycloak cluster for authentication and SSO, a database for users and configuration, a load balancer across Keycloak nodes, directory synchronisation with corporate accounts, and an observability layer.

Keycloak fits because it is open source and Kubernetes-native, supports multi-tenancy through realms, speaks OIDC, SAML and WebAuthn, and can be extended through SPIs and event listeners.

Placement is driven by data: map where users are, align hubs with existing SASE points of presence, group regions with similar compliance rules, pick cloud regions with strong service, and test latency from real user locations. He suggests starting with three or four hubs. Sync goes through shared directories such as AD or LDAP or database replication, with GitOps workflows for policy, cross-cluster token validation, Infinispan distributed caches or token exchange between hubs.

## Automate it or don't do it

Several Keycloak clusters by hand is a recipe for drift, so automation carries the design: Keycloak configuration as code through GitOps, the Keycloak Operator on Kubernetes, canary rollouts and per-region observability of login flows, latency and errors. He lists the costs too: data consistency across regions (define authoritative sources and conflict rules), more operational complexity, tricky failover (health-aware global load balancers, tested regularly), higher spend and harder compliance.

His suggested first step is modest: map your users, find the hotspots, and pilot a two-region deployment.

## Who should watch

Identity and platform engineers running Keycloak for users on more than one continent, and anyone designing zero trust access who has only planned for one region. If you want Keycloak 101, start with the docs; this assumes you know realms and clients.

## Related talks

- Mahesh Vankayala on the SSO side: [Identity Federation: Enhancing Digital Security and Efficiency Through Single Sign-On in DevSecOps](https://www.conf42.com/DevSecOps_2024_Mahesh_Vankayala_identity_federation_security).
- Zero trust for machines rather than people: Venkata Velavarthipati on [Secretless Multi-Cloud Authentication with Workload Identity](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless).
- Md Azmal brings zero trust to the mesh in [Ambient Mesh: The new sidecar less & faster Istio for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust).

[Watch Vivek Koodakkara Shanmughan's talk](https://www.conf42.com/Kube_Native_2025_Vivek_Koodakkara_Shanmughan_identity_keycloak_deployment)

[Watch the talk on YouTube](https://youtu.be/aWZxmQ5RFPE).

## Watch the talk

[Scaling Identity for Global SASE with Keycloak: The Regional Hub Deployment Model](https://www.conf42.com/Kube_Native_2025_Vivek_Koodakkara_Shanmughan_identity_keycloak_deployment) at Conf42 Kube Native 2025.
