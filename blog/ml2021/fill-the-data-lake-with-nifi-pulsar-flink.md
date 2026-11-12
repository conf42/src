# An empty data lake trains nothing - stream into it instead

Conf42 Blog, 2021-07-30. https://www.conf42.com/blog/ml2021/fill-the-data-lake-with-nifi-pulsar-flink

In short: Tim Spann (StreamNative) at Conf42 Machine Learning 2021 on filling a cloud data lake in real time with Apache NiFi, Pulsar and Flink SQL

A machine learning model is only as fresh as the data you can get to it, and a data lake fed by a nightly batch is a day stale before anyone queries it. At Conf42 Machine Learning 2021, Tim Spann, Developer Advocate at StreamNative, shows how he fills a cloud data lake continuously with open-source Apache tools: NiFi for ingestion, Pulsar for messaging, Flink SQL for queries over the stream, with deep learning running inside the pipeline.

He admits up front that a streaming talk in the machine learning track might seem odd. The argument is that your data scientists can't train or score anything until the data shows up, and most of the pain lives in getting it there.

## What goes wrong when every source gets its own script?

Tim's problem statement is one most data teams will recognise: high-volume sources, lots of message formats, different protocols, many vendors, and no visibility into where data is stuck. The usual fix is a pile of Python and shell scripts. His slides call the result code sprawl: custom scripts of various quality spread across environments, nobody sure which VM or Kubernetes pod is running what, and every new source means learning another tool.

The cost shows up as delay. If a new weather provider or IoT device takes weeks to onboard, your models wait weeks for its data. The outcome his slides promise is onboarding a new source in days rather than weeks.

## The stack: FLiP and FLaNK

Tim calls his stack FLiP (Flink plus Pulsar, usually with NiFi) or FLaNK. The roles are clear:

- **Apache NiFi** ingests and routes almost anything (XML, JSON, Avro, Parquet, PDFs, logs, images) through drag-and-drop processors, over 300 of them per the slides, with back pressure and guaranteed delivery. Its data provenance gives full lineage for every record.
- **Apache Pulsar** is the messaging layer: pub-sub, geo-replication, Pulsar Functions, multi-protocol support (MQTT, AMQP, JMS, Kafka), and tiered storage that offloads topics to S3 without extra code.
- **Apache Flink**, via StreamNative's open-source Pulsar-Flink connector, runs continuous SQL over the stream. Flink parses SQL with Apache Calcite, so anyone who knows ANSI SQL is most of the way there.

## What does the demo actually do?

Most of the talk is a live NiFi canvas, which is the right call. An edge device posts sensor readings over HTTPS; NiFi queues them, runs a query filtering readings above 60 degrees Fahrenheit, splits the batch into records and pushes them to the messaging layer. Writing to a cloud store needs only a server, a table name and a format. NiFi's record readers infer or look up the schema, so there's no hand-written mapping.

The second stream is US weather data from NOAA, which publishes a zip of every station reading every 15 minutes. NiFi unzips it, keeps only airport stations, validates the records against a schema, and converts XML to JSON.

"I don't really like XML. I'm going to get rid of that as soon as possible," Tim Spann said at Conf42 Machine Learning 2021.

From there the same stream lands as ORC files in S3 (Parquet and Kudu work the same way) and keeps flowing into Flink SQL for live min, max and average temperatures per location, a join of the energy and sensor topics, and materialized views served as REST endpoints that return JSON to a Jupyter notebook or an app.

## Deep learning inside the pipeline

The ML part is a custom NiFi processor Tim wrote on the Deep Java Library (DJL), running a ResNet-50 over images in the flow and writing labels, bounding boxes and confidence into the record's metadata. He also has an Apache OpenNLP processor for entity extraction. The detector correctly finds a person in a photo of the side of his own head, with the caveat that on other days it has labelled the cat a person.

## Who should watch?

Data engineers who feed ML teams and are tired of maintaining one-off ingestion scripts, and data scientists who want to know why their training data is always a day late. It's a demo-driven tour rather than a production war story, with no benchmarks, but you see a working pipeline end to end.

Related Conf42 talks go further on the same tools: [Tim Spann's Apache Pulsar development 101 with Python](https://www.conf42.com/Cloud_Native_2022_Tim_Spann_apache_pulsar_development_101_python), [Mary Grygleski on event streaming with Apache Pulsar](https://www.conf42.com/Cloud_Native_2022_Mary_Grygleski_event_streaming_processing_apache_pulsar), and [Lorna Mitchell on Apache Kafka from Go](https://www.conf42.com/Golang_2021_Lorna_Mitchell_go_big_apache_kafka_open_source).

[Watch Tim Spann's talk](https://www.conf42.com/Machine_Learning_2021_Tim_Spann_From_Stream_to_Lake) from [Conf42 Machine Learning 2021](https://www.conf42.com/ml2021).

## From StreamNative

The talk uses StreamNative's open-source Pulsar-Flink connector to join Flink jobs and Pulsar topics as sources and sinks.

- StreamNative Cloud: [streamnative.io](https://streamnative.io/en/cloud/hosted)

[Watch the talk on YouTube](https://youtu.be/CfCp_xPvxCg).

## Watch the talk

[Hail Hydrate! From Stream to Lake](https://www.conf42.com/Machine_Learning_2021_Tim_Spann_From_Stream_to_Lake) at Conf42 Machine Learning 2021.
