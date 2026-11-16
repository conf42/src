# Hallucinations are a symptom; missing context in the IDE is the bug

Conf42 Blog, 2025-10-01, updated 2026-11-09. https://www.conf42.com/blog/js2025/docs-context-ai-ide-cloudinary

In short: Sharon Yelenik of Cloudinary at Conf42 JavaScript 2025 on MCP servers, indexed docs, Context7 and rules files that make AI coding in the IDE accurate.

Your AI assistant does not hallucinate because it is dim. It guesses because nobody told it your project's rules. That is the core claim Sharon Yelenik, senior developer experience and API content writer at Cloudinary, made at Conf42 JavaScript 2025, and she backed it with a step-by-step setup that feeds documentation straight into the LLM client inside the IDE.

Sharon spent the previous year on a large Cloudinary team turning the company's APIs into Model Context Protocol (MCP) servers. The talk is what that work taught her about documentation accuracy, with Cloudinary as the worked example and Cursor as the IDE. The same recipe applies to Auth0, Firebase, Supabase, Slack, Shopify and other APIs she lists at the end.

## Two jobs for the AI in your editor

She splits IDE AI into two use cases. The familiar one is code generation and refactoring. The second is agentic work: uploading assets, configuring environments, the backend chores you normally leave the editor to do. MCP servers handle the authentication, validation and execution so the agent can act on your behalf without you switching to a web console.

The motivation is trust. Sharon cites survey data that only 3.8% of developers report both low hallucination and high confidence, and that agent adoption is still a minority. Her reading: hallucinations are not the root problem, they are a symptom. The model does not know your architecture, your naming conventions or the documented rules of the product you are calling, so it guesses, and every bad guess erodes the team's willingness to use it.

## Four layers of context

The practical core is four habits, each demoed in Cursor:

- **Add the vendor's MCP servers.** She pastes Cloudinary's remote MCP server config into Cursor's tools settings, authenticates once per server, and the tools light up.
- **Index the docs site.** Cursor's docs indexing takes the documentation URL; then you attach those docs as context on each request.
- **Use Context7.** Its MCP server indexes the code snippets and examples from API docs, so generated code comes from documented examples, not guesses. Not every product is indexed yet, and she suggests asking vendors for it.
- **Write rules files.** MDC files in Cursor, with equivalents in JetBrains and VS Code. Some APIs ship them already; Cloudinary has one explaining transformation parameter order and invalid combinations.

## Rules files: compatibility, conventions, constraints, canon

Her mnemonic for writing your own rules is four Cs: compatibility notes (what plays well together), conventions (naming, folders, architecture), constraints (what the AI must never do, such as exposing secrets or calling admin APIs from the browser) and canon (short correct snippets to copy). Keep them one to three pages, review them often, link the official docs.

Her Cloudinary examples are refreshingly specific: always apply automatic format and quality, use named transformations for hero images and thumbnails instead of ad hoc ones, and only pair face gravity with automatic cropping because other combinations misbehave. These are exactly the bugs that are tedious to find later.

## The demo closes the loop

The finale runs the whole stack. From inside the IDE she uploads a portrait image to Cloudinary via MCP, asks for a wide hero version (the agent checks for an existing named transformation, finds one that does not match, creates a new one and wires the URL into the page), adds a text overlay that follows her rules file's font and placement standard, and crops a face-centred thumbnail that comes back with the right parameters. The thumbnail is a bit big, which she notes honestly: no rule said otherwise.

## Who should watch

JavaScript developers and team leads trying to get colleagues to trust AI coding, and anyone writing docs for an API that agents will consume. It shows Cloudinary's own MCP servers, so it is partly a vendor walkthrough, but the habits transfer to any well-documented API. If you already run curated rules and MCP tools daily, the four Cs checklist is the part worth stealing.

## Related Conf42 talks

- [Nishant Kumar Thakur and Sonam Raj of Adobe on context engineering for MCP tool-calling](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) at Conf42 Prompt Engineering 2026.
- [Austin Gil on JSDoc and TypeScript](https://www.conf42.com/JavaScript_2022_Austin_Gil_jsdocs_typescript) at Conf42 JavaScript 2022.
- [Alex Shershebnev of Zencoder on using MCP in DevOps without opening a security hole](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure) at Conf42 DevSecOps 2025.

[Watch Sharon Yelenik's talk](https://www.conf42.com/JavaScript_2025_Sharon_Yelenik_ai_docs_accuracy), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/tiJ8Ve2smkE).

## Watch the talk

[Making Docs and AI Work Together: Improving Context, Accuracy, and Agentic Coding in the IDE](https://www.conf42.com/JavaScript_2025_Sharon_Yelenik_ai_docs_accuracy) at Conf42 JavaScript 2025.
