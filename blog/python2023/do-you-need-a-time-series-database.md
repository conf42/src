# Six questions that tell you whether you need a time series database

Conf42 Blog, 2023-03-08. https://www.conf42.com/blog/python2023/do-you-need-a-time-series-database

In short: Anais Dotis-Georgiou (InfluxData) at Conf42 Python 2023 on what makes time series data different and six questions for picking a time series database

A weather station that only shows the current temperature does not need a time series database. One that shows today's high and low probably does. At Conf42 Python 2023, [Anais Dotis-Georgiou](https://www.conf42.com/Python_2023_Anais_DotisGeorgiou_time_series_database_application_architecture), Developer Advocate at InfluxData, explains what makes time series data its own workload, what a time series database trades away to handle it, and the six questions she uses to decide whether your application needs one.

It is an introductory architecture talk from the company behind InfluxDB, and she says plainly at the end that relational databases are still the best choice for plenty of data.

## What counts as time series data?

Her definition: a collection of observations obtained through repeated measurements over time. The examples make it concrete. A home weather station sends temperature, dew point, humidity, wind and pressure to Weather Underground every 5 minutes. A friend's predictive maintenance company measures vibration on bearings and fans to replace parts before they fail. Patient charts track pulse, blood pressure and temperature, where one bad half hour is the reading that matters.

She splits the data into two kinds. Metrics arrive at regular intervals, like a pulse reading. Events happen at specific points in time, like an arrhythmia. And she points out a statistical quirk: on a time series chart, time is not really an independent variable, because values correlate with it (it is almost always colder at night), which makes the analysis harder than it looks.

The volume comes from machines, not people. Her own home automation setup has dozens of smart switches, each producing more data than she could. Customers named in the talk include Tesla, which monitors home Powerwall and solar setups, Nest, Disney+ tracking video delivery across its CDN, and Rappi adjusting on-demand delivery pricing.

## What does a time series database do differently?

Ingest volume first. One device writing once a second is 86,400 records a day; at nanosecond precision it is 86.4 trillion. To keep up, time series databases make deliberate trade-offs, deprioritising updates and deletes of individual points in favour of ingest and query speed.

Then queries. Records are indexed and stored by time, so a time range sits together on disk and comes back fast, which is not the case when time is just a column in a relational table.

Then lifecycle management, at the database engine level rather than in your application code:

- **Retention policies** expire old data automatically, and because data is organised by time, deleting a large block doesn't hurt the way mass deletes can elsewhere.
- **Downsampling** replaces raw high-precision data with an aggregate: a sample every 5 minutes is 288 records a day, the daily average is one.
- **Compression** exploits how repetitive the data is. Her example is a railroad crossing sensor that reports zero for hours before the one reading that closes the gate.

## The six questions

Her checklist for a software engineer choosing a database:

1. **Does my data have a time element?** "So if there's no time element, then a time series database is not a good fit and you should find a different database for it," Anais Dotis-Georgiou said at Conf42 Python 2023.
2. **Do I care about changes over time?** If you only need the current value, an updated field in a relational table works, until the feature request for today's high and low arrives.
3. **How much data, now or later?** Small amounts can live in the database you already know; large volumes with a time element build the case for switching.
4. **Will I need analytics?** Analysis usually means looking across time, which is the access pattern these databases are built for.
5. **Am I concerned with storage costs that a time series database could reduce?** Often yes, sometimes dramatically, though it can take a prototype to find out.
6. **Do I need to retrieve blocks of time quickly?** For graphs and analysis over time ranges, this is where time series databases shine.

## Who should watch

Python developers designing an IoT, monitoring or fintech backend who are about to put timestamps in a Postgres table and wonder if they will regret it. It is a 101 on the category, not a benchmark or an InfluxDB tutorial. For the hands-on side, she gave a second talk at the same event on [building an IoT monitoring app with InfluxDB, Python and Flask](https://www.conf42.com/Python_2023_Anais_DotisGeorgiou_iot_monitoring_app_influxdb_flask_edge_cloud_replication).

Related Conf42 talks:

- Anais Dotis-Georgiou on [Apache Arrow Flight and InfluxDB](https://www.conf42.com/Python_2024_Anais_DotisGeorgiou_apache_flight_influxdb), Conf42 Python 2024.
- Piotr Stepinski on [forecasting time series](https://www.conf42.com/Machine_Learning_2024_Piotr_Stepinski_forecasting_timeseries), Conf42 Machine Learning 2024.

## From InfluxData

InfluxData, founded in 2013 by CTO Paul Dix, makes InfluxDB and the open-source collection agent Telegraf. Its slides count 1,300+ customers and 736,000 daily active open-source deployments. InfluxDB comes as an open-source version and a hosted cloud option, and InfluxDB University offers courses on the stack.

- [InfluxData](https://www.influxdata.com/)

[Watch the talk on YouTube](https://youtu.be/9j-oDghxc30).

## Watch the talk

[Time series database: Should I use one in my application architecture?](https://www.conf42.com/Python_2023_Anais_DotisGeorgiou_time_series_database_application_architecture) at Conf42 Python 2023.
