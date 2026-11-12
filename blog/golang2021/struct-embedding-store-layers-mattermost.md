# Mattermost's database store is an onion of embedded Go structs

Conf42 Blog, 2021-06-23. https://www.conf42.com/blog/golang2021/struct-embedding-store-layers-mattermost

In short: Jesus Espino (Mattermost) at Conf42 Golang 2021 on stacking cache, retry, search and timer layers over one store interface with struct embedding

Mattermost wanted a cache in front of its database layer without a single line of cache invalidation leaking into the SQL code. At Conf42 Golang 2021, Jesus Espino, Full Stack Engineer at Mattermost, explains how they got there: drop a hand-rolled middleware chain, wrap one big store interface in layers built with Go struct embedding, and let code generators write the boring layers for you.

It's a design talk drawn from a real, open-source codebase (the Mattermost server's store directory), so every pattern in it is something you can go and read.

## Why did the middleware chain go?

Mattermost's app layer knows nothing about SQL. It talks to a `Store` interface made of sub-stores (teams, channels, posts, users, bots, audits and so on), and the SQL store implements every method.

The first cache attempt used a classic middleware pattern: a layered store with its own supplier interface, chain-next methods and hints passed down from the app layer. Conceptually familiar, and the hints let the app layer tell the cache what to do. In practice it was hard to follow, and adding a new cache meant touching the cache layer, the SQL layer and the layered store, which made it error-prone. The hints, the one clever feature, went mostly unused.

## A layer that embeds a store is a store

The replacement uses struct embedding. A `LocalCacheStore` embeds `store.Store`, so with zero methods of its own it already satisfies the interface. You override only what the cache cares about. A cached `Get` on the team store checks the cache, falls through to the embedded store on a miss, and caches the result if there's no error. Everything else passes straight through.

Adding a cache became a matter of overriding a method in one place. The catch is the one every Go developer meets eventually: embedding is not inheritance. When a call falls through to the embedded struct, that method runs in the embedded struct's context and knows nothing about the outer one, so if it calls another method you overrode, it calls its own version.

"So you need to understand that well and how embedding works to not end up having weird bugs that are really hard to debug," Jesus Espino said at Conf42 Golang 2021.

The other cost is that every layer shares one homogeneous interface, so per-layer extras like cache hints would mean widening the whole store interface.

## Once you have layers, everything wants to be one

The cache layer turned out to be a general mechanism. Jesus lists what came next: instrumentation, tracing, logging, storage and query delegation, extra validation, and error handling.

- **Timer layer.** Wraps every store method, times it and records a Prometheus histogram labelled by method and success. In Grafana that shows both the slow method called rarely and the fast method called millions of times, and lets the team alert when a method gets, say, 10% slower after an upgrade.
- **OpenTracing layer.** The same shape, emitting spans. It's optional and usually off because of its performance cost. They generated an interface for the app layer too, so tracing reaches there without touching business code.
- **Retry layer.** Mattermost wanted the Serializable isolation level, where concurrent transactions fail with repeatable errors that simply need re-running. The layer retries those and gives up after three consecutive failures. It also absorbs the occasional deadlock victim instead of bouncing an error up to the API.
- **Search layer.** Written by hand: saves go to SQL and then update the Elasticsearch or Bleve index; searches try each enabled engine in turn and fall back to database full-text search unless that's disabled.

The final onion is built in a few lines: SQL store, wrapped in retry, local cache, search, then timer. Because every wrapper is a store, you can reorder them. Move the timer directly above the SQL store and you measure the database alone, not the cache hits.

## Let the generator write the identical methods

Writing a timer wrapper for every method of every sub-store is exactly the code nobody should write by hand. Mattermost parses the store interface with Go's AST package into a struct of sub-stores, methods, parameters and results, feeds that into one template per layer (timer, OpenTracing, retry), and runs the output through `go/format` rather than trying to emit perfectly formatted code. Change the store, run make generate, and all three layers are up to date.

"It's not easy to understand, but once you write this has been working really well for a long time without almost any maintenance," Jesus Espino said at Conf42 Golang 2021, about the timer template.

## Who should watch?

Go developers with a large interface and a growing list of cross-cutting concerns: caching, metrics, tracing, retries. If you've ever pasted the same timing code into forty methods, this is the talk. Newer Gophers get a clear explanation of why embedding is not inheritance, with a production bug class to go with it.

More from Conf42 Golang: [Jesus Espino dissecting slices, maps and channels](https://www.conf42.com/Golang_2022_Jesus_Espino_dissecting_slices_maps_channels) the following year, [Francisco Daines on enforcing architecture rules with arch-go](https://www.conf42.com/Golang_2021_Francisco_Daines_archgo_architecture_tooling_test_guidelines_automation), and [Ilia Sergunin on transactions and the repository pattern](https://www.conf42.com/Golang_2023_Ilia_Sergunin_transaction_management_repository_pattern).

[Watch Jesus Espino's talk](https://www.conf42.com/Golang_2021_Jesus_Espino_struct_embedding_instrumentation_code_generation) from [Conf42 Golang 2021](https://www.conf42.com/golang2021).

## From Mattermost

Mattermost is an open-source communication platform with a Go backend and a TypeScript and React frontend, available self-hosted or in the cloud. The store layers from the talk live in the store directory of the mattermost-server repository on GitHub.

- Mattermost: [mattermost.com](https://mattermost.com/)
- Source: [github.com/mattermost/mattermost-server](https://github.com/mattermost/mattermost-server)

[Watch the talk on YouTube](https://youtu.be/Y-URSLmIPIg).

## Watch the talk

[Struct Embedding, Instrumentation and Code Generation](https://www.conf42.com/Golang_2021_Jesus_Espino_struct_embedding_instrumentation_code_generation) at Conf42 Golang 2021.
