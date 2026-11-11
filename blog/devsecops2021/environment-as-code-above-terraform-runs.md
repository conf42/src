# Terraform builds the Lego pieces, Environment as Code builds the toy

Conf42 Blog, 2021-12-03. https://www.conf42.com/blog/devsecops2021/environment-as-code-above-terraform-runs

In short: Adarsh Shah (CompuZest) at Conf42 DevSecOps 2021 on why scaling IaC breaks down and Environment as Code, a control plane over many Terraform runs

Splitting a monolith Terraform setup into small, loosely coupled runs is the right move, right up until an app team asks for a whole environment and someone has to run networking, then EKS and Postgres, then the Kubernetes add-ons, in the right order, and tear it all down backwards. At Conf42 DevSecOps 2021, Adarsh Shah, founder and CEO of CompuZest, named the pain and proposed a layer above it: Environment as Code, a declarative definition of an entire environment with a control plane that orders the IaC runs, tracks state, detects drift and reconciles.

He says up front that some of the idea was new and he wanted feedback. Expect a concept talk with diagrams and a look at CompuZest's product, not a tutorial.

## Who has this problem?

Not everyone. Adarsh scopes the talk to teams that have already broken their IaC into smaller runs (separate state files for networking, platform-ec2, platform-k8s, postgres, k8s-addons), and already run them from a pipeline or GitOps rather than an engineer's laptop. If your setup still fits in one run, you will not hit most of this.

## Why don't monoliths or pipelines cut it?

To get a full environment out of split IaC you have two options. A monolith IaC couples everything and grows painful state files. Or you hand-roll pipelines in Jenkins or CircleCI that encode the dependency graph. The catch: your IaC is declarative and idempotent, but those pipelines are not. You write custom code for provisioning, teardown and failure handling, and failures mid-run usually get fixed by hand. "As you can tell, these options are inefficient, costly, and typically requires a dedicated team," Adarsh Shah said at Conf42 DevSecOps 2021.

Three more challenges pile on. Replicating environments means more custom code. Understanding them is hard: cloud dashboards confuse, and diagrams drawn in Visio or draw.io go stale and end up spreading wrong information. And drift is only detected when a pipeline next runs that particular IaC, and only within it, not across the environment.

## What is Environment as Code?

His analogy: infrastructure as code automates the Lego pieces; Environment as Code automates how they connect into the Lego toy. The definition from the talk: an abstraction over IaC that defines an entire environment declaratively, with a control plane managing environment state, including relationships between resources, detecting drift and enabling reconciliation, and supporting loose coupling, idempotency and immutability for the whole environment.

In practice you push the environment definition to source control. The control plane picks it up, records environment state and dependencies, and reconciles component by component. Terraform still provisions the actual cloud resources and keeps each component's own state. Teardown reverses the graph, starting from the leaf nodes.

## What do you get at the environment level?

- **One definition.** The example is a custom YAML format listing components, each with its IaC type (Terraform) and its dependencies, such as a component depending on networking. Any format would do.
- **An environment state file** with the last operation and status, plus each component's operation and status.
- **Idempotency.** His example: apply IaC for three VMs twice. Non-idempotent code gives you six; idempotent code gives three. Pipelines cannot offer that for a whole environment; a control plane tracking environment state can.
- **Immutability.** Instead of patching long-lived environments and accumulating drift, bring up a brand new environment and replace the old one, the same way immutable infrastructure replaces servers.
- **Visualisation** generated from the definition, so the diagram cannot go stale.
- **Drift detection and reconciliation**, a control loop much like Kubernetes controllers (you could build it with them), ideally with an approval step that shows the plan, since reconciling may destroy or recreate infrastructure.
- **Compare and promote** changes between environments, and GitOps for the whole thing: branch, validate, pull request, approve, merge, and the control plane reconciles.

## Who should watch

Platform teams that already split their Terraform and are now maintaining a pipeline full of ordering logic, and anyone who has ever torn down an environment by hand in reverse. The ideas map to tools you may already have, such as controllers and GitOps.

## Related Conf42 talks

- Dmytro Prekrasnyi on [managing multiple Terraform projects](https://www.conf42.com/DevOps_2024_Dmytro_Prekrasnyi_multiple_terraform_projects) at Conf42 DevOps 2024.
- Jim Sheldon on [Terraform, GitOps and Kubernetes for managing infrastructure](https://www.conf42.com/Cloud_Native_2022_Jim_Sheldon_terraform_gitops_kubernetes_manage_infrastructure_aac) at Conf42 Cloud Native 2022.
- Roberth Strand on [GitOps with Terraform and Kubernetes](https://www.conf42.com/DevOps_2023_Roberth_Strand_achieve_gitops_terraform_kubernetes) at Conf42 DevOps 2023.

[Watch Adarsh Shah's talk](https://www.conf42.com/DevSecOps_2021_Adarsh_Shah_From_IaC_to_Environment_as_Code) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From CompuZest

CompuZest, founded by Adarsh Shah, helps companies adopt infrastructure as code; its product zLifecycle is built on the Environment as Code concept shown in the talk, including the environment visualisation.

- CompuZest: [compuzest.com](https://compuzest.com/)
- The link Adarsh shares on every slide: [bit.ly/iac-to-eac](https://bit.ly/iac-to-eac)

[Watch the talk on YouTube](https://youtu.be/EAPe0r_yJgU).

## Watch the talk

[From Infrastructure as Code to Environment as Code: Challenges scaling IaC and how to resolve them](https://www.conf42.com/DevSecOps_2021_Adarsh_Shah_From_IaC_to_Environment_as_Code) at Conf42 DevSecOps 2021.
