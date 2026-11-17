# An 833-parameter model on the phone beats a chatbot round trip

Conf42 Blog, 2026-11-15, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/edge-mlops-pytorch-to-executorch

In short: RanjithKumar Ragavan (T-Mobile) at Conf42 MLOps 2026 on exporting a tiny PyTorch model to ExecuTorch so health data is scored on the phone.

RanjithKumar Ragavan caught himself screenshotting his Oura Ring metrics every morning and pasting them into a cloud chatbot to ask whether he should work out. At Conf42 MLOps 2026, the Member of Technical Staff at T-Mobile shows what he built instead: Noctua, an open-source Kotlin SDK that runs an 833-parameter PyTorch model on the phone through ExecuTorch, in under five milliseconds by his account, with no health data leaving the device. He is clear that it is a personal project, independent of his employer.

The itch is what he calls the gap between measurement and coaching. The ring tracks heart rate variability, sleep stages, resting heart rate and skin temperature, the app reports a readiness score, and none of it answers the question of whether to train hard today. Uploading a continuous physiological history to a third party to answer something the phone's processor can compute is the anti-pattern he set out to remove.

## The phone is the feature pipeline

In cloud MLOps a warehouse and a feature store prepare the inputs. Here the handset does it. Noctua's core module fetches the trailing 21 days of data from the Oura API v2 and folds readiness, sleep, activity and HRV into an immutable Kotlin object. A feature extractor then normalises it against the wearer's own baseline, because raw HRV means nothing across people: fifty milliseconds can be good recovery for one person and deep fatigue for another. Out come eight floating-point features, including accumulated sleep debt, HRV against a fourteen-day rolling baseline, the resting heart rate delta and three-day readiness momentum.

The SDK is split into three Gradle modules: a pure Kotlin, coroutine-first API client that handles OAuth, token refresh and pagination; the AI module with feature extraction, a heuristic engine and the ExecuTorch bridge; and a Jetpack Compose example app. That app has a deterministic 21-day synthetic demo mode, so you can watch the model run without owning a ring.

## Eight inputs do not need a two-gigabyte model

His strongest opinion is about sizing. It is tempting to quantize a multi-gigabyte language model for everything, and wasteful to spend a user's battery and storage that way to predict one score from eight numbers. Noctua uses a multilayer perceptron with an 8-32-16-1 topology. The hidden layers are there because the features interact: the same workout strain leads to a good day with a positive HRV baseline and a sharp readiness drop with a negative one plus sleep debt. A linear equation misses that.

The whole network is 833 float32 parameters, and the compiled program is about eight kilobytes on disk as he gives it, smaller than an app icon.

## Three lowering stages and ten lines of Python

The export script is short. Put the model in eval mode, create a sample input of shape one by eight, then run ExecuTorch's ahead-of-time pipeline. First, torch.export captures a static graph in the core ATen dialect, and the Python overhead is gone. Second, to_edge lowers it to the Edge dialect and normalises operators. Third, to_executorch does static memory planning, working out the offsets of intermediate tensors at compile time so the phone does no dynamic allocation during inference. The result is written out as a .pte file.

## The native runtime is optional by design

Shipping a C++ runtime inside an SDK invites a classic crash: one consumer leaves out the native dependency to keep the APK small, a CI server runs tests on a desktop JVM with no JNI library, and everything dies on an unsatisfied link error. Noctua loads the ExecuTorch runtime reflectively and, if the runtime or the .pte file is missing, falls back to a zero-dependency linear model in pure Kotlin. The UI badge says which engine produced the number. All sixteen unit tests run on a plain JVM as a result.

The neural forecast is paired with deterministic, unit-tested rules that run on the same features and flag things like sleep debt or HRV below baseline with a confidence figure. His reason: "you cannot afford hallucinated medical advice". The network forecasts, and the rules keep every recommendation traceable.

He compares the result with the cloud route on four counts: privacy, explainability, speed and resilience. A cloud round trip takes from 500 milliseconds to a couple of seconds and fails on a flight or a trail. "privacy is the product", RanjithKumar Ragavan said at Conf42 MLOps 2026.

## Who should watch

Android and mobile engineers who want a small, complete ExecuTorch example, and ML engineers curious about what the export path looks like end to end. Set expectations against the abstract, though: this is a twenty-minute case study of one tiny tabular model. Quantization-aware training, pruning, distillation, NPU versus CPU paths and device-tier validation are not covered. The roadmap he lists is a local LLM coach through ExecuTorch's Llama runner, overnight on-device fine-tuning, Android Health Connect write-back and a Kotlin Multiplatform port for iOS. The project is MIT licensed.

## Related Conf42 talks

- [Edge-Ready GenAI: Engineering Low-Latency Solutions for Resource-Constrained Environments](https://www.conf42.com/Machine_Learning_2025_Sai_KR_Pentaparthi_latency_solutions_genai) by Sai KR Pentaparthi at Conf42 Machine Learning 2025.
- Pradeep Kumar Vattumilli's talk on [edge computing and TinyML](https://www.conf42.com/Golang_2025_Pradeep_Kumar_Vattumilli_edge_tinyml_ai) at Conf42 Golang 2025.
- [Building Reliable AI-Driven Mobile Platforms for Healthcare and Commerce](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Dipta_Rakshit_building_reliable_driven) by Dipta Rakshit of Walmart Global Tech at Conf42 SRE 2026.

[Watch RanjithKumar Ragavan's talk](https://www.conf42.com/MLOps_2026_RanjithKumar_Ragavan_executorch_pytorch_edge) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Edge MLOps: Building a Pipeline from PyTorch Training to On-Device Inference with ExecuTorch](https://www.conf42.com/MLOps_2026_RanjithKumar_Ragavan_executorch_pytorch_edge) at Conf42 MLOps 2026.
