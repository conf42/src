# You Can't Rerun Sunlight: Designing ML Data Architectures for Physical AI

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [An Phan](https://www.conf42.com/speaker_An_Phan) (Senior Data Infrastructure Engineer @ Hippo Harvest). Page: https://www.conf42.com/MLOps_2026_An_Phan_physical_sunlight_data

## Abstract

In software, when something goes wrong, we often retry. In machine learning, we rerun a pipeline, backfill missing data, or reproduce a model with the same code and inputs. But what happens when that model is connected to the physical world?  In physical AI systems, data comes from sensors, cameras, robots, and real environments. It can arrive late, be corrected later, or never be captured at all. After a backfill, yesterday’s dataset may look complete even though the model making a decision yesterday did not have that information.  This talk explores how to design ML data architectures that preserve not only what we know now, but what the system knew at the time a decision was made. I’ll share lessons from building data infrastructure for robotics and machine learning in agriculture, including late-arriving data, backfills, point-in-time reproducibility, and tracing data from physical events through ML pipelines and downstream decisions.  You can rerun the pipeline. You can rerun the model. But you can’t rerun sunlight.
