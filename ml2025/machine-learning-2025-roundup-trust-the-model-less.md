# Conf42 Machine Learning 2025 - when "don't" means nothing to your embeddings

Conf42 Blog, 2025-05-09. https://www.conf42.com/ml2025/machine-learning-2025-roundup-trust-the-model-less

In short: Conf42 Machine Learning 2025 in review, 136 talks on embedding blind spots, LLM evaluation, tiny models, agents, guardrails and ML in finance and health.

[Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) went out on May 8, 2025 with 136 talks, enough to fill a long weekend of viewing. Under the volume sat a sensible mood: less awe at what models can do, more scrutiny of where they quietly fail and what it takes to run them somewhere real. Speakers came from Google DeepMind, Microsoft, Meta, AWS, NVIDIA, Dropbox, Samsung Research, Expedia Group, Palo Alto Networks, Walmart, JPMorgan Chase and many more.

## Your model is more confident than it should be

The talk most likely to change how you build RAG came from [Ritesh Modi](https://www.conf42.com/Machine_Learning_2025_Ritesh_Modi_embedding_models_language) (Microsoft). In *Hallucination by Design* he shows test results where embedding models treat "take medication" and "don't take medication" as the same thing, then walks through the patterns that cause it and how to make GenAI systems more reliable anyway. Negation, it turns out, is a rounding error in vector space.

[Alok Ranjan and Saurabh Suman](https://www.conf42.com/Machine_Learning_2025_Alok_Ranjan_Saurabh_Suman_modern_approaches_bleu) (Dropbox, San José State University) argued that BLEU and ROUGE can't measure what modern LLMs do, and moved through benchmarks like MMLU and TruthfulQA to real-world and human-in-the-loop evaluation. [Andrei Stroganov and Andrei Visochan](https://www.conf42.com/Machine_Learning_2025_Andrei_Stroganov_Andrei_Visochan_estimation_regression_confidence) (Samsung Research) took the mathematical route: fast, real-time confidence estimation for classification and regression models using C++ compile-time numerical integration. [Gaurav Bansal](https://www.conf42.com/Machine_Learning_2025_Gaurav_Bansal_evaluation_enterprise_language) covered scalable evaluation and QA for enterprise LLMs.

## Small models, tight budgets

Not every model gets an H100. [Max Navrotsky and Oleksandr Gordieiev](https://www.conf42.com/Machine_Learning_2025_Max_Navrotsky_Oleksandr_Gordieiev_llms_optimization_devices) (VGS, Lutsk National Technical University) shrank GPT-2 for very weak hardware with pruning, quantisation and fine-tuning. [Hitesh Saai Mananchery](https://www.conf42.com/Machine_Learning_2025_Hitesh_Saai_Mananchery_compression_pixel_video) (Expedia Group) presented R2S, an ML approach to video compression that removes frame redundancy by tracking pixel shifts. At the other end of the scale, [Praneel Madabushini](https://www.conf42.com/Machine_Learning_2025_Praneel_Madabushini_tesla_openai) (NVIDIA) looked at how Kubernetes handles resource-hungry AI and ML workloads, with lessons drawn from Tesla and OpenAI, and [Bhaskar Goyal](https://www.conf42.com/Machine_Learning_2025_Bhaskar_Goyal_enterprise_cloud_patterns) (Google) covered architectural patterns for cloud-native AI at scale.

## Agents, with and without guardrails

[Naman Goyal](https://www.conf42.com/Machine_Learning_2025_Naman_Goyal_generation_text_agentic) (Google DeepMind) traced the move from passive text generators to agents that make decisions and act on their environment. [Alex Shershebnev](https://www.conf42.com/Machine_Learning_2025_Alex_Shershebnev_code_agents_coding) (Zencoder) got practical about AI coding agents and how to build them, and [Samuel Baruffi](https://www.conf42.com/Machine_Learning_2025_Samuel_Baruffi_chatbots_bedrock_enterprise) (AWS) showed Amazon Bedrock Agents orchestrating enterprise workflows with access to business data and APIs. [Mohamed Najaaf](https://www.conf42.com/Machine_Learning_2025_Mohamed_Najaaf_guardrails_responsible_bedrock) (AWS) followed with the brakes: Amazon Bedrock Guardrails for responsible AI. [Laly Bar-Ilan](https://www.conf42.com/Machine_Learning_2025_Laly_BarIlan_language_components_understand) (Bit) proposed composable components as the shared language between developers, non-technical teams and AI, so an agent can build features from product intent while humans stay in the loop.

For anyone still fuzzy on the basics, [Veliswa Boya](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector) (AWS) gave a good first talk on vector embeddings and RAG, and [Sergey Polyashov](https://www.conf42.com/Machine_Learning_2025_Sergey_Polyashov_recommendation_search_scalable) (Microsoft) did the same for search and recommendation systems, trade-offs and pitfalls included.

## ML where mistakes have consequences

Trust and safety got serious treatment. [Georgina Tryfou](https://www.conf42.com/Machine_Learning_2025_Georgina_Tryfou_moderation_scalable_safety) (Gcore) described an AI system for detecting and moderating harmful content such as CSAM in near real time, with privacy built into the design. [Lianne Potter](https://www.conf42.com/Machine_Learning_2025_Lianne_Potter_bias_builders_history) (Compromising Positions) went back to the early builders of AI to show how their choices about bias and power still shape what we build. [Arun Vivek Supramanian](https://www.conf42.com/Machine_Learning_2025_Arun_Vivek_Supramanian_privacy_engineering_ethical) (Amazon) covered privacy, bias and fairness from the data engineering side.

Finance and healthcare filled whole tracks. Highlights include [Venkateswarlu Boggavarapu](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) (JPMorganChase) on graph databases for fraud detection, [Surendra Lakkaraju](https://www.conf42.com/Machine_Learning_2025_Surendra_Lakkaraju_ecommerce_fraud) (Amazon) on real-time e-commerce fraud detection, [Sandeep Gourneni](https://www.conf42.com/Machine_Learning_2025_Sandeep_Gourneni_banking_optimization) (Hitachi Digital Services) on LLM-assisted legacy banking code transformation, and [Sachin Telalwar](https://www.conf42.com/Machine_Learning_2025_Sachin_Telalwar_compliance_healthcare) (Zocdoc) on secure distributed healthcare systems.

## ML out in the world

Some of the most memorable talks left the data centre. [Aroma Rodrigues](https://www.conf42.com/Machine_Learning_2025_Aroma_Rodrigues_imagination_source_journey) (Microsoft) told the story of an open source journey that began in 2016 with a shoe for visually impaired people, built from an Arduino, an Android phone and an unreasonable amount of optimism. [Dmytro Hlotenko](https://www.conf42.com/Machine_Learning_2025_Dmytro_Hlotenko_photography_community_serverless) (APA-IT) processed 8,000 event photos in real time on AWS AI and serverless at Community Day DACH 2024, sorting them and delivering them back to the community. [Avraam Tolmidis](https://www.conf42.com/Machine_Learning_2025_Avraam_Tolmidis_traffic_smart_systems) (Meta) applied multi-agent systems and predictive optimisation to urban traffic, and [Karthikeyan Rajamani](https://www.conf42.com/Machine_Learning_2025_Karthikeyan_Rajamani_iot_accoustic_analysis) (Thomson Reuters) listened to machines, literally, with IoT acoustic analysis for predictive maintenance.

## Sponsors and where to watch

Thanks to [Rapydo](https://www.rapydo.io/) at Gold and [APA Tech](https://apa.at/about/apa-tech/) at Silver. All 136 talks are on the [event page](https://www.conf42.com/ml2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDbH1VBaoA60lLAAVqmiLPe). Start with Modi's embedding tests; you will look at your retrieval results differently afterwards.

The series returns with [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).
