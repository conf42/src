# Teaching an 8-year-old observability with a thirsty house plant

Conf42 Blog, 2025-11-18, updated 2026-11-09. https://www.conf42.com/blog/iot2025/plant-monitoring-esp32-prometheus-grafana-cloud

In short: Marie Cruz of Grafana Labs at Conf42 IoT 2025 builds a soil moisture monitor with an ESP32, Prometheus and Grafana Cloud alongside her daughter.

A house plant makes a surprisingly good on-call rotation: it fails silently, nobody notices until it is too late, and the postmortem always blames too much or too little water. At Conf42 Internet of Things (IoT) 2025, Marie Cruz, Senior Developer Advocate at Grafana Labs, showed how she and her 8-year-old daughter wired a soil moisture sensor to an ESP32, shipped readings to Prometheus in Grafana Cloud, and got a Telegram alert whenever the plant was thirsty.

The project is deliberately beginner-level, and Marie says so. The interesting part is less the hardware than the way she explains monitoring and observability to someone with zero jargon, which is a skill most of us could use at work too.

## Monitoring is a yes or no, observability asks why

Marie's framing for her daughter: each plant gets a little helper, a sensor in the soil, and the internet of things is just a way to connect objects like that so they can report, communicate and sometimes act on their own.

Monitoring, in her version, is checking whether the soil is dry and reacting. Useful, but it only answers yes or no. If the plant still looks sad after watering, monitoring has nothing more to say. Observability means looking at the data over time: does moisture drop at a certain hour, should room temperature and humidity be in the picture, or is one of the family dogs up to something? Without signals you are guessing; with them the black box becomes a clear box. That is the same pitch you would give a VP about distributed tracing, just with more chlorophyll.

## The bill of materials fits in a shoebox

The hardware list is short: a soil moisture sensor, an ESP32-S3 dev kit, a breadboard, DuPont jumper wires and a USB-C cable. Software is the Arduino IDE plus a Grafana Cloud account on the free tier, which conveniently comes with a managed Prometheus instance.

Marie walks through the wiring pin by pin (VCC to 3.3 V, ground to ground, analog out to pin 11) and how she explained it: VCC is the plus side of the battery, ground is the minus side. The sensor itself is two metal prongs; wet soil conducts better than dry soil, so a high analog reading means dry and a low one means wet. Her first program reads the value every five seconds and reports dry soil above 500. She explains the 9,600 baud rate as a group of friends who all agree to speak at the same speed, which is honestly a better definition than most serial port docs offer.

## From serial monitor to dashboard to alert

Staring at the Arduino serial monitor around the clock is nobody's idea of observability, so the second iteration pushes readings to Prometheus. Prometheus became a gardener who collects every value and keeps it in a time series toolbox with timestamps; PromQL is the language you use to ask the gardener questions. The team used the Prometheus Arduino libraries, a config file with the instance URL, user and API token plus Wi-Fi details, and a certificates file copied from that project. When her daughter asked whether copying the example code was cheating, Marie had to break the news that this is just programming.

The Grafana dashboard has a text panel with a photo of the plant, a stat panel and a gauge with a threshold at 500, and a time series panel. Value mappings turn the stat and gauge from green to red when the soil dries out. Finally, a Grafana alert rule fires above 500 and sends the message to a Telegram contact point. She also tried Grafana Assistant, the AI agent built into Grafana Cloud, to tidy up the dashboard's look.

## Who should watch

Parents and teachers looking for a weekend STEM project with real tools, and anyone who has to explain monitoring versus observability to non-engineers. It is also a compact, honest tour of the Prometheus and Grafana Cloud path for a single ESP32 device. If you already run Grafana in production, the value is in the explanations, not the stack. Marie's full project lives in her plant monitoring GitHub repo, linked from the talk.

## Pair it with

- [Guillermo Ruiz on building the largest Raspberry Pi Kubernetes PostgreSQL cluster](https://www.conf42.com/Internet_of_Things_IoT_2024_Guillermo_Ruiz_raspberrypi_kubernetes_postgresql) at Conf42 IoT 2024, for when the hobby project gets out of hand.
- [Youhana Hana on building a smart robot with AWS IoT](https://www.conf42.com/Internet_of_Things_IoT_2023_Youhana_Hana_build_smart_robot_aws) at Conf42 IoT 2023.
- [Samuel Arogbonlo on exposing log metrics to Prometheus](https://www.conf42.com/Site_Reliability_Engineering_2022_Samuel_Arogbonlo_logmetrics_prometheus) at Conf42 SRE 2022.

[Watch Marie Cruz's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Marie_Cruz_sensors_gardening_analytics) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/M5BerP-gpws).

## Watch the talk

[STEM in the Garden: How to Monitor Plants with IoT Sensors and Grafana Cloud](https://www.conf42.com/Internet_of_Things_IoT_2025_Marie_Cruz_sensors_gardening_analytics) at Conf42 Internet of Things (IoT) 2025.
