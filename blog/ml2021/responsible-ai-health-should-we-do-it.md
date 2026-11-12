# Responsible AI in health starts with asking whether you need AI at all

Conf42 Blog, 2021-07-28. https://www.conf42.com/blog/ml2021/responsible-ai-health-should-we-do-it

In short: Tempest van Schaik (Microsoft) at Conf42 Machine Learning 2021 on turning responsible AI principles into review questions and fairness tooling for health

Sometimes the most responsible machine learning model is a SQL query. Dr. [Tempest van Schaik](https://www.conf42.com/Machine_Learning_2021_Tempest_van_Schaik_Responsible_AI_in_Health), a machine learning engineer in Microsoft's Commercial Software Engineering team and a biomedical engineer by training, used her Conf42 Machine Learning 2021 talk to show how her team turns responsible AI from a list of principles into a review board, a set of blunt questions and three open source tools. Her takeaway: keep the sensitive attributes you are tempted to delete, because without them you cannot prove your model is fair.

It is a short, practical talk aimed at practitioners rather than ethicists, with a healthcare lens throughout.

## Why does responsible AI look like early car safety?

She opens with cars. The first car on the street was followed by the first car fatality, and only then came windshields, headlights, traffic lights, seatbelts and, in 1955, the driver's test. Her view is that AI is at the windshield stage: the technology is out, and the safety work is catching up.

Facial recognition is her example of the shift. A few years earlier it was a genuine engineering breakthrough everyone wanted to crack; once the consequences showed up, companies started asking whether to ship it at all. Tempest van Schaik said at Conf42 Machine Learning 2021 that "machine learning researchers and practitioners have moved from asking, can we do it? To should we do it?"

## What can ML borrow from medical research ethics?

Medical research had its reckoning decades earlier, with the Belmont Report in 1979. Several of its norms map directly onto ML work:

- **Data transparency.** A paper with human subjects has to state who was studied: how many people, their race, sex, education and region. Responsible AI now asks the same of a data set, including who is missing from it.
- **Informed consent.** Did people agree to have their data used by this algorithm, not just collected?
- **Group and individual harm.** A study can hurt one participant or the whole group they belong to; so can a model.
- **Privacy.** Keeping personal data private is the practitioner's job, not a legal afterthought.

Her own route into the topic was a project she had ethical concerns about, and leadership that backed her when she asked whether the team should take it on.

## What does the review board actually ask?

Her team works across very different customer AI projects, so it runs a responsible AI review board as a sounding board that ends in recommendations. The questions are the useful part:

- Is this solvable with AI, or would a SQL query or a social intervention do? Machine learning brings maintenance and responsibility of its own.
- Who are the stakeholders, and are any of them vulnerable: children, the elderly, immigrant groups, historically oppressed groups? Regulators and the company's own brand count too.
- What are the benefits and harms for each stakeholder, listed exhaustively?
- Does the data contain personally identifiable information you do not need? Training rarely needs names, addresses or phone numbers.
- Does the model feed consequential decisions such as jobs, loans or health care? Then it probably needs to be explainable.
- How could it be misused? She calls this Black Mirror brainstorming, after the TV series where technology goes very wrong.
- Is it accurate overall but bad for one group, and does the training data resemble production? A language model trained on tweets is the wrong tool for searching medical literature.
- What is the environmental cost of training a huge model for days or weeks?

## What changes when the data is medical?

Health adds its own list. Genetic data says a lot about a person and their relatives, so privacy and security (HIPAA training included) are table stakes. Domain experts matter more than anywhere: a doctor, nurse or patient who can sense-check the work. Open science pulls the other way, since a genome set collected for cardiovascular research could help respiratory researchers too, and that has to be balanced against privacy.

Then cost. Having moved to the USA, she flags billing and price data as a bias trap, because they reflect unequal access to healthcare. She points to the Obermeyer et al. paper, Dissecting racial bias in an algorithm used to manage the health of populations, about a production algorithm that never used race as a feature and was still racially biased.

That is why she argues against simply dropping race and sex. They can be real disease predictors, as COVID showed, and they can encode historical unfairness. Tempest van Schaik said at Conf42 Machine Learning 2021 that "what works really well is to capture that data and keep that data so that you can actually audit how fair your model is for those different groups."

## Which tools does she use?

- **Datasheets for Datasets**, borrowed from electronics: every microcontroller ships with a data sheet, so every data set should ship with one saying how it was collected, who is in it, who is not, and its limits.
- **Fairlearn**, Microsoft's open source Python package, to break a metric down by sensitive feature. Her example model had an area under the ROC curve of 92% overall, which looks great until you split it by sex and race.
- **InterpretML**, also open source from Microsoft, including the Explainable Boosting Machine. On the adult income data set (predicting who earns more than $50,000 a year) it shows, per person, which features pushed the prediction up, such as years of education, and which pushed it down, such as marital status and age.

She closes with reading: Cathy O'Neil, Hanna Wallach, Timnit Gebru, Rachel Thomas, Deborah Raji, Kate Crawford and Arvind Narayanan, the Coded Bias documentary, Kate Crawford's Atlas of AI, and her team's public engineering playbook on GitHub.

## Who should watch?

ML engineers about to start a project with people in the data, especially in health, and anyone who has to run an ethics review without a philosophy degree. The question list alone is worth stealing for your next kickoff.

## Related Conf42 talks

- [Utilizing the power of machine learning in healthcare](https://www.conf42.com/Machine_Learning_2023_Yogesh_Seenichamy_ml_healthcare) at Conf42 Machine Learning 2023.
- [Ethical AI through prompt engineering: mitigating bias](https://www.conf42.com/Prompt_Engineering_2024_Parvin_Gasimzade_ethical_ai_bias) at Conf42 Prompt Engineering 2024.
- [Healthcare chatbot transparency with explainable AI](https://www.conf42.com/DevSecOps_2024_Abhishek_Vajpayee_Rathish_Mohan_healthcare_chatbot_transparency) at Conf42 DevSecOps 2024.

[Watch the talk on YouTube](https://youtu.be/iWpCDH9l8G4).

## From Microsoft

- Microsoft: [microsoft.com](https://www.microsoft.com/en-ie/)
- Fairlearn, the open source fairness toolkit shown in the talk: [fairlearn.org](https://fairlearn.org/)
- InterpretML and the Explainable Boosting Machine: [interpret.ml](https://interpret.ml/)

## Watch the talk

[Responsible AI in Health: From Principles to Practice](https://www.conf42.com/Machine_Learning_2021_Tempest_van_Schaik_Responsible_AI_in_Health) at Conf42 Machine Learning 2021.
