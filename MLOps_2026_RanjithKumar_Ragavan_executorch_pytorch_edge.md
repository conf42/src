# Edge MLOps: Building a Pipeline from PyTorch Training to On-Device Inference with ExecuTorch

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [RanjithKumar Ragavan](https://www.conf42.com/speaker_RanjithKumar_Ragavan) (Member of Technical Staff @ T-Mobile). Page: https://www.conf42.com/MLOps_2026_RanjithKumar_Ragavan_executorch_pytorch_edge

## Abstract

Most MLOps pipelines end at a cloud endpoint. When the target is a phone, the pipeline has to account for memory limits, thermal budgets, battery drain, and a fleet of devices with very different hardware. Drawing on contributions to Meta's open-source PyTorch ExecuTorch runtime, this talk walks through what an edge-focused MLOps pipeline needs:  Exporting PyTorch models into a mobile runtime built on a model loader, execution planner, memory manager, and operator registry Making compression part of the pipeline: quantization-aware training, structured pruning, and knowledge distillation Why quantization-aware training preserves accuracy better than post-training quantization alone Validating models across device tiers, including NPU versus CPU execution paths Fitting models within binary-size and thermal constraints before release  Attendees leave with a reference pipeline for taking models from training to production on consumer mobile devices.
