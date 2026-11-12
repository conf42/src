# Why keyword search can't find a wine for your seafood dinner

Conf42 Blog, 2021-07-30. https://www.conf42.com/blog/ml2021/weaviate-vector-search-wine-for-seafood

In short: Laura Ham (SeMI Technologies) at Conf42 Machine Learning 2021 on Weaviate, the open source vector search engine, with live semantic and question-answering queries

Search your wine database for something to go with seafood and a keyword engine comes back empty, because the Chardonnay's description only says it is good with fish. [Laura Ham](https://www.conf42.com/Machine_Learning_2021_Laura_Ham_Weaviate_outofthebox_machine_learning_models), Community Solution Engineer at SeMI Technologies, opened her Conf42 Machine Learning 2021 talk with that example to introduce Weaviate, the company's open source vector search engine, which stores each object next to an ML-computed vector so queries match on meaning instead of exact words.

It is a short introduction aimed at people new to vector search, with a live demo on a news article data set, and it is about SeMI's own product.

## What is the problem with unstructured data?

Most of it goes unused. Her slides put unstructured data at about 93% of a company's data (citing Ciklum), say about 80% of businesses do not know how to use it (Forbes), and add that analysts spend 80% of their time preparing data to answer business questions (HBR). Business documents, emails, tickets, chat messages, medical records: none of it fits a predefined schema.

Searching it with exact keyword matching misses anything phrased differently. Google, she points out, handles abstract questions such as what colour of wine Chardonnay is, and returns a precise answer from one page, quickly. Her slides add that Google indexes only a tiny fraction of the world's unstructured data, because the rest sits inside companies. The pitch is the same kind of search over your own data, in a simple and secure way.

Laura Ham said at Conf42 Machine Learning 2021: "Weaviate is a database that uses machine learning to understand the data that is in it."

## How does vector search work in Weaviate?

Four steps. A pretrained model, a text vectoriser module based on fastText or a BERT-style transformer, already places known concepts from everyday language in a high-dimensional space. When you import data, each object is vectorised by that model and indexed in the same space, so a Chardonnay ends up close to wine, white and the food it suits. A query in natural language gets vectorised the same way. The engine then runs a nearest-neighbour similarity search and returns the objects closest to the query vector.

On top of that core, she lists what you can do: search, discover answers to specific questions, classify and label data automatically, and predict relations between objects. Weaviate has full CRUD for both data and vectors, GraphQL and RESTful APIs, and lets you combine vector search with scalar filters, so semantic and traditional search can go in the same query.

## What are modules for?

Everything model-specific is a module attached to the core vector database: a text vectoriser, an image vectoriser for searching images, a question answering module, any transformer NLP model, or your own ML model. That last option is the bit she stresses for an ML audience: Weaviate as a way to run your own models at production scale, not only a search box.

## What does the demo show?

A news article data set, the same one SeMI ran publicly on its website at the time, queried through GraphQL.

- **Plain scalar query.** A Get query returns titles, URLs and word counts in random order. You can also ask for the raw vector of each object, which is a long list of numbers and a useful reminder of what is stored.
- **Semantic filter.** A nearText query for housing prices returns articles ordered by relevance (housing as the biggest asset class, expensive housing), even though the query words do not appear in the titles. In her words, "weaviate uses semantics and the context rather than exact matching keywords."
- **Certainty.** Each result carries a certainty score; the top hit was around 87%. Filtering to results above 80% trims the list, and a more concrete query about house prices in Greece returns a single article that never says Greece, only its capital, Athens.
- **Graph plus vectors.** Articles link to the publication they appeared in, so she combines the housing prices vector query with a scalar filter on publication, here The Economist.
- **Question answering.** With the Q&A module enabled, she asks what the monkey was doing in the Neuralink video. Weaviate pulls the answer, playing MindPong, out of the article summary, a chunk of unstructured text.

The Neuralink question is a good test of the idea: no field in the schema says monkey, game or pong, and the answer still comes back in one query.

## Who should watch?

Developers and data people who keep hearing about vector databases and want a quick, concrete picture of how one works, end to end, in under half an hour, with no prior technical knowledge assumed. It is an introduction, not a benchmark: there is no discussion of index types, recall trade-offs or scaling numbers. If you already run a vector store in production, the follow-up talk below goes further.

## Related Conf42 talks

- Laura Ham on [building a search application with Weaviate](https://www.conf42.com/Machine_Learning_2022_Laura_Ham_build_search_application_vector_search_engine_weaviate) at Conf42 Machine Learning 2022.
- Zain Hasan on [vector databases](https://www.conf42.com/Machine_Learning_2023_Zain_Hasan_vector_databases) at Conf42 Machine Learning 2023.
- Daniel Svonava on [vector ops for embedding-powered apps](https://www.conf42.com/Machine_Learning_2023_Daniel_Svonava_vector_ops_embeddingpowered_apps) at Conf42 Machine Learning 2023.

[Watch the talk on YouTube](https://youtu.be/e2jeukR8ZaA).

## From SeMI Technologies

- Weaviate product page: [semi.technology/products/weaviate](https://www.semi.technology/products/weaviate/index.html)
- Weaviate on GitHub: [github.com/semi-technologies/weaviate](https://github.com/semi-technologies/weaviate)

## Watch the talk

[Search through your data with Weaviate and out-of-the-box machine learning models](https://www.conf42.com/Machine_Learning_2021_Laura_Ham_Weaviate_outofthebox_machine_learning_models) at Conf42 Machine Learning 2021.
