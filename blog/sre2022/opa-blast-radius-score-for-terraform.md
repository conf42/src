# Give every Terraform plan a blast-radius score and let OPA say no

Conf42 Blog, 2022-06-08. https://www.conf42.com/blog/sre2022/opa-blast-radius-score-for-terraform

In short: Peter ONeill (Styra) at Conf42 Site Reliability Engineering 2022 on gating terraform apply with Open Policy Agent and Rego in a GitHub Actions pipeline

The Terraform change that hurts you is rarely malicious. It's the typo that creates 1,000 containers instead of 100, or the refactor that quietly strips every tag. At Conf42 Site Reliability Engineering 2022, Peter ONeill, Community Advocate at [Styra](https://www.styra.com/das-free?utm_medium=direct&utm_source=tradeshow&utm_campaign=dmge&utm_content=conf42sre_event-tradeshow) for the Open Policy Agent project, showed how to put OPA in the pipeline as a second set of eyes: score each plan's blast radius with a Rego policy and fail the build when it's too big.

It's a short talk with a working demo, and the demo repository is public, so you can lift the pattern directly.

## Declarative infrastructure, three phases

Peter starts with a driving analogy for infrastructure as code. Imperative is driving yourself and choosing every turn; declarative is naming the destination and letting a rideshare work out the route.

"So imperative is you decide each twist and turn on how to get there and then declarative is just wanting to get to the destination and letting the service handle the rest," Peter ONeill said at Conf42 Site Reliability Engineering 2022.

Terraform work then has three phases: code (write the manifests, pick the destination), plan (see the route, every resource to create or modify), and apply (drive it, and surface errors where reality no longer matches the plan). Running apply from a laptop is fine in dev. In a shared or production environment it belongs in continuous delivery or deployment, with GitOps rules: Git as the single source of truth, declarative HCL, every change versioned through a PR, and no manual changes that let real state drift from the repo.

## Authorization is more than keeping attackers out

The authorization step sits between the delivered plan and the deployment. Peter's list of what it has to protect against: secrets (don't store keys in code), malicious actors known and unknown, unintentional changes such as deleting all tags from a set of resources, and radical changes outside the usual parameters, like the extra zero. In a continuous deployment model, where code goes straight from the repo to infrastructure, policy is what replaces the human approver.

## Why decouple policy from the service?

OPA is a general-purpose policy engine: it takes a query as JSON and returns a decision as JSON, so it works with Terraform or anything else. Policies live outside the service that asks for the decision, written in Rego, a declarative policy language that fits the same GitOps flow as the HCL next to it. That gives policies their own life cycle: you can change what is enforced without restarting services or recreating resources.

His secured pipeline has five steps: write the manifests, validate locally with OPA before committing, open a PR, let automated testing (GitHub Actions in the demo) authorize the plan against the Rego policies, and only then let Terraform deploy.

## The demo: 16 instances fail, 3 pass

The demo uses the AWS EC2 module and a Rego policy with a blast radius of 30. Each planned action carries a weight: a delete scores 10, a create 2, a modify 1. The first test case creates 16 EC2 instances, scoring 32, just over the limit. The second creates three, scoring 6.

Locally, Peter runs terraform plan, converts the binary plan to JSON and asks OPA for the score rule with opa eval: 32. Pushed anyway, the GitHub Actions workflow installs Terraform and OPA, runs format, init, validate and plan, converts the plan to JSON, and hands it to OPA, which exits with status 1. Cut the change to three instances and the same pipeline goes green, ready to hand to the deployment system. A small detail he points out: the rule name used for the decision is just a variable, not a Rego keyword, so name it allow, deny or whatever reads best.

## Who should watch

Platform and SRE teams running Terraform through CI who want a guardrail cheaper than a human reviewer on every plan. If you already use OPA with Kubernetes admission control, this shows the same engine on infrastructure plans.

He also points to other routes to the same idea: opa exec, Conftest (built on OPA and Rego), and OPA's integration with AWS CloudFormation hooks. Related Conf42 talks: Ara Pulido on [policy as code with OPA Gatekeeper](https://www.conf42.com/Cloud_Native_2021_Ara_Pulido_poilcyascode_kubernetes_opa_gatekeeper), Noaa Barki on [OPA, Conftest and Gatekeeper in action](https://www.conf42.com/Cloud_Native_2022_Noaa_Barki_open_policy_agent_conftest_gatekeeper_kubernetes_policy_in_action), and Hila Fish on [Terraform practices](https://www.conf42.com/Cloud_Native_2022_Hila_Fish_terraform_practices).

[Watch Peter ONeill's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Peter_ONeill_terraform_apply_secured_open_policy_agent) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From Styra

Styra created Open Policy Agent; Styra DAS is its policy management product, and Styra Academy offers OPA courses. The talk's resources:

- [Styra DAS Free](https://www.styra.com/das-free?utm_medium=direct&utm_source=tradeshow&utm_campaign=dmge&utm_content=conf42sre_event-tradeshow)
- [Styra Academy](https://academy.styra.com/)
- [Open Policy Agent documentation](https://www.openpolicyagent.org/docs/latest/)
- [The demo repository](https://github.com/peteroneilljr/Conf42-and-open-policy-agent)

[Watch the talk on YouTube](https://youtu.be/bRyDk5IFB2Q).

## Watch the talk

[Terraform apply secured by Open Policy Agent](https://www.conf42.com/Site_Reliability_Engineering_2022_Peter_ONeill_terraform_apply_secured_open_policy_agent) at Conf42 Site Reliability Engineering 2022.
