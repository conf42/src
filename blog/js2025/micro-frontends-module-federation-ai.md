# Ship AI features as micro frontends, not monolith releases

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/micro-frontends-module-federation-ai

In short: Linga Annela at Conf42 JavaScript 2025 on Module Federation, edge-side composition and WebAssembly for adding AI features to large web apps.

Adding a chatbot to a big monolithic front end usually means touching shared code, rerunning the whole regression suite and waiting for the next release train. At Conf42 JavaScript 2025, Linga Annela argued that micro frontends let teams ship AI features (a chatbot, a recommendation widget, a predictive dashboard) as independent units with their own stack and schedule, and walked through the techniques that make that practical.

It is an architecture overview rather than a hands-on demo: one pattern per slide, explained at the level you would use to brief a team before a migration.

## Micro frontends are microservices for the browser

Linga's definition is the familiar one: split one big JavaScript app into smaller, independently deployable pieces, each owned by a team or domain, each free to pick React, Vue, Angular or plain JavaScript. The AI angle is that a feature team can put a conversational assistant or a personalisation engine live without touching the core application, and run experiments in isolation. The talk also cites industry figures for faster delivery and A/B testing; it doesn't name the studies, so treat them as directional.

## The toolkit, one technique at a time

- **Module Federation in Webpack 5.** Applications, even ones built with different frameworks, share code at runtime. You expose a component, say the recommendation widget, from one project and consume it in another without rebuilding or redeploying, and share common dependencies like React to keep bundles down.
- **Edge-side composition.** Instead of assembling micro frontends in the browser, the CDN stitches together only the pieces each route needs, which helps time to interactive and lets each piece cache independently.
- **WebAssembly for inference.** Compile models from TensorFlow or PyTorch to WebAssembly and run predictions, image classification or sentiment analysis on the client, with no server round trip and sensitive data staying on the device.
- **API patterns.** Plain REST endpoints owned by each micro frontend, so teams can update models independently, or GraphQL Federation, where each micro frontend contributes a subgraph to one typed schema.

## State is the hard part

Linga flags state management as the most important piece of distributed front ends. The layered approach in the talk: keep state local to each micro frontend where possible, use custom events or a lightweight shared store for what must be shared, and use optimistic rendering so the UI stays consistent when AI features are loaded or swapped at runtime. Anyone who has watched two micro frontends disagree about who the logged-in user is will appreciate the emphasis.

Performance comes next: lazy-load components on demand, share common dependencies instead of duplicating them, cache API responses and predictions in service workers, and deploy to edge runtimes.

## Start with one widget

The roadmap is sensible and modest. Find where the monolith blocks AI work, draw boundaries around business domains, set up Module Federation with shared dependencies and pipelines, then ship one small AI feature, like a chatbot or analytics widget, as a proof of concept before scaling. Linga mentions applying the approach to an e-commerce project with customer, admin and driver apps, still in progress at the time of the talk.

## Who should watch

Front-end leads with a large single-page app and a queue of AI feature requests, and architects weighing micro frontends for team autonomy. If your app is small and one team owns it, the coordination problem this solves may not exist for you yet.

## Related Conf42 talks

- [Saravana Balaji Srinivasan of Red Hat on platform freedom with micro frontends](https://www.conf42.com/JavaScript_2022_Saravana_Balaji_Srinivasan_platform_freedom_microfrontends) at Conf42 JavaScript 2022.
- [Maksim Zemskov of Yandex on scaling an application without micro frontends](https://www.conf42.com/JavaScript_2023_Maksim_Zemskov_glorious_monolith_scaling_application_microfrontends) at Conf42 JavaScript 2023.
- [Konstantinos Leimonis of Bit.dev on web bundling with Rspack](https://www.conf42.com/JavaScript_2024_Konstantinos_Leimonis_34_rspack_bundling_webdevelopment) at Conf42 JavaScript 2024.

[Watch Linga Annela's talk](https://www.conf42.com/JavaScript_2025_Linga_Annela_micro_frontends_fast), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/-rhxpBNeH2o).

## Watch the talk

[JavaScript Micro Frontends: Fast-Track AI Integration for Modern Web Apps](https://www.conf42.com/JavaScript_2025_Linga_Annela_micro_frontends_fast) at Conf42 JavaScript 2025.
