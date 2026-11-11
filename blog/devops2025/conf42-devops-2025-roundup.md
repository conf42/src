# Conf42 DevOps 2025: caches, flaky tests, Terraform and culture

Conf42 Blog, 2025-01-24. https://www.conf42.com/blog/devops2025/conf42-devops-2025-roundup

In short: Conf42 DevOps 2025 roundup - scaling Sofascore with caching, frugal serverless, flaky tests, Terraform supply chain risk, incident response and LLMs in CI/CD.

Conf42 DevOps 2025 ran online on January 23, 2025, with 58 talks, and it opened the year with a reassuringly practical mix. Yes, LLMs showed up in CI pipelines and Kubernetes troubleshooting. But the talks that stuck were about the fundamentals: caching done right, bills kept small, tests that stop flaking, supply chains that do not hand over your cloud, and people who still have to respond when the pager goes off.

Every session is on the [Conf42 DevOps 2025 event page](https://www.conf42.com/devops2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCdGhBCZtLYRLD9MT4ddCES).

## Scale is mostly boring, and that's good

[Josip Stuhli](https://www.conf42.com/DevOps_2025_Josip_Stuhli_scaling_users_performance), CTO of Sofascore, gave the kind of scaling talk that makes you want to look at your own cache config. In the talk he puts Sofascore at more than 28 million monthly active users and 400 billion requests a month, with a peak of 1.6 million requests per second. The early fix for servers falling over at peaks was a full-page memcache, which then hit the classic cache stampede: a missing key, thousands of users asking for it at once, and every request going straight to the database. The talk walks through the fix and other low-hanging fruit that is often overlooked.

[Yan Cui](https://www.conf42.com/DevOps_2025_Yan_Cui_serverless_saving_tips) of Lumigo, an AWS Serverless Hero who has worked on AWS since 2010, brought a fire hose of money-saving tips for serverless, starting with the one everyone should do on day one: set up billing alarms. They lag by a few hours, but finding out hours late beats finding out when the bill arrives.

Gold sponsor Rapydo tackled the database side. [Matan Nataf](https://www.conf42.com/DevOps_2025_Matan_Nataf_db_ops_rapydo), co-founder and CEO of Rapydo, explained why per-instance tools fail for fleets of MySQL and Postgres databases, and demoed throttling a runaway query that kept coming back after it was killed.

## Tests you can trust

Testing got a lot of airtime. [Mike Morgan](https://www.conf42.com/DevOps_2025_Mike_Morgan_testing_flaky_strategies) of Buildkite covered how to identify, isolate, and eliminate flaky tests before they erode trust in the pipeline. [Mesut Durukal](https://www.conf42.com/DevOps_2025_Mesut_Durukal_agile_automation_test) of Indeed asked whether test automation is a silver bullet (it isn't) and listed the common pitfalls. Analog Devices sent three DevOps engineers with hardware-flavoured problems: [Bianca Popu](https://www.conf42.com/DevOps_2025_Bianca_Popu_github_infrastructure_testing) on securely wiring public GitHub repositories to private Jenkins test infrastructure, [Stefan Raus](https://www.conf42.com/DevOps_2025_Stefan_Raus_arm_fpga_testing) on test harnesses for ARM and FPGA-based systems, and [Andreea Andrisan](https://www.conf42.com/DevOps_2025_Andreea_Andrisan_linux_distro_release) on the release strategy for a custom Linux distribution.

## Your supply chain has root access

[Uri Aronovici](https://www.conf42.com/DevOps_2025_Uri_Aronovici_cloud_terraform_hack), co-founder and CTO of ZEST Security, showed how widely used open-source Terraform providers and modules can be abused to take full control of a cloud production environment, with two attack flows and mitigation practices. If your modules are pinned to whatever latest happened to be, watch this one first.

The security track continued with [Josh Hankins](https://www.conf42.com/DevOps_2025_Josh_Hankins_devsecops_program_start) of CBTS on starting a DevSecOps program from scratch, [Krishna Chaitanya Rudraraju](https://www.conf42.com/DevOps_2025_Krishna_Chaitanya_Rudraraju_threat_modeling_developers) of Microsoft on threat modelling inside DevOps pipelines, [Hariharan Ragothaman](https://www.conf42.com/DevOps_2025_Hariharan_Ragothaman_deployments_governance_securely) of athenahealth on unifying deployments for governance, and [Sheshananda Reddy Kandula](https://www.conf42.com/DevOps_2025_Sheshananda_Reddy_Kandula_mobile_security_automation) of Adobe on automating mobile security assessments with MobSF and Jenkins.

## When it breaks anyway

PagerDuty brought two talks on the human side of operations. [Daniel Afonso](https://www.conf42.com/DevOps_2025_Daniel_Afonso_incident_response_effective) shared lessons for effective incident response under the banner "Don't Panic!", and [Mandi Walls](https://www.conf42.com/DevOps_2025_Mandi_Walls_culture_challenges_devops) argued that culture is still the challenge: when the only tool a team controls is its tooling, every problem looks like a tooling problem.

Observability had its say too. [Dave McAllister](https://www.conf42.com/DevOps_2025_Dave_McAllister_nginx_metrics_monitor) of NGINX walked through 15 NGINX metrics from the application layer down to the host, [Amir Krayden](https://www.conf42.com/DevOps_2025_Amir_Krayden_kubernetes_blind_spots) of Senser combined topology with existing observability to find Kubernetes blind spots, [Shyam Sreevalsan](https://www.conf42.com/DevOps_2025_Shyam_Sreevalsan_observability_future_years) of Netdata sketched the next ten years of observability, and [Pradeep Gaddamidi](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring) of Evernote shared how a budget-tight team built open-source monitoring and logging.

## LLMs join the pipeline

AI talks were plentiful and mostly grounded. [Rajeshwari Ganesan and Chidambaram Ganapathy Sundaram](https://www.conf42.com/DevOps_2025_Rajeshwari_Ganesan_Chidambaram_Ganapathy_Sundaram_devsecops_automation_systems) of Infosys built a multi-agent LLM system to resolve build failures across more than 100 internal applications. [Kosseila Haddalene](https://www.conf42.com/DevOps_2025_Kosseila_Haddalene_kubernetes_ai_troubleshooting) of cloudthrill demoed K8sGPT for troubleshooting managed clusters including Oracle OKE, with OpenAI, Cohere, or Ollama behind it. [Nirhoshan Sivaroopan](https://www.conf42.com/DevOps_2025_Nirhoshan_Sivaroopan_ai_accuracy_trust) of WSO2 covered accuracy evaluation for RAG systems, and [Praveen Payili](https://www.conf42.com/DevOps_2025_Praveen_Payili_ai_data_enterprise) presented AskDataAI, an agent for enterprise data access.

## People, code and the rest

Some of the most-shared talks were not technical at all. [Pawel Zajaczkowski](https://www.conf42.com/DevOps_2025_Pawel_Zajaczkowski_tech_impostor_syndrome) of Xebia tackled impostor syndrome, and [Tomasz Manugiewicz](https://www.conf42.com/DevOps_2025_Tomasz_Manugiewicz_engineers_power_quiet) of evoke made the case for the quiet engineers whose contributions get missed in extrovert-dominated teams. [Muhammad Ahsan Ayaz](https://www.conf42.com/DevOps_2025_Muhammad_Ahsan_Ayaz_angular_refactoring_projects) of Scania told the story of refactoring a sprawling estate of Angular projects and what went wrong, [Denis Ermakov](https://www.conf42.com/DevOps_2025_Denis_Ermakov_coding_sustainable_development) of Techflow argued that less is more in code, [Tiago Barbosa](https://www.conf42.com/DevOps_2025_Tiago_Barbosa_api_development_software) of Rely.io made the case for API-first development, and [Caio Medeiros Pinto](https://www.conf42.com/DevOps_2025_Caio_Medeiros_Pinto_environment_products_innovation) of Citi pitched environments as a service.

## Sponsors and what's next

Thanks to gold sponsor [Rapydo](https://www.rapydo.io/), the [StarterAI](https://www.starterai.dev/) newsletter, the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners on the event page.

The series continued with [Conf42 DevOps 2026](https://www.conf42.com/devops2026) and returns as [Conf42 DevOps 2027](https://www.conf42.com/devops2027) on January 21, 2027.
