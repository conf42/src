# When a security bug can delay chemotherapy, DevSecOps is the design

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/devsecops-for-cancer-patient-mobile-app

In short: Mahendar Ramidi at Conf42 DevSecOps 2025 on securing a HIPAA-compliant cancer patient app with zero trust, offline-first encryption and policy as code.

In most apps a security failure is an embarrassing incident. In a symptom tracker for cancer patients it can mean a wrong medication or a missed treatment. At Conf42 DevSecOps 2025, [Mahendar Ramidi](https://www.conf42.com/DevSecOps_2025_Mahendar_Ramidi_health_cloud_scale), a mobile architect in health technology at Maryland Health Benefits Exchange, described how his team applied DevSecOps to My Story, a mobile platform for cancer patients that supports active clinical trials.

According to the abstract, the platform serves 450+ patients across 12 cancer centres with a 92% completion rate. The talk spends its time on the architecture rather than those outcomes, so treat it as a blueprint for regulated mobile apps.

## Why healthcare raises the stakes

Ramidi's starting point is that there's no margin for error. A patient's chemotherapy schedule depends on precise data transmission, clinical trial results depend on data integrity, and the information is deeply personal. He sees three forces. Regulatory complexity: HIPAA sets the baseline, clinical trials add FDA oversight, states add their own rules, and international work brings GDPR. Attractive data: medical records sell for more than credit card numbers because you can't change your medical history. And patient safety, where a security failure can have physical consequences.

Mobile makes it harder. Data moves between personal devices and cloud services, phones join untrusted networks next to other apps with broad permissions, and patients need their information offline, in hospitals with poor reception, while travelling or in rural areas.

## Zero trust, from enrolment to idle timeout

His zero-trust model has four layers. Patients can't just sign up; they're provisioned through a secure enrolment that requires multi-factor authentication with verified health-system credentials. After authentication, the patient's identity is cryptographically bound to their device so stolen credentials alone aren't enough. Biometrics (fingerprint or face) add another factor on enrolled devices. And verification is continuous: short-lived tokens refresh every few minutes, and idle sessions are killed, so the user has to log in again.

Encryption is data-centric. Data is encrypted on the device before it leaves, transmitted with certificate pinning, stored encrypted with hierarchical key management, and decrypted only on authorised devices.

## Offline-first is a security problem

The offline section is the most distinctive part. Full-device encryption is only the baseline; on top of it the app adds application-level encryption with keys derived from patient credentials, plus secure element integration and hardware-protected keys. Because patients edit data offline, sync needs conflict resolution: vector clocks track modification history, operational transformation keeps eventual consistency, and every offline change lands in an audit trail. Anyone who has debugged a mobile sync bug will appreciate doing that under HIPAA.

## Compliance as code and a five-layer pipeline

Ramidi treats regulations as requirements that automation can verify continuously. HIPAA requires encryption at rest and in transit, so the infrastructure code refuses to provision storage or networks without it, and policy-as-code tools check infrastructure against compliance rules before deployment. Try to deploy an unencrypted database and the pipeline rejects it, naming the requirement it would violate.

The CI/CD pipeline has five security layers: static analysis for hard-coded credentials, SQL injection and insecure crypto; dependency scanning that blocks deployment on known vulnerabilities; dynamic testing against running builds for authentication bypass; container image scanning; and API security tests for unauthorised access and rate limits. He names Sonar among the scanners in that pipeline.

## Monitoring and response

Production gets application and infrastructure monitoring, audit log analysis for suspicious patterns in authentication, data access and configuration changes, and behaviour analytics that learn typical patterns for patients and clinicians. His incident response follows detection, containment, eradication, recovery and post-incident analysis. The closing argument: patients trust the app with data that could save their lives, so robust security isn't optional, and it doesn't have to cost the user experience.

## Who should watch

Mobile and backend engineers building regulated health apps, and anyone designing offline-capable apps that handle sensitive data. It's a broad architecture walk-through, not a code demo.

## Related Conf42 talks

- [When Compliance Meets Crisis: Managing Regulatory Incidents in HIPAA, GDPR, and DMA Environments](https://www.conf42.com/Incident_Management_2025_Nisheedh_Raveendran_compliance_hipaa_gdpr) picks up where Ramidi's response framework ends.
- [Go Secure: Building Resilient Telemedicine Platforms](https://www.conf42.com/Golang_2025_Smita_Verma_telemedicine_security_resilience) is another take on securing healthcare platforms.
- [Attacking/Defending Mobile Apps Training](https://www.conf42.com/Chaos_Engineering_2021_Romansh_Yadav_mobile_apps_attack_defend) shows the mobile attacker's side.

[Watch Mahendar Ramidi's talk](https://www.conf42.com/DevSecOps_2025_Mahendar_Ramidi_health_cloud_scale)

[Watch the talk on YouTube](https://youtu.be/Zgdf3Zhfmf8).

## Watch the talk

[Securing Healthcare at Scale: DevSecOps for Critical Patient Platforms](https://www.conf42.com/DevSecOps_2025_Mahendar_Ramidi_health_cloud_scale) at Conf42 DevSecOps 2025.
