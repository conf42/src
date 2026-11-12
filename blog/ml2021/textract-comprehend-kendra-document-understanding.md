# Extract, understand, then let a human check the low-confidence bits

Conf42 Blog, 2021-07-28. https://www.conf42.com/blog/ml2021/textract-comprehend-kendra-document-understanding

In short: Matteo Gabrielli (AWS) at Conf42 Machine Learning 2021 on document processing with Textract, Comprehend, Comprehend Medical, Kendra and Augmented AI

Paper is not going away; Gartner research quoted in the talk has organisations using 25% more of it each year. [Matteo Gabrielli](https://www.conf42.com/Machine_Learning_2021_Matteo_Gabrielli_Empower_business_insights_text), Solutions Architect at AWS, used his Conf42 Machine Learning 2021 talk to frame document processing as three steps (extract the text, make sense of it, have a human verify it) and to show how AWS AI services cover each one, ending with a demo of the open source Document Understanding Solution.

It is an AWS services overview with a demo, pitched at developers who want results from documents without building OCR or NLP models themselves.

## Why is document processing still hard?

Documents are the primary business tool in finance, marketing and most other industries: emails, internal docs, invoices, menus, technical manuals, spread across data stores and growing every year. He lists four problems with the usual ways of handling them:

- Manual extraction is time-consuming, error-prone and expensive, and it does not scale.
- Rules-based systems are rigid and break when the format changes.
- Doing it with ML needs labelled data and ML skills.
- Some use cases need human oversight, and building review workflows is complex enough to delay shipping.

## Which services cover which step?

He places them in the top layer of the AWS ML stack, the AI services that wrap pretrained models behind an API, above SageMaker and the raw frameworks.

- **Amazon Textract** extracts text, forms and tables from PDFs and images. The pitch is an intelligent OCR you call from your workflow: document in, Textract, rows into a database.
- **Amazon Comprehend** finds insights in text from email, chat, social posts or transcribed phone calls: entities (people, organisations), key phrases, PII, sentiment, language, syntax, topics, events, plus custom classification and custom entities. Typical uses he lists are email workflow automation, routing support tickets, tagging documents and media, contact centre call analysis and intelligent document processing.
- **Amazon Comprehend Medical** does the same for clinical text: medications, medical conditions, tests, treatments and procedures, anatomy, and the relationships between them, such as a medication and its dosage.
- **Amazon Kendra** is search by meaning rather than keywords, using natural language understanding over unstructured content.

Matteo Gabrielli said at Conf42 Machine Learning 2021 that you can think of "the AWS services in general as Lego blocks that you are trying to put together in order to create your solution."

## Where does the human come in?

Amazon Augmented AI (A2I) is the fourth step and probably the most useful idea in the talk for anyone designing these pipelines. A client application sends data, the model predicts, and high-confidence results go straight through. Low-confidence ones go to human reviewers, whose consolidated answers are stored in S3 and can later feed back into improving the model. A2I supplies the review UIs and lets you choose the workforce: your own private team, a vendor trained on the task, or the public crowd through Amazon Mechanical Turk.

The trigger conditions are what make it practical. He shows three for Textract:

- A confidence threshold. As he put it, "if the score is less than 90%, send it to review."
- A missing field, such as no name or no account number found in the document.
- A random sample, for example 10% of all documents, for ongoing quality checks.

Reasons to add review include regulatory requirements, sensitive decisions and documents that are simply hard to read.

## What does the Document Understanding Solution demo show?

The solution combines Textract, Comprehend, Comprehend Medical and Kendra behind a web app, with three areas: discovery, compliance (redaction) and workflow automation. In his deployed copy, he opens a sample document and:

- previews it, highlights text and searches for a keyword such as health;
- converts the document to raw text, and has Textract find a table and download it as CSV;
- runs Comprehend entity detection, highlighting organisations such as the American Diabetes Association, and quantities;
- switches to Comprehend Medical to highlight medical conditions (diabetes, prediabetes, pregnancy), tests, treatments and protected health information;
- redacts every medical condition with one click and downloads the redacted document, the same move you would use for PII.

Search is the comparison worth seeing. A query for diabetes shows three tabs: keyword results from Elasticsearch, semantic results from Kendra (with FAQ-style answers and a relevance feedback button), and the two side by side.

Under the hood the solution also uses S3, Lambda, DynamoDB, Elasticsearch, Cognito for sign-in and CloudFront for delivery. It follows the AWS Well-Architected Framework, is open source on GitHub, is built with React and the AWS CDK, and deploys with a one-click CloudFormation template. He says it can process hundreds of thousands of documents.

## Who should watch?

Developers handed a pile of PDFs and a deadline, and architects in healthcare or finance who need redaction and human review in the pipeline from day one. ML specialists will find little new about the models themselves; the value is in how the pieces fit, and in the A2I trigger patterns.

## Related Conf42 talks

- Asif Mujawar on [Amazon Connect with Lex, Kendra and Neptune](https://www.conf42.com/Machine_Learning_2021_Asif_Mujawar_Seamless_Customer_Service_Amazon_Connect_Alexa) at Conf42 Machine Learning 2021.
- Gajendra Deshpande on [multilingual natural language processing](https://www.conf42.com/Machine_Learning_2021_Gajendra_Deshpande_Multilingual_Natural_Language_Processing) at Conf42 Machine Learning 2021.
- Dinesh Subramani on [word embeddings with SageMaker BlazingText](https://www.conf42.com/Machine_Learning_2021_Dinesh_Subramani_Natural_language_modelling_Amazon_SageMaker_BlazingText_algor) at Conf42 Machine Learning 2021.

[Watch the talk on YouTube](https://youtu.be/mIX_TU-7kP4).

## From AWS

- Amazon Web Services: [aws.amazon.com](https://aws.amazon.com/)
- Amazon Textract: [aws.amazon.com/textract](https://aws.amazon.com/textract/)
- Amazon Comprehend: [aws.amazon.com/comprehend](https://aws.amazon.com/comprehend/)
- Amazon Augmented AI: [aws.amazon.com/augmented-ai](https://aws.amazon.com/augmented-ai/)

## Watch the talk

[Empower your business use cases by getting insights from text](https://www.conf42.com/Machine_Learning_2021_Matteo_Gabrielli_Empower_business_insights_text) at Conf42 Machine Learning 2021.
