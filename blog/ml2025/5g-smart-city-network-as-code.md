# Treating a city's 5G network as code, not as ladder work

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/5g-smart-city-network-as-code

In short: Anil Thimmapuram at Conf42 Machine Learning 2025 on applying DevOps and infrastructure as code to 5G small cells, edge nodes and IoT for smart cities.

In one city, Anil Thimmapuram recalls, updating a traffic light meant sending a person out with a USB stick. At Conf42 Machine Learning 2025, Thimmapuram, a DevOps engineer, made the case that 5G is less about faster video and more about giving cities a network that can be deployed, tested and rolled back like software.

It is a short, upbeat talk built around one deployment story. The numbers he shares he calls approximate, and he does not name the city, so read it as a practitioner's account rather than a case study with an appendix.

## The problem is cities running on timers

The opening picture is easy to recognize: traffic lights on fixed timers from another decade, power grids that are always on whether anyone needs them or not, and emergency vehicles following a GPS route with no live data about the jam ahead. Inefficient, he says, but also dangerous and expensive, since every change needs someone on site.

His fix combines three things: 5G small cells and edge computing for low latency, a dense IoT layer for sensing, and DevOps practice for running all of it.

## DevOps for routers, not just microservices

This is the sharpest idea in the talk. Usually DevOps means CI/CD for application code. Thimmapuram's team pointed it at the network itself. Every router, switch and edge node was defined as code. Terraform plans spun up 5G clusters on AWS, Helm charts configured edge services, and pipelines automatically tested latency, bandwidth and even failure cases before anything went live.

The cultural change fits in one line: instead of sending someone up a ladder, push to prod. He credits the automation with cutting deployment time by 85% and, just as important, giving the network rollback options that traditional networking did not have. Anyone who has ever reverted a bad router config by driving to the data center will appreciate that last part.

## Sub-10 ms needs the compute on the light pole

For a city to react in real time, he targets latency under 10 milliseconds. That meant small cells on light poles, buildings and buses (anywhere with power and fiber backhaul) and edge nodes doing local processing instead of a round trip to a distant cloud region. That is what enables live video analytics and instant alerts: a camera spots a fire, traffic is rerouted and ambulances get a clear path.

On top sits the IoT layer, up to 10,000 connected endpoints per square mile: smart meters, pollution sensors, cameras, emergency buttons, EV chargers. His favourite example: sensors picked up an air-quality spike and school buses were rerouted away from it with no human in the loop.

## Traffic, power and the rollout

With AI-driven video analysis, traffic lights adapted to conditions instead of timers, green waves reduced stop-and-go, and emergency corridors opened dynamically. On the power side, IoT meters balanced the grid: charging EV stations when solar output was high, running street lights from stored batteries at night, and shifting load when a neighbourhood surged.

The rollout was deliberately phased: an assessment that mapped every duct, pole and antenna; an automation framework with CI/CD pipelines for infrastructure; a pilot in dense downtown zones; then a parallel citywide rollout using infrastructure as code, with each deployment validating itself.

The approximate results he reports: commute times down about a quarter, emergency response 42% faster, 35% energy savings, a 28% drop in carbon output and a 64% rise in resident satisfaction. The team then open-sourced the blueprint as modular, vendor-neutral playbooks with a training program, and he says they are working with more than 15 cities, adding privacy-focused designs.

## Who should watch

Platform and network engineers curious about infrastructure as code beyond the usual cloud estate, and anyone working on smart-city or telecom programs who needs a short, motivating story. If you want architecture diagrams, Terraform modules or a methodology for those percentages, the talk stays high level.

## Related talks

- [Sai Charan Madugula on software-defined networking for IoT and 5G](https://www.conf42.com/Cloud_Native_2025_Sai_Charan_Madugula_networking_iot_5g) at Conf42 Cloud Native 2025
- [Andrey Slastenov on IoT and 5G devices in DDoS attacks](https://www.conf42.com/DevSecOps_2023_Andrey_Slastenov_iot_5g_devices_ddos_threat_landscape) at Conf42 DevSecOps 2023
- [Bhaskara Beeraka on scaling a telecom BSS with Go microservices](https://www.conf42.com/Golang_2025_Bhaskara_Beeraka_telecom_microservices_scaling) at Conf42 Golang 2025

[Watch Anil Thimmapuram's talk](https://www.conf42.com/Machine_Learning_2025_Anil_Thimmapuram_automation_infrastructure_smart)

[Watch the talk on YouTube](https://youtu.be/STx7Sy9PujE).

## Watch the talk

[5G Infrastructure Automation: Building the Foundation for Data-Driven Smart Cities](https://www.conf42.com/Machine_Learning_2025_Anil_Thimmapuram_automation_infrastructure_smart) at Conf42 Machine Learning 2025.
