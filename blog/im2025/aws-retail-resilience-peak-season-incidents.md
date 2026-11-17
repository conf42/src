# Retail incident response on AWS, built for the Thanksgiving spike

Conf42 Blog, 2025-09-10, updated 2026-11-09. https://www.conf42.com/blog/im2025/aws-retail-resilience-peak-season-incidents

In short: Mahesh Yadlapati (Haliburton) at Conf42 Incident Management 2025 on using AWS forecasting, Lambda remediation and DR drills to keep retail sites up at peak.

Retail outages don't stay internal for long: a checkout that falls over on Thanksgiving is on social media before the pager finishes ringing. At Conf42 Incident Management 2025, Mahesh Yadlapati, Senior DevOps Engineer at Haliburton, made the case for cloud-native incident response in retail, with AWS as the toolkit, and argued that the goal is customer experience during the bad moment, not just uptime.

This is an introductory, AWS-centric talk. It spends its first half on why cloud beats traditional data centres for this job and its second on which AWS services fill which role, sprinkled with a few incidents from his own work.

## Think like the customer, then size for the holiday

Yadlapati's starting point is that retailers should judge incidents by what the shopper sees: customer experience, revenue lost during peak periods, and brand reputation once complaints go public. He then compares traditional IT with cloud across infrastructure, scalability, recovery, monitoring and cost.

The core argument is about peaks. On-premises, you size for the holiday season and carry that hardware all year. In the cloud, autoscaling and elastic load balancing run normal capacity most of the time and scale up when traffic arrives. The same logic applies to recovery: rather than a duplicate physical DR site, you replicate across regions and fail over with tools like AWS Elastic Disaster Recovery. He mentions once recovering from DR within minutes, which is what sold him on the approach.

## Forecast the spike, automate the fix

On the AWS side, three services do most of the customer-facing work in his design:

- **Amazon Forecast** looks at previous years' data to predict how much traffic a holiday will bring, so you can scale ahead of it, manually or by automation.
- **Amazon Personalize** keeps recommendations working as a fallback when primary systems are degraded.
- **Amazon Connect** routes customer inquiries during incidents so support quality holds up under pressure.

Underneath, CloudWatch watches infrastructure and applications, alerting application owners for app issues and invoking Lambda for infrastructure ones. His example: in a pool of four servers, one runs hot on CPU and memory. Lambda either adds a server to share the load or spins up a replacement and removes the sick one, and health checks keep traffic away from it in the meantime. He also lists X-Ray and OpenTelemetry for tracing, Rekognition for watching visual content for anomalies and IoT Core for in-store devices.

## Small incidents teach the most

The most relatable story is not about a region failing. After the team installed new antivirus software, monitoring flagged abnormal CPU spikes across servers. They traced it to the antivirus, uninstalled it and switched to one that used less CPU. Monitoring that knows what normal looks like catches the change you made yourself, which is where a lot of incidents come from.

## Practise the failover

His best-practice list is short and sensible. Design for failure, with graceful degradation that keeps core shopping working when non-essential services break. Automate detection, escalation and first response, keeping humans for complex decisions. Monitor customer-facing metrics, not just technical ones. And practise: run chaos exercises and actually switch to the second region to check it has the data and works. A DR plan you have never exercised is a hypothesis.

## Who should watch

Teams moving retail platforms from on-premises to AWS, and engineers who need a map of which managed services cover which part of incident response. If you already run multi-region active-active with automated failover, most of this will be familiar; the customer-first framing is still worth the time.

## Related Conf42 talks

- [Proactive Incident Management: Leveraging Forecasting Models to Enhance Retail Operational Resilience](https://www.conf42.com/Incident_Management_2024_Sijo_Valayakkad_Manikandan_43_forecasting_retail_resilience) by Sijo Valayakkad Manikandan goes deeper on the forecasting side.
- [Securing the Future: How AIOps Drives Operational Resilience on AWS](https://www.conf42.com/DevSecOps_2024_Indika_Wimalasuriya_aiops_resilience_aws) by Indika Wimalasuriya adds the AIOps layer on AWS.
- [Disaster Recovery preparedness using Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness) by Kyle Shelton shows how to drill the failover.

[Watch Mahesh Yadlapati's talk](https://www.conf42.com/Incident_Management_2025_Mahesh_Yadlapati_retail_aws_resilience)

[Watch the talk on YouTube](https://youtu.be/Kq57GRRKGM0).

## Watch the talk

[Cloud-Powered Retail Resilience: How AWS Drives Customer-Centric Incident Response](https://www.conf42.com/Incident_Management_2025_Mahesh_Yadlapati_retail_aws_resilience) at Conf42 Incident Management 2025.
