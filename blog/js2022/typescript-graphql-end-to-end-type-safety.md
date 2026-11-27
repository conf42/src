# Generate your TypeScript types from the GraphQL schema

Conf42 Blog, 2022-11-16. https://www.conf42.com/blog/js2022/typescript-graphql-end-to-end-type-safety

In short: Roy Derks (StepZen) at Conf42 JavaScript 2022 on end-to-end type safety by generating TypeScript types and hooks from a GraphQL schema

If your API already has a type system, writing TypeScript types for it by hand is duplicated work waiting to drift. At Conf42 JavaScript 2022, Roy Derks of StepZen showed how to treat the GraphQL schema as the single source of truth and generate TypeScript types, and even React hooks, from it with GraphQL Code Generator. He calls the result the holy grail of full-stack development: end-to-end type safety.

It's an introductory talk that assumes you may know neither language, and it builds up to one focused demo.

## What is a date, anyway?

Roy opens with a riddle. A date is a calendar day, a dried fruit, the word date spelled in dried fruit, and a romantic scene from a Disney film. In JavaScript it can be a Date object, a string, a timestamp or some other object entirely. That versatility is why JavaScript is error-prone, and why the undefined errors in your console are the kind of thing a type system catches at build time instead of in a user's browser.

## TypeScript and GraphQL in a nutshell

TypeScript is a typed superset of JavaScript: everything JavaScript has, plus static type checking, compiled down to plain JavaScript because browsers can't parse TypeScript. Give a function a typed input, and the compiler can infer its output, such as an array of strings.

GraphQL is a query language for APIs, not a framework, and it isn't tied to JavaScript. It has three operation types: query, mutation and subscription. "So how graphql works, you get only the data you ask for and only this data," Roy Derks said at Conf42 JavaScript 2022, before comparing it to the Spice Girls (tell GraphQL what you want, what you really, really want). It serves many resources from a single endpoint, and its schema makes the API self-documenting in a GraphQL playground.

His example of the single-endpoint benefit uses the Twitter REST API, wrapped as GraphQL with StepZen. Search for tweets containing Einstein, and the REST response lacks the author's name, so you'd need a second request. With the nested author relationship in GraphQL, it's one request.

## The two type systems are nearly twins

Put a Product type side by side in both languages and they look alike: id, title, thumbnail, price, categories, reviews. The differences are worth knowing:

- **Numbers.** GraphQL has Int and Float; TypeScript just has number.
- **Lists.** Both use square brackets for a list of a related type, such as categories.
- **Nullability.** In TypeScript everything is required by default; in GraphQL everything is optional by default, so one type can serve different clients and screens.

## Let the schema write the types

Typing those by hand means updating TypeScript every time someone changes the API, possibly without telling you. GraphQL Code Generator, an open source CLI, introspects the API, reads the schema and your operations, and writes TypeScript types: a Scalars mapping for ID, String, Boolean, Int and Float, plus every object type and relationship. An integer ID in the API is always a number in your app.

The demo runs against a GraphQL wrapper around the DEV (dev.to) REST API, with pagination and article queries. With the typescript-react-apollo plugin, one npx graphql-codegen run against a codegen.yml config produces a file of type definitions and ready-made Apollo hooks for the query, including a lazy variant. A small lesson in the demo: an unnamed operation produces an unnamed query hook, so name your operations. Add a field to the query, such as description, rerun the generator and the types follow. Because it's a CLI, it slots into any build pipeline.

## How not to migrate to TypeScript

Roy's closing anecdote will feel familiar. The first time he moved a project to TypeScript, he renamed all the files at once and everything imploded. His advice: migrate gradually, a few files at a time, keeping the rest in JavaScript until they're type safe. If you already use GraphQL, generating the types makes that faster.

## Who should watch

Front-end and full-stack developers who use GraphQL and still hand-write interfaces, and JavaScript teams weighing TypeScript. If you already run GraphQL Code Generator in CI, you'll know most of this.

More on types and API contracts at Conf42: [Austin Gil on TypeScript checking with JSDoc](https://www.conf42.com/JavaScript_2022_Austin_Gil_jsdocs_typescript) and [Serhii Bilyk on safer TypeScript](https://www.conf42.com/JavaScript_2022_Serhii_Bilyk_safer_typescript), both from the same event, and [Joe Wingard on auto-provisioned REST, GraphQL and gRPC](https://www.conf42.com/JavaScript_2021_Joe_Wingard_Autoprovisioned_REST_GraphQL_gRPC) at JavaScript 2021.

[Watch Roy Derks's talk](https://www.conf42.com/JavaScript_2022_Roy_Derks_web_apps_future_typescript_graphql) from [Conf42 JavaScript 2022](https://www.conf42.com/js2022).

## From StepZen

Roy describes StepZen as a company that makes it easy to build GraphQL APIs, with a CLI-first tool. In the talk he uses it to turn an existing REST API, Twitter's search API, into GraphQL without prior knowledge of building GraphQL servers, including nested relationships such as a tweet's author.

- StepZen: [stepzen.com](https://stepzen.com/)

[Watch the talk on YouTube](https://youtu.be/437uNCsnG5c).

## Watch the talk

[Web applications of the future with TypeScript and GraphQL](https://www.conf42.com/JavaScript_2022_Roy_Derks_web_apps_future_typescript_graphql) at Conf42 JavaScript 2022.
