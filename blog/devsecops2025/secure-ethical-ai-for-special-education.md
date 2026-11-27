# Adaptive learning for students with disabilities needs DevSecOps first

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/secure-ethical-ai-for-special-education

In short: Raghav Sai Cheedalla of Meta at Conf42 DevSecOps 2025 on building AI learning pathways for special-needs students that stay private, fair and accessible.

More than 7.5 million US students receive services under the Individuals with Disabilities Education Act, and traditional instruction was never built to adapt to each of them. At Conf42 DevSecOps 2025, Raghav Sai Cheedalla, Senior Software Engineer at Meta, showed how adaptive AI can personalise their learning, and argued that in education the pipeline around the model (security, privacy, accessibility and bias checks) matters as much as the model itself.

His core belief, stated at the start: AI in education has to be secure, transparent and equitable if it is going to change lives.

## Three ways a system adapts

Raghav describes three mechanisms for personalised learning. **Modality adaptation** works out whether a student learns best visually, by ear or another way. **Difficulty calibration** keeps tasks in the student's optimal zone so skills come faster. **Scaffolding intelligence** gives hints, examples and explanations at the right moment and fades them out as mastery grows, which he says reduces learned helplessness and builds confidence.

The outcomes he cites are large: skill acquisition up 41%, engagement up 35%, and reading challenges detected as early as seven months. With accessible design such as screen readers and speech-to-text, he reports close to a 50% increase in independent task completion.

## The threat model is a child's file

The security section is what earns this talk its slot at a DevSecOps event. AI in education carries particular risks: exposure of sensitive student data, model inversion attacks, biased outcomes, spoofing of assistive technology interfaces and insider threats. Those risks, he says, define the guardrails you have to build from day one.

His design rules: meet FERPA and GDPR, encrypt the data, use zero-trust security, and continuously monitor both access and model behaviour, so students never have to trade privacy for personalisation. For the data lifecycle: collect minimally, encrypt thoroughly, get consent, keep logs only for a set period, and let families revoke consent.

## Explainable, audited, and still the teacher's call

Trust, in his framing, needs interpretable models, audits, dashboards for teachers and clear explanations for families, so no decision feels like a black box. Bias in educational AI has real consequences, so he wants diverse training data, fairness metrics, routine audits and inclusive design, all built into the development lifecycle as a continuous responsibility rather than a checkbox.

He is clear that AI should not replace educators. Automating grading and content adaptation frees teachers for the emotional connection, context and individual support that only humans give.

## The pipeline that makes it real

The DevSecOps blueprint is concrete: infrastructure as code, automated security and accessibility testing, model signing and tamper detection, continuous monitoring and feedback-driven iteration. In the ML pipeline he adds secrets scanning, FERPA and GDPR checks, fairness tests for bias and drift, and model behaviour monitoring. Compliance checks for FERPA, GDPR, the ADA and WCAG run directly in CI/CD, so compliance becomes proactive instead of reactive.

One lesson stands out for anyone in a regulated sector: treat accessibility issues as severity one. For this audience, an inaccessible feature is a broken feature.

## Who should watch

Engineers building edtech, health or any product where users are vulnerable and regulated, plus accessibility advocates looking for language that lands with platform teams. The numbers come from the speaker's slides rather than a study he walks through, so treat them as his summary of the field.

## Related talks

- [Operationalizing Predictive Analytics in Education](https://www.conf42.com/DevOps_2026_Venkatesan_Kandavelu_education_mlops_ethics) by Venkatesan Kandavelu, on MLOps for ethical student success.
- [Security and Accessibility can be friends!](https://www.conf42.com/DevOps_2026_Gian_Wild_accessibility_security_inclusion) by Gian Wild.
- Lalitha Potharalanka on [scaling educational AI at the edge](https://www.conf42.com/MLOps_2025_Lalitha_Potharalanka_scaling_educational_ai).

[Watch Raghav Sai Cheedalla's talk](https://www.conf42.com/DevSecOps_2025_Raghav_Sai_Cheedalla_ai_ethics_edu)

[Watch the talk on YouTube](https://youtu.be/5lmBGWbej3o).

## Watch the talk

[AI for Inclusive Education: Secure and Ethical Personalization of Learning Pathways](https://www.conf42.com/DevSecOps_2025_Raghav_Sai_Cheedalla_ai_ethics_edu) at Conf42 DevSecOps 2025.
