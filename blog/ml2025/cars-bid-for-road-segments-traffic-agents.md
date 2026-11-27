# Letting cars bid for road segments to beat congestion

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/cars-bid-for-road-segments-traffic-agents

In short: Avraam Tolmidis of Meta at Conf42 Machine Learning 2025 on multi-agent traffic routing where vehicles take bids from intersections and re-plan as conditions change.

What if every car and every intersection negotiated? At Conf42 Machine Learning 2025, Avraam Tolmidis, Software Engineering Manager at Meta with a PhD focused on multi-objective optimization and four years in automated driving, presented a decentralized traffic system in which vehicle agents ask nearby intersections for bids on the next road segment and keep re-planning as the city changes around them.

It is a research-flavoured talk with a clear algorithm and simulation results, not a product pitch, and Tolmidis (a former teacher) explains it step by step.

## Central traffic control reacts too late

The problem is the one you sat in this morning. Congestion grows with urban population and vehicle counts, infrastructure is outdated or was never built for today's load, and when something happens on the road the response is slow because a human has to detect it and a human has to intervene. The cost is time, fuel and, in the worst cases, lives.

His proposal flips the model. Instead of one system timing lights for everyone, each vehicle is a mobile agent and each intersection a stationary agent. Decisions are mostly local, with optional centralized policies when you want to optimize for a wider area.

## Routing as an auction with weighted objectives

He calls the approach AMOR: adaptive multi-objective optimized routing agents. A vehicle approaching a decision point sends its route request to nearby stationary agents, along with weights for the objectives it cares about: travel time, distance, monetary cost (tolls), emissions, or anything else that makes sense.

Each stationary agent pulls segment data, refreshes estimates when the data is stale, normalizes the values and scores each segment with the weighted objective function. For time, distance and cost, that is simply each weight times its normalized value, summed. A route's cost is the sum of its segments, found with Dijkstra or something fancier, and the agent's bid is its cheapest route. No route, and it returns a negative value. The vehicle picks the lowest positive bid and drives the first segments of that route.

The key word is adaptive. Every few nodes, or whenever congestion or an emergency appears ahead, the vehicle starts a new auction. Stationary agents can also exchange data to sharpen their estimates. Routes evolve with the traffic instead of being fixed at departure, which is roughly what a good taxi driver does with a radio, minus the opinions.

## Re-planning is where the gains show up

Tolmidis ran a few hundred simulations in NetLogo with congestion, emergencies and mixed vehicle types over a fixed distance, comparing three strategies: plain distance-based routing, multi-objective routing planned once at the start, and AMOR with dynamic re-planning.

Both multi-objective approaches came out cheaper than distance-only routing, and both were faster. AMOR was faster still. The biggest difference showed up when congestion hit mid-trip: the other two strategies saw trip duration climb sharply, while AMOR kept the increase under 20%. Planning well at the start helps; being able to change your mind helps more.

## What a city would need

The infrastructure list is concrete. V2X (vehicle-to-everything) communication so vehicles can talk to each other, to smart traffic lights, to adaptive road signs, and even to a pedestrian's phone around the corner. Roadside units acting as the stationary agents. V2X-capable vehicles running the agent software. Local edge terminals for fast computation and a city traffic management center if you want a central view.

He is explicit about the assumptions: the map is known (no live mapping), road segments can carry tolls, historical traffic data exists and keeps being collected, and vehicles know their global position.

The benefits he lists follow from the design: smoother flow and fewer bottlenecks, shorter trips, priority lanes on demand for buses and emergency vehicles (an ambulance negotiating its own green wave), faster rerouting around closures, and lower emissions because there is less stop-and-go.

## Who should watch

Engineers interested in multi-agent systems, optimization or mobility will like the clean auction design and the honest simulation framing. If you want field deployment data, this talk does not claim any; it is a well-explained model with simulated results.

## Related talks

- [Mayur Bhandari on engineering resilient smart city platforms](https://www.conf42.com/Platform_Engineering_2025_Mayur_Bhandari_smart_city_urban) at Conf42 Platform Engineering 2025
- [Karan Singh on an edge-to-core ML pipeline for a smart city](https://www.conf42.com/Machine_Learning_2022_Karan_Singh_edgetocore_data_pipeline_kubernetes_smart_city) at Conf42 Machine Learning 2022
- [Tim Spann on data-driven automation for smart cities](https://www.conf42.com/Cloud_Native_2025_Tim_Spann_smart_cities_datadriven_automation) at Conf42 Cloud Native 2025

[Watch Avraam Tolmidis's talk](https://www.conf42.com/Machine_Learning_2025_Avraam_Tolmidis_traffic_smart_systems)

[Watch the talk on YouTube](https://youtu.be/ylpODQKnGL0).

## Watch the talk

[AI on the Fast Lane: Smart Traffic Systems to Unclog our Cities](https://www.conf42.com/Machine_Learning_2025_Avraam_Tolmidis_traffic_smart_systems) at Conf42 Machine Learning 2025.
