# Model weights pass every pipeline gate without being read

Conf42 Blog, 2026-09-06, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/model-weights-pass-every-pipeline-gate-unread

In short: Emmy Eide of Realign Labs at Conf42 DevSecOps 2026 walks a model-bearing image through six pipeline gates and shows where "no findings" is mistaken for clean.

A scanner that can't parse an artifact doesn't return an error. It returns zero findings, and zero findings looks exactly like clean. At Conf42 DevSecOps 2026, Emmy Eide, engineering and cybersecurity lead at Realign Labs and formerly director of product security for SDLC and supply chain security at Red Hat, pushed a model-bearing image through a competent pipeline gate by gate and showed which controls go quiet, which answer the wrong question, and which keep working perfectly while meaning less than you think.

It's the clearest framing of the AI supply chain gap you're likely to find, and it's generous to the tooling we already have.

## A missing decision, not a skipped one

Emmy's core point is about what supply chain security is for: turning risk into a decision somebody makes, with a name and a date. When a CVE ships unnoticed, that's a process failure you can fix. Model risk is worse, because there was never a decision point at all. The tooling came back green, and green says no decision is needed. In her words, "Silence isn't the absence of risk in scanners. It's the absence of a decision."

## The assumption nobody wrote down

Everything in modern DevSecOps (scanning, SBOMs, licence checks, even signing) assumes the artifact is code you can read, enumerate and diff. For twenty years identity stood in for behaviour: name the package version and you knew what it would do. Weights break that three ways. Nothing reads a few billion floating point numbers in any CVE-shaped sense. Behaviour comes from training, not reviewable source. And a version no longer pins behaviour, because the output also depends on the prompt, the retrieved context, the tools and sampling.

The more common case is worse still: you don't ship the model, you call one over an API. Then there's no blob to hash and your SBOM can at best point at a URL whose behaviour can change without a rebuild. Emmy is firm that this doesn't move the obligation; under the EU AI Act and GDPR, the deployer or controller still answers for the output.

## Six gates, six different failures

The walk is the heart of the talk:

1. **Dependency scanning** sees an eight-gigabyte file with no package URL or CPE, files it next to fonts and fixtures, and reports nothing. Failure mode: silence.
2. **SBOM generation** produces a valid, beautiful document where the model is one line at best. Incompleteness presented as completeness.
3. **Licence compliance** finds Apache 2.0 and MIT and misses the bespoke community licence and the training-data provenance. True, but the wrong scope.
4. **Signing** keeps working, and you should keep doing it. It proves who built the bytes, and with non-deterministic behaviour you lose the testing that used to cover the rest.
5. **Provenance-based admission** correctly answers "did this come from us?", a question that used to be a usable proxy for behaviour.
6. **Runtime** becomes the only place behaviour can be observed, on a security budget sized for a backstop.

She's fair to the new model scanners too (Checkmarx, HiddenLayer's engine, ModelScan, Fickling): they catch weaponised packages and pickle gadget chains, which is a real attack class. By their own scope statements, they cover the file, not what the model does when it works as intended.

## The G7 SBOM for AI helps, then hands off

The G7's SBOM for AI defines solid minimum elements, but many are links to model cards and prose, and a pipeline gate checks that a link exists, not that it's true. The level of autonomy was considered and left out. More record without more verification renders as more green.

## What to do this quarter

Emmy's asks are concrete. Request an SBOM for AI against the G7 elements and ask which fields are attested versus declared. Read your model scanner's scope statement and find the sentence about what it doesn't cover. Keep signing, but stop letting a green tick read as a safety verdict, and invest in runtime evidence of what the model called, reached and emitted. The afternoon task: point your scanner at a model image and check whether it read the thing at all. The real task: get someone to answer the autonomy question in writing, with a name and a date.

## Who should watch

Supply chain and AppSec engineers who own the scanner dashboard, and anyone signing off releases of AI features. Platform folks running self-hosted open-weight models will get the most out of the gate walk.

## Related Conf42 talks

- [Supply Chain Defense by Default — SBOMs, SLSA, and Provenance in CI/CD](https://www.conf42.com/DevSecOps_2025_Bhaskar_Bharat_Sawant_supply_chain_ci) by Bhaskar Bharat Sawant of Cornerstone Building Brands at Conf42 DevSecOps 2025.
- [RAGged and Compromised: Hacking Retrieval-Augmented Generation Systems](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) by Blaize Stewart of GBLI at Conf42 AI Agents 2026.
- [From Reliable Models to Resilient ML Platforms: Designing Secure, Highly Available Infrastructure for Production Machine Learning](https://www.conf42.com/Machine_Learning_2026_Srinivas_Talasila_compliance_governance_ai) by Srinivas Talasila of SAP at Conf42 Machine Learning 2026.

[Watch Emmy Eide's talk](https://www.conf42.com/DevSecOps_2026_Emmy_Eide_sbom_models_supplychain) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/i1ULxAbM_pE).

## Watch the talk

[Your SBOM Stops at the model](https://www.conf42.com/DevSecOps_2026_Emmy_Eide_sbom_models_supplychain) at Conf42 DevSecOps 2026.
