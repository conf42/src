# Stop passing CAD files around and start streaming design events

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/event-driven-observability-ecad-mcad

In short: Pradeep Karanam at Conf42 Observability 2025 on replacing ECAD and MCAD file snapshots with Kafka events so design conflicts surface in minutes.

Hardware teams still collaborate the way software teams did before CI: electrical and mechanical engineers exchange files at gated milestones and find conflicts weeks later. At Conf42 Observability 2025, Pradeep Karanam, a solutions architect at Facebook, showed how an event-driven observability layer between ECAD and MCAD tools makes cross-domain changes visible in real time. In his pilots, revision lead time dropped from seven days to three.

## Three millimetres, six weeks

The story that frames the talk: mid-program, the mechanical team moves a chassis rib by three millimetres. The ECAD side keeps routing the board, unaware. A week later the conflict surfaces, and the team is staring at a costly respin and a six-week slip. The root cause is not bad tools, Pradeep argues; the information arrived too late to matter.

He backs this with the wider pattern: a study across eight boards found more than ten file snapshots per spin, each one a possible reroute, and industry data puts late rework at an 8 to 10% cost increase and four to six weeks of schedule. Engineers end up doing forensics on which file version changed which part, instead of design.

## Why events instead of files

Events are push-based: a tool emits a lightweight message the moment something meaningful happens. They are context-rich, carrying geometry hashes, user IDs and variant tags. They allow automatic downstream checks. And they flow through a broker that tolerates outages: if the MCAD side is down, ECAD keeps publishing and the broker replays when it returns. Decisions that waited for the next milestone now happen in minutes.

## Three building blocks

- **A shared schema**: every ECAD change and MCAD update follows one contract with item ID, revision ID, geometry hash, user and timestamp, plus optional blocks for BOM variants. Tools validate events locally, so malformed ones never leave the workstation.
- **Audit logging**: every event also lands in an immutable store recording who changed what and when, exportable to CSV for compliance reviews in regulated domains like medical and automotive hardware.
- **Library sync**: exports and multi-revision check-ins keep symbols and footprints aligned across tools such as OrCAD, Allegro and NX, and the sync status becomes another event so stale footprints get caught before they reach a schematic.

Two cross-cutting enablers sit on top. A taxonomy separates geometry events (board outline, keep-outs, mounting holes), component events (placement moves, part swaps) and analysis events (DFM or thermal results); simple heuristics there cut irrelevant chatter by 54%. And resilience: back pressure and replay, compensating transactions for partial writes, a checksum verifier for corrupt payloads, and a circuit breaker around flaky PLM APIs.

## The pipeline end to end

ECAD and MCAD publish to a Kafka broker. A stream processor compares geometry deltas and BOM differences, and violations go to dashboards and chat channels, while the audit store keeps everything. Pradeep stresses that every component is off the shelf. The keep-out example shows the loop: MCAD publishes an update adding a rib, the processor compares geometry hashes, the rule engine flags a keep-out breach, and both teams get an alert with a 3D overlay within a minute.

Pilot results: revision lead time from seven days to three, part number approvals from four days to a day and a half, and board spins from three to two. The pipeline watches itself too, with Grafana tracking event volume and broker lag and Kibana for inspecting payloads.

## Start small

The rollout runs in four phases, starting with low-noise BOM and outline events and ending with suppliers and manufacturing on the same streams. The advice is hard-won: too many events too soon erodes trust, version the schema because silent field changes break integrations fastest, align ECAD and MCAD naming on day one, and watch broker lag early.

## Who should watch

Hardware and PLM engineers, and software engineers who like seeing event-driven patterns applied outside their usual habitat. It is a fast, dense talk; the architecture is generic enough to reuse anywhere two teams share an artefact through file drops.

## Related Conf42 talks

- [Henrik Rexed on the art of event-driven observability with OpenTelemetry](https://www.conf42.com/Observability_2023_Henrik_Rexed_event_driven_observability_opentelemetry) at Conf42 Observability 2023.
- [James Eastham on what it takes to build an event-driven system](https://www.conf42.com/Cloud_Native_2024_James_Eastham_event_driven_system) at Conf42 Cloud Native 2024.

[Watch Pradeep Karanam's talk](https://www.conf42.com/Observability_2025_Pradeep_Karanam_ecad_mcad)

[Watch the talk on YouTube](https://youtu.be/is0Tja04RNU).

## Watch the talk

[Lighting Up Design Blind Spots: Event‑Driven Observability for ECAD–MCAD Collaboration](https://www.conf42.com/Observability_2025_Pradeep_Karanam_ecad_mcad) at Conf42 Observability 2025.
