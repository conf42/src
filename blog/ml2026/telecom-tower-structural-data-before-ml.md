# Telecom towers need structured engineering data before machine learning

Conf42 Blog, 2026-01-29, updated 2026-11-09. https://www.conf42.com/blog/ml2026/telecom-tower-structural-data-before-ml

In short: Crown Castle's Sudarshan Kasera at Conf42 Machine Learning 2026 on turning telecom tower structural analysis into ML-ready data in the 5G era.

Many US telecom towers were designed in the 1980s and 1990s for much lighter antennas than 5G hangs on them today. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Sudarshan Kasera, a structural engineer and senior project engineer at Crown Castle with more than ten years in the tower industry, explained how tower analysis works and why the route to predictive models runs through structured engineering data first.

His message to the tech audience is repeated on purpose: the engineering fundamentals must come first. It's a bridge talk between infrastructure and data people, not an ML methods talk.

## Heavier equipment, older steel

Each wireless generation from 2G to 5G has added load: bigger, heavier equipment on ageing structures, while densification and rural broadband keep the market growing. Towers carry public safety and emergency communications, so continuous uptime is a hard requirement, and structural analysis has to account for every component accurately.

## The code stack is the spec

Before analytics, Kasera lays out the standards that govern every tower in the US. The International Building Code is the legal umbrella. ANSI/TIA-222 is the primary standard for antenna-supporting structures: self-support towers, monopoles, guyed towers. ASCE 7 supplies the environmental loads, from wind speed maps to ice and seismic parameters. AISC 360 governs steel members and connections, ACI 318 the concrete foundations. Any automation has to stay fully compliant with that hierarchy.

The load types are the model inputs. Dead loads cover the tower and everything bolted to it, where accurate equipment inventory is where analytics can cut errors. Wind usually governs, and the wind load on antennas and appurtenances can exceed the load on the structure itself. Ice adds weight and projected area in cold climates. Seismic can control foundation design in high-seismic zones. Thermal effects are easy to overlook in guyed towers and long monopoles. Each produces large volumes of site-specific data.

## From PDF reports to queryable data

Software such as RISA Tower and TNX already automates hundreds of load combinations and member-by-member checks. The structural analysis report, with sealed drawings, is what gets a permit, and without a permit nothing gets built or modified. The problem is that results often live in isolated PDF reports. For operators that own anywhere from hundreds to over 40,000 towers, centralised data is the difference between one-off projects and portfolio-wide analysis.

The data he wants integrated: material properties and member dimensions, stress (demand-to-capacity) ratios across members and analysis runs, deflection and dynamic response such as natural frequency and vortex shedding, and digitised inspection records of corrosion, loose connections and foundation cracks that models alone can't predict.

## The maturity curve

Kasera's roadmap has five steps: traditional code-based analysis, digital 3D finite element modelling (where he places the industry today), data integration, analytics, and finally predictive analysis with ML. His warning to anyone keen to jump ahead: "you cannot skip straight to machine learning without first having structured high quality engineering data."

The payoff he describes is concrete: extending tower life beyond the original 25 to 30 year design expectation, with every extra five to ten years avoiding the cost of a new build; lower liability through traceable decisions; and capital planning based on portfolio data instead of emergencies and permit deadlines.

## Who should watch

Data and ML engineers working with physical infrastructure, utilities or telecom who need to understand the domain before modelling it, and structural engineers wondering what "ML-ready" would mean for their reports. Expect engineering standards, not neural networks.

## Related Conf42 talks

- [Aircraft observability: how digital twins turn flight data into predictive maintenance](https://www.conf42.com/Observability_2025_Divakar_Duraiyan_aircraft_digital_twins), Divakar Duraiyan (Tata Consultancy Services), Conf42 Observability 2025
- [AI-powered anomaly detection for telecom service reliability](https://www.conf42.com/Observability_2025_Ajay_Averineni_service_telecom_reliability), Ajay Averineni (IBM), Conf42 Observability 2025
- [AI-powered digital twins: patterns for smart manufacturing](https://www.conf42.com/Cloud_Native_2025_Vinoth_Manamala_digital_twins_manufacturing), Vinoth Manamala (TIBCO Software), Conf42 Cloud Native 2025

[Watch Sudarshan Kasera's talk](https://www.conf42.com/Machine_Learning_2026_Sudarshan_Kasera_monitoring_drift_models)

[Watch the talk on YouTube](https://youtu.be/FzbgXHv1SI0).

## Watch the talk

[Data-Driven Structural Intelligence for Telecom Towers in the 5G Era](https://www.conf42.com/Machine_Learning_2026_Sudarshan_Kasera_monitoring_drift_models) at Conf42 Machine Learning 2026.
