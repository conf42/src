# An AI security gate in CI is only as good as the policy you give it

Conf42 Blog, 2026-05-18, updated 2026-11-09. https://www.conf42.com/blog/golang2026/ai-pipeline-guardrail-needs-your-policy

In short: Emmanuela Opurum of SoftNet Technologies at Conf42 Golang 2026 demos a CI/CD guardrail where an LLM agent checks code against a written policy and fails the build.

Static scanners look for a fixed list of problems, and a general-purpose AI model has no idea what your organisation considers a problem. At Conf42 Golang 2026, Emmanuela Opurum, Solutions/System Architect at SoftNet Technologies, showed a pipeline guardrail that sits between those two failures: an AI agent wired into the CI workflow, told exactly what to look for by a written policy, and allowed to stop the build.

It is a short, demo-led talk aimed at teams that want a working starting point rather than a framework, and she published the whole thing as a repository so viewers can reuse it.

## Fast pipelines ship vulnerabilities fast too

Emmanuela starts from the obvious tension. CI/CD exists to get code to production quickly, and without security checks it gets vulnerabilities to production just as quickly. Her critique of the usual fixes is that static analysis tools catch particular vulnerability classes without reflecting an organisation's own rules, while a standalone AI tool fails because it does not know your policy. Neither, on its own, knows what you care about.

## The flow: push, scan against policy, ship or stop

The architecture is deliberately simple, and she notes it carries over to whatever code platform you use:

1. A developer pushes to the GitHub repo, which triggers the workflow.
2. The workflow calls an agent (she used OpenAI's GPT-4o) loaded with a policy covering security detection, pattern scanning and policy validation.
3. If the agent finds nothing that violates the policy, the code proceeds to deployment.
4. If it does, the pipeline fails and a Slack message goes to the team with what failed, on which line, why, and a suggested fix.

The demo shows two runs. The first passes. The second fails because someone left an API key in a file, and the Slack alert names the problem and recommends removing hard-coded secrets in favour of environment variables. The leaked-key example is the oldest one in the book, which is exactly why it is still worth a gate.

## Humans stay in the loop at both ends

Her main lesson is about where people fit. An AI agent cannot decide what your organisation's security rules are; a human has to write the policy into the pipeline. And when the gate trips, a human still has to respond. What the agent changes is the speed of that response: instead of digging through logs to find why a build failed, the engineer gets the reason and a starting fix in the channel they already watch.

For next steps she suggests extending the policies to cover more languages and integrating the same gate into cloud deployment flows.

## How much Go?

Honest scope: the abstract frames this as Go-based automation for CI/CD across AWS, Azure and GCP, but the recorded talk spends its time on the workflow design, the agent policy and the Slack loop rather than on Go code. The repository, which she names on screen as GoCICD Security Guardrail under her cloud-architect-emma GitHub handle, is where the implementation lives.

## Who should watch

Platform and DevOps engineers who want a quick pattern for adding a policy-driven AI check to an existing pipeline, and teams starting out with DevSecOps who need a concrete first gate. If you already run secret scanning, SAST and policy-as-code in CI, this is a lightweight variation rather than a new technique, but the point about writing the policy down holds either way.

## Related Conf42 talks

- [Mert Coskuner and Cenk Kalpakoglu on securing CI/CD runners](https://www.conf42.com/Cloud_Native_2024_Mert_Coskuner_Cenk_Kalpakoglu_securing_ci_cd_runners) at Conf42 Cloud Native 2024
- [Rosemary Wang on handling secrets securely](https://www.conf42.com/Cloud_Native_2025_Rosemary_Wang_secrets_handling_security) at Conf42 Cloud Native 2025
- [Chinmay Gaikwad on CI/CD with agentic AI](https://www.conf42.com/DevOps_2026_Chinmay_Gaikwad_cicd_agentic_ai) at Conf42 DevOps 2026

[Watch Emmanuela Opurum's talk](https://www.conf42.com/Golang_2026_Emmanuela_Opurum_building_secure_pipelines)

[Watch the talk on YouTube](https://youtu.be/V0jzP1qWEA8).

## Watch the talk

[Building Secure CI/CD Pipelines with Go-Based Automation](https://www.conf42.com/Golang_2026_Emmanuela_Opurum_building_secure_pipelines) at Conf42 Golang 2026.
