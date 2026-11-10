# A Rule Is a Door: What Changes When You Enforce an AI Agent's Rules in Code

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Dylan Merigaud](https://www.conf42.com/speaker_Dylan_Merigaud) (Freelance AI Engineer @ Merigaud Consulting). Page: https://www.conf42.com/MLOps_2026_Dylan_Merigaud_rules_agent_code

## Abstract

A coding agent that runs unattended for months is told what not to do in sentences. Does it listen? I kept each rule of one such agent in two forms: a sentence in an instruction file and, for some rules, code on the path of the action (a hook that refuses, a write path that rejects, a scheduler precondition). In a preregistered replay of 5 rules, 200 runs, one sentence cut violations from 100% to 0% on 2 rules and to 10% or 20% on 2 more. The door alone did not hold: 53% of runs still broke the 4 rules it covered, and one hook never fired in 10 of 10 runs that broke its rule. Where the write hook blocked, the block took effect 10 of 10 times. The talk covers the cases and what I check before I trust a guardrail.
