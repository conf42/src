# AI coding tools for fullstack work: hand over the work, keep the judgment

Conf42 Blog, 2026-08-30, updated 2026-11-09. https://www.conf42.com/blog/agents2026/transfer-the-workload-not-the-judgment

In short: Kabir Ibraheem of Meltwater at Conf42 AI Agents 2026 walks one to-do form through Claude, Copilot and Cursor, with context, plans and tests owned by the engineer.

The fastest way to lose an afternoon with an AI coding tool is to let it spend ten minutes writing a feature and then spend an hour fixing it. At Conf42 AI Agents 2026, Kabir Ibraheem, a software engineer at Meltwater, argued that fullstack engineers should hand the tools the workload while keeping the judgment, and showed what that looks like on one deliberately boring feature: a form that saves a to-do item.

This is an introductory, practical talk. No model training, no benchmark charts. It is about the day-to-day workflow with Claude, GitHub Copilot and Cursor, and about not becoming what Kabir calls a problem debugger instead of a problem solver.

## The architect and the builder

His central analogy is an architect and a builder. The architect knows what needs to be built and designs it; the builder pours the slab where the drawing says. The architect still walks the site. Kabir maps that onto AI-assisted development: you hold the full context of the problem, the tool does the lifting, and you check in on the work.

That leads to a clean split. Delegate the things these tools are good at: explaining unfamiliar code (to you and to the tool itself), proposing implementations, and hunting for edge cases and their duplicates across the codebase. Own the rest: confirming requirements, judging whether a proposal fits the architecture you already have, and verifying that the result is safe and ready to ship.

## Do the thinking before you open the tool

Most of the talk happens before any code gets generated. For the to-do form, Kabir works through the questions that used to be the job anyway. Why are we saving this data, and does that mean a table or a JSON blob? Is it auto-save, save on click or save on focus? Does the logic live in services, controllers or utility functions? What are the passing criteria? For this feature: validate the title, save for the logged-in user, handle failures gracefully.

Where does the saved time go? Into that preparation, so that the thirty-minute task stays thirty minutes instead of quietly turning into five hours.

## Pick the tool per job, and stop wishing at it

His tool map is opinionated and simple. Cursor for getting from a design to the first skeleton of the UI. Claude for backend changes, reading files and running commands in context. Copilot for in-editor autocomplete. The problem picks the tool, not the other way round. When a colleague announces the next great tool over coffee, the answer is that it's a tool, not the solution; be a problem solver, not a tool chaser.

Two concrete habits stand out:

- **Persistent context in a CLAUDE.md file.** Follow existing route patterns, reuse UI components, ask before adding dependencies (both for bundle size and for the risk of pulling in something malicious), keep changes small enough to review, run tests and type checks, and check in before patching lint or build failures in unrelated code.
- **Plan first, then approve.** Instead of asking for a task API that saves to the database, ask the tool to inspect the existing task routes and validations, plan a create-task endpoint, reuse current dependencies, list the files and tests it will touch, and wait. Engineers, he notes, are often guilty of talking to agents like they are making a wish.

## Tests should argue with the code

Borrowing from TDD, Kabir wants the generated tests to challenge the generated implementation against the requirements written at the start, not merely to pass. The review then checks three things: correctness, maintainability and safety. Those three are a reasonable checklist for any PR that contains AI-written code.

## Who should watch

Fullstack and product engineers who use AI assistants daily but feel the review and rework eat the gains, and team leads looking for a shared, low-ceremony workflow to write down. Experienced users of agentic coding tools will find the material familiar; the value is in how plainly it is laid out around a single feature.

## Related Conf42 talks

- [Beyond AI Coding: The New Bottlenecks of Software Delivery](https://www.conf42.com/Platform_Engineering_2026_Lucas_Mateus_Mazei_Sobrinho_delivery_bottlenecks_coding) by Lucas Mateus Mazei Sobrinho at Conf42 Platform Engineering 2026.
- [Verification Timing: Why Checking AI-Written Code at the Gate Is Already Too Late](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates) by Yunhao Jiao at Conf42 DevSecOps 2026.
- [Three Hours Debugging Code I Never Wrote](https://www.conf42.com/Observability_2026_Artemis_Leonardou_debugging_agents_codegeneration) by Artemis Leonardou at Conf42 Observability 2026.

[Watch Kabir Ibraheem's talk](https://www.conf42.com/AI_Agents_2026_Kabir_Ibraheem_fullstack_tooling_productivity) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/yKjWTlMAdYM).

## Watch the talk

[Riding the AI wave as a fullstack engineer](https://www.conf42.com/AI_Agents_2026_Kabir_Ibraheem_fullstack_tooling_productivity) at Conf42 AI Agents 2026.
