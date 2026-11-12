# Teaching a model to read 2,000-year-old Roman coins

Conf42 Blog, 2021-07-29. https://www.conf42.com/blog/ml2021/coin-search-augments-museum-curators

In short: Nicolas Metallo (AWS) at Conf42 Machine Learning 2021 on cleaning up phone photos of ancient coins so visual search can match them to a museum collection

Identifying a worn Roman coin from a blurry smartphone photo can take an expert curator anything from 10 minutes to several hours. At Conf42 Machine Learning 2021, Nicolas Metallo, Senior Data Scientist at AWS, walks through the prototype AWS built with the University of Oxford's Gardens, Libraries and Museums (GLAM) to cut that down to a shortlist of eight candidates, then shows how to rebuild each piece yourself on Amazon SageMaker.

The talk splits into two halves: the museum case study, and a hands-on tour of image classification, background removal and visual search. It's a vendor talk and the tooling is all AWS, but the problem framing is the part worth stealing.

## Why does a museum need machine learning at all?

Oxford's GLAM holds 21 million objects and has room to display about 10% of them at once, with a large cataloguing backlog behind that. The prototype candidate was the Roman Provincial Coinage digital collection at the Ashmolean Museum, which Nicolas describes as the world's largest digital collection of Roman provincial coinage, free to browse online.

Getting a specimen into that collection needs a curator, and curators are scarce. Researchers, other institutions and members of the public send in photos asking what they have. Volunteers help, but even simple matches can defeat a small group. The goal was explicit about where the humans stay.

"What we wanted to do is not automate this task, but augment the humans behind it," Nicolas Metallo said at Conf42 Machine Learning 2021. In practice that means fewer hours spent rotating photos until they line up, and more time on the judgement calls.

## The first model just answers heads or tails

The first prediction was deliberately simple: is this photo the obverse or the reverse? Knowing that halves the search space, because you only compare obverses against obverses. Nicolas says the classifier reached 95% accuracy, and the metadata extracted alongside it (material, region, city, province, the person on the coin) narrows things further.

## Make the amateur photo look like the museum photo

The hard part is that collection images are shot with professional kit: even light, no background, sharp focus. Photos from the outside world are low resolution, noisy, unevenly lit, and the coins themselves are often badly worn. Comparing those directly against the collection doesn't work.

So the pipeline does the cleanup first. It finds the region of interest, removes the background, auto-rotates the coin, then deblurs and upscales it so it resembles the collection's own photos. Only then does it extract features and run a similarity search. The demo, a Streamlit app, takes a rotated, blurry upload and returns eight lookalike items with their metadata, so a volunteer checks eight images instead of thousands.

The numbers Nicolas gives: eleven machine learning models built and deployed in about ten weeks, an expected saving of up to three years of work cataloguing a 300,000-coin collection, and an analysis time of a few minutes per coin. He also mentions an open-source successor in the works, aimed at any collection object (gems, fossils), not just coins.

## How would you build it yourself?

The second half rebuilds the three pieces:

- **Classification** with SageMaker JumpStart: pick a pretrained EfficientNet (he goes for the B7 variant), point fine-tuning at an S3 bucket with one folder per class, train, and deploy an endpoint.
- **Background removal** with a Mask R-CNN trained via the IceVision library (built on PyTorch, PyTorch Lightning and fastai) on the coin class of the Open Images segmentation set, after converting annotations from Pascal VOC to COCO format. He points to U-2-Net on Papers with Code as an off-the-shelf saliency option. The training job ran about 22 minutes.
- **Visual search** following AWS's SageMaker plus Elasticsearch blog post: a ResNet-50 endpoint returns feature vectors, which go into an Elasticsearch index for k-nearest-neighbour queries. The sample uses a fashion dataset of about 10,000 images; swap in coins.

The most transferable tip is about cost. Managed spot training, which Nicolas puts at 60% to 90% cheaper than on-demand with checkpointing handling interruptions, takes a few lines of configuration. For the 22-minute job he estimates around 70% off.

## Who should watch?

Anyone building search over a catalogue where the query images come from the messy outside world: museums, parts catalogues, insurance claims. If you already run SageMaker in production, the second half will be familiar; the first half's normalise-then-search framing is still worth the time.

For more from the same event, [Joshua Arvin Lat on pragmatic ML with SageMaker](https://www.conf42.com/Machine_Learning_2021_Joshua_Arvin_Lat_Pragmatic_Machine_Learning_and_ML_Engineering_Amazon_SageMake), [Eduardo Dixo comparing transformers and CNNs for drone object detection](https://www.conf42.com/Machine_Learning_2021_Eduardo_Dixo_Object_Detection_Transformers_CNNs_Drone_Case_Study), and [Laura Ham on Weaviate's out-of-the-box vector search](https://www.conf42.com/Machine_Learning_2021_Laura_Ham_Weaviate_outofthebox_machine_learning_models) pair well with it.

[Watch Nicolas Metallo's talk](https://www.conf42.com/Machine_Learning_2021_Nicolas_Metallo_History_meets_AI_ancient_coins) from [Conf42 Machine Learning 2021](https://www.conf42.com/ml2021).

## From Amazon Web Services (AWS)

The talk uses Amazon SageMaker Studio, SageMaker JumpStart, managed spot training, Amazon S3 and Elasticsearch on AWS.

- AWS: [aws.amazon.com](https://aws.amazon.com/)

[Watch the talk on YouTube](https://youtu.be/5uJdBnY-zcE).

## Watch the talk

[History meets AI: Unveiling the secrets of ancient coins](https://www.conf42.com/Machine_Learning_2021_Nicolas_Metallo_History_meets_AI_ancient_coins) at Conf42 Machine Learning 2021.
