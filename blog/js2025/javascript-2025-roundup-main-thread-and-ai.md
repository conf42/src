# Conf42 JavaScript 2025 - give the main thread a break, give the AI the docs

Conf42 Blog, 2025-10-31. https://www.conf42.com/blog/js2025/javascript-2025-roundup-main-thread-and-ai

In short: Conf42 JavaScript 2025 in review, 25 talks on scheduler.yield(), testing pain, accessible JS, web games, docs-as-context for AI and privacy in the browser.

[Conf42 JavaScript 2025](https://www.conf42.com/js2025) streamed on October 30, 2025 with 25 talks, and the programme split neatly in two. Half was about the browser itself: a main thread that needs to breathe, tests that still hurt, forms that still lock people out. The other half was about JavaScript as the glue around AI, from docs wired into the IDE to NLP running client-side. Speakers came from PagerDuty, Cloudinary, Playtech, Microsoft, Meta, Apple, Nike, ADP, UBS and the game studio Hology.

## The main thread is a shared resource

[Aleksandr Tkachenko](https://www.conf42.com/JavaScript_2025_Aleksandr_Tkachenko_let_browser_take) (Playtech) gave the most immediately useful talk of the day on `scheduler.yield()`, part of the new Prioritized Task Scheduling API. You call it inside a long task and the browser gets to handle the clicks and keystrokes that piled up, then resumes your code where it left off, which helps Interaction to Next Paint. He is upfront that the API is experimental and not in every browser yet, and spends time on the imperfect alternatives you can use in the meantime. Think of it as a polite `await` for the main thread.

[Deepika Annam](https://www.conf42.com/JavaScript_2025_Deepika_Annam_revolutionizing_performance_intelligent) (Nike) covered optimisation techniques across Node.js backends and React frontends, and [Lakshmi Bhargavi Mullapudi](https://www.conf42.com/JavaScript_2025_Lakshmi_Bhargavi_Mullapudi_real_time_engineering) (Techstar Group) looked at the architectures behind real-time systems for fraud detection and personalisation.

## Testing still hurts, and the survey says where

[Daniel Afonso](https://www.conf42.com/JavaScript_2025_Daniel_Afonso_state_testing_tech) (PagerDuty) built his state of JavaScript testing around the State of JS survey. Mocking came out as the number one pain point, ahead of configuration, performance, the ESM versus CommonJS mess, excessive complexity and flakiness, and satisfaction with testing sat at 2.5 out of 4. From there he traced a decade of change in test runners, testing libraries, mocking and production practices, and where AI-based tools fit. Come for the history, stay for the honest scorecard.

## Accessibility is a JavaScript problem with JavaScript fixes

Two talks argued that accessible front ends are mostly a matter of knowing the rules. [Gian Wild](https://www.conf42.com/JavaScript_2025_Gian_Wild_accessible_easier_than) (AccessibilityOz) gave concrete code examples, the three types of JavaScript functionality, and ten principles for accessible JavaScript and forms, starting from the fact that around twenty percent of people have a disability. [Anisat Ahmed](https://www.conf42.com/JavaScript_2025_Anisat_Ahmed_introduction_aria_guide) delivered a good first talk on ARIA, cutting a confusing set of attributes down to how to use them well.

## Docs are the context your AI is missing

[Sharon Yelenik](https://www.conf42.com/JavaScript_2025_Sharon_Yelenik_ai_docs_accuracy) (Cloudinary) worked on turning Cloudinary's APIs into MCP servers and came away convinced that the thing holding AI back in the IDE is the context it gets as much as its accuracy. Her talk shows what happens when documentation is connected directly to the LLM client in the editor, with examples across Cloudinary, Auth0 and Firebase. It is one of the more grounded takes on agentic coding from the docs side of the house.

Agents showed up elsewhere too. [Jyoti Kunal Shah](https://www.conf42.com/JavaScript_2025_Jyoti_Kunal_Shah_agentic_autonomous_micro) (ADP) proposed an agentic framework that co-evolves React micro-frontends with the microservices behind them, [Ajitha Buvanachandran](https://www.conf42.com/JavaScript_2025_Ajitha_Buvanachandran_agentic_search_multi) built multi-agent search that decomposes queries, and [Linga Annela](https://www.conf42.com/JavaScript_2025_Linga_Annela_micro_frontends_fast) used Module Federation micro frontends to ship AI features without touching the monolith. [Ujjwala Modepalli](https://www.conf42.com/JavaScript_2025_Ujjwala_Modepalli_client_side_nlp) (Wells Fargo) kept the text analytics in the browser with Natural.js and TensorFlow.js, no backend required.

## Securing the stack from npm to the VM

[Srinivasa Rao Gunda](https://www.conf42.com/JavaScript_2025_Srinivasa_Rao_Gunda_securing_framework_frontend) (UBS) laid out a vulnerability management framework for full-stack JavaScript, from npm dependencies to DOM-based attacks. [Vivekananda Chittireddy](https://www.conf42.com/JavaScript_2025_Vivekananda_Chittireddy_privacy_design_building) (Meta) brought privacy by design to JavaScript data systems with differential privacy, anonymisation and encryption. [Rehana Sultana Khan](https://www.conf42.com/JavaScript_2025_Rehana_Sultana_Khan_rate_limiting_cost) (Versa Networks) built adaptive, AI-driven API rate limiting, and [Priyadarshni Shanmugavadivelu](https://www.conf42.com/JavaScript_2025_Priyadarshni_Shanmugavadivelu_scaling_trust_security) (Microsoft) went below the runtime to confidential computing, Trusted Launch and zero trust for VMs.

## And yes, games

[Annie Tsai and Adam Ringhede](https://www.conf42.com/JavaScript_2025_Annie_Tsai_Adam_Ringhede_level_why_typescript) (Hology) made the case for TypeScript and JavaScript as game development languages. Web game platforms such as Poki reach players in over 100 countries, Discord activities put games where people already hang out, and the genre range has stretched from puzzle and cozy games to racing and FPS. A long way from playing Flash games and hiding the browser from your parents.

## Where to watch

All 25 talks are on the [event page](https://www.conf42.com/js2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCSMU1ZoGrRWPFA6oD7KG3X). Start with Tkachenko if your INP is red and with Afonso if your mocks are.
