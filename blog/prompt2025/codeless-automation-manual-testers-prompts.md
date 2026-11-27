# Manual testers already write prompts; codeless tools make them run

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/codeless-automation-manual-testers-prompts

In short: Balraj Govindaraj of MVP Plus Consulting at Conf42 Prompt Engineering 2025 on a four-phase plan to move manual testers to codeless, prompt-driven automation.

A good bug report is already a prompt. At Conf42 Prompt Engineering 2025, Balraj Govindaraj, QA architect and IT Specialist Expert at MVP Plus Consulting, argued that manual testers can become automation contributors through codeless platforms and natural-language prompts, and laid out a four-phase framework for getting a QA team there without throwing away its domain knowledge.

## The widening gap

Balraj starts with the job market. Postings ask for automation skills, and script-based tools such as Selenium and Cypress remain out of reach for many testers who do not code. The people with the deepest product knowledge get sidelined just as AI-driven development and fast CI/CD raise the bar for feedback speed and coverage.

He names three traditional barriers: coding prerequisites (Java, Python, JavaScript), complex frameworks that shift focus from what to test to how to code the test, and the maintenance tax of scripts that break with every UI change.

## Plain language as the test spec

The bridge, in his telling, is prompt engineering. Testers have spent years writing test cases and bug reports in precise natural language, and codeless platforms with AI features can now execute that kind of text. His examples are close to what a tester would write anyway: navigate to checkout and confirm the total matches the cart; find the submit button in the login form even if its ID or class changes between releases; confirm an error message appears when the email format is invalid and that it includes helpful guidance.

The locator example is the quiet win. Self-healing locators described in words cut the maintenance burden that sinks so many Selenium suites, because the test describes intent instead of a CSS path.

## Four phases

Balraj's framework:

1. **Platform evaluation.** Choose tools with native prompt-driven test generation, visual workflow builders that mirror how testers think, integrations with Jira, CI/CD and test management, self-healing, and team features such as version control and shared libraries. Avoid tools that merely hide code or need heavy scripting for advanced cases.
2. **Knowledge transfer.** Present visual workflows as an extension of manual test cases, teach prompt basics with simple examples first, give testers a sandbox environment, and celebrate early wins publicly.
3. **Standardisation.** Build prompt libraries for common flows (login, form validation, data checks), test templates for regression, smoke and integration suites, and quality guidelines for naming and review.
4. **Scaling.** Run the tests in CI/CD on commits and pull requests, expand from critical journeys to edge cases, and track execution time, pass rates, maintenance effort and time to feedback.

## The examples

He illustrates each phase with team stories. A financial services QA team generated 120 login and dashboard tests from plain English prompts in a week. A government QA team converted 50 manual UI flows into visual workflows. One team kept a central prompt library in Confluence covering 12 microservices, so one improved prompt updated every linked test. On an insurance modernisation project, suites ran from GitHub Actions and Azure DevOps pipelines on every commit, and within three sprints 80% of regression checks ran automatically. Another team started with a handful of critical flows (registration, payments, reports) and used prompt-based generation to reach more than 45 edge scenarios.

## The objections, answered

Will AI replace testers? Balraj says no: it supports judgment but cannot replicate the critical thinking and context experienced testers bring. Are codeless tools strong enough? He points to API testing, database validation and conditional logic. Vendor lock-in? Pick platforms with export and open integrations. His summary is that encoding tester knowledge into reusable prompts turns tribal wisdom into documentation that survives turnover.

## Who should watch

QA leads with strong manual testers and a mandate to automate, and engineering managers deciding whether to retrain or replace. Test automation engineers who live in code will find the tooling advice generic, but the change-management plan is worth borrowing.

## Related Conf42 talks

- [Ludovico Besana on prompt engineering for test automation](https://www.conf42.com/Prompt_Engineering_2024_Ludovico_Besana_promptengineering_automation_quality) at Conf42 Prompt Engineering 2024.
- [Tim Spann on codeless generative AI pipelines](https://www.conf42.com/Prompt_Engineering_2024_Tim_Spann_codeless_ai_automation), codeless thinking applied to data flows.
- [Vitali Shchur on the QA ownership mindset](https://www.conf42.com/Chaos_Engineering_2025_Vitali_Shchur_qa_mindset_startup) at Conf42 Chaos Engineering 2025.

[Watch Balraj Govindaraj's talk](https://www.conf42.com/Prompt_Engineering_2025_Balraj_Govindaraj_testing_automation_agile), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/fDGvgGjekDk).

## Watch the talk

[From Manual Testing to Prompt Mastery: How Codeless Automation and AI Prompts Empower Testers in Agile Transformation](https://www.conf42.com/Prompt_Engineering_2025_Balraj_Govindaraj_testing_automation_agile) at Conf42 Prompt Engineering 2025.
