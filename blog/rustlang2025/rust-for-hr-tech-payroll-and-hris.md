# Why Rust fits HR tech, from payroll runs to open enrollment

Conf42 Blog, 2025-08-21, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-for-hr-tech-payroll-and-hris

In short: Swetha Priya Sathiyam of ADP at Conf42 Rustlang 2025 on how Rust's safety and concurrency map onto HRIS systems that touch every employee.

HR systems are one of the few enterprise platforms that touch every person in a company, from the day they are recruited to their last paycheck. At Conf42 Rustlang 2025, Swetha Priya Sathiyam, Director of Solution Design for ADP Lyric HCM at ADP, made the case that Rust's safety and concurrency guarantees line up unusually well with what an HRIS has to get right.

Be clear on the scope: this is an architect's argument for where Rust could fit in HR technology, built on domain experience and published case studies, not a tour of a Rust codebase at ADP. Taken that way, it is a useful map of a domain most Rust talks never visit.

## Open enrollment is a load test with a deadline

Swetha traced HR tech through three eras: paper files and timecards, mainframe and on-premise HRIS (with core payroll still in COBOL at many large companies, reliable but expensive to change), and today's cloud suites like Workday, SAP SuccessFactors and Oracle Cloud HCM.

Her point is that even the modern platforms hit scaling walls. She described open-enrollment windows where a benefits page took minutes to load because everyone logged in at once. Every HR engineer knows the calendar: the traffic spike is scheduled, and so is the outage if you are unlucky.

## The domain maps neatly onto Rust's features

The most interesting part of the talk is how specific the mapping gets.

Memory safety matters more than usual because the data is Social Security numbers, bank details and medical information. Fearless concurrency matters because payroll, benefits processing and a performance cycle can all be running at once for tens of thousands of employees. Explicit error handling forces you to decide what happens when a tax rate file is missing or a benefits vendor API is down, instead of finding out on payday.

Her best example is the type system. A job grade, she noted, is not a number: it is tied to bands, locations and rules. Rust lets you model that in types so invalid combinations do not compile. The same goes for workflows: a state machine can make it impossible to mark a candidate as hired before the background check completes.

## A reference architecture in layers

Swetha sketched a modular Rust HRIS: a data layer with compile-time checked queries, an API layer on Actix Web for employee self-service portals that must absorb spikes, authentication with strong cryptography and role-based access control modelled in code rather than config, and async background jobs for payroll batches and compliance reports. Her payroll example runs tax calculations per jurisdiction concurrently and merges the results.

Security got its own section: RBAC in the code, tamper-evident audit logging of every access to sensitive data, and the ownership model as a natural fit for data lifecycle rules like deletion after a retention period, which matters for GDPR and HIPAA.

## The case studies, and the practices

She cited case studies she researched, including a financial services firm moving payroll from COBOL to Rust with a large cut in processing time, a tech company replacing a Java onboarding app that crashed during graduate hiring, and a healthcare platform meeting HIPAA requirements. The companies are not named, so treat these as illustrations.

The best-practice list is solid and transferable: domain-driven design to model HR processes, consistent error handling so payroll failures surface early, end-to-end tests for compliance and data integrity, minimal `unsafe`, audited third-party crates, and documented HR logic so the next team can onboard.

## Who should watch

Engineers and architects in HR, payroll or other regulated enterprise systems who are weighing Rust for a new service. Rust specialists will not learn new language tricks here, but they will get a sharp picture of a domain where correctness has a payday.

## Related Conf42 talks

- [SBB: Secure Building Blocks in Rust](https://www.conf42.com/Rustlang_2023_Yashwanth_Singh_M_sbb_secure_building_blocks) by Yashwanth Singh M: security primitives for the PII-heavy parts.
- [Employee Self-Service in SAP HR with SAPUI5 and JavaScript](https://www.conf42.com/JavaScript_2024_Lakshmi_Gogula_ess_sap_hr_sapui5) by Lakshmi Gogula: the self-service portal side from the SAP world.
- [Fall in LOVE with Unit Testing!](https://www.conf42.com/Rustlang_2023_Joe_Skeen_love_unit_testing) by Joe Skeen: for the "comprehensive tests" part of the checklist.

[Watch Swetha Priya Sathiyam's talk](https://www.conf42.com/Rustlang_2025_Swetha_Priya_Sathiyam_systems_memory_code)

[Watch the talk on YouTube](https://youtu.be/ddAX1IM-K7Q).

## Watch the talk

[Building the Future of HR Tech with Rust: Revolutionizing Employee Experience](https://www.conf42.com/Rustlang_2025_Swetha_Priya_Sathiyam_systems_memory_code) at Conf42 Rustlang 2025.
