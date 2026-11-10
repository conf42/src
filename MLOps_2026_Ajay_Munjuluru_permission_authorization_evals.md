# Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Ajay Munjuluru](https://www.conf42.com/speaker_Ajay_Munjuluru) (Sr. Lead Software Engineer @ JPMorgan Chase). Page: https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals

## Abstract

Most agent evaluation suites measure accuracy, helpfulness, and task completion. Few test whether the agent reveals data the current user isn’t allowed to see. In regulated environments, that gap is the one that matters most.  This talk shows how to treat authorization as a testable property of an agent system and run it in the delivery pipeline like any other regression suite. Drawing on experience building multi-agent systems over enterprise banking CRM data, it covers:  Persona-based test users with different entitlements running the same tasks Leak assertions that check responses, summaries, and tool calls for restricted facts Combination tests that catch disclosures created when individually permitted results are joined Regression triggers for model upgrades, prompt changes, and new tools Making failures debuggable by linking each leak to the tool call and context that caused it  Attendees will leave with a blueprint for adding authorization evals to their agent release process.
