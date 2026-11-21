# Put AI inside the platform loop, and keep a rollback for the model

Conf42 Blog, 2025-08-12, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-in-the-platform-loop-for-ci-cd

In short: Praveen Kumar Guguloth at Conf42 Platform Engineering 2025 on AI-driven platforms, four architecture patterns, guardrails and gradual adoption for CI/CD.

Monitoring that tells you what broke is useful; a platform that scales before the Black Friday spike is better. At Conf42 Platform Engineering 2025, Praveen Kumar Guguloth, a VP of engineering in financial technology with over 14 years in IT, argued that AI should move from a tool developers use to a layer inside the platform itself, closing the loop between observing and acting.

It is a short, strategic talk. The abstract leads with headline results (47% faster CI/CD across 150+ enterprises); the talk itself spends its time on patterns and guardrails rather than walking through those numbers, so treat them as the framing, not the content.

## Complexity beyond human scale

Praveen's diagnosis: traditional platforms rely on manual configuration, monitoring explains failures after the fact, and developers spend more time debugging infrastructure than writing features. With hundreds of interacting microservices, no human team can model all the relationships intuitively. That is the opening for AI: spotting patterns humans miss and automating routine pain.

He describes AI as a closed optimisation loop. Observe system data in real time, learn from history, act proactively (scale before the traffic arrives, rebalance before the bottleneck, adapt to business criticality), and get smarter with every cycle.

## Four architecture patterns

The core of the talk is four patterns:

- **Federated AI models** keep decisions close to where the action is and avoid a central bottleneck.
- **AI orchestration layers** act as the platform's brain, seeing the whole system and making optimisations no single service could.
- **Event-driven intelligence** responds to context in real time, for example triggering auto-healing on a predicted anomaly instead of on downtime.
- **Edge-based processing** pushes AI into the developer workflow for faster code review and CI/CD feedback.

His two domain examples show different priorities. In e-commerce it is about surviving peak days: pre-emptive scaling, prioritising critical fixes, rolling back a bad release automatically. In finance it is continuous compliance auditing, secure provisioning and predictive risk detection, where intelligence is about avoiding catastrophic mistakes as much as speed.

## Guardrails before autonomy

The best section is the least glamorous. Praveen insists on progressive adoption: start with service meshes that learn anomaly patterns, then add automated performance tuning gradually, then developer-workflow assistants. Build trust in the algorithms and with the engineers who rely on them.

He wants AI-driven systems to avoid becoming black boxes: careful data pipelines, rigorous model deployment workflows, and the ability to roll back a model just like application code. Security covers the models too, since they can be poisoned, and regulation demands explainability. If the platform denies a transaction or reconfigures resources, someone must be able to say why. Without those guardrails, in his framing, AI becomes a liability.

He closes looking ahead to largely self-adjusting platforms, which he compares to a self-driving car for infrastructure.

## Who should watch

Engineering leaders building a roadmap for AI in their platform, and SREs who want a vocabulary for where predictive automation fits. Hands-on engineers looking for implementation detail will want to pair it with something more concrete.

## Related Conf42 talks

- [Chinmay Gaikwad on enterprise-ready CI/CD pipelines with agentic AI](https://www.conf42.com/DevOps_2026_Chinmay_Gaikwad_cicd_agentic_ai) is the hands-on version.
- [Debosmit Ray on a GitOps and automation approach to developer platforms](https://www.conf42.com/DevOps_2024_Debosmit_Ray_gitops_automation_efficient_platforms) covers the declarative foundation AI would sit on.

[Watch Praveen Kumar Guguloth's talk](https://www.conf42.com/Platform_Engineering_2025_Praveen_Kumar_Guguloth_faster_experience_developer)

[Watch the talk on YouTube](https://youtu.be/d64FWTdsC08).

## Watch the talk

[AI-Driven Platform Engineering: 47% Faster CI/CD & Developer Experience](https://www.conf42.com/Platform_Engineering_2025_Praveen_Kumar_Guguloth_faster_experience_developer) at Conf42 Platform Engineering 2025.
