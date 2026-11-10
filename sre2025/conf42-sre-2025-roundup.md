# Conf42 SRE 2025: postmortems, pit stops and SLOs over alerts

Conf42 Blog, 2025-04-18. https://www.conf42.com/sre2025/conf42-sre-2025-roundup

In short: Conf42 SRE 2025 roundup - postmortem lessons from reality TV and Formula 1, SLOs against alert fatigue, databases without DBAs, and AI in incident response.

Conf42 Site Reliability Engineering (SRE) 2025 ran online on April 17, 2025, with 107 talks, one of the largest lineups Conf42 has run. With that many sessions, the tracks covered almost everything that can page you: observability, SLOs, resilience, databases, cloud, fintech, healthcare, and a growing pile of AI. The talks worth starting with, though, were the ones about people: how teams review incidents, decide what deserves an alert, and stay curious about their systems.

Every session is on the [Conf42 SRE 2025 event page](https://www.conf42.com/sre2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCu4WV3_Ve7-ChGVhr_-DbU). Below is a guided path through it.

## Incident reviews, from unexpected teachers

[Paige Cruz](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Paige_Cruz_what_real_housewives), Principal Developer Advocate at Chronosphere, gave the most quotable title of the event: what The Real Housewives taught her about postmortem meetings. Bringing "receipts" and holding "the meeting before the meeting" turn out to be useful habits for structured, blame-aware incident reviews. It is funnier than most postmortems and more useful than most postmortem templates.

[Ricardo Castro](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Ricardo_Castro_what_can_we), Principal Engineer and SRE at FanDuel, found his teacher in Formula 1: the race where Red Bull Racing repaired Max Verstappen's car in Hungary and turned a potential disaster into a podium finish. The talk pulls out the incident management lessons that apply when your outage has no pit wall.

[Saurabh Phaltane](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Saurabh_Phaltane_curious_sre_cultivating), a Senior SRE at Google, argued for curiosity as the core SRE skill, balancing breadth and depth and thinking about the system as a whole. [Shaalmali Raychaudhury](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Shaalmali_Raychaudhury_navigating_sre_incident) of PayPal and [Pradeep Gaddamidi](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Pradeep_Gaddamidi_deployments_downtime_unexpected) added practitioner stories about incident management and deploy-day fires.

## Alert on what users feel

[Mandi Walls](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue), DevOps Advocate at PagerDuty, took on alert fatigue with SLOs: metrics centred on the user experience give teams a focus, and give them permission to disable alerts that contribute nothing to customer happiness. [Siddharth Joshi](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Siddharth_Joshi_reliability_excellence_slo) of Nagarro covered the tooling side of SLO management, and [Gaurav Mittal](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Gaurav_Mittal_slos_failute_prediction) of Nordstrom went beyond SLOs to anomaly detection, finding the signals hidden in your data before they become outages.

[Veliswa Boya](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Veliswa_Boya_application_resilience_whose), Senior Developer Advocate at AWS, asked whose job application resilience is anyway, and how resilience and innovation can coexist through both culture and technical choices. [Sai Sahiti Nemalikanti](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sai_Sahiti_Nemalikanti_designing_failure_using) of AWS followed with patterns for designing for failure.

## Observability you can actually use

[Alok Ranjan](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Alok_Ranjan_fragmented_logs_unified), an Engineering Manager at Dropbox, told the story of unifying fragmented container logs with open-source tools, along with what it taught him about DevOps culture. [Swapnil Kulkarni](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Swapnil_Kulkarni_observe_or_not) of Kloudfuse reframed the debate: whether to observe is not the question; whether observability solves the right use cases is. [Sai KR Pentaparthi](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sai_KR_Pentaparthi_xray_ebpf_o11y) showed eBPF for network-level visibility in cloud-native systems, and [Mohit Menghnani](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mohit_Menghnani_unlocking_observability_react) of Twilio brought observability to React and Node.js applications.

## Databases without a DBA

[Renato Losio](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Renato_Losio_things_fall_apart), Principal Cloud Architect at Funambol, shared a decade of running managed production databases without DBA expertise, from crashing managed instances to storage costs that grew far faster than planned, plus a warning about trusting benchmarks. [Samuel Baruffi](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Samuel_Baruffi_amazon_aurora_dsql), Principal Global Solutions Architect at AWS, introduced Amazon Aurora DSQL, a serverless distributed SQL database with active-active availability. [Andrei Manakov](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Andrei_Manakov_tradeoffs_distributed_nosql) of ShareChat walked through the real-world CAP trade-offs in distributed NoSQL design.

## Real-time systems with no second chances

Some talks dealt with systems where reliability is not abstract. [Vlad Onetiu](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Vlad_Onetiu_serverless_confluent_kafka) of DataIceberg built a real-time earthquake alert system with Lambda functions and Confluent Kafka that checks for event changes every second and sends SMS and email notifications. [Bhushan Gopala Reddy](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Bhushan_Gopala_Reddy_resilient_health_monitoring) of Aruba Networks engineered Bluetooth Low Energy health monitoring for disaster zones. [Srihari Pakalapati](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Srihari_Pakalapati_ransomware_readiness_backup) of Trader Interactive covered ransomware readiness with immutable backups and automated recovery, and [Payal Godhani](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Payal_Godhani_zero_downtime_ml) of Oracle Cloud Infrastructure applied SRE techniques to zero-downtime ML deployments.

## AI on call

AI was everywhere, and the most practical uses were small. [David Asamu](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_David_Asamu_ai_sre_prometheus_nl), who leads the SRE team at Nomba, started from a wish every on-call engineer has had: "What if you could chat with your monitoring metrics?" The talk shows asking Prometheus questions in natural language instead of writing queries mid-incident. [Smita Verma](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Smita_Verma_alerts_action_building) of Adobe built AI-powered autonomous incident response at scale, and [Rahul Amte](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Rahul_Amte_smarter_failure_testing) of Nivid Technologies combined AI with chaos engineering for smarter failure testing. [Peter De Tender](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Peter_De_Tender_azure_load_testing) of Microsoft kept it grounded with a hands-on tour of Azure Load Testing.

Beyond these, the lineup ran deep into fintech, healthcare, insurance, and manufacturing reliability, with dozens more case studies on the event page.

## Sponsors and what's next

Thanks to diamond sponsor [SREday](https://www.sreday.com/), gold sponsor [Rapydo](https://www.rapydo.io/), the [StarterAI](https://www.starterai.dev/) newsletter, the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners on the event page.

The series continued with [Conf42 SRE 2026](https://www.conf42.com/sre2026) and returns as [Conf42 SRE 2027](https://www.conf42.com/sre2027) on March 4, 2027.
