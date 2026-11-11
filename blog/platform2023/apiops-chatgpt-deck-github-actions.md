# From an empty folder to a rate-limited API, mostly by asking ChatGPT

Conf42 Blog, 2023-09-07. https://www.conf42.com/blog/platform2023/apiops-chatgpt-deck-github-actions

In short: Rick Spurgeon (Kong) at Conf42 Platform Engineering 2023 on APIOps with ChatGPT, decK and GitHub Actions, from OpenAPI spec to a gateway via pull requests.

APIOps is GitOps for the API layer: the OpenAPI spec is the source of truth, and the gateway configuration is generated from it and shipped through pull requests. At Conf42 Platform Engineering 2023, Rick Spurgeon, Developer Advocate at Kong, demonstrated it end to end, starting from an empty directory, using ChatGPT on the command line to write the service and the spec, and Kong's decK tool in GitHub Actions to carry it to a gateway without ever clicking through the UI.

It's a Kong talk with a Kong product at the end of the pipeline, and mostly a live demo. The workflow shape, though, is portable to any team that wants a spec-driven gateway config with review gates.

## Why does APIOps need to be federated?

Rick's framing: API-first means a textual specification defines the API's behaviour and can generate docs and client and server code. API gateways take care of cross-cutting behaviour such as security and traffic control, so service code doesn't have to. decK bridges the two by generating a declarative Kong Gateway configuration from an OpenAPI spec and syncing it to the gateway.

Simple, until microservices and domain-driven design split the work across many teams. Rick's answer is federated APIOps: development teams self-serve and own their API delivery, while a platform team keeps governance and may own the final deployment to infrastructure. decK supports that with more than generation: transformations, merging, linting and verification, all of which slot into CI/CD stages.

## How much of the service did ChatGPT write?

All of it, in the demo. Rick uses chatblade, a CLI for the ChatGPT API that reads standard input and writes standard output, aliased to a short command. He pipes prompts in and tees the answers into files so he can vet them before running anything. Its last-session flag keeps the conversation going, so each prompt builds on the previous answer.

In sequence: a bash script to initialise a Node.js project, an OpenAPI spec for a hello-world API, a JavaScript service implementing that spec, a Dockerfile, and a script that builds the image and runs it on a named Docker network so the gateway can reach it later.

The limit showed up at the CI layer. Rick bootstrapped the GitHub Actions workflows by hand: "In my experience they're not well trained on these tools and it's also quite difficult to express the question clearly enough to have it generate these for you," Rick Spurgeon said at Conf42 Platform Engineering 2023.

## What does the pipeline look like?

The gateway side is Kong Konnect, Kong's SaaS with a hosted control plane. Rick creates a control plane (a runtime group named hello world) through the Konnect API with a personal access token, runs a Kong Gateway data plane locally in Docker on the same network as the service, and creates a public GitHub repository with the GitHub CLI. Three workflows do the rest:

1. **Convert.** On a push that changes the OpenAPI spec on main, decK converts it into a staged Kong declarative config, then a second APIOps command adds a rate-limiting plugin to every service via a JSONPath selector. The result goes into a pull request for review.
2. **Stage.** Merging that PR triggers a decK diff against the live control plane, which catches any drift in production. The diff output becomes the description of a second PR, the platform team's approval gate.
3. **Deploy.** Merging the second PR runs decK sync, which pushes the config to Konnect, which pushes it down to the gateway.

At the end, Konnect shows a hello world service on port 3000, a route on /hello and the rate-limiting plugin with a five-second window, none of it entered by hand. Requests through the gateway now carry the rate limiting the service itself never implemented. Rick finishes with a quick look at Konnect's traffic analytics across APIs and points at the go-apiops repository in the Kong GitHub organisation, where the APIOps capabilities for decK are being built.

## Who should watch

Platform teams that own an API gateway and want app teams to ship routes and plugins through PRs instead of tickets. It is a demo, so expect setup steps (tokens, repo permissions, secrets) rather than a discussion of how this scales across dozens of teams; the two-PR split between team review and platform approval is the part to steal.

For more on the same layer: [Arlemi Turpault on API-first](https://www.conf42.com/Chaos_Engineering_2022_Arlemi_Turpault_how_to_win_friends_and_influence_people_with_api_first), [Bobur Umurzokov on API gateway plugins](https://www.conf42.com/Observability_2023_Bobur_Umurzokov_api_gateway_plugins), and [Wenchao Xiang on Kong Gateway performance](https://www.conf42.com/DevOps_2024_Wenchao_Xiang_kong_gateway_performance_enhancement).

[Watch Rick Spurgeon's talk](https://www.conf42.com/Platform_Engineering_2023_Rick_Spurgeon_apiops_amplified_ai_rapid_api_delivery) from [Conf42 Platform Engineering 2023](https://www.conf42.com/platform2023).

## From Kong

The talk used decK (Kong's declarative configuration tool), Kong Gateway as the data plane and Kong Konnect as the hosted control plane, with the Konnect APIs for automation.

- Kong: [konghq.com](https://konghq.com/)
- APIOps library for decK: [github.com/Kong/go-apiops](https://github.com/Kong/go-apiops)

[Watch the talk on YouTube](https://youtu.be/rDtTWuSqZrs).

## Watch the talk

[APIOps Amplified: Harnessing AI for Rapid API Delivery](https://www.conf42.com/Platform_Engineering_2023_Rick_Spurgeon_apiops_amplified_ai_rapid_api_delivery) at Conf42 Platform Engineering 2023.
