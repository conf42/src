# Self-service BI works when security is neither too tight nor too loose

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/secure-self-service-bi-dropbox

In short: Mallikarjun Bussa of Dropbox at Conf42 DevSecOps 2025 on letting everyone query data with AI-powered BI while least privilege, masking and lineage keep it safe.

Everyone wants answers from the data, and nobody wants to wait a week for a report. At Conf42 DevSecOps 2025, Mallikarjun Bussa, Lead Business Intelligence Engineer at Dropbox, made the case that self-service BI and DevSecOps belong together: give people direct, AI-assisted access to data, and build the security in from the start so that access does not turn into a leak.

It is a short, plain-spoken talk from someone with 18 years in BI and data, aimed at the balance point rather than at any one tool.

## Too much data, too few answers

Mallikarjun's diagnosis is familiar to anyone who has owned a reporting backlog. Companies have more data than ever and still struggle to answer simple questions, because the data sits in too many systems and silos and every report takes too long. Self-service BI is his answer: marketing, HR, finance and operations open a dashboard and get the insight in minutes instead of filing a ticket and waiting.

The catch is obvious. Hand more people access and you widen the blast radius. That is where he brings in DevSecOps: build security into development, deployment and daily operations instead of patching it on at the end. His analogy: you put the seatbelt on before driving, not after.

## Why most BI projects fail

He cites studies saying 70% of BI projects fail, and the reasons he lists are about people and governance rather than technology: no governance, untrained users, access that is either too open or too restricted, and systems too complicated to use. The 30% that succeed balance security with easy access. Too tight and people route around it; too loose and you end up in an incident review.

## AI makes it easier, which raises the stakes

Natural language querying changes who can ask questions. Instead of SQL, users ask for this month's revenue or for the top reasons for churn, and the system finds patterns, predicts outcomes and guides them. He likens it to a small data analyst sitting on your shoulder. The more powerful the tool, he warns, the more the security matters.

His two examples keep it grounded. A marketing team using AI-powered BI saw campaign reporting drop from hours to minutes, cut costs and improved ROI while staying compliant with privacy law. An HR team used predictive analytics to spot employees likely to leave so it could offer help early, which only worked because the sensitive details were visible to HR alone and every access was audited.

## The controls are simple on purpose

The security baseline he recommends is deliberately unexciting: least-privilege access, masking sensitive data for people who should not see it, multi-factor authentication, and sessions that time out automatically. On top of that sits lineage, the story of where a number came from, what transformed it and who touched it, so that when a leader asks about a figure on a dashboard, you have an answer, and the auditors stay happy.

He closes on culture: leadership support, trained users, clear policies, continuous improvement. His roadmap is four steps (assess the current state, design the architecture with security and automation in mind, enable and train users, monitor and optimise), and he says it works for small teams and large enterprises alike.

## Who should watch

Data platform and analytics engineers rolling out self-service tooling or natural-language querying, and security teams asked to approve it. It is an overview, so treat it as a checklist for the conversation rather than an implementation guide.

## Related talks

- [AI-Driven Sensitive Data Discovery for Secure DevSecOps and Privacy Compliance](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) by Mary Sirisha Duggimpudi, on finding the data you need to mask.
- Satya Manesh Veerapaneni on [AI-powered BI in healthcare with Go](https://www.conf42.com/Golang_2025_Satya_Manesh_Veerapaneni_healthcare_bi_analytics).

[Watch Mallikarjun Bussa's talk](https://www.conf42.com/DevSecOps_2025_Mallikarjun_Bussa_data_access_secure)

[Watch the talk on YouTube](https://youtu.be/jP5dW9j_Zlw).

## Watch the talk

[Secure Self-Service BI: Democratizing Data Access in the DevSecOps Era](https://www.conf42.com/DevSecOps_2025_Mallikarjun_Bussa_data_access_secure) at Conf42 DevSecOps 2025.
