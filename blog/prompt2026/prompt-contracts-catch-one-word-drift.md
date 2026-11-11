# Prompt contracts catch the one-word edit that flips the meaning

Conf42 Blog, 2026-10-23, updated 2026-11-09. https://www.conf42.com/blog/prompt2026/prompt-contracts-catch-one-word-drift

In short: Sachin Gupta (eBay) at Conf42 Prompt Engineering 2026 on prompt contracts, the schema, claim, tool and policy checks that stop prompt drift in CI.

"Debug logs are retained for 14 days" and "debug logs are not retained for 14 days" differ by one word, and in Sachin Gupta's demo the second one sailed through every check until he added the right one. At Conf42 Prompt Engineering 2026, Sachin, Member of Technical Staff at eBay, presented prompt contracts: turning the clauses of a prompt into written requirements, each backed by an automated check, so drift shows up in CI instead of in user complaints.

## Stable doesn't mean identical

His definition of drift is behavioural: a prompt-driven app moving away from its intended behaviour when the instructions or the surrounding conditions change. The running example is an IT assistant explaining debug log retention from a policy that says 14 days. "Debug logs are retained for fourteen days" and "we keep the debug logs for fourteen days" are both fine. Seven days, or "not retained", is not.

So stability means the requirements still hold under the changes you're testing, not that the wording never moves. And if the approved policy changes, the expected answer changes with it; the test follows the requirement, never the other way round.

## The harmless tone edit

The revision under examination is the kind every team makes: add a warmer, more reassuring tone for the engineer filing the incident. Reasonable intent, real risk. Reassurance can mean acknowledging the concern and saying the incident will be investigated; it must not become a promise that it will be resolved.

His clearer prompt names the boundaries explicitly: the task and evidence (explain retention from the supplied policy, preserve the period), the style boundary (supportive, without promising an outcome), the fallback (return insufficient evidence rather than guessing), and named output fields including a citation with an exact source quotation. He's careful to say rewritten wording is a design decision, not proof it works; its effect still needs evidence.

## Each clause becomes a check

The contract maps prompt to test. Required JSON becomes a schema check on fields and types. Exact source quotes become a check that the source exists and contains the quotation. No resolution guarantee becomes a forbidden-phrase check, which he admits has limited coverage. Preserving the policy meaning needs a separate check on the claim itself. Passing one row proves nothing about the others.

For comparisons, decide before editing which examples should pass and fail (normal requests, missing evidence, harmless paraphrases, boundary-pushing instructions), keep fresh cases outside the development set, run the unchanged baseline repeatedly first, and hold the model and generation settings fixed.

## The six-tab demo

The demo app, with Java checks, walks through six tabs. The baseline passes. The tone edit produces "your incident is guaranteed to be resolved" and the forbidden-claim check blocks it. The tool boundary tab is the sneaky one: the answer and its shape are fine, but the agent tries to close a ticket when it only had permission to create one, so the tool contract gate fails. Drift, he points out, isn't only in the text; tool calling drifts too.

Then the meaning escape: "not retained" gets released, because no bounded policy check existed. Add one and it's withheld. The final trade-off tab is a creative paraphrase that keeps the meaning; the system withholds it for human review rather than auto-passing something it can't confidently recognise.

A CI fixture suite ties it together: a valid control passes; forbidden guarantees, wrong tool, wrong tool version, wrong call order and policy contradictions fail; valid paraphrases and missing-evidence cases (where no tool should be called) pass.

## Who should watch

Teams shipping LLM features that talk about policy, support or anything with facts a user will act on, and anyone who has tweaked a prompt for tone and wondered what else changed. The demo uses prepared examples, so it shows the checks working rather than a measured comparison across live generations; Sachin says as much.

## Related Conf42 talks

- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler (Adobe) at Conf42 MLOps 2026.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev at Conf42 Large Language Models 2026.
- [Evals for Generators: Testing an LLM That Writes Clinical Configuration](https://www.conf42.com/MLOps_2026_Ocean_Coldiron_evals_clinical_configuration) by Ocean Coldiron (ModMed) at Conf42 MLOps 2026.

[Watch Sachin Gupta's talk](https://www.conf42.com/Prompt_Engineering_2026_Sachin_Gupta_drift_prompts_stable) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/c-ms45Ab_vs?si=evF_ziR1zuPOYKsY).

## Watch the talk

[Prompt Drift Kills: How to Make Prompts Stable](https://www.conf42.com/Prompt_Engineering_2026_Sachin_Gupta_drift_prompts_stable) at Conf42 Prompt Engineering 2026.
