# A houseplant, four sensors and InfluxDB replicating from edge to cloud

Conf42 Blog, 2023-03-10. https://www.conf42.com/blog/python2023/plant-buddy-influxdb-edge-replication

In short: Anais Dotis-Georgiou (InfluxData) at Conf42 Python 2023 on building a plant monitoring app with InfluxDB, Telegraf, Flask and edge to cloud replication

The first item on the parts list is a plant, preferably alive. At Conf42 Python 2023, [Anais Dotis-Georgiou](https://www.conf42.com/Python_2023_Anais_DotisGeorgiou_iot_monitoring_app_influxdb_flask_edge_cloud_replication), Developer Advocate at InfluxData, walks through Plant Buddy, a plant monitoring app built with InfluxDB, Telegraf, Python and Flask, where an open-source InfluxDB instance at the edge downsamples sensor readings and replicates them to InfluxDB Cloud.

It is a build walkthrough of InfluxData's own stack, with the full code on GitHub. Along the way it also catches a moment in InfluxDB's history: the move from Flux to SQL in the cloud.

## What hardware do you need?

The slides list a plant, a Particle Boron microcontroller (or another compatible board), at least one sensor, and a breadboard with jump wires and terminal strips. Plant Buddy uses four sensors: temperature and humidity, light, soil moisture, and soil temperature. Every reading is a timestamped measurement, which is the whole case for a time series database here. The microcontroller is plugged straight into her laptop, and the Particle serial monitor shows the readings streaming in.

## The stack

- **Flask** runs the local app and routing.
- **InfluxDB** stores the data and adds a visualisation layer and a query and task engine.
- **Telegraf**, InfluxData's open-source, plugin-driven collection agent with 300+ plugins, configured in a single TOML file.
- **The InfluxDB Python client library**, for writing and querying when you'd rather not use Telegraf.
- **The Flux extension for VS Code**, so you don't flip between the editor and the InfluxDB UI to build queries.
- **Plotly** for the interactive graphs.

## How does the data get in?

In the InfluxDB UI she creates a bucket, sets its retention policy (how long data lives before it expires), and creates an API token. All-access tokens are handy for development, she says, but be careful with them, and scope a read/write token to the bucket for anything real.

There are two ingest paths. With the client library, a few lines of Python build a point, tag it (to tell temperature from humidity, or one plant from another) and write it to the bucket. With Telegraf, the execd plugin runs the Python script that reads the serial port, and the agent handles the writing. The repo has both; the project uses Telegraf.

## Flux in open source, SQL in the cloud

Flux is the data scripting language embedded in InfluxDB OSS: JavaScript-like syntax, but it behaves more like pandas, piping each line's output into the next function. Plant Buddy's base query takes the device ID, field and bucket as variables and reads the last 24 hours, so one query feeds every graph.

In InfluxDB Cloud, Flux was being replaced by SQL on the new IOx storage engine, which stores data as Parquet with unlimited cardinality and builds on Apache Arrow, DataFusion and Parquet. The reason is refreshingly blunt. "We find that most users don't want to take on the burden of learning a new language that is proprietary to a single piece of technology they use," Anais Dotis-Georgiou said at Conf42 Python 2023. OSS users keep Flux for now, with IOx and SQL planned for open source later, and Flight SQL plugins connect tools like Apache Superset, Tableau, Power BI and Grafana. In the Python code the switch is a couple of lines using Arrow Flight SQL, returning a DataFrame either way.

## Why replicate from edge to cloud?

Edge data replication copies data from an OSS instance at the edge to a cloud instance. The advantages she lists are lower bandwidth costs, since you don't ship high-fidelity data upstream, and resilience to intermittent network failures. Mundane jobs such as downsampling, tuned per device type, stay at the edge, leaving the cloud for the interesting analysis and long-term storage.

The feature itself is small: two API endpoints and two CLI commands (remotes and replications), plus a disk-backed queue per replicated bucket that buffers data through disruptions. Setup is two steps, create a remote connection, then a replication rule from localhost to the cloud bucket. The Flask app then queries into a DataFrame and draws the Plotly dashboard: overall light, soil and room temperature, room humidity and soil moisture.

## Who should watch

Python developers starting an IoT side project, and anyone weighing an edge plus cloud split for sensor data. Expect a guided tour with code, not a deep look at InfluxDB internals. For the why behind the database choice, pair it with her other talk at the same event, [on whether you need a time series database at all](https://www.conf42.com/Python_2023_Anais_DotisGeorgiou_time_series_database_application_architecture).

Related Conf42 talks:

- Anais Dotis-Georgiou on [Apache Arrow Flight and InfluxDB](https://www.conf42.com/Python_2024_Anais_DotisGeorgiou_apache_flight_influxdb), Conf42 Python 2024.
- Joe Karlsson on [the internet of toilets, an IoT litter box](https://www.conf42.com/JavaScript_2020_Joe_Karlsson_internet_of_toilets_iot_kitty_litter_box), Conf42 JavaScript 2020.

## From InfluxData

InfluxData makes InfluxDB, Telegraf and the client libraries used throughout the build, and hosts the Plant Buddy code in its InfluxCommunity GitHub organisation.

- [InfluxData](https://www.influxdata.com/)
- [Plant Buddy on GitHub](https://github.com/InfluxCommunity/plant_buddy)
- [InfluxDB documentation](https://docs.influxdata.com/)

[Watch the talk on YouTube](https://youtu.be/KnOjmPHvwe4).

## Watch the talk

[Building an IoT Monitoring App with InfluxDB, Python, and Flask with Edge to cloud replication](https://www.conf42.com/Python_2023_Anais_DotisGeorgiou_iot_monitoring_app_influxdb_flask_edge_cloud_replication) at Conf42 Python 2023.
