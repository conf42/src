# Telecom AI will copy old investment bias unless you code against it

Conf42 Blog, 2026-03-25, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/telecom-ai-fairness-carbon-in-the-pipeline

In short: Researcher Bhavika Reddy Jalli at Conf42 Cloud Native 2026 on algorithmic redlining in 5G/6G automation and putting fairness and carbon checks into pipelines.

Train a capacity-planning agent on ten years of telecom investment data and it will learn, very efficiently, that rural regions do not matter. At Conf42 Cloud Native 2026, independent researcher Bhavika Reddy Jalli argued that as 5G gives way to 6G and algorithms take over spectrum allocation, fault detection and power management, fairness and carbon accounting have to be engineered into cloud-native network pipelines rather than written into a policy PDF.

This is a research talk, not a tooling demo. It draws on her work on the societal effects of deep learning and agentic AI in telecommunications, and it is upfront that its central example is hypothetical, though grounded in documented patterns.

## Low usage is not the same as low demand

The starting point is the connectivity divide. Bhavika cites figures of 4.5 billion people with high-speed access, 1.5 billion with limited connectivity and 1.1 billion with none, much of the last group in Sub-Saharan Africa. (The talk abstract gives 4.0 billion for the first figure; the recording says 4.5.) Operators have historically invested in high-revenue urban areas. An allocation model trained on that history reads thin usage in an underserved region as weak demand, when the real cause is that nobody built the infrastructure.

The paper behind the talk calls this algorithmic redlining. The cloud-native twist is speed: skewed training data produces skewed allocation policies, those policies get deployed automatically across edge nodes, and the resulting coverage gaps feed back into the next round of training data. Each layer amplifies the one upstream, and it happens before a human gets a chance to notice.

## The worked example: 500 edge nodes and one reward function

The hypothetical is concrete enough to reason about. A national operator trains a reinforcement learning agent on a decade of investment data to automate base station capacity planning across 500 edge nodes. Rural regions with historically low usage get deprioritized, because a skewed reward signal tells the agent that is the efficient choice.

The fixes she proposes are equally concrete: coverage equity thresholds as hard constraints inside the RL reward function, geographic fairness audits at each deployment stage, and demographic parity checks before and after rollout. She reports that such interventions have shown rural coverage improving by 23% while urban efficiency gains were preserved. Her blunt summary of the alternative is that without these guardrails, optimization defaults to the high-revenue areas.

## Net carbon, not gross savings

The second thread is what she calls the sustainability paradox. Reinforcement learning can cut idle base station energy by replacing static, peak-power capacity planning with dynamic optimization, and digital twins let operators test strategies before touching real hardware. But training and continuous inference across edge and cloud cost real compute. Whether the network ends up greener depends on whether the efficiency gains outweigh the AI footprint, and that varies by deployment.

Hence her takeaway that sustainability requires net accounting. Measure the energy cost of training, inference and continuous relearning across the whole lifecycle, not only the watts saved at the base station.

## Governance as four things in the pipeline

The framework has four parts: transparency for regulators and operators, fairness evaluation that tests models against geographic and demographic equity metrics, accountability mapping so every automated decision traces to a responsible owner across microservices, and carbon reporting wired into CI/CD so each model update and inference workload carries a measured cost. The engineering message is that this runs continuously from training data curation through post-deployment observability, not as a gate at the end.

She also pushes back on the idea that governance slows teams down. Building auditability in from day one makes new regulation cheaper to absorb than retrofitting, and transparency becomes a trust asset with regulators, communities and enterprise customers.

## Who should watch

Engineers and architects working on network automation, RL-driven resource allocation, or any system where historical data encodes past underinvestment. Platform teams thinking about carbon metrics in CI will find the net-accounting framing useful. If you want code or a reference implementation, this talk stays at the framework level.

## Related Conf42 talks

- [Neelima Verma on why a compliant ML model may still be causing the most harm](https://www.conf42.com/MLOps_2026_Neelima_Verma_fairness_compliant_harm) at Conf42 MLOps 2026.
- [Ajay Averineni on AI-powered anomaly detection for telecom service reliability](https://www.conf42.com/Observability_2025_Ajay_Averineni_service_telecom_reliability) at Conf42 Observability 2025.
- [Sai Charan Madugula on software-defined networking for IoT and 5G](https://www.conf42.com/Cloud_Native_2025_Sai_Charan_Madugula_networking_iot_5g) at Conf42 Cloud Native 2025.

[Watch Bhavika Reddy Jalli's talk](https://www.conf42.com/Cloud_Native_2026_Bhavika_Reddy_Jalli_ai_agents_decisioning)

[Watch the talk on YouTube](https://youtu.be/hdNBeK9DsnM).

## Watch the talk

[Responsible Agentic AI for Equitable and Sustainable Cloud Native Telecom](https://www.conf42.com/Cloud_Native_2026_Bhavika_Reddy_Jalli_ai_agents_decisioning) at Conf42 Cloud Native 2026.
