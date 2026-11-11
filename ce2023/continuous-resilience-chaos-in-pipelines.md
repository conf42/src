# Measure resilience coverage like code coverage and let the pipeline roll back

Conf42 Blog, 2023-02-16. https://www.conf42.com/ce2023/continuous-resilience-chaos-in-pipelines

In short: Uma Mukkara (Harness) at Conf42 Chaos Engineering 2023 on continuous resilience, chaos experiments in CD pipelines scored and gated like tests

Chaos engineering usually gets sold as outage reduction for SREs. At Conf42 Chaos Engineering 2023, [Uma Mukkara](https://www.conf42.com/Chaos_Engineering_2023_Uma_Mukkara_continuous_resilience), Head of Chaos Engineering at Harness and co-founder of the LitmusChaos CNCF project, pitches it as a developer productivity tool instead: run chaos experiments in every pipeline stage, score each run, track resilience coverage the way you track code coverage, and let a low score roll the deployment back. He calls the pattern continuous resilience.

The demos run on Harness Chaos Engineering and Harness pipelines, but he notes that any pipeline tool plus any chaos tool can do the same.

## Why make this a developer problem?

He starts with money. The slides put it at 27 million developers worldwide on an average $100K salary, $2.7 trillion of annual payroll, while a poll he cites says more than half of developers spend less than 3 hours a day writing code. The rest goes on toil: building environments, deploying and debugging. His slides claim that halving that toil would redirect $675 billion back into development.

Debugging is the slice he goes after, and he lists why bugs leak: plain oversight, untested dependencies, new people who don't know the whole architecture, and code that meets an environment it wasn't written for. Cloud native makes the last three worse. Developers ship fast, focused on one container and its APIs, while faults in deep dependencies (APIs, databases, message queues, Kubernetes itself) carry the biggest outage impact. Finding such a bug in production costs more than ten times what it costs in QA. So cloud native developers need chaos testing for the dependencies their code relies on.

## What is continuous resilience?

Traditional chaos engineering has been reactive, or driven by regulations such as banking disaster recovery, and built on game days: on-demand, heavily prepared, run by SREs, with a high adoption barrier. The newer drivers are developer productivity, quality for QA teams facing a flood of microservices, and confidence when moving a business-critical monolith to cloud native.

"So chaos engineering, done in automated way across your DevOps spectrum, is called continuous resilience," Uma Mukkara said at Conf42 Chaos Engineering 2023. Dev, QA, pre-prod and eventually production, with all personas involved. Unlike game days, pipeline experiments run continuously with little preparation, and a failure just slows a build down.

## The two metrics

- **Resilience score**: the average success percentage of the steady-state checks during an experiment, for an experiment, a component or a service.
- **Resilience coverage**: chaos tests executed divided by the total possible chaos tests, times 100. The possible tests come from combining the resources a service is made of, from infrastructure and network to APIs and containers.

Coverage fixes an old problem: with game days nobody knows how many more experiments are needed, and SRE time for writing them is never budgeted. In the continuous model it becomes a team sport. Developers extend their integration tests with dependency faults, QA reuses and adds to them, SREs reuse those, and everything lives as code in git, in shared chaos hubs.

## What do the demos show?

An experiment in Harness Chaos Engineering is one or more faults, in series or parallel, each with a target, duration and repetitions, plus probes that check the steady state while the fault runs. His example injects a CPU hog into a pod with three probes: the pod's health, an HTTP endpoint, and the latency of a separate front-end service. Watch the wider system, not just the pod you are hurting. All three passed, so the score was 100%. The hubs also get access control, down to game day reports that nobody can delete.

In the pipeline, a chaos experiment is just another step after deployment and functional tests, with an expected resilience score and a failure strategy if it is missed: observe, ask for manual intervention, or roll back. In the failed run he shows, the CPU-stressed service stayed available, but a different service hit a latency problem, the probe failed, and the stage rolled back. The second demo is a pipeline Harness uses internally: the existing stages are untouched, and a separate step group runs several chaos experiments in parallel whose combined scores decide whether to proceed.

## Who should watch

Platform and DevOps engineers who own CD pipelines, and SREs tired of being the only people who write chaos experiments. If you already run LitmusChaos, this is the clearest statement of where its authors think the practice is going.

Related Conf42 talks:

- Uma Mukkara on [continuous SLO validation with chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering), Conf42 SRE 2021.
- Akram Riahi on [chaos engineering alongside Litmus and Jenkins](https://www.conf42.com/Chaos_Engineering_2022_Akram_Riahi_chaos_engineering_alongside_litmus_and_jenkins), Conf42 Chaos Engineering 2022.
- Mandi Walls on [game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering), Conf42 Incident Management 2022.

## From Harness

Harness builds the software delivery platform used in both demos, including Harness Chaos Engineering with its chaos hubs, probes and resilience scores, and its CD pipelines with chaos steps and rollback strategies.

- [Harness](https://www.harness.io/)

[Watch the talk on YouTube](https://youtu.be/8bUiFaPqRj8).

## Watch the talk

[Continuous Resilience with Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2023_Uma_Mukkara_continuous_resilience) at Conf42 Chaos Engineering 2023.
