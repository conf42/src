# Shrinking GPT-2 for tiny devices works only if you fine-tune first

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/shrinking-gpt2-tiny-devices-fine-tune-first

In short: Max Navrotsky (VGS) and Oleksandr Gordieiev at Conf42 Machine Learning 2025 on trimming, pruning and quantising GPT-2, and why distillation broke.

The compression trick that made GPT-2 fit on weak hardware was not a compression trick at all. It was fine-tuning. At Conf42 Machine Learning 2025, Max Navrotsky, Senior Software Engineer at VGS, presented joint research with Oleksandr Gordieiev, Professor at the Software Engineering Department of Lutsk National Technical University, on aggressively optimising GPT-2 for low-end, CPU-only devices, and found that a model focused on one task survives compression that wrecks a general one.

It is a clear, experiment-driven talk with a refreshingly honest failure in the middle.

## Why GPT-2, and what "tiny" means

The target is field operations, offline systems and embedded devices: hardware where a modern LLM is out of the question. They picked GPT-2 because it is open source (no licence or API limits), small at 117 million parameters and around 500 MB, not already compressed, well documented, and still good at coherent generation for its age. The test task is concrete: fine-tune it to generate ISO-compliant software requirements, then measure perplexity, CPU usage, memory, inference speed and model size. In Max's words, if they could carry one model into a forest on an old laptop, it would be GPT-2.

## Three aggressive cuts, one gentle one

The talk sorts techniques into aggressive ones, which change the model's structure or weights, and a non-aggressive one:

- **Architecture trimming.** Half the layers removed (12 to 6) and hidden size halved (768 to 384). Layers were removed symmetrically from the centre, keeping the bottom layers for syntax and token-level understanding and the top layers for higher-level structure.
- **Pruning.** Rank weights by absolute value and drop the smallest, 40% in the final setup. Max's analogy: muting the quietest voices in a noisy room.
- **Quantisation.** Weights from float32 to int8. Nothing deleted, just less precision, and a big drop in CPU load.
- **Knowledge distillation.** The student mimics the teacher without architecture changes.

## Distillation failed, and that is the interesting result

After trimming, the student was too small to understand the teacher's outputs. It compensated the only way it could, with hallucinations and repetition, and the output was unusable. The conclusion: non-aggressive methods don't stack on top of aggressive ones, so distillation was dropped from the final pipeline. Reporting the thing that didn't work is worth the price of admission on its own.

## The combined result, and the memory trade-off

The final model is fine-tuned GPT-2 trimmed to six layers, 40% pruned and int8-quantised. Compared with raw GPT-2, CPU load roughly halves, the model is about five times smaller, inference is faster and perplexity barely moves. The catch is RAM, which went up by about 200 MB, as the optimisations trade CPU time for larger tensors, caching and parallel processing. Max argues that is the right trade for battery-powered devices, where CPU is the biggest power draw, though it matters on microcontrollers with very little memory.

## Fine-tuning creates "resistance"

The key idea is what the authors call model resistance: how well a model keeps output quality under compression. A model fine-tuned for one clear task has strong internal signal and degrades slowly even under heavy pruning and quantisation. A general model has many overlapping skills and breaks fast; when they applied the same cuts to raw GPT-2, results were unusable and perplexity shot up. Fine-tuning, in their framing, is what makes optimisation possible at all.

## Who should watch

Engineers deploying language models on edge, offline or embedded hardware, and anyone choosing between a big general model and a small specialised one. The results are on GPT-2 and one task, so test before generalising to newer models.

## Related Conf42 talks

- [Rishab Mehra on the disruptive potential of on-device large language models](https://www.conf42.com/Prompt_Engineering_2024_Rishab_Mehra_ondevice_models_ai), the why behind this how.
- [Pradeep Kumar Vattumilli on edge computing and TinyML for autonomous IoT](https://www.conf42.com/Golang_2025_Pradeep_Kumar_Vattumilli_edge_tinyml_ai), for even smaller targets.
- [Murali Krishna Reddy Mandalapu (Renesas Electronics) on real-time AI inference at the edge for vehicles](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge), where latency is a safety requirement.

[Watch Max Navrotsky and Oleksandr Gordieiev's talk](https://www.conf42.com/Machine_Learning_2025_Max_Navrotsky_Oleksandr_Gordieiev_llms_optimization_devices)

[Watch the talk on YouTube](https://youtu.be/85k01nwkN5s).

## Watch the talk

[Aggressive LLMs Optimization: Making Them Work on Tiny Devices](https://www.conf42.com/Machine_Learning_2025_Max_Navrotsky_Oleksandr_Gordieiev_llms_optimization_devices) at Conf42 Machine Learning 2025.
