# Multi-cloud is a data problem first, and outages make the case

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/multicloud-data-is-the-bottleneck

In short: Adrienne Tacke (MongoDB) at Conf42 Cloud Native 2021 on real multi-cloud cluster use cases, from Canadian data residency to cross-cloud migrations

The hard part of running across AWS, Google Cloud and Azure has never been the compute; it is getting the data to follow you. At Conf42 Cloud Native 2021, Adrienne Tacke, Senior Developer Advocate at MongoDB, walked through the real deployments where a single database cluster spanning several cloud providers solved a problem, and was honest about where it doesn't.

Her definition is the plain one: any single architecture that uses two or more cloud providers, which can include a mix of public and private clouds.

## Do we really need multi-cloud?

Tacke answers with an outage timeline. June 2019: the Google Cloud outage Wired called the Catch-22 that broke the internet, where a routine maintenance event plus misconfigurations and bugs led automation to deschedule network control jobs in several locations. Then an AWS outage traced to a bug in third-party software in its data centre cooling control system. March 2020: a router failure in a Google data centre in Atlanta. Spring 2020: Azure capacity shortages in Europe as pandemic demand surged, with Microsoft Teams at about 44 million daily users generating over 900 million meeting and calling minutes in a single week. June 2020: Azure bottlenecks in APAC. November 2020: the AWS Kinesis Data Streams outage that took down a big chunk of the internet.

The point is not that outages happen; everyone knows that. It is that, in Tacke's words at Conf42 Cloud Native 2021, "no cloud is spared from the outages."

She adds a CIO think tank from June 2020, where about 30 IT leaders agreed multi-cloud was a question of when, not if. Gregory Scher of Fiserv put the regulated-industry reason plainly: "We have banks who have an Azure preference, we have banks who have an AWS preference, Google Cloud and on and on, we don't really get to choose."

## Data residency: when one region per provider isn't enough

The Government of Canada's direction on electronic data residency requires sensitive government data to stay inside Canada. An emergency services application ran on AWS Montreal, the only AWS region available, and the November 2020 outage made a single region feel like a single point of failure. Their answer: fail over to Google Cloud's Montreal region, the only other provider there, plus Azure Canada Central (Toronto) and Azure Canada East (Quebec) in case the whole of Montreal goes dark.

Australia's My Health Records Act 2012 creates the same shape: AWS and Google Cloud both in Sydney, with Azure regions in Melbourne and two in Canberra built for in-country disaster recovery.

## Best tool per cloud, without copying the data around

An internal help desk app ran on MongoDB Atlas on AWS and wanted a recommendation feature built on Google's AutoML. The options were custom scripts (works, but another bespoke thing to maintain), Kafka streaming (another service they didn't want), or backup and restore into Google Cloud (batch ETL, so analysts always had stale data). They chose a multi-cloud cluster with a read-only analytics node on Google Cloud, so long-running analytics never competed with the operational workload on AWS.

Two cost stories follow. One client wanted to burst workloads to whichever provider was cheapest at the moment, still experimental because of small differences between providers. A major car manufacturer wanted to switch providers as soon as it negotiated a better deal: change the highest-priority provider in the cluster settings and the cluster rolls over.

Tacke is careful with the caveat: none of this works unless the application is built so that only the data needs to move. "Do a multicloud cluster and all your problems are solved. That's not the case," she said.

## A migration without a connection string change

The cleanest example is a European, all-Azure company that acquired one on AWS. Atlas live migration was available but still meant cutting over a connection string. With a multi-cloud cluster, the three-node replica set moves in steps: migrate the two secondaries to Azure, elect a new primary on Azure, migrate the last secondary. Same connection string, no downtime.

The demo is short: turn on multi-cloud in the Atlas cluster builder, pick electable, read-only and analytics nodes, and keep an odd number of electable nodes so elections can't split. She set up a 2-2-1 distribution across Google Cloud, AWS and Azure, the minimum she gives for equivalent read and write availability.

## Who should watch

Architects weighing multi-cloud for availability or regulation, and anyone stuck in a single region. The use cases are worth the time even if you don't run MongoDB; the demo shows the Atlas UI.

## Related Conf42 talks

- Lawrence Finn on [a cloud sidecar for multi-cloud](https://www.conf42.com/Cloud_Native_2021_Lawrence_Finn_multicloud_breaking_cloud_sidecar) at Conf42 Cloud Native 2021.
- Paweł Skrzypek and Alicja Reniewicz on [autonomous multi-cloud serverless deployment](https://www.conf42.com/Cloud_Native_2021_Pawe_Skrzypek_Alicja_Reniewicz_autonomous_multicloud_serverless_deployment) at Conf42 Cloud Native 2021.
- Gilbert Cabillic on [hot migration across clouds](https://www.conf42.com/Cloud_Native_2022_Gilbert_Cabillic_instant_provisioning_hot_migration_multicloud_environment) at Conf42 Cloud Native 2022.

[Watch Adrienne Tacke's talk](https://www.conf42.com/Cloud_Native_2021_Adrienne_Tacke_multicloud_magic_clusters)

## From MongoDB

MongoDB Atlas is MongoDB's cloud database service, the one the talk's multi-cloud clusters run on.

- [MongoDB Atlas](https://www.mongodb.com/atlas)

[Watch the talk on YouTube](https://youtu.be/-IBtLTprnfY).

## Watch the talk

[Multi-Cloud Magic: Leveraging Multi-Cloud Clusters in Real-World Scenarios](https://www.conf42.com/Cloud_Native_2021_Adrienne_Tacke_multicloud_magic_clusters) at Conf42 Cloud Native 2021.
