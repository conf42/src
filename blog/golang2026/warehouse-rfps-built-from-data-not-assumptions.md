# A 3PL proposal should be built from the customer's data, not last year's

Conf42 Blog, 2026-05-07, updated 2026-11-09. https://www.conf42.com/blog/golang2026/warehouse-rfps-built-from-data-not-assumptions

In short: Vivek Sander of Sunland Logistics Solution at Conf42 Golang 2026 lays out a six-layer, data-first method for warehouse design in 3PL RFP responses.

When a warehousing RFP lands with a tight deadline, the shortcut is to copy assumptions from the last similar customer and price that. At Conf42 Golang 2026, Vivek Sander, Director of Engineering at Sunland Logistics Solution, showed why that shortcut becomes a startup problem later, and laid out a six-layer framework for designing the warehouse from the customer's own data instead.

A note on scope first: despite the Go conference, this is a logistics solution-design talk with no code in it. It is about how a third-party logistics (3PL) provider turns raw operational data into a proposal that survives contact with the real floor.

## Generic proposals fail after you win

Vivek names the failure modes: costing based on assumptions, a fulfilment strategy that does not match the business, and a cost structure nobody can defend. The pricing looks fine on paper, then the disconnect between what was quoted and what the operation actually needs shows up during go-live, and the partnership starts eroding. Speed matters in RFPs, he says, but speed built on borrowed assumptions just moves the pain downstream.

## Six layers, each feeding the next

The method is a pipeline, which may be why it found an audience of engineers:

1. **Throughput analysis.** Inbound per day, peaks and daily variation, pallets handled; outbound order volume, shipment patterns, seasonality and lines per order. This defines true capacity, and every later decision rests on it.
2. **Order profile analysis.** Retail versus direct-to-consumer, SKU breadth, order size distribution. A business with a hundred SKUs needs different pick and zoning strategies from one with a thousand; single-line orders tend toward batch picking with segregation at staging, multi-line orders toward zone or wave picking.
3. **SKU and inventory profiling.** Velocity-based segmentation into fast, medium and slow movers, with fast movers placed near staging so pickers walk less. Less walking, more efficient labour, a cheaper solution.
4. **Layout and storage design.** Material flow, dock configuration and door counts from container and truck volumes, and a storage system that follows the inventory: low SKU count with deep inventory points to bulk storage, many SKUs with low pallet quantities points to racking, drive-in or flow racks.
5. **Labour modelling.** Engineered standards such as MTM and MOST put a time on every step (receiving, put-away, replenishment, picking, packing, shipping), with peaks built into annual hours plus supervisor and indirect labour ratios.
6. **Equipment and cost.** Automation such as AMRs or AS/RS earns its place at high volume and multi-shift operation; at low volume the ROI is not there and lift trucks and other material handling equipment make more sense.

## Traceable cost is the trust mechanism

The idea Vivek keeps returning to is that inputs define outputs. If the customer can trace each cost line back to throughput, square footage, infrastructure and equipment, they can trust both the solution and the price. It is the warehouse version of showing your working in a maths exam, and it earns the same marks.

Two steps are easy to skip under deadline pressure, and he argues against skipping either. Validate the throughput, order profile, layout and labour numbers with the customer before costing, because the customer knows their business. And document the data and decisions so they hand over cleanly to implementation, which is what makes the path from award to go-live faster and lower risk.

## Who should watch

Solution engineers and operations leads at 3PLs are the obvious audience. Software engineers building warehouse management, slotting or labour-planning tools will get a compact map of the inputs their users reason about, which is useful domain context even without code. If you came for goroutines, this is not that talk.

## Related Conf42 talks

- [Vishnu Prasad on supply chain reliability in warehouses](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses) at Conf42 DevOps 2026
- [Maimoon Saleem on logistics optimisation](https://www.conf42.com/Cloud_Native_2025_Maimoon_Saleem_logistics_optimization_efficiency) at Conf42 Cloud Native 2025
- [Pavan Boppidi on autonomy and AI in logistics](https://www.conf42.com/Feature_Flags_2026_Pavan_Boppidi_autonomy_ai_logistics) at Conf42 Feature Flags 2026

[Watch Vivek Sander's talk](https://www.conf42.com/Golang_2026_Vivek_Sander_data_driven_warehouse)

[Watch the talk on YouTube](https://youtu.be/nH8oUtZK8mQ).

## Watch the talk

[Data-Driven Warehouse Design for Scalable, Risk-Resilient 3PL RFPs](https://www.conf42.com/Golang_2026_Vivek_Sander_data_driven_warehouse) at Conf42 Golang 2026.
