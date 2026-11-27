# Voice biometrics can retire the date-of-birth check in healthcare

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/voice-biometrics-replace-date-of-birth-checks

In short: Sreenivasul Reddy Meegada at Conf42 Incident Management 2025 on replacing knowledge-based checks in healthcare with voice biometrics, and its limits.

If your security question is a date of birth and a zip code, an attacker with a search engine already knows the answer. At Conf42 Incident Management 2025, Sreenivasul Reddy Meegada, a technical lead and solutions architect, made the case for voice biometrics as the replacement for knowledge-based authentication in healthcare, with a frank list of where it breaks.

## Why attackers love healthcare records

He opens with the economics. On the black market, he said, a credit card record goes for around $5 while a healthcare record goes for around $250. That gap explains why healthcare is a favourite target, and why weak, password-based and knowledge-based authentication is a liability rather than a nuisance.

Healthcare also adds its own twist. Clinicians work under pressure with access to life-and-death information, and in an emergency a slow login is a clinical problem, not a UX complaint. Get authentication wrong in the other direction and you get medical identity theft, which can lead to incorrect treatment, insurance fraud and altered records.

## What a voiceprint actually measures

The useful explainer in the middle covers what a voiceprint is. Part of it is physiological: everyone's vocal tract produces a distinctive signature. Part of it is behavioural: pronunciation, rhythm and intonation patterns built up over years of speaking. Systems combine features such as fundamental frequency and spectral distribution with machine learning to build the print, which is why, in his telling, false accepts stay low and simple impersonation does not get far. He also notes systems can distinguish a live human from an automated playback.

The applications he lists are concrete: staff access control, fraud prevention on insurance claims, and authentication in the contact centre, where callers no longer need to recite member numbers and birthdays. The abstract points to real deployments built on NICE and Omilia.

## The results, and the honest caveats

Citing a recent survey of clinical deployments, he reports an 83% reduction in authentication time and a 67% reduction in support requests, most of which were authentication problems in the first place. Fewer "I can't log in" calls is an incident-reduction story in its own right.

Then the part many vendor decks skip. Background noise causes mismatches. People sound different when they are ill or emotional. Licensing, training and workflow disruption cost real money. Privacy rules (HIPAA, GDPR and others) apply to biometric data, so privacy and security teams belong in the strategy discussion from day one. And you have to pick a match threshold: accept only high-confidence matches, or allow medium ones, depending on the business requirement.

## How to roll it out without a new incident class

His deployment advice is conservative in a good way. Do a pre-rollout assessment with site surveys, infrastructure audits and user interviews. Keep multimodal fallback: when voice fails, drop back to knowledge-based authentication without blocking the clinician or the member. Pilot with one department, tune, then expand in phases. Check whether the vendor supports enrolment from historical recordings, so returning callers do not have to enrol again, and how well it integrates with your IVR and CRM.

On compliance he highlights a quieter benefit: voice authentication creates non-repudiable records of who accessed what, which supports HIPAA audit logging and fine-grained, least-privilege access.

## Who should watch

Security architects and contact-centre platform owners in healthcare and insurance weighing biometrics, and anyone running an identity verification flow that still asks for a birthday. It is a strategy and rollout talk, not a demo of a specific product.

## Related Conf42 talks

- [Building Voice AI for People Who Don't Trust AI](https://www.conf42.com/Large_Language_Models_LLMs_2026_Pavel_Shchekotov_voice_ai_trust) by Pavel Shchekotov, on the trust problem from the user's side of the call.
- [Agile Transformation for Scalable Healthcare IT in Regulated AI Era](https://www.conf42.com/Large_Language_Models_LLMs_2026_ShubhaPriya_Muthuramalingam_healthcare_agile_regulation) by ShubhaPriya Muthuramalingam, for shipping change inside healthcare regulation.

[Watch Sreenivasul Reddy Meegada's talk](https://www.conf42.com/Incident_Management_2025_Sreenivasul_Reddy_Meegada_healthcare_biometrics_security)

[Watch the talk on YouTube](https://youtu.be/uxGHNubWqFE).

## Watch the talk

[Voice Biometrics in Healthcare: Securing Systems and Streamlining Workflows](https://www.conf42.com/Incident_Management_2025_Sreenivasul_Reddy_Meegada_healthcare_biometrics_security) at Conf42 Incident Management 2025.
