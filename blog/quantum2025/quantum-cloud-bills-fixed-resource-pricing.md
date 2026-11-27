# Quantum jobs will make cloud bills even harder to predict

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-cloud-bills-fixed-resource-pricing

In short: Qumulus developer relations engineer Denish Tomar argues at Conf42 Quantum Computing 2025 that metered pricing breaks down for quantum workloads.

Nobody can say exactly what their cloud bill will be next month, and quantum workloads will make that worse. That is the argument Denish Tomar, Developer Relations Engineer at Qumulus, made at Conf42 Quantum Computing 2025: usage-based pricing already confuses teams running well-understood CPUs and memory, and a quantum job whose runtime, retries and error correction are unknowable in advance turns metering into a guessing game.

This is a vendor talk and it says whose product it shows: the second half presents Qumulus's fixed-resource model as the alternative.

## The $10,000 autoscaling surprise

Tomar opens with a story worth the price of admission. A startup founder's AWS bill came in around $10,000 against a usual $2,000. The cause was one autoscaling mistake: instead of scaling up to five servers it scaled to 50, and instead of running for two hours it ran for three days before anyone noticed. Then came the line items nobody could explain: NAT gateway processing charges, CloudWatch logs, load balancer capacity units, cross-availability-zone transfer, API gateway requests and Lambda cold starts.

His challenge to the audience: open your cloud dashboard and state exactly what you will spend next month. Not approximately. You can't, and that's with technology we have optimised for decades.

## Why quantum makes metering worse

The quantum section explains superposition and entanglement for a general audience (spinning coins, mazes explored in parallel), then gets to the billing point. A quantum algorithm might finish in 30 seconds or 30 hours. It might need one run or 500, because results are probabilistic. It might use cheap basic operations or need error correction that costs a hundred times more. Tomar's example: the same quantum job could cost anywhere from $500 to $5,000, and you wouldn't know which until the bill arrives.

His view is that the big providers are struggling with this too: classical bills meter known quantities, while quantum bills meter unknown time, unknown errors and unknown retries.

## The Qumulus pitch

The alternative he presents is predefined, fixed resources at a fixed price instead of metering each operation, compared to a subscription you use without watching the meter. Qumulus is built on OpenStack, which he argues means no vendor lock-in to anyone's quantum ecosystem. He shares a before-and-after from a startup that moved from AWS: before, a bill that swung widely month to month and a fifth of engineering time spent on cost optimisation; after, a predictable bill and no time spent chasing it. The founder's line, as he tells it, was that the best part was building things instead of optimising for AWS pricing.

His closing line sums it up: "your cloud bill doesn't have to be quantum chaotic".

## How to take it

The diagnosis is the strongest part: unpredictable cost is already an engineering tax, and probabilistic workloads with variable retries make it heavier. Whether fixed-resource pricing is the answer for your team depends on how bursty your workloads are, which the talk doesn't model. The quantum billing figures are projections, not quotes from a provider's price list, so read them as the shape of the problem.

## Who should watch

FinOps practitioners, startup CTOs and platform teams who own the cloud bill, plus anyone planning to experiment with quantum services and wondering how to budget for them. If you already run strict cost controls on AWS, the first half will feel familiar; the quantum billing argument is the new part.

## Related Conf42 talks

- [Mastering the chaos: cost-effective cloud monitoring and logging](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring) by Pradeep Gaddamidi, on the CloudWatch-style line items from the opening story.
- [Real-time FinOps intelligence for streaming financial events](https://www.conf42.com/DevOps_2026_Tina_Kanth_finops_streaming_prompts) by Tina Kanth, for watching spend as it happens.
- [Your cloud emits CO2](https://www.conf42.com/Internet_of_Things_IoT_2023_Olivier_Bierlaire_your_cloud_emits_co2) by Olivier Bierlaire, another bill your cloud runs up quietly.

[Watch Denish Tomar's talk](https://www.conf42.com/Quantum_Computing_2025_Denish_Tomar_quantum_cloud_qum)

[Watch the talk on YouTube](https://youtu.be/lpQ3maIbZi4).

## Watch the talk

[Clouds Aren't Ready for Quantum (But QUMs Are)](https://www.conf42.com/Quantum_Computing_2025_Denish_Tomar_quantum_cloud_qum) at Conf42 Quantum Computing 2025.
