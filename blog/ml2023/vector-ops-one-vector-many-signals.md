# Stop benchmarking vector databases on speed, build better vectors

Conf42 Blog, 2023-05-17. https://www.conf42.com/blog/ml2023/vector-ops-one-vector-many-signals

In short: Daniel Svonava (Superlinked) at Conf42 Machine Learning 2023 on packing recency, popularity and topic into one vector for search and recommendations

Most vector search demos stop at one semantic embedding and a cosine similarity call. At Conf42 Machine Learning 2023, Daniel Svonava, co-founder of Superlinked and a former tech lead at YouTube for seven years, argued that the interesting part of a vector-powered app is how you build the vectors, not how fast your database returns them: concatenate topic, popularity, quality and recency into one content vector, build a user vector in the same space, and let approximate nearest neighbour search do the ranking.

Superlinked builds a vector ops platform, which he mentions only in the last minute; the rest is a practical map of search and recommendations with embeddings.

## Why bother with vectors at all?

He starts in the basement: a photo is about a million pixels, and a human compresses it to "field of grass". Feed those three words to Midjourney and you get a very different field. Add words until you have 16 of them and the reconstruction is still worlds apart, and the same description fits several pictures. Language is a lossy, ambiguous bottleneck, and so is any structured representation of real-world data. Vectors keep the resolution: they are expressive and smooth, so nearby points are similar things you can explore. The catch, in his summary, is that a printed vector tells you nothing.

## What was wrong with search and recommendations before?

Keyword search means custom NLP pipelines, a full-text index and years of hand-tuned rules, and it still misses. His example is an online pharmacy where a search for a splitting headache returns one essential oil and no painkillers. Recommendations are no better: his LinkedIn job suggestions include intern roles after 15-plus years in the industry, and jobs at "Stealth", the company tens of thousands of LinkedIn users claim to work at.

The classic recommender stack retrieves about 10,000 rough candidates from a feature store, scores each one with a ranking model, and returns the top three. It takes months to build and its recall is capped by whatever the candidate step happened to fetch.

## One vector, several objectives

The vector version is simpler: index the whole catalogue, and query it with a user vector. The trick is in construction. For a social feed he builds the content vector from normalised, weighted parts: topical relevance, contextual popularity, quality and recency.

"The new thing with vectors is that you can actually take all these features and literally just concatenate them into the content vector, right?" Daniel Svonava said at Conf42 Machine Learning 2023.

The user vector mirrors it in the same space: topical preference, popularity preference, quality tolerance, recency preference. Search with the user vector and the nearest neighbour index balances all those trade-offs at once. User-to-user search falls out for free: lookalike audiences, bot detection and, yes, dating apps.

A query manager on top handles what vectors express badly. Swap the topical part of the user vector for a query embedding and your recommender becomes personalised search. Issue several searches into different author clusters to force diversity. Post-filter a small share of results, because approximate retrieval gives no guarantees. One trap: encode content age naively and you recompute every vector nightly.

## How fast is fast enough?

He thinks the vector database market has coalesced around queries-per-second benchmarks because they are easy to measure. His rule of thumb: thousands of queries per second per machine with tens of thousands of vectors in the index, a recall of 80 to 90% for search and recommendation use cases, and vectors up to about 2,000 dimensions for a healthy system (the benchmark he shows uses roughly 800).

"When you choose a vector database to work with, I wouldn't focus so much on the speed, right." His advice is to pick one that is good enough and spend the effort on the vectors.

## From notebook to production

The staged path is the most reusable part:

- **Getting started**: your data, a Python notebook, an embedding model from Hugging Face or the OpenAI API, and scikit-learn's cosine similarity. Brute force works fine for thousands of vectors.
- **MVP**: add a vector database and, just as important, evaluation: eyeball 20 random inputs and their top ten results, back-test against historical clicks, collect user feedback, and set up analytics, which he calls the be-all and end-all.
- **Production**: APIs that ingest content, user metadata and events, a transform step, vectorisation with your own models next to the pretrained ones, real-time vector updates if you want TikTok-level freshness, then retrieval behind another API.

## Where generative AI fits

The closing section connects this to LLMs through memory. A chat model has none beyond its context window, which he demonstrates with a guess-my-secret-number game the model happily plays despite having nowhere to keep the number. Chunk documents, store paragraph vectors in a vector database, and an agent (LangChain, AutoGPT) can retrieve them.

## Who should watch

Engineers moving an embeddings prototype towards a real search or recommendation feature, especially anyone whose plan so far is one embedding model plus whichever vector database topped a benchmark. Pair it with [Zain Hasan on vector databases](https://www.conf42.com/Machine_Learning_2023_Zain_Hasan_vector_databases) from the same event, [Stephen Batifol on how vector databases work](https://www.conf42.com/Machine_Learning_2024_Stephen_Batifol_vector_databases_work) and [Lei Xu on LanceDB](https://www.conf42.com/Rustlang_2023_Lei_Xu_lancedb_oss_serverless_vector_db).

[Watch Daniel Svonava's talk](https://www.conf42.com/Machine_Learning_2023_Daniel_Svonava_vector_ops_embeddingpowered_apps)

## From Superlinked

- [Superlinked](https://superlinked.com/?ref=conf42): the vector ops platform Daniel Svonava's team builds for search and recommendations on vector embeddings.

[Watch the talk on YouTube](https://youtu.be/v6rKfdqlwec).

## Watch the talk

[Vector Ops: How to run vector embedding-powered apps in production](https://www.conf42.com/Machine_Learning_2023_Daniel_Svonava_vector_ops_embeddingpowered_apps) at Conf42 Machine Learning 2023.
