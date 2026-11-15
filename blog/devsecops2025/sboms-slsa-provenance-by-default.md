# Supply chain security should be the default path in CI, not a checklist

Conf42 Blog, 2025-11-17, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/sboms-slsa-provenance-by-default

In short: Bhaskar Bharat Sawant of Cornerstone Building Brands at Conf42 DevSecOps 2025 on automatic SBOMs, SLSA, provenance and deploy-time verification.

When Log4j hit, one team needed almost a full week just to find the affected services. After they built supply chain defence into their pipeline, a simulated vulnerability event took minutes. At Conf42 DevSecOps 2025, Bhaskar Bharat Sawant, Lead Engineer at Cornerstone Building Brands and an IEEE senior member, explained how automatic SBOMs, SLSA, provenance and deploy-time verification make the secure path the default one.

His stance is practical from the first minute: no theoretical frameworks, no checklist documents nobody reads, and no late-night heroics that depend on someone remembering a manual step.

## CI/CD is trusted most and verified least

Attackers used to aim at SQL injection and cross-site scripting. Now they go upstream, at open-source dependencies, package managers, build systems and artifact repositories. Bhaskar's line about pipelines is pointed: in many organisations CI/CD is the most trusted system and the least verified. His three cautionary tales: SolarWinds was a build system compromise, Log4j was a visibility failure, and the XZ backdoor showed that even long-standing open-source maintainers can become attack vectors. The shared lesson is that you cannot secure a supply chain you cannot see.

## The pieces of defence by default

**SBOMs.** An ingredient list for your application, but only useful if generated automatically on every build and stored with the artifact. Then the Log4j questions (are we affected, where, which versions) have instant answers. He calls them operationally lifesaving rather than paperwork.

**Provenance and attestations.** A chain of custody for each artifact: who built it, when, from which source, with which pipeline, in what environment, with signed attestations as proof. Missing or wrong provenance should make an artifact undeployable, and a system, not a human, should enforce that.

**SLSA as a ladder.** Start where you are: logged builds, then builds from version-controlled scripts, then provenance and signing, eventually hermetic and reproducible builds. He frames it as strengthening each link rather than chasing perfection.

**Hardening controls.** Keyless signing with short-lived CI identities instead of stored private keys, ephemeral runners destroyed after each run, immutable artifacts that cannot be silently swapped, and hermetic builds with no network access that rely on pre-approved pinned components. Reproducible builds mean the same input always gives the same output, so tampering shows up immediately.

**Dependency hygiene.** Pin versions, review new libraries, avoid floating versions and stop automated updates from bypassing review. Dull, and one of the most effective things you can do.

## The before and after

The example team deployed microservices to Kubernetes with a fast but unverified pipeline: developers could push local images to the registry, SBOMs were inconsistent and provenance was not enforced. After adoption, every build was signed automatically, every artifact came with an SBOM, Kubernetes enforced signature verification and dependency metadata was centralised. Security went up and, he stresses, velocity did not drop.

Deployment is the point of no return, so that is where enforcement belongs: a missing signature or provenance means a hard fail, not a warning email. Roll it out in phases: SBOMs first, then signing and provenance in CI, verification in staging, enforcement in production once it is stable.

## The culture shift

His closing argument is about mindset: from "we trust our pipeline" to a pipeline that proves it can be trusted, from hoping dependencies are safe to knowing what you ship, and from security slowing you down to security preventing the emergencies that do.

## Who should watch

Platform and release engineers who own CI/CD and the Kubernetes admission path, and security teams who want a phased SLSA story to bring to developers. If you already enforce signed images at deploy time, the talk is a good sanity check; if you do not, it is a plan.

## Related talks

- [Making Software Bill of Materials (SBOMs) Actionable](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable) by Ciara Carey.
- [Securing the software supply chain: beyond SBOM](https://www.conf42.com/DevSecOps_2023_Marek_Najmajer_Aleksander_Baranowski_beyond_sbom_risk_assessment) by Marek Najmajer and Aleksander Baranowski, on vulnerability risk assessment.
- Emmy Eide's [Your SBOM Stops at the model](https://www.conf42.com/DevSecOps_2026_Emmy_Eide_sbom_models_supplychain), for when the artifact is an ML model.

[Watch Bhaskar Bharat Sawant's talk](https://www.conf42.com/DevSecOps_2025_Bhaskar_Bharat_Sawant_supply_chain_ci)

[Watch the talk on YouTube](https://youtu.be/28OftT0yHhg).

## Watch the talk

[Supply Chain Defense by Default — SBOMs, SLSA, and Provenance in CI/CD](https://www.conf42.com/DevSecOps_2025_Bhaskar_Bharat_Sawant_supply_chain_ci) at Conf42 DevSecOps 2025.
