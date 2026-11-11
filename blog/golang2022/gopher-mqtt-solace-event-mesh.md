# One Go publisher, one JavaScript MQTT subscriber, same broker

Conf42 Blog, 2022-03-31. https://www.conf42.com/blog/golang2022/gopher-mqtt-solace-event-mesh

In short: Tamimi (Solace) at Conf42 Golang 2022 on fitting Go into event-driven architecture, from Paho MQTT and Watermill to a multi-protocol broker

Your Go service speaks one protocol, the browser app speaks MQTT, the legacy system speaks JMS, and somehow they all need the same order event. At Conf42 Golang 2022, Tamimi, Developer Advocate in the Office of the CTO at Solace, walked a cartoon gopher through three ways to make Go talk in an event-driven system: a raw protocol library, an abstraction framework, and a broker that translates protocols for you.

It is a light, introductory talk with two live demos, and the second one shows Solace's then brand-new PubSub+ Messaging API for Go.

## What is an event-driven architecture, briefly?

Applications communicate asynchronously by publishing and subscribing to events over a broker, using a messaging protocol. Publishers send to a topic, subscribers listen on topics, and the broker handles routing. Tamimi's real-world example is a single tap on a mobile shopping app: one order event fans out to inventory, payment authorisation, shipping, a loyalty programme and the customer data platform, all in real time. The catch is that the producers and consumers are written in different languages, speak different protocols, and run on premises, in public cloud and in private cloud.

## Option one: pick a protocol and a library

The first demo uses MQTT, the lightweight OASIS-standard pub/sub protocol popular with IoT devices, via the Eclipse Paho MQTT library for Go. The code is short: initialise a module, go get the Paho package, configure the client with a broker address (port 1883), credentials and callbacks for connect, connection lost and incoming messages. A publish function sends ten numbered messages a second apart to a conf42/go topic, and the subscriber listens on conf42/# using MQTT's multi-level wildcard. Run it and the subscriber prints zero to nine.

That works, as long as everyone speaks MQTT.

## Option two: abstract the messaging API

For Go teams that want to swap the underlying system, Tamimi points to Watermill, a Go library that hides the messaging implementation behind two interfaces, a Publisher and a Subscriber. You create, say, an AMQP publisher and call the same Publish method you would on any other integration. The limitation he flags: you only get the integrations Watermill supports, and it only helps Go applications. Your JavaScript and Java services are on their own.

## Option three: let the broker translate

For true multi-language, multi-protocol systems he argues for an advanced broker that does protocol interoperability and translation. The second demo makes the case concretely. A Go program built with the Solace PubSub+ Messaging API for Go (a builder-pattern API: create a messaging service, build a direct message publisher, build messages) publishes a sequence-numbered greeting every second to a dynamic topic under conf42/solace/go. Shutdown uses Go channels: block on a channel listening for an OS interrupt, then terminate the publisher and the service cleanly.

On the other side, a browser-based MQTT client written in JavaScript (the HiveMQ web client) connects to the same Solace Cloud broker and subscribes to conf42/>, the Solace multi-level wildcard. The messages from the Go native API arrive in the MQTT client. Different language, different protocol, same stream. The Go API was released on April 1, 2022, the day after the talk; the slides add that this was not an April Fools joke.

## Why pub/sub is the easy part

Tamimi closes by zooming out. At enterprise scale you face hybrid, multi-cloud and multi-region deployments; a mix of microservices, IoT, cloud-native services, iPaaS and legacy ESB and ERP; and demands for performance, reliability, scalability, WAN optimisation, security and compliance. On top of that come event design, discovery, governance and access control. Tamimi said at Conf42 Golang 2022: "It can feel daunting at first, but it's all necessary to do this well."

## Who should watch

Go developers new to messaging who want a quick map from raw MQTT to frameworks to brokers, with runnable code. If you already run Kafka or NATS in production, the architecture section will be familiar, but the cross-protocol demo is a neat 30-second argument for broker-side translation.

## Related Conf42 talks

- Lorna Mitchell on [Go and Apache Kafka](https://www.conf42.com/Golang_2021_Lorna_Mitchell_go_big_apache_kafka_open_source) at Conf42 Golang 2021.
- James Eastham on [building an event-driven system](https://www.conf42.com/Cloud_Native_2024_James_Eastham_event_driven_system) at Conf42 Cloud Native 2024.
- Grace Jansen on [living in an event-driven world](https://www.conf42.com/Enterprise_Software_2021_Grace_Jansen_event_driven_world) at Conf42 Enterprise Software 2021.

[Watch Tamimi's talk](https://www.conf42.com/Golang_2022_Tamimi_eventdriven_playground)

## From Solace

The talk demos Solace PubSub+ as the protocol-translating broker and the PubSub+ Messaging API for Go as its native Go client. Solace also runs a developer community and the EDA Summit.

- Solace: [solace.com](https://solace.com/?utm_source=golang&utm_medium=referral&utm_content=website-banner-golang&utm_campaign=field_2022)
- Solace Community: [solace.community](https://solace.community/)
- EDA Summit: [edasummit.com](https://edasummit.com/)

[Watch the talk on YouTube](https://youtu.be/XBkBpFYAHiw).

## Watch the talk

[Gopher in an Event-Driven playground](https://www.conf42.com/Golang_2022_Tamimi_eventdriven_playground) at Conf42 Golang 2022.
