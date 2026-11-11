# Ship the sentiment model to the data, as a Rust Wasm UDF

Conf42 Blog, 2023-05-19. https://www.conf42.com/ml2023/rust-sentiment-udf-webassembly-in-database

In short: Akmal Chaudhri (SingleStore) at Conf42 Machine Learning 2023 on compiling a Rust VADER sentiment analyser to WebAssembly and running it inside SQL.

Scoring 25,000 movie reviews for sentiment usually means pulling them out of the database into a Python process. At Conf42 Machine Learning 2023, Akmal Chaudhri, Senior Technical Evangelist at SingleStore, did it the other way round: he compiled an existing Rust port of the VADER sentiment analyser to WebAssembly, loaded it into SingleStoreDB as a table-valued function, and called it from a plain SELECT.

It's a short, step-by-step walkthrough on SingleStore's own database, and Akmal is upfront about that. The local toolchain setup, though, is vendor-neutral, and the idea, running existing library code safely next to the data, travels.

## Why put WebAssembly inside a database?

Akmal's list of problems it solves: some logic is too hard to write in procedural SQL, some needs the engine doesn't support at all (ML scoring, fuzzy text matching), and moving lots of data to the application is slow. "Moving data around is also costly and we would prefer not to do that all the time," Akmal Chaudhri said at Conf42 Machine Learning 2023.

Wasm adds the chance to reuse code already written in C, C++ or Rust: compile it to a module, and the database runs it in a sandbox, in-process, at near-native speed. "As far as the database engine is concerned, it will treat it just as though it's a UDF," he said. Within SingleStore it sits beside the other ML routes he mentions: Apache Spark, the Python client with ML libraries, OpenAI, and SingleStore's vector functions.

## What does the toolchain look like?

The setup, in order:

1. Download the WASI SDK (version 20.0 on the slides), unpack it under /opt and add its bin directory to the PATH.
2. Install the Rust toolchain with rustup and wit-bindgen from the Bytecode Alliance repository.
3. Add the wasm32-wasi target to Rust, which isn't installed by default.
4. For SingleStore specifically, clone and build pushwasm from singlestore-labs, the tool that loads a module into the database. Install libssl if the build complains.

Then the code. A WIT interface definition file declares a sentiment table function that takes a string and returns polarity scores: compound, positive, negative and neutral. Cargo.toml pulls in the existing Rust port of VADER (Valence Aware Dictionary and sEntiment Reasoner), which does the actual analysis; the Rust implementation just maps the crate's scores onto the interface. One cargo build later there is a .wasm file.

## How does it run?

Akmal creates a database called demo on a cloud SingleStoreDB instance with an ordinary MySQL client, then runs pushwasm with the function name, the WIT file, the compiled module and the connection details. It answers that the Wasm function was created.

The first test calls the function on a literal string: the movie was great returns zero negative, a positive and neutral split and a compound score. Change it to GREAT with an exclamation mark and the positive and compound scores go up and neutral goes down, because VADER takes capitalisation and punctuation into account.

The real demo runs the same function in a query over an IMDb reviews table, 25,000 rows from the Large Movie Review dataset, returning the four scores per review alongside the text. Listing the database's functions shows the sentiment table function as table-valued, with Wasm as its runtime.

## What's the catch?

The talk doesn't benchmark it against exporting the data, and VADER is a lexicon-based analyser, not a trained deep model, so this is about where code runs rather than model quality. Language support depends on the Wasm toolchain: Rust today, with C, C++ and others mentioned. Akmal also notes that pushwasm's syntax has changed since his Medium write-up of the same example, so the talk is the more current reference.

## Who should watch

Engineers who keep exporting tables to run a small scoring function, and anyone curious how WebAssembly is moving beyond the browser. It's short and mostly terminal.

Related Conf42 talks: [Sohan Maheshwar on the future of cloud with WebAssembly](https://www.conf42.com/Cloud_Native_2024_Sohan_Maheshwar_future_cloud_webassembly), [Deepu K Sasidharan on containerless Kubernetes with WebAssembly](https://www.conf42.com/Rustlang_2024_Deepu_K_Sasidharan_kubernetes_containerless_webassembly), and [Thorsten Hans on serverless WebAssembly](https://www.conf42.com/Golang_2024_Thorsten_Hans_serverless_webassembly).

[Watch Akmal Chaudhri's talk](https://www.conf42.com/Machine_Learning_2023_Akmal_Chaudhri_webassembly_indatabase_ml) from [Conf42 Machine Learning 2023](https://www.conf42.com/ml2023).

## From SingleStore

In the talk, SingleStoreDB is a real-time distributed SQL database with one engine for transactions and analytics and support for several data models; its Code Engine runs Wasm modules as UDFs and table-valued functions.

- SingleStore: [singlestore.com](https://www.singlestore.com/)
- pushwasm: [github.com/singlestore-labs/pushwasm](https://github.com/singlestore-labs/pushwasm)

[Watch the talk on YouTube](https://youtu.be/szdOtPWFuY4).

## Watch the talk

[Using WebAssembly for in-database Machine Learning](https://www.conf42.com/Machine_Learning_2023_Akmal_Chaudhri_webassembly_indatabase_ml) at Conf42 Machine Learning 2023.
