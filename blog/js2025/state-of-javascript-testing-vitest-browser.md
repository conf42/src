# JavaScript testing is heading back to the real browser

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/state-of-javascript-testing-vitest-browser

In short: Daniel Afonso of PagerDuty at Conf42 JavaScript 2025 on the state of JS testing, from Vitest browser mode and MSW to Playwright and AI.

Ten years ago we ran component tests in a real browser with Karma and Jasmine, hated how flaky they were, and fled to jsdom. At Conf42 JavaScript 2025, Daniel Afonso, developer advocate at PagerDuty, argued that the industry is now walking back into the browser, this time with tools that make it bearable, and laid out the rest of the 2025 JavaScript testing picture on the way.

Daniel is on the SolidJS DX team and wrote a book on React Query, so he speaks as someone who writes and migrates a lot of tests. He grounds the talk in two sources: the State of JS survey (mocking is the top pain point; overall testing happiness sits at 2.5 out of 4) and an informal poll of eight friends about how their companies actually test.

## Eight companies, eight definitions of "unit"

The friend poll is the most relatable section. Jest plus React Testing Library dominates unit and integration work; Cypress or Playwright handle end-to-end; Storybook shows up as a component catalogue; one team still runs Karma and Jasmine; one writes BDD tests in Gherkin. Only one person counted static analysis (TypeScript and ESLint) as part of testing, and one team has a tidy migration rule: new tests in Testing Library, old Enzyme tests get migrated whenever someone touches them.

Daniel's diagnosis is what he calls the backend fallacy. Testing Library's user-centric philosophy removed implementation details from front-end tests, so the backend definitions of unit and integration stopped fitting, and every organisation he has met now draws the lines differently.

## jsdom pretends to be a browser and ends up neither

The core of the talk is the test-runner story. Jest's TypeScript and ESM support are still experimental, and wiring it to Webpack is configuration pain. Vitest fixed that by sharing the bundler with your app. Then Artem Zakharchenko, creator of Mock Service Worker, wrote a post arguing that jsdom runs in Node and fakes browser APIs, and that the closer the test environment is to production, the more the test is worth. His recommendation: Vitest browser mode.

Daniel migrated and lists what changed: `queryBy` and `findBy` became `getBy`, the `waitFor` wrappers went away because browser mode retries assertions automatically, MSW switched to its service worker mode, tests went async, and mocks for things like localStorage were deleted because the real API is there. The cost was two to three seconds of extra runtime, which he happily pays. Testing Library's own author later wrote that he was glad to see people uninstalling it, because Playwright and Vitest had absorbed its ideas natively.

## End-to-end tools want to be the whole suite

Playwright is winning adoption with cross-browser support, codegen, tracing and free parallelism. Daniel's sharper observation is that end-to-end tools, and Storybook, now all offer visual, component, API and accessibility testing, so his updated testing trophy has static analysis at the base, then unit, then component and end-to-end, with visual and accessibility testing across the top. MSW, meanwhile, has become the default for network mocking across REST, GraphQL and WebSocket, in the browser, Node and React Native.

## AI speeds you up but won't close your knowledge gap

On AI, he is pragmatic. Copilots speed you up, but check their output, especially on newer patterns like browser mode. Playwright's MCP server can explore a site and generate a test. Natural-language test tools such as Midscene get close to self-healing tests (a moved logout button no longer fails the run), at the cost of speed, and vision models like UI-TARS take terser prompts than text-only models working from the DOM.

## Who should watch

Front-end teams still on Jest with jsdom, anyone deciding between Cypress and Playwright, and leads who need a map of 2025 testing tools to justify a migration. It is a survey talk, so depth varies, but the browser-mode migration checklist alone saves an afternoon.

## Related Conf42 talks

- [Gil Zilberfeld on Playwright automation](https://www.conf42.com/JavaScript_2024_Gil_Zilberfeld_26_playwright_automation_testing) at Conf42 JavaScript 2024.
- [Rob Richardson on confidence with Cypress tests](https://www.conf42.com/JavaScript_2022_Rob_Richardson_confidence_cypress_tests) at Conf42 JavaScript 2022.
- [Mike Morgan on strategies for flaky tests](https://www.conf42.com/DevOps_2025_Mike_Morgan_testing_flaky_strategies) at Conf42 DevOps 2025.

[Watch Daniel Afonso's talk](https://www.conf42.com/JavaScript_2025_Daniel_Afonso_state_testing_tech), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/CRzEAv1GzSI).

## Watch the talk

[The 2025 State of JavaScript Testing](https://www.conf42.com/JavaScript_2025_Daniel_Afonso_state_testing_tech) at Conf42 JavaScript 2025.
