# One JavaScript feature pipeline from Kafka to in-browser inference

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/one-feature-pipeline-from-kafka-to-the-browser

In short: Apple data engineer Venkata Chandra Sekhar Sastry Chilkuri showed at Conf42 JavaScript 2025 how Node.js, Redis and TensorFlow.js serve fresh ML features.

Personalisation that updates overnight feels broken to users who expect the page to react to what they just did. At Conf42 JavaScript 2025, Venkata Chandra Sekhar Sastry Chilkuri, Senior Data Engineer at Apple, showed how to build the whole feature pipeline in JavaScript: Node.js consumers on Kafka compute features, Redis serves them, WebSockets push them, and TensorFlow.js runs the model in the browser.

## Three hard problems

He frames real-time feature pipelines around three problems: computing features fast at scale, caching them so they stay fresh without hurting performance, and keeping the logic identical across Node.js servers, edge workers and browsers. Miss one and you get stale experiences, jittery latency, or training-serving skew, where the model in production sees features computed differently from the ones it trained on.

His argument for JavaScript is that one language runs in all three places. Async/await and non-blocking I/O suit event-driven workloads, and the ecosystem covers every stage, from Kafka clients to TensorFlow.js.

## The four building blocks

1. **Feature computation in Node.js**: microservices consume user events from Kafka, compute rolling counts and session stats, and publish features downstream. Transforms are kept idempotent and windowed so retries and back pressure don't corrupt results.
2. **Redis as the feature store**: computed features are cached with configurable TTLs for sub-millisecond reads during online inference.
3. **WebSockets**: push updates instead of polling.
4. **Edge or browser inference**: the app uses cached features with TensorFlow.js or ONNX.js to run models locally, skipping the server round trip.

Caching is layered by access pattern: browser memory for hot features on the current page, Redis for shared online reads, and an edge cache for global reach. TTLs plus pub/sub or WebSocket refreshes keep features fresh just in time. He also mentioned OpenAI's Atlas browser as a sign of how far local AI in the browser has come.

## Isomorphic feature code kills training-serving skew

The most useful section is about consistency. Ship isomorphic modules for feature logic so the same code computes a feature in Node.js and in the browser. Test both with the same fixtures. Lock schemas with TypeScript types or JSON Schema. Monitor feature distributions so drift shows up before model quality drops. It's the JavaScript version of the feature-store promise, without needing a separate platform team.

## Measure before you scale

Metrics he tracks: p50, p95 and p99 latency for computation, retrieval and inference; features per second; cache hit ratio; WebSocket delivery success; and skew between training and serving. Those numbers drive window sizes, TTLs, model size and fan-out strategy, and tell you whether to scale up for peak hours or down to save money.

Use cases: recommendations that update with every interaction, personalised UI with predictive prefetching and adaptive notification timing, and live analytics aggregated client-side and streamed over WebSockets.

His rollout order is sensible: ship offline features with a cache first, add real-time computation with Kafka, then client-side inference with small models, and scale based on observed metrics, not assumptions. Decouple compute from serving, design fallbacks and graceful TTLs for failures, and version features like APIs so you can roll back.

## Who should watch

Full-stack JavaScript developers working with data teams on personalisation, and ML engineers whose features keep drifting between offline training and online serving. It's an architecture walk-through with small code examples, not a production case study.

## Related talks

- [Every Node.js app should have real-time collaboration features](https://www.conf42.com/JavaScript_2023_Vladi_Stevanovic_nodejs_app_realtime_collaboration) covers the real-time delivery side in Node.js.
- [Using the FLiPN Stack for Edge AI (Flink, NiFi, Pulsar)](https://www.conf42.com/Internet_of_Things_IoT_2023_Tim_Spann_David_Kjerrumgaard_flipn_stack_edge_ai_flink_nifi_pulsar) builds streaming plus edge inference with a different stack.
- [Hyper-Personalization: Using AI & Analytics to Fuel Digital Transformation & Growth](https://www.conf42.com/Machine_Learning_2025_Lakshmi_Narayana_Gupta_Koralla_hyper_personalization) looks at the business side of personalisation.

[Watch Venkata Chandra Sekhar Sastry Chilkuri's talk](https://www.conf42.com/JavaScript_2025_Venkata_Chandra_Sekhar_Sastry_Chilkuri_building_real_time)

[Watch the talk on YouTube](https://youtu.be/XdnqS2X9tZs).

## Watch the talk

[Building Real-Time Feature Pipelines: JavaScript's Role in Modern Data-Driven Applications](https://www.conf42.com/JavaScript_2025_Venkata_Chandra_Sekhar_Sastry_Chilkuri_building_real_time) at Conf42 JavaScript 2025.
