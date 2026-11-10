# You can't rerun sunlight, so store what the model knew at the time

Conf42 Blog, 2026-11-10. https://www.conf42.com/mlops2026/you-cant-rerun-sunlight-physical-ai-data

In short: An Phan (Hippo Harvest) at Conf42 MLOps 2026 on data architecture for physical AI: late sensor data, backfills and point-in-time reproducibility.

After a backfill, yesterday's dataset can look complete even though the model that made yesterday's decision never saw half of it. At Conf42 MLOps 2026 on November 19, An Phan, Senior Data Infrastructure Engineer at Hippo Harvest, explains how to design ML data architectures for physical AI that preserve what the system knew at the moment it decided, not just what we know now.

## Software can retry. Crops can't.

The title is the whole argument in four words. In software, when something goes wrong, we retry. In machine learning, we rerun a pipeline, backfill missing data, or reproduce a model with the same code and inputs. All of that assumes the inputs can be produced again.

Physical AI breaks the assumption. Data comes from sensors, cameras, robots and real environments. It can arrive late, be corrected later, or never be captured at all. The afternoon light over a crop on a given Tuesday happened once. You can rerun the pipeline and rerun the model, but the world that produced the data has moved on.

## Complete is not the same as correct-at-the-time

The most interesting idea in the talk is a distinction that is easy to miss: the dataset as it looks today versus the dataset as it looked when a decision was made.

Late-arriving data and backfills are good for analytics. They fill gaps and fix errors. For explaining or reproducing a model decision, they can mislead you. If you debug yesterday's robot action against today's backfilled table, you are judging the model on information it did not have. That is not reproducibility; it is hindsight with a schema.

An's answer is architecture that keeps both views: what we know now, and what the system knew at decision time. In data terms, that is point-in-time reproducibility, applied all the way from physical events through ML pipelines to downstream decisions.

## Lessons from robots in agriculture

The talk draws on An's work building data infrastructure for robotics and machine learning in agriculture at Hippo Harvest. The topics on the list are the ones that bite in practice:

- late-arriving data from devices and sensors
- backfills, and what they do to history
- point-in-time reproducibility for models
- tracing data from a physical event through the pipeline to the decision it influenced

That last one is lineage with a physical starting point. When a robot does something odd, the question is which reading, from which sensor, at what time, fed the decision, and whether that reading was later corrected.

## Who should watch

Data and ML engineers working anywhere the real world feeds the model: robotics, IoT, agriculture, manufacturing, logistics, vehicles. Feature store and data platform owners who have wrestled with time travel queries will find familiar problems in a new setting. Teams whose data is purely digital clickstreams will still recognise the backfill trap; they just get more chances to rerun things.

## Related Conf42 talks

- [Building a Production Computer Vision Verification System for Warehouse Receiving](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification) by Anton Solomonov, cameras meeting physical operations.
- [Real-Time Embedded AI for Deterministic, Adaptive, and Sustainable Robotics](https://www.conf42.com/DevOps_2026_Rasmi_Ranjan_Nayak_embedded_robotics_ai) by Rasmi Ranjan Nayak, the robot end of the pipeline.
- [Cloud-Native AI Infrastructure Transforming Modern Agriculture](https://www.conf42.com/Cloud_Native_2026_Mallikarjuna_Muchu_security_cloud_compliance) by Mallikarjuna Muchu, another view of ML infrastructure on the farm.

[Watch An Phan's talk](https://www.conf42.com/MLOps_2026_An_Phan_physical_sunlight_data) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[You Can't Rerun Sunlight: Designing ML Data Architectures for Physical AI](https://www.conf42.com/MLOps_2026_An_Phan_physical_sunlight_data) at Conf42 MLOps 2026.
