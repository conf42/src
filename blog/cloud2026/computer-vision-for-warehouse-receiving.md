# Computer vision that cut warehouse receiving errors by 99%

Conf42 Blog, 2026-04-21. https://www.conf42.com/blog/cloud2026/computer-vision-for-warehouse-receiving

In short: Anton Solomonov of SIMPLE at Conf42 Cloud Native 2026 on a production computer vision check for near-identical spare parts in a mining supplier's warehouse.

Two spare parts that differ by a millimetre or two in thread or geometry look identical to a warehouse operator on a deadline, and are entirely different SKUs to the mining customer waiting for them. At Conf42 Cloud Native 2026, [Anton Solomonov](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification), Lead Data & AI Architect at SIMPLE, presented a case study of a computer vision verification step built into warehouse receiving that reduced spare-part mismatches by 99%.

His framing is refreshingly unflashy: the interesting AI cases aren't the impressive demos, they are the ones embedded in a real process that keep working.

## The problem was the process, not the people

The client manufactures equipment and spare parts for the mining industry and receives high volumes of shipments from overseas suppliers. The paperwork said which part numbers should arrive. Reality kept delivering a very similar, different part: supplier mistakes, mixed-up part numbers, one item shipped under another's description.

The usual reaction is to tell people to be more careful and add a manual check. Solomonov argues that couldn't work. Under volume, time pressure and a complex catalog, nobody can measure every part and dig through technical documentation and still hit receiving targets. The business wanted both speed and accuracy, and manual work couldn't deliver both. So the brief became: reduce the probability of error exactly where the error happens. Starting from the process, not the technology, is what kept the design practical.

## A verification service, not an image classifier

The system compares more than pixels. Its data layer combines part photos, catalog images, text descriptions, technical specifications, item master data, historical receiving and error records, and the expected part number for the shipment. Images alone weren't enough, because some differences are too subtle to see. Context like SKU, product family and catalog attributes is what stops the model making a confident wrong call.

The recognition engine compares the photo against reference patterns for the expected item and its closest alternatives. Crucially it doesn't answer only yes or no. It returns a confidence level, the most likely part number, a list of similar alternatives, and the distinguishing features the operator should check. In production, he says, the dangerous system isn't the one that hesitates; it's the one that is confidently wrong.

## Confidence thresholds route the work

The operator takes a photo, the service pulls the shipment context, and the answer comes back in a form that's easy to read. High confidence confirms the match. Medium confidence flags risk and asks for extra verification, like a measurement or a catalog check. Low confidence routes the item to an exception flow. That human-in-the-loop design improved reliability, built trust with warehouse staff faster, and turned every ambiguous case into a new training example.

## Four trade-offs he made on purpose

The engineering section is the best part of the talk:

- **Accuracy versus speed.** Deep validation on every part would wreck receiving throughput, so the system was tuned for usefulness inside the process: accurate enough to catch problem cases, fast enough not to break the rhythm.
- **Automatic decisions versus controlled escalation.** Forcing a final verdict would create dangerous false positives and negatives in edge cases. Thresholds and escalation paths were less magical and more correct.
- **Scalability versus maintainability.** The model, reference data, matching logic, workflow, exception handling and quality monitoring were kept separate so a growing catalog didn't turn the system into a monolith.
- **Trust versus black box.** A bare "not a match" kills adoption. Showing why an item was flagged made the tool an assistant rather than a barrier.

## Production means living by the warehouse's rules

His definition of working in production is operational: available during shifts, fast responses, integration errors that never block receiving, fallback scenarios, monitored quality, and catalog and master-data updates that the system absorbs. Beyond the 99% figure, he points to less dependence on specific experienced employees, more consistent receiving quality and fewer disputes.

## Who should watch

ML engineers and architects taking a vision model out of a notebook and into an operational workflow, especially where errors are expensive and users are busy. The talk has no code but plenty of decisions worth copying.

## Related Conf42 talks

- [Serverless Architecture for Product Defect Detection Using Computer Vision](https://www.conf42.com/Machine_Learning_2022_Mohsin_Khan_product_defect_detection_computer_vision) by Mohsin Khan at Conf42 Machine Learning 2022.
- [SRE for Supply Chain: Building Reliable Human-AI Warehouse Operations at Scale](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses) by Vishnu Prasad at Conf42 DevOps 2026.
- [Cascade models in computer vision to boost accuracy and performance](https://www.conf42.com/Machine_Learning_2023_Argo_Saakyan_cascade_models_computer_vision_accuracy_performance) by Argo Saakyan at Conf42 Machine Learning 2023.

[Watch Anton Solomonov's talk](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification) or the [YouTube recording](https://youtu.be/SGM_iIqXock).

## Watch the talk

[Building a Production Computer Vision Verification System for Warehouse Receiving](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification) at Conf42 Cloud Native 2026.
