# Start from a pretrained model, train only when it fails you

Conf42 Blog, 2022-05-18. https://www.conf42.com/blog/ml2022/pretrained-model-first-training-last

In short: Julien Simon (Hugging Face) at Conf42 Machine Learning 2022 on Deep Learning 2.0, where a pretrained Transformer and a business KPI come before any training

Most machine learning projects die between the notebook and production, and Julien Simon, Chief Evangelist at Hugging Face, thinks a lot of that is self-inflicted. At Conf42 Machine Learning 2022 he argued for what he calls Deep Learning 2.0: pick a pretrained Transformer that matches your task, test it on real data, fine-tune only if it falls short, and spend your effort on latency and the business KPI instead of rebuilding tooling.

It is a vendor talk, and it says so: the tools are Hugging Face's libraries, Hub and services, plus Amazon SageMaker. But the recipe at the end works whatever you run it on.

## Why does so much deep learning never ship?

Simon starts with Deep Learning 1.0, four planets that aligned: neural networks came back, a few big open datasets such as ImageNet appeared, GPUs got cheap and rentable, and expert tools (Theano, Torch, later TensorFlow) arrived. The project shape that followed he describes as a waterfall pretending to be agile: collect, clean and label data (by his estimate 50% to 80% of the time), experiment, train, evaluate, engineer features, optimise, and finally deploy, which he calls the hardest part because now you have to live with the model.

The numbers he cites are grim: 87% of data science projects never make it into production (a VentureBeat figure from 2019), and only 25% of companies report widespread adoption (PwC).

## What changes in Deep Learning 2.0?

The same four planets, upgraded. Transformers replace CNNs and RNNs, and not only for NLP: they now cover computer vision, speech and audio, and reinforcement learning. Transfer learning replaces building a huge dataset. Purpose-built ML chips join GPUs. And the tools become friendly enough for a backend developer.

He backs the Transformers point with the Hub's own traffic, over a million model downloads a day, and with the GitHub star curve of the transformers library, which he says climbs faster than Kubernetes, Node or PyTorch did.

The transfer learning pitch is about scale. Fine-tuning needs one or two orders of magnitude less data than training from scratch, so it is faster to build, faster to train and cheaper. Often you don't fine-tune at all. Sentiment analysis, for example, usually works out of the box.

"Transfer learning is much, much faster than training from scratch because you don't have to build that huge data set, basically," Julien Simon said at Conf42 Machine Learning 2022.

## What do the demos show?

Three of them, none involving training from scratch:

- **Translation plus entity extraction in five lines.** A multilingual pipeline translates English to Hungarian, and a second off-the-shelf pipeline, built for Hungarian token classification, tags dates, persons, ordinals and geopolitical entities in the output.
- **Voice queries on SEC filings.** A Hugging Face Space chains Facebook's wav2vec2 speech-to-text model (21 languages, with built-in translation) and a Sentence Transformers semantic search over annual reports. He asks in French who the CFO of Gap is and gets Gap's annual report back, top matching sentences first. The whole app is about 100 lines, half of them user interface.
- **From the Hub to SageMaker and back.** He fine-tunes DistilBERT on a product review dataset from the Hub, maps four and five stars to positive and the rest to negative, and runs vanilla Transformers code through SageMaker script mode with the Hugging Face estimator on a single-GPU instance. One line deploys it to a CPU endpoint; after deleting the endpoint, he redeploys straight from the Hub.

For hardware, the Optimum library swaps a few Trainer objects for chip-specific ones (Habana and Graphcore for training; Intel, Qualcomm and AWS Inferentia for inference) so you don't rewrite the training loop.

## The recipe worth stealing

The closing takeaways are the part to pin above your desk. He says plainly that the complexity is ours.

"ML tends to be complicated because we love to make it complicated," Julien Simon said at Conf42 Machine Learning 2022.

His seven steps: find a pretrained model that fits the business use case; pick a business KPI that shows success, not just an ML metric; measure the model on real-life data, not a tidy sandbox test set; if it's good enough, you're done; if you need more accuracy (domain vocabulary is the usual culprit), fine-tune on your data; optimise prediction latency, because for many workloads you can't skip it; move to the next project. Done that way, he says, production is a matter of weeks, not months.

## Who should watch

Developers and data scientists who still start every NLP project by building a dataset, and teams weighing whether they need a training pipeline at all. If you already live in the Hugging Face ecosystem, the demos will be familiar; the KPI-first recipe is still a useful checklist to hand a manager.

## Related Conf42 talks

- Gajendra Deshpande on [multilingual natural language processing](https://www.conf42.com/Machine_Learning_2021_Gajendra_Deshpande_Multilingual_Natural_Language_Processing) at Conf42 Machine Learning 2021.
- Anais Dotis-Georgiou on [Quix and Hugging Face](https://www.conf42.com/Machine_Learning_2024_Anais_DotisGeorgiou_quix_hugging_face) at Conf42 Machine Learning 2024.
- Darya Petrashka on [building a Hugging Face agent](https://www.conf42.com/Python_2024_Darya_Petrashka_unlock_power_llm_build_huggingface_agent) at Conf42 Python 2024.

[Watch Julien Simon's talk](https://www.conf42.com/Machine_Learning_2022_Julien_Simon_hugging_face)

## From Hugging Face

In the talk, Simon walks through the Hugging Face Hub (models, datasets, Spaces), the transformers and Optimum libraries, AutoTrain for no-code training, the hardware-accelerated Inference API and the SageMaker integration.

- Hugging Face Inference API: [huggingface.co/inference-api](https://huggingface.co/inference-api)
- Hugging Face course: [huggingface.co/course](https://huggingface.co/course)
- Optimum on GitHub: [github.com/huggingface/optimum](https://github.com/huggingface/optimum)

[Watch the talk on YouTube](https://youtu.be/BiJWFHL7u_Y).

## Watch the talk

[Machine Learning 2.0 with Hugging Face](https://www.conf42.com/Machine_Learning_2022_Julien_Simon_hugging_face) at Conf42 Machine Learning 2022.
