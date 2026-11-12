# Your Monitors Approved Every Bad Fix: What Happened When AI Agents Repaired 64 Broken Pipelines

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Akshay Sharma](https://www.conf42.com/speaker_Akshay_Sharma) (Lead Member of Technical Staff @ Salesforce). Page: https://www.conf42.com/Chaos_Engineering_2026_Akshay_Sharma_agents_pipelines_monitors

## Abstract

AI agents are starting to fix production incidents, so we tested one on purpose. I built PipeMend, an open benchmark of 64 broken data pipelines, and let Claude agents of three sizes diagnose and repair them.  The uncomfortable result: production-style monitors approved every harmful fix the agents made. Row counts looked fine, jobs went green, and the data was wrong. The best warning sign wasn’t the monitoring at all. It was the agent’s own confidence score.  This talk walks through the experiment like a chaos game day: how the failures were injected, where the agents fixed the symptom instead of the cause, and why “the job succeeded” is the wrong check for AI-made changes. I’ll close with pipeverify, an open-source tool and GitHub Action that checks a pipeline change against the source data before it ships.  You’ll leave with a practical rule for letting agents touch production: decide whether to fix or page based on evidence, not green dashboards.
