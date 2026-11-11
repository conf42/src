# The cloud isn't broken, it just needs an edge for its ML models

Conf42 Blog, 2023-05-17. https://www.conf42.com/ml2023/mlops-at-the-edge-cloud-needs-friends

In short: Alejandro Cantos (Barbara) at Conf42 Machine Learning 2023 on when ML models belong at the edge, and what it takes to run MLOps across thousands of devices.

A model that retrains per sensor, in a water treatment plant whose owner won't let the data leave the site, doesn't belong in a cloud region three countries away. At Conf42 Machine Learning 2023, Alejandro Cantos, VP of Product at Barbara, made the case for running ML at the edge, walked through two industrial deployments, and showed what MLOps looks like when your fleet is a thousand remote boxes instead of one cluster.

He opens with a deliberately blunt claim, that the cloud is broken, and walks it back by the end. It's an introductory talk from an industrial edge computing vendor, with a demo of Barbara's platform; the framing of where workloads should live is useful beyond it.

## What's the case against the cloud?

Alejandro lists eight problems: dependence on the internet, round-trip latency that real-time applications can't afford, service availability, loss of control over infrastructure you don't own, unpredictable usage-based costs (computer vision is his example of a data-greedy workload that gets expensive when every camera feed goes upstream), vendor lock-in, security and privacy for data that crosses the public internet, and compliance rules about where data may live.

Edge computing answers most of these by moving processing next to where data is produced, ideally onto the local network. The four drivers he names are low latency, lower bandwidth consumption, privacy and security (data that never leaves the factory is hard to steal) and autonomy: an edge system keeps working when the connection or the cloud service doesn't. Following Gartner's layering, the edge runs from regional and local data centres down to compute edge servers, gateway edge machines and device edge embedded systems such as PLCs, with the gateway and device layers tipped as the most promising.

## What do real deployments look like?

**Acciona, water treatment.** Dosing chemicals is trial and error: add some, wait for the water to stabilise, measure, repeat, and overspend on chemicals along the way. A model trained on past data predicts the right dose up front. It runs at the edge because each plant belongs to a different company wary of its data, and because models are fine-tuned per sensor (12, 20, 30 sensors a plant) and drift as the sensors age and as the predictions themselves change the process, so they need frequent local retraining. The case study figures in the talk: deployment time for edge applications cut by 86%, and around $250,000 saved per plant in the first year in regulatory and chemical costs.

**EDP, home energy.** Solar panels, batteries, an EV charger and the grid in one home, with an ML model deciding when to produce, store or use energy to maximise renewable use. Thousands of households make central per-home modelling messy, and the data is private. The next step Alejandro sketches is homes coordinating as an energy community, taking turns to charge cars to flatten the peak.

## Is Alexa edge or cloud?

Both, which is the point. Keyword spotting runs locally on the device; speech-to-text, the request analysis and the response run in Amazon's cloud. Alejandro calls this the edge-to-cloud continuum: most systems split their workloads, and the design work is deciding which computation goes where. "So maybe the cloud is not broken. Maybe it just needs some friends," Alejandro Cantos said at Conf42 Machine Learning 2023.

## Why is MLOps harder at the edge?

MLOps means deploying, monitoring, collecting data, retraining and redeploying, which is manageable for 10 or 20 models in one cloud and messy for a thousand devices in remote places on unreliable links. Citing the AI Infrastructure Alliance, he notes that companies commonly take between two months and a year to put a validated model into production, with deployment and monitoring the biggest hurdles.

On platforms, he reads the market as split: AWS and Azure have large edge stacks, Google and IBM have retired their IoT offerings, and a set of edge-native startups, Barbara among them, build only for the edge. Their architectures look alike: a Linux-based OS on each device, an agent (Barbara calls it the node manager) that executes commands and reports back, workloads in Docker containers, and a single cloud API and panel managing all the devices.

The demo shows Barbara's panel: devices in groups, a vision node running an image recognition model alongside Grafana and InfluxDB, removing and redeploying the model from the marketplace, batch operations that install or update a model across many devices at once, and a view of every workload across the fleet. Disconnected devices keep running.

## Who should watch

ML engineers whose models need to run in factories, plants or homes, and architects deciding what stays in the cloud. Skip it if you want hands-on details on model compression or on-device inference; this is about where to put workloads and how to manage the fleet.

Related talks: [Karan Singh on an edge-to-core data pipeline for a smart city](https://www.conf42.com/Machine_Learning_2022_Karan_Singh_edgetocore_data_pipeline_kubernetes_smart_city), [Tim Spann and David Kjerrumgaard on edge AI with Flink, NiFi and Pulsar](https://www.conf42.com/Internet_of_Things_IoT_2023_Tim_Spann_David_Kjerrumgaard_flipn_stack_edge_ai_flink_nifi_pulsar), and [Michele Taroni on a global pipeline to the edge](https://www.conf42.com/Machine_Learning_2024_Michele_Taroni_global_pipeline_edge).

[Watch Alejandro Cantos's talk](https://www.conf42.com/Machine_Learning_2023_Alejandro_Cantos_introduction_mlops_edge) from [Conf42 Machine Learning 2023](https://www.conf42.com/ml2023).

## From Barbara

In the talk, Barbara's platform has Barbara OS and a node manager agent on each device, a marketplace of pre-built connectors, databases and ML models, and Barbara Panel for monitoring and commanding the fleet, individually or in batches. Its use cases cover smart water, smart grids, manufacturing and computer vision.

- Barbara: [barbaraiot.com](https://barbaraiot.com/)

[Watch the talk on YouTube](https://youtu.be/d9sD-rVCALE).

## Watch the talk

[Introduction to MLOps at the Edge](https://www.conf42.com/Machine_Learning_2023_Alejandro_Cantos_introduction_mlops_edge) at Conf42 Machine Learning 2023.
