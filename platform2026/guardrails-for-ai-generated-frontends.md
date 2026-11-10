# Put frontend standards in the platform, not in the prompt

Conf42 Blog, 2026-10-26, updated 2026-11-09. https://www.conf42.com/platform2026/guardrails-for-ai-generated-frontends

In short: Niharika P Pujari (McGraw Hill) at Conf42 Platform Engineering 2026 on guardrails for AI-generated frontends with design systems, Storybook, Playwright, axe-core and CI.

A generated dialog can look perfect in the browser and still lose keyboard focus the moment it closes. At Conf42 Platform Engineering 2026, Niharika P Pujari, Lead Software Engineer at McGraw Hill working across frontend architecture, accessibility and software quality, argued that AI-generated frontend code shouldn't get its own, looser path: the standards we expect from humans should live in components, tests and CI gates that both humans and coding agents run into by default.

Her question is the right one for platform teams: how do you shape the environment so generated code lands closer to the standards in the first place, instead of reviewing it ever harder afterwards?

## Three ways to ask a model for a form

Niharika compares three approaches, using accessibility as the running example.

1. **Generate first.** Ask for a feature and review what comes back. It feels fast because progress is visible, but frontend quality is behavioural. A dialog may render and lose focus; a validation message may show but never be announced; a custom control may duplicate something the design system already solved. The cost moves downstream into QA, accessibility testing or production fixes.
2. **Prompt harder.** Tell the model to use semantic HTML, support keyboard navigation and use the design system. Better than nothing, but every developer and agent has to remember the wording, and prompt templates silently go stale as the design system evolves. In her words, a prompt is still a request, not an enforcement mechanism.
3. **Change the environment.** Make approved components, test utilities, Storybook examples and CI checks part of the architecture. Instead of asking for an accessible modal, give the model a modal component that already handles focus and keyboard behaviour.

Her rule of thumb for what to encode: if a requirement is stable, repeatable and important enough that you'd reject a pull request over it, look for the part of it that can be automated.

## Defence in depth for the frontend

She describes the guardrails as a stack where no single layer has to be perfect. Composition steers code toward approved components; she calls a mature design system a policy engine expressed as reusable code, with APIs that make the common case easy. Storybook makes forgotten states (errors, loading, empty, focus, responsive layouts) part of the component contract, and doubles as better context for an AI assistant than bare TypeScript types. Playwright checks real flows: tab through the form, open the dialog, close it with Escape, get focus back where it belongs. axe-core catches structural, rule-based issues. CI turns all of it into a delivery rule.

Two craft notes stand out. Test user outcomes (the error is announced, focus moves correctly) rather than DOM structure, so the implementation can change. And make failures actionable: a gate that just says the accessibility check failed is bureaucracy, while one that names the rule and the element is help.

## Honest about the limits

Niharika is careful with claims. Architectural guardrails cost upfront platform investment and maintenance; they pay off for standards that recur across teams, less so for a one-off experiment. An automated scan is one layer of evidence, not proof of accessibility: tools can tell you a control has no name, not whether the name is right or whether a screen reader user can finish the task. Manual and assistive-technology testing still matter.

Her starting point needs no new programme: look at recurring PR comments, accessibility bugs and patterns teams keep reinventing, and move one stable expectation into a component, a Playwright helper or a CI check. Over time the platform becomes a memory system for engineering lessons, which matters more when agents multiply whatever patterns they find.

## Who should watch

Frontend leads and design-system owners whose teams already use coding assistants, and accessibility advocates looking for an argument platform teams will buy. It's conceptual rather than a live build, with the tooling named and the trade-offs spelled out.

## Related Conf42 talks

- [Automated Web Accessibility testing with playwright.js and axe-core](https://www.conf42.com/JavaScript_2023_Taslan_A_Graham_web_accessibility_testing_playwrightjs_axecore) by Taslan A. Graham (CradleApps)
- [Design Tokens as Platform Infrastructure: Architecting Scalable Multi-Platform Design Systems](https://www.conf42.com/Platform_Engineering_2025_Pallav_Laskar_design_tokens_multi) by Pallav Laskar (Zscaler)
- [The Fifth Golden Signal: Making Accessibility Observable](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) by Victoria Nduka (VictoriaMetrics)

[Watch Niharika's talk](https://www.conf42.com/Platform_Engineering_2026_Niharika_P_Pujari_guardrails_frontends_generated)

[Watch the talk on YouTube](https://youtu.be/mxH0y1bG4FM).

## Watch the talk

[Building Guardrails for AI-Generated Frontends: A Platform Engineering Approach](https://www.conf42.com/Platform_Engineering_2026_Niharika_P_Pujari_guardrails_frontends_generated) at Conf42 Platform Engineering 2026.
