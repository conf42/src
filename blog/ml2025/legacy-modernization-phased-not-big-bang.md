# Legacy modernization works in phases, and people decide if it sticks

Conf42 Blog, 2025-05-06, updated 2026-11-09. https://www.conf42.com/blog/ml2025/legacy-modernization-phased-not-big-bang

In short: Sasidhar Reddy Somula of Accenture at Conf42 Machine Learning 2025 on modernizing legacy systems in phases, with change management as the real budget line.

Most legacy systems are not broken. They are expensive, slow to change and impossible to retire, which is worse. At Conf42 Machine Learning 2025, Sasidhar Reddy Somula, Technology Architect and Application Development Manager at Accenture, argued that modernization succeeds when it is phased, measured and planned around the people who have to use the result, and that the technology choice is the easier half.

This is a strategy talk, not a code walkthrough. If you want Terraform, look elsewhere. If you are the person who has to explain to a steering committee why the mainframe migration needs a training budget, keep reading.

## The maintenance bill eats the innovation budget

Somula opens with the number every architect in a large enterprise has heard in some form: his slides put legacy upkeep at 60 to 80% of IT budgets. Whatever the exact figure in your shop, the shape is familiar. The money goes to keeping the old thing alive, and the new thing waits.

He frames three challenges that keep teams stuck. First, the financial one: transformation costs money before it returns any. Second, organizational culture, which resists change at least as hard as the code does. Third, the balancing act between stability and new capability. His analogy is fixing an airplane while it is still flying, which anyone who has done a zero-downtime cutover will recognize as optimistic about how much room there is in the cabin.

## Pick a migration pattern per application, not per company

The architecture section is the most practical part. Somula walks through the "six R" approach to cloud migration (rehost, replatform, refactor and friends) and makes the point that it is a per-application decision. Each system gets weighed on business criticality, technical debt and the performance it has to keep.

He singles out the strangler fig pattern as the safer route for systems that cannot go dark: replace functionality piece by piece behind a stable interface instead of a big-bang rewrite. His slides cite studies showing a meaningful risk reduction compared with big-bang approaches. The underlying logic needs no citation: a cutover you can roll back one slice at a time is a cutover you can survive.

Lift and shift gets a fair hearing too, with a caveat. Moving a problem to the cloud does not solve it. You just pay for it by the hour now.

## The failure mode is change management, not technology

The part worth the watch is the turn from architecture to people. Somula cites the oft-repeated figure that most digital transformations fail on change management rather than technology, then gets specific about what helps:

- incremental interface changes instead of an all-at-once UI swap
- change champions embedded in departments, who his slides credit with far higher adoption than rollouts without them
- digital adoption platforms and modern documentation (videos, interactive guides) instead of a PDF nobody opens
- real-time feedback channels so users can say what broke before they quietly route around it

His recommendation is concrete: set aside 15 to 20% of the modernization budget for training, support and adoption. That line item is the first thing cut in most project plans, which may explain a lot.

## Measure the outcome, not the migration

Somula closes with how to keep stakeholders on board: track business outcomes (cost, response time, adaptability, user satisfaction) alongside technical metrics, and show progress visually so the business side sees value before the final cutover. He also mentions using large language models for code analysis and dependency mapping during migration planning, which is the one place the talk touches the conference's machine learning theme directly.

His closing takeaways are short: balance stability with innovation, prioritize people, measure holistically, go phased. Transformation is a marathon, he says, not a sprint.

## Who should watch

Architects and engineering managers about to pitch, scope or rescue a modernization program will get a tidy framework and a vocabulary for the meeting. Engineers hoping for implementation detail on the strangler pattern or a migration war story can skip it; the talk stays at the strategy level, and many of its numbers come from industry studies on slides rather than one project.

## Related talks

- [Rajkumar Chindanuru on strategies for modernizing legacy applications](https://www.conf42.com/Golang_2025_Rajkumar_Chindanuru_legacy_modernization_strategies) at Conf42 Golang 2025
- [Hareesh Iyer on moving from monoliths to microservices in phases](https://www.conf42.com/Cloud_Native_2024_Hareesh_Iyer_modernize_monoliths_microservices) at Conf42 Cloud Native 2024
- [Swetha Lakkaraju on decoupling legacy banking cores](https://www.conf42.com/Internet_of_Things_IoT_2025_Swetha_Lakkaraju_banking_modular_modernization) at Conf42 IoT 2025

[Watch Sasidhar Reddy Somula's talk](https://www.conf42.com/Machine_Learning_2025_Sasidhar_Reddy_Somula_systems_legacy_modernizing)

[Watch the talk on YouTube](https://youtu.be/8I7ChAZgC0k).

## Watch the talk

[Modernizing Legacy Systems: Achieving Innovation and Stability for Future-Ready Enterprises](https://www.conf42.com/Machine_Learning_2025_Sasidhar_Reddy_Somula_systems_legacy_modernizing) at Conf42 Machine Learning 2025.
