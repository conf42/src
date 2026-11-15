# An ML platform is only as secure as the identities that can touch it

Conf42 Blog, 2026-02-13, updated 2026-11-09. https://www.conf42.com/blog/ml2026/ml-platform-security-starts-with-identity

In short: Neha Asthana (Abbott) at Conf42 Machine Learning 2026 on identity lifecycle, access reviews, RBAC and privileged access management for enterprise ML platforms.

The quickest way to steal a model is often to borrow the service account that trains it. At Conf42 Machine Learning 2026, Neha Asthana, Identity Solutions Architect at Abbott, walked through the identity and access management foundations an enterprise ML platform needs: lifecycle automation, access certification, role-based access and privileged access management, tied together under one governance view.

This is an IAM fundamentals talk applied to ML, from someone who works in a regulated industry. If identity has always been somebody else's job on your platform, it is a compact correction.

## ML platforms multiply identities

Asthana's framing is growth. As organisations scale ML and data-heavy workloads, the population of users and service accounts expands faster than traditional controls can keep up with. Data access patterns span pipelines and analytical tools, automation needs elevated privileges, and regulated industries keep raising the bar. The result is three familiar failures: access sprawl across platforms, compliance gaps at audit time, and privileged accounts used without proper controls.

## Let HR be the source of truth

The first fix is identity lifecycle management connected to an authoritative source, usually the HR system. Four events drive everything: onboarding creates accounts and roles from job title and department, role changes adjust access on transfer or promotion, offboarding revokes access immediately, and rehires reactivate an identity instead of minting a duplicate. Automating these removes manual steps and, with them, the orphan accounts that linger after someone leaves.

## Review access, then model it as roles

Access certification campaigns ask managers and data owners to periodically confirm that each person still needs what they hold. That is how privilege creep and dormant accounts get found and removed, and it is the evidence auditors ask for.

RBAC then ties permissions to roles rather than people. Her examples map neatly onto an ML team: a data scientist needs the ML platform, training environments and approved datasets; a business analyst running dashboards can usually make do with read-only access; the infrastructure team needs admin rights for logging and monitoring. Get the roles right and most access requests answer themselves.

## Privileged accounts are where ML is most exposed

The section that makes this an ML talk is privileged access management. Service accounts run training jobs, CI/CD pipelines deploy models to production, and data engineers administer infrastructure holding huge volumes of data. Every one of those needs elevated permissions, which makes each an attack path to models, training data and pipelines.

The PAM capabilities she lists are concrete: credential vaulting to get secrets out of code, automated password rotation, session brokering so humans use privileged sessions without ever seeing the credential, session recording for anomaly detection and forensics, and just-in-time access with time-bound elevation and automatic revocation. Applied to ML, that means protecting proprietary models and training data, securing automated workflows, and controlling who can modify or export sensitive datasets.

## One governance view for humans and machines

The finish is integration: IAM governance (she mentions SailPoint IdentityIQ) combined with a PAM execution layer, so human and non-human identities sit in one inventory, privileged and service accounts get certified alongside people, and the same policy applies everywhere. For healthcare and other regulated sectors, that produces the audit logs, attestations, separation of duties and documentation that HIPAA, SOX and GDPR reviews look for.

## Who should watch

ML platform owners who have never been through an access review, security engineers newly assigned to an ML team, and anyone counting the long-lived tokens in their training pipelines. Identity specialists will find the fundamentals familiar; the value is in mapping them onto ML roles and service accounts.

## Related Conf42 talks

- [Who Is Calling Your Model? Identity and Authorization for AI Agents and ML Pipelines](https://www.conf42.com/MLOps_2026_Bhavik_Thakkar_identity_authorization_agents) by Bhavik Thakkar (Okta) extends the non-human identity problem to agents.
- [Identity-Centric Security for AI Systems: IAM as Cybersecurity Infrastructure](https://www.conf42.com/Large_Language_Models_LLMs_2026_Arunkumar_Muthuramalingam_identity_security_iam) by Arunkumar Muthuramalingam (General Reinsurance) makes the case for IAM as core infrastructure.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq (Simplify9) shows least privilege for autonomous callers.

[Watch Neha Asthana's talk](https://www.conf42.com/Machine_Learning_2026_Neha_Asthana_simulation_synthetic_data)

[Watch the talk on YouTube](https://youtu.be/RlyV-J9dAYk).

## Watch the talk

[IAM and Privileged Access Foundations for Secure Enterprise ML Platforms](https://www.conf42.com/Machine_Learning_2026_Neha_Asthana_simulation_synthetic_data) at Conf42 Machine Learning 2026.
