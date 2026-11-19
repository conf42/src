# AI in the platform should earn autonomy like a new hire

Conf42 Blog, 2025-08-23, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-platforms-earn-autonomy-like-new-hires

In short: Manoj Kumar Vunnava (GoDaddy) at Conf42 Platform Engineering 2025 on smarter pipelines, predictive ops and ML-driven scaling, rolled out gradually.

You wouldn't give a new team member production admin on day one, so don't give it to your AI either. That's the most practical idea in Manoj Kumar Vunnava's talk at Conf42 Platform Engineering 2025. Manoj, a Senior Telecom Engineer at GoDaddy, walks through where AI and machine learning fit into an internal platform, and argues for introducing them in stages: recommendations first, semi-automation next, full automation last.

## Why the old platform model stopped scaling

Manoj starts with a short history. Platform engineering began as a standard kit of pipelines, deployment scripts and dashboards, and it worked until the estate grew from a few servers to thousands of containers across regions. He names four resulting problems: mental overload from dozens of dashboards and alerts, maintenance overhead that eats the platform team's time, scaling bottlenecks (ten times the traffic can't mean ten times the engineers), and cloud bills growing faster than the business. His analogy is a manual gearbox in rush hour versus a car with adaptive cruise control: you still choose the destination, the system does the tedious work.

## Five places AI earns its keep

He breaks the AI-driven platform into building blocks:

- **Smarter CI/CD.** Pipelines that pick the tests a change actually needs, predict deployment risk, and roll back automatically before customers notice. His kitchen analogy: a chef who knows which steps matter for this dish, instead of running the same ten-step recipe every time.
- **Predictive analysis and incident resolution.** Spotting unusual patterns, doing root cause analysis across logs and metrics faster than a human, filtering alert noise, and applying safe routine fixes such as adding CPU or memory to a struggling process.
- **Automated remediation**, for the fixes that are routine enough to trust.
- **Dynamic resource optimisation.** ML that forecasts demand from past usage and right-sizes capacity instead of overprovisioning "just to be safe". He cites 15 to 30% cloud cost savings reported by companies doing this.
- **Intelligent observability** that feeds all of the above.

## Two case studies, told as scenarios

Manoj illustrates the ideas with two unnamed organisations, presented as illustrative scenarios rather than named customers. A global financial services firm with slow deployments and frequent incidents adds predictive scaling, ML anomaly detection and staged rollouts, and reports 65% faster deployments, 42% fewer production incidents and 22% lower infrastructure cost. A fast-growing e-commerce platform uses AI-assisted self-service configuration and auto-troubleshooting observability so its platform team supports three times the developers without new headcount.

## The rollout is the real content

The implementation advice is where the talk is strongest. Start small with something high-value and low-risk, like test optimisation or autoscaling. Get the data foundation right first, because AI only sees what your logs and metrics show it. Keep humans in the loop at the start: if the system recommends scaling down, an engineer approves it. Architect for modularity (AI as plug-in components, not a rip-and-replace), explainability, manual fallbacks and continuous learning.

He's also candid about the obstacles: data quality, legacy integration, keeping models current, skill gaps and teams worried about losing control. His remedy is upskilling, small pilots and clear communication about what the AI will and won't do.

## Who should watch

Platform leads deciding where to start with AI and wanting a sensible order of operations. If you already run ML-driven autoscaling and AIOps, this is an overview you can skip; if you're pitching it internally, the staged-autonomy argument is worth borrowing.

## Related Conf42 talks

- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz (ilert), on the alert-filtering piece in practice.
- [Securing the Future: How AIOps Drives Operational Resilience on AWS](https://www.conf42.com/DevSecOps_2024_Indika_Wimalasuriya_aiops_resilience_aws) by Indika Wimalasuriya (Virtusa), a cloud-specific AIOps view.

[Watch Manoj Kumar Vunnava's talk](https://www.conf42.com/Platform_Engineering_2025_Manoj_Kumar_Vunnava_transforming_intelligent_experience)

[Watch the talk on YouTube](https://youtu.be/zn5pzTTs9As).

## Watch the talk

[AI-Driven Platform Engineering: Transforming Developer Experience Through Intelligent Infrastructure Automation](https://www.conf42.com/Platform_Engineering_2025_Manoj_Kumar_Vunnava_transforming_intelligent_experience) at Conf42 Platform Engineering 2025.
