# When Agents Fail in Production: Incident Stories and Recovery Patterns

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Meher Bhaskar Madiraju](https://www.conf42.com/speaker_Meher_Bhaskar_Madiraju) (Senior Data Scientist @ Walmart Global Tech). Page: https://www.conf42.com/Chaos_Engineering_2026_Meher_Bhaskar_Madiraju_agents_incident_recovery

## Abstract

The most instructive production lessons come from things breaking. This talk is a field guide to agentic AI incidents drawn from running multi-agent systems in production at retail scale: the agent that confidently presented hallucinated inventory numbers to merchants, the runaway tool-call loop that burned a week's inference budget in an afternoon, the silent data drift that corrupted outputs for days before anyone noticed, and the cascading failure when one agent's bad output poisoned every downstream step. For each incident: what broke, how it was detected (or why it wasn't), the recovery playbook, and the engineering change that prevents recurrence. Attendees leave with a catalog of failure modes to defend against and detection patterns that catch them early.
