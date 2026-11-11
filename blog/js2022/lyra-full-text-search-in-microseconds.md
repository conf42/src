# Lyra searches a million movie titles in 41 microseconds, in JavaScript

Conf42 Blog, 2022-11-18. https://www.conf42.com/blog/js2022/lyra-full-text-search-in-microseconds

In short: Michele Riva (NearForm) at Conf42 JavaScript 2022 on Lyra, a dependency-free full-text search engine in TypeScript that runs on every JavaScript runtime

A full-text search engine written in TypeScript can be fast enough to answer in microseconds and small enough to run on an edge worker. At Conf42 JavaScript 2022, Michele Riva, Staff Engineer at NearForm, told the story of Lyra, the open source search engine he built to understand how Elasticsearch works, and showed it deploying to Cloudflare Workers in about five seconds.

## Why rebuild Elasticsearch?

Michele is clear that he loves Elasticsearch; he calls it his favourite open source project. He worked with it, with Solr and with Lucene directly, and on Apache Unomi, a customer data platform built on Elasticsearch that took millions of records a day without search slowing down. He wanted to know how that was possible.

He also lists his gripes, with the caveat that they may have been his own fault: hard to deploy and upgrade, a big memory footprint, heavy CPU use, and costly whether hosted or self-managed. His learning motto is Richard Feynman's: what I cannot create, I do not understand. So he set himself a goal, a talk on how full-text search works, and started building one.

## Rust, then Go, then JavaScript

The language detour is the funniest part. Michele has no degree and learned the algorithms and data structures from scratch. He started in Rust because cool people use Rust, found it wasn't for him, rewrote everything in Go, and then remembered Atwood's Law: any application that can be written in JavaScript will eventually be written in JavaScript.

The JavaScript version couldn't outperform the others but came very close, which led to the lesson he repeats through the talk. "There is no slow programming language, but just bad algorithms in data structure design," Michele Riva said at Conf42 JavaScript 2022. His JavaScript was simply better than his Rust.

## How does Lyra work?

Lyra has no dependencies and targets every JavaScript runtime: Node.js, Deno, Bun, browsers, React Native, AWS Lambda and Lambda@Edge, Cloudflare Workers and Netlify Functions. Everything is implemented from scratch: prefix trees, inverted indexes, B-trees, tree maps, stemming and stop words.

The API is a handful of functions: create, insert, remove and search. Unlike Elasticsearch, it isn't schemaless; you declare a schema, for example an author string and a quote string. Insert is synchronous, and there is an asynchronous batch insert that doesn't block the event loop. Search takes a term and the properties to search, and returns results with a count and the elapsed time.

The elapsed time in his first example is 99, and the unit is microseconds. Four documents is not a benchmark, so he loaded 1 million movie titles from IMDb. A search for believe across all indexes averaged 41 microseconds; criminal minds took 187, because two terms mean two searches and an intersection.

## Stemming in 23 languages

Michele is Italian, so English-only was never going to do. Lyra removes stop words and stems terms, so lucky and luckiest both match luck, unless you ask for exact results. Stemmers for 23 languages come from Snowball, Martin Porter's project, whose published rules make it straightforward to write new ones; he wrote the Italian tests himself. You can plug in your own stemmer, which is just a function that takes a word and returns a word, and add, remove or replace stop words.

## Ship the index, not a cluster

The design goals were to run on any runtime, stay small and fast, and be easy to maintain and deploy, with a hook system and plugins on top. The data persistence plugin serialises an index to disk (MessagePack by default, or JSON) on Node.js and Bun, and another machine restores it into memory and searches immediately.

That enables the architectures he sketches. A React Native app keeps a local index as an offline fallback, refreshed from the server every few minutes. A CI job rebuilds the index on a schedule, drops it in S3, and an SNS notification redeploys Lambdas carrying the in-memory index, with no cluster management or consistency concerns of your own.

The demo uses Nebula, Lyra's build system, then in beta. A YAML file names the schema, the data source (a JSON file of Pokémon), the output bundle and the target, Cloudflare Workers. One deploy command later, a curl for pika returns results from the edge. The edge version came out of a conference conversation in Berlin, where a colleague answered the idea with hold my beer and shipped a basic version the next day.

## Who should watch

JavaScript developers curious about what's inside a search engine, teams who want search without running a cluster, and anyone building for edge runtimes. It's an enthusiastic, story-driven talk; for a full benchmark methodology, look elsewhere.

Pair it with [Yagiz Nizipli on a performant URL parser in Rust and WebAssembly](https://www.conf42.com/JavaScript_2022_Yagiz_Nizipli_performant_url_parser) and [Gaurab Patra and Bhagyajit Jagdev on data analytics in the browser with AlaSQL](https://www.conf42.com/JavaScript_2022_Gaurab_Patra_Bhagyajit_Jagdev_data_analytics_browser_alasqljs), both from the same event, and [Liam Hampton on taking code to the edge](https://www.conf42.com/Golang_2022_Liam_Hampton_to_the_edge) at Golang 2022.

[Watch Michele Riva's talk](https://www.conf42.com/JavaScript_2022_Michele_Riva_lyra_disrupting_fulltext_search_industry) from [Conf42 JavaScript 2022](https://www.conf42.com/js2022).

## From NearForm

Michele thanks NearForm for letting him work on Lyra, describing it as a professional services company specialising in Node.js, DevOps and React Native that maintains a lot of open source. He says NearForm is responsible for almost 8% of the npm modules used globally, downloaded around 1 billion times a month, and that it hires remotely worldwide.

- NearForm: [nearform.com](https://www.nearform.com/)

[Watch the talk on YouTube](https://youtu.be/A5raon-jtTU).

## Watch the talk

[Lyra: Disrupting the full-text search industry with JavaScript](https://www.conf42.com/JavaScript_2022_Michele_Riva_lyra_disrupting_fulltext_search_industry) at Conf42 JavaScript 2022.
