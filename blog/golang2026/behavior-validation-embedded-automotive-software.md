# Correct code can still fail the car, so validate behaviour early

Conf42 Blog, 2026-04-22, updated 2026-11-09. https://www.conf42.com/blog/golang2026/behavior-validation-embedded-automotive-software

In short: Sana Fatima of General Motors at Conf42 Golang 2026 on behaviour-driven validation that catches cross-module defects before vehicle-level testing.

A chassis control module can be correctly written, compile cleanly, pass every unit test and still misbehave once it shares a bus with the brakes and the steering. [Sana Fatima](https://www.conf42.com/Golang_2026_Sana_Fatima_from_code_correctness), Software System Test Engineer at General Motors, spent her Conf42 Golang 2026 talk on that gap: the defects that matter in software-defined vehicles are increasingly behavioural mismatches between correct modules, and the fix is to make expected behaviour an executable artifact from the design phase on.

Despite the conference, this is not a Go talk. It is a validation-process talk from someone with more than ten years in automotive software and system validation, and it applies to any system built from modules that each "work".

## Unit tests stop at the boundary

Sana's framing is that validation falls short in three places. Unit testing ends at the module edge, so cross-module assumptions are never stated, let alone checked. Behavioural intent lives in documents and tribal knowledge instead of anything a pipeline can run. And integration gets tested late, at system or vehicle level, which is exactly where diagnosis and rework are most expensive.

The stakes she describes are structural: modern vehicles carry over a hundred ECUs and tens of millions of lines of code from multiple suppliers, sharing buses and dependencies. One violated assumption can cascade into something safety relevant. Defects found at vehicle validation can trigger regression cycles across supplier teams and even hardware re-spins.

## Coding errors are the easy class now

The sharpest point in the talk is the distinction between coding errors and behavioural mismatches. Modern toolchains, and increasingly AI tools, are good at catching the first. The second is individually correct modules producing an incorrect system outcome, and it needs a different kind of validation.

The classes she lists are worth stealing for any test strategy review: timing violations across module boundaries that isolated tests can't see, violated interface contracts (mismatched assumptions about signal ranges or error handling between producer and consumer), invalid state combinations that only appear under specific input sequences, and faults handled locally that propagate differently once integrated.

## Specs as the single source of truth

Behaviour-driven validation, as Sana lays it out, starts with explicit behavioural specifications treated as a first-class engineering artifact: expected responses, state transitions and timing constraints. They are written in structured natural language such as Gherkin-style given-when-then, or as state machines, and broken down to module level so that software and tests are built from the same source in parallel.

Those specs become executable tests that run on every build and integration event in CI, not once at vehicle level. When a test fails, you check the code and the requirement together, because traceability runs from requirement to test to implementation. That same trace gives you the auditable evidence that ISO safety work and ASPICE expect, which is the quiet business case: the test record doubles as compliance paperwork.

## Who should watch

Test and validation engineers in automotive, aerospace, medical or industrial control, and anyone whose integration phase keeps producing surprises that unit tests swore weren't there. It is conceptual rather than hands-on: no framework demo, no code. If you already run BDD-style specs in CI with requirement traceability, you can skim it.

## Related Conf42 talks

- [Scalable HIL Architecture: Observability-Driven Validation in Software-Defined Vehicles](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation) by Sumaiyya Fatima, the hardware-in-the-loop side of the same problem.
- [BDD with JUnit 5 and Cucumber](https://www.conf42.com/Enterprise_Software_2021_Catalin_Tudose_bdd_junit_5_cucumber) by Catalin Tudose, given-when-then made concrete in code.
- [Building Robust V2X Communication Networks in Go](https://www.conf42.com/Golang_2025_Utham_Kumar_v2x_communication_vehicles) by Utham Kumar, for the connected-vehicle software Go actually runs.

[Watch Sana Fatima's talk](https://www.conf42.com/Golang_2026_Sana_Fatima_from_code_correctness)

[Watch the talk on YouTube](https://youtu.be/8pL1nBOSjtw).

## Watch the talk

[From Code Correctness to Behavior Validation: Detecting Defects Early in Embedded Automotive Software](https://www.conf42.com/Golang_2026_Sana_Fatima_from_code_correctness) at Conf42 Golang 2026.
