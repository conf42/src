# Inject a Lost Response, Then Count the Writes

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Hanif Karimi](https://www.conf42.com/speaker_Hanif_Karimi) (Senior Manager @ Accenture). Page: https://www.conf42.com/Chaos_Engineering_2026_Hanif_Karimi_response_writes_inject

## Abstract

A failed response and a failed operation are different fault models. This talk starts with a local simulation in which a record is changed but the caller receives no acknowledgement. We count the resulting writes after a blind retry and after a retry under an explicitly assumed durable idempotency contract. Further cases change the payload and version precondition. The exercise shows how to state the fault window, decide what evidence is independent of the caller, and preserve an unresolved state until authoritative evidence is available. Attendees receive a small fault-scenario matrix they can adapt to their own services. This is an instructional simulation, not a chaos experiment against a deployed system.
