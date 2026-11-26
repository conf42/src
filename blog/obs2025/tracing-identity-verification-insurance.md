# Trace every step of identity verification, not just the login

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/obs2025/tracing-identity-verification-insurance

In short: Shikha Gurjar of Guidewire Software shows at Conf42 Observability 2025 how tracing, correlation and behavioural baselines make identity checks observable.

A document scan that passes, a selfie match that's slightly off and a database check that's a little inconsistent each look fine on their own. Together they can be a spoofing attempt. At Conf42 Observability 2025, Shikha Gurjar, Technical Project Manager for Essential Services at Guidewire Software and ten years into the property and casualty insurance industry, explained how instrumenting identity verification end to end turns that black box into something teams can see, correlate and act on in real time.

## Identity verification is a distributed system

Gurjar's framing is that a modern identity check is a pipeline of services: biometrics (fingerprint, face or voice), AI analysis of the process, sometimes blockchain for an audit trail, and a lot of third-party calls. Observable identity systems instrument each step, capturing biometric results, response times and error patterns, and feed them into monitoring and alerting so a failed verification or a suspicious login shows up in minutes rather than days.

The talk puts a number on the payoff: an 87% cut in the time it takes to identify a problem. It also credits modern observable systems with catching sophisticated spoofing, fake IDs and deepfakes, at 99.99% accuracy. Those are the speaker's figures for the industry; the talk doesn't break down where they were measured.

## Five spans that tell the whole story

The clearest section is a worked distributed tracing example for an online verification:

1. **Document upload**: how long it took, whether the file arrived, logs on errors.
2. **Document validation**: authenticity, expiry and tamper checks, pass or fail, processing time.
3. **Biometric matching**: the selfie comparison time and the match confidence score.
4. **Data verification**: each external call to government databases or credit bureaus, timed, so third-party delays stand out.
5. **Risk assessment**: how the inputs flowed into the trust score and which rule raised a flag.

With that trace you can tell that biometric matching is consistently the slow step, or that document validation crashes intermittently, before customers notice. It's the same playbook as tracing a checkout flow, applied to a domain where a slow step is also a fraud signal.

## Baselines catch the attacker with the right password

Two techniques sit on top of the traces. Correlation engines link events across steps and learn normal patterns (time taken, device type, match scores), so small deviations get flagged together instead of being dismissed one by one. Behavioural anomaly detection goes further: learn what normal looks like per user or group (login times, devices, locations, upload habits), score each action by how far it strays, and trigger adaptive authentication when the score crosses a threshold. That can mean an OTP, a manual review or blocking the action outright. The point is catching attacks where the credentials are correct.

## Privacy is a design constraint, not a footnote

All this telemetry is sensitive by definition, and Gurjar spends real time on it: collect only what's needed, anonymise or encrypt personal data, be transparent about what's collected, and design for privacy by default. Her roadmap is phased: assess current telemetry and blind spots, instrument the identity workflow, integrate alerts and adaptive responses, then refine the models and baselines. A full rollout takes six to twelve months in her estimate, with benefits visible after two to three if you go incrementally.

## Who should watch

Engineers building onboarding or KYC flows in insurance, banking or anywhere fraud is a cost line, and SREs who already trace payments and want to extend the habit to identity. It's a strategy talk without code. If you only take one thing, take the five-span trace and draw it for your own verification flow.

## Related Conf42 talks

- Sreenivasul Reddy Meegada on [Voice Biometrics in Healthcare: Securing Systems and Streamlining Workflows](https://www.conf42.com/Incident_Management_2025_Sreenivasul_Reddy_Meegada_healthcare_biometrics_security).
- Rahul Ganti on [Building Resilient AI Platforms: Engineering Financial Fraud Detection at Scale](https://www.conf42.com/Platform_Engineering_2025_Rahul_Ganti_fraud_detection_financial).
- Giriprasad Manoharan on [AI and data engineering for fraud detection in banking](https://www.conf42.com/Observability_2024_Giriprasad_Manoharan_ai_fraud_detection).

[Watch Shikha Gurjar's talk](https://www.conf42.com/Observability_2025_Shikha_Gurjar_security_insights_identity)

[Watch the talk on YouTube](https://youtu.be/a2jzoU-zaRo).

## Watch the talk

[From Blind Spots to Insights: How Observable Identity Systems Transform Security and Performance](https://www.conf42.com/Observability_2025_Shikha_Gurjar_security_insights_identity) at Conf42 Observability 2025.
