# What platform teams can borrow from a century of car platforms

Conf42 Blog, 2025-08-17, updated 2026-11-09. https://www.conf42.com/blog/platform2025/platform-lessons-from-car-factories

In short: Nikunj Karoliya of Pebble Mobility at Conf42 Platform Engineering 2025 maps VW's MQB, Ford's shared platforms and Tesla OTA onto internal developer platforms.

Car makers solved the problem of many products built from shared parts decades before anyone wrote an internal developer platform. At Conf42 Platform Engineering 2025, Nikunj Karoliya, Lead Engineer at Pebble Mobility, walked through how automotive manufacturing handles modularity, standardisation, versioning and technical debt, and what each lesson means for software platform teams.

This is an analogy talk, and a well-chosen one. There is no code; the value is in the mental models and the concrete automotive examples behind them.

## Shared chassis, different cars

Early car makers built every model as a one-off with its own components and assembly lines: duplication, siloed expertise, slow and expensive scaling. The shift to shared platforms (common chassis, interchangeable parts, unified processes across vehicle lines) is the same shift software made towards shared services and internal platforms. His motto for it: build once, reuse often.

Karoliya grounds the parallel in three architecture principles:

- **Separation of concerns.** Chassis, powertrain and user-facing features are designed by independent teams who meet at well-defined interfaces, just as infrastructure, backend and frontend teams meet at API contracts.
- **A flexible foundation.** Volkswagen's MQB platform supports both combustion and electric powertrains through standardised mounting points. The software equivalent is one API layer over both containers and serverless functions.
- **Standard interfaces.** Hundreds of electronic control units talk over protocols such as CAN and FlexRay so a brake system from one supplier works with traction control from another. In software that is gRPC, REST and event buses.

## Standardise the suspension bolts, not the interior

The sharpest section is on what to standardise. Car makers standardise chassis frames, suspension mounting points and crash structures: heavy engineering, strict regulation, and nobody buys a car for its rear suspension bolts. They keep freedom for the interior, the driving feel and infotainment.

Translated: authentication, logging, monitoring and deployment pipelines are your chassis. Rebuilding them per team adds cost and no value. Recommendation engines and UI personalisation are your interior. His example is a company with both a food delivery and a ride-hailing app: share payment processing, let each product own its matching algorithm and tracking UI.

## Versioning for things that live 20 years

Cars stay on the road for 10 to 20 years, so replacement parts must stay compatible across generations. Karoliya uses that to argue for architecture review boards that keep a platform coherent, explicit backward-compatibility and long-term support policies, and stability guarantees for components like identity and billing that other teams depend on. Moving fast is fine for features; your logging library should be boring for years.

Across product lines, that means dependency tracking to see the ripple effect of a change, coordinated phased releases, and extensive compatibility testing. Ford introducing a new part to the F-150 line through testing, pilot runs and phased rollout is, in his telling, a canary release with a supply chain attached.

## Technical debt measured by impact, not age

Automakers cannot wipe the slate clean with each model; tooling, training and supply chains represent decades of investment. They modernise behind abstraction layers so new components fit old platforms. Karoliya recommends the same for software (APIs, adapters and bridges instead of a big-bang rewrite) and a definition of debt that counts code that slows you down or blocks integration, not merely old code.

## Platform teams and product teams, Ford edition

The organisational example is Ford moving from vehicle-line teams (one for the F-150, another for the Mustang) to cross-functional platform teams owning shared architecture, with the F-150 and Ranger sharing much of their platform while product teams focus on model-specific features. Add centres of excellence, training and internal conferences to spread the knowledge, and you have the platform-team operating model in sheet metal. Tesla's over-the-air updates and Volkswagen's MEB electric platform close the talk as the point where cars became software platforms in their own right.

## Who should watch

Platform leads who need to explain to leadership why shared components, governance and versioning policies matter; the automotive vocabulary lands well with non-engineers. If you already run a mature platform org, the standardisation and versioning sections are still a good sanity check.

## Related Conf42 talks

- Maksim Lykov on the [IT revolution in the automotive business](https://www.conf42.com/Internet_of_Things_IoT_2024_Maksim_Lykov_it_automotive_business) at IoT 2024.
- Sumaiyya Fatima on [observability-driven hardware-in-the-loop validation for software-defined vehicles](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation) at Observability 2026.

[Watch Nikunj Karoliya's talk](https://www.conf42.com/Platform_Engineering_2025_Nikunj_Karoliya_complex_automotive_manufacturing)

[Watch the talk on YouTube](https://youtu.be/bDBIybL5R_w).

## Watch the talk

[Platform Engineering Principles in Complex Systems: Lessons from Automotive Manufacturing Transformation](https://www.conf42.com/Platform_Engineering_2025_Nikunj_Karoliya_complex_automotive_manufacturing) at Conf42 Platform Engineering 2025.
