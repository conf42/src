# Teaching SageMaker BlazingText Tamil from a Wikipedia dump

Conf42 Blog, 2021-07-30. https://www.conf42.com/blog/ml2021/tamil-word-embeddings-sagemaker-blazingtext

In short: Dinesh Subramani (AWS) at Conf42 Machine Learning 2021 on learning Tamil word embeddings with the SageMaker BlazingText algorithm, from wiki dump to endpoint

Most word2vec demos use English, so you can check the answers in your head. [Dinesh Subramani](https://www.conf42.com/Machine_Learning_2021_Dinesh_Subramani_Natural_language_modelling_Amazon_SageMaker_BlazingText_algor), Solutions Architect at AWS, picked Tamil for his Conf42 Machine Learning 2021 talk instead: a classical language with a history going back to around 300 BC, which he speaks and most of his audience does not. He fed a Tamil Wikipedia dump to the BlazingText algorithm built into Amazon SageMaker and checked whether the resulting embeddings put music near song and politics near leader. They did.

His stated aim is to show that you do not need an ML background to try this. Dinesh Subramani said at Conf42 Machine Learning 2021 that "you don't need machine learning degree to take advantage of tooling AWS has put at your disposal". It is a beginner-friendly talk: word embeddings from first principles, a tour of SageMaker, then the notebook.

## Why can't a model just read the words?

Words have different lengths, spellings vary by language and even by region (he notes the same Tamil word can be spelled differently across Tamil Nadu), and most ML techniques want numbers. Giving each word an integer label invents relationships that do not exist: in to be or not to be, labelling the words 0, 1, 2, 3 makes be closer to or than to not, which means nothing. One-hot encoding fixes that but scales badly, since a rich vocabulary means enormous sparse vectors.

## What does word2vec actually learn?

The other side of the coin is context. Next to Tom Hanks you would expect words like great and actor, and you would not expect quantum physics (not impossible, just much less likely). Train a network to predict context words for each input word, and you get a dense vector per word, with a dimension you choose. Words used in similar contexts end up with similar vectors.

The classic check is vector arithmetic: king minus man plus woman lands near queen, with the caveat that it depends entirely on the training corpus. To see the result he shows English embeddings in 100 dimensions squashed into a t-SNE plot, where American, British, English, London, England, French, France and German cluster together, as do son, family, children, father, death and life. He mentions BERT and RoBERTa in passing; the end goal is still embeddings.

## Where does SageMaker fit?

He walks the AWS ML stack (AI services behind an API call, SageMaker in the middle, frameworks and GPU instances at the bottom) and the SageMaker workflow: prebuilt example notebooks, built-in algorithms shipped as containers (or your own container), training launched with one line of SDK code on as many instances as you specify, with the model written back to S3. Automatic model tuning runs hyperparameter optimisation jobs using Bayesian search, so you are not left guessing values or brute-forcing a grid. SageMaker Neo compiles models for different target processors. Deployment is another single line, and SageMaker Pipelines can automate the run from ingestion to an approval step before production.

He also says something worth remembering about any of this: "Your models are as good as your training data."

## Why BlazingText?

BlazingText, published by Amazon researchers in 2017, is a highly optimised implementation of word2vec and of text classification that extends fastText with GPU acceleration through custom CUDA kernels and can spread across multiple CPUs. The talk's figures: it can train on more than a billion words in a couple of minutes, runs 21 times faster and 20% cheaper than fastText on a single C4 instance, and reaches up to 50 million words per second in distributed training. On a single CPU it uses Intel BLAS and shares negative samples to speed up skip-gram. His benchmark comparison plots cost against accuracy, with BlazingText reaching about the same accuracy as fastText at much lower cost.

## How does the Tamil demo go?

In a SageMaker notebook:

1. Download a Tamil Wikipedia dump and clean it with the open source WikiExtractor script from GitHub, which produces plain Tamil text. He stopped extraction early because the dump was huge; more data would mean better embeddings.
2. Create a SageMaker session, upload the cleaned text to the default S3 bucket and set an output location.
3. Retrieve the BlazingText container image URI for the region (eu-west-1 here), build an estimator with an IAM role, four ml.c4.2xlarge instances and File input mode, set hyperparameters by hand and call fit. You pay only for the seconds the training job runs.
4. Deploy the model to an endpoint with one line, then send a list of words: Tamil, language, music, song, politics, leader, year, century, in Tamil.

The endpoint returns a vector for each word. Music and song come out close together, and so do politics and leader, while music and politics sit further apart. He is upfront that he trained on a reduced corpus without tuning, so the numbers are rough; hyperparameter optimisation and more data would sharpen them. You can also unpack the model and plot the words in two dimensions with Matplotlib.

## Who should watch?

Developers new to NLP who want word embeddings explained without equations, and anyone wanting a template for training embeddings in a language that pretrained models serve poorly. Swap the Wikipedia dump for your language and the notebook works as is.

## Related Conf42 talks

- Gajendra Deshpande on [multilingual natural language processing](https://www.conf42.com/Machine_Learning_2021_Gajendra_Deshpande_Multilingual_Natural_Language_Processing) at Conf42 Machine Learning 2021.
- Joshua Arvin Lat on [pragmatic ML engineering with Amazon SageMaker](https://www.conf42.com/Machine_Learning_2021_Joshua_Arvin_Lat_Pragmatic_Machine_Learning_and_ML_Engineering_Amazon_SageMake) at Conf42 Machine Learning 2021.
- Akshay Jain on [topic modelling for text](https://www.conf42.com/Machine_Learning_2024_Akshay_Jain_topic_modelling_text) at Conf42 Machine Learning 2024.

[Watch the talk on YouTube](https://youtu.be/Ta5Lq2kbiQQ).

## From AWS

- Amazon Web Services: [aws.amazon.com](https://aws.amazon.com/)
- Amazon SageMaker: [aws.amazon.com/sagemaker](https://aws.amazon.com/sagemaker/)
- BlazingText algorithm documentation: [docs.aws.amazon.com/sagemaker/latest/dg/blazingtext.html](https://docs.aws.amazon.com/sagemaker/latest/dg/blazingtext.html)

## Watch the talk

[Natural language modelling with Amazon SageMaker BlazingText algorithm](https://www.conf42.com/Machine_Learning_2021_Dinesh_Subramani_Natural_language_modelling_Amazon_SageMaker_BlazingText_algor) at Conf42 Machine Learning 2021.
