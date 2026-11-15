# Snowflake turned weeks of CSAT triage into an overnight job

Conf42 Blog, 2025-11-05, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/snowflake-ai-csat-feedback-overnight

In short: Rajanikant Vellaturi of Snowflake at Conf42 DevSecOps 2025 on starting AI customer experience small: classify survey feedback inside the workflow you have.

Thousands of free-text survey answers a week, three people reading them by hand, and the insight arriving after it stopped mattering. At Conf42 DevSecOps 2025, Rajanikant Vellaturi, Senior Support Communications Manager at Snowflake, showed how his team plugged an AI classifier into its existing feedback pipeline and turned weeks of manual tagging into a job that finishes overnight.

The talk is broad, covering personalisation, AI agents and predictive support across retail, finance, healthcare, telecom, SaaS and manufacturing, but the Snowflake case study is the part with real engineering in it.

## The CSAT problem, in the speaker's words

When a support ticket closes, Snowflake sends a survey with an open text box. Customers use it for anything: feature complaints, service quality, a thank-you to the engineer who fixed their issue. That is thousands of responses every week, and a team of three was reading each one, tagging sentiment as positive, negative or neutral, and mapping it to an issue type such as product feature, service quality or technical issue.

It did not scale. Rajanikant describes the work as repetitive data entry that burned the team out, and by the time a bucket of feedback reached the team that owned the problem, it was stale.

## Plug the model in, don't rebuild the house

The fix is deliberately boring. Survey responses already landed in a Snowflake table. The team added an AI classification step that reads that table, assigns sentiment and issue type at scale, and writes the results to another table. The job is scheduled for Sunday night, so on Monday morning the teams find last week's feedback sorted and ready to act on.

Results, as he reports them: processing time dropped from weeks to hours, CSAT and response times improved, and the people who used to tag rows now spend that time on cross-functional fixes and closing the loop with customers. The lesson he keeps repeating is that nothing was built from scratch. The workflow stayed; one manual step became a model call.

## Agents, prediction and the creepy line

Beyond the case study, Rajanikant contrasts script-based chatbots that answer "what are your store hours" with agents that keep context, notice frustration and hand off to a human with the full history, so the customer never starts over. His airline example: miss a flight, and the app's agent rebooks you and you just click accept.

On prediction, he lists telecom companies spotting signal drops before customers notice, SaaS products spotting unused features and sending tailored tutorials, IoT sensors scheduling maintenance before machines fail, and payment systems issuing refunds before anyone complains.

He is candid about the challenges: data scattered across CRM, transaction systems and warehouses, bias from narrow training data, and over-personalisation that unsettles customers. His answers are data integration and governance first, fairness testing across segments, telling customers you use AI with an opt-out, and a human in the loop for critical decisions.

## Five practices worth copying

His closing list: data first; integrate AI into existing workflows; keep a human in the loop; measure continuously (before and after CSAT, resolution times, retention); be transparent with customers. Start small, he says, find where people do the most manual work, and put the model there.

## Who should watch

Support and CX leads who are being asked for an AI strategy and want a first project that will actually ship, and data engineers who own the tables those projects will read. If you want architecture diagrams or model choices, this is not that talk; it is a practitioner's playbook.

## Related talks

- Dmitry Kindrya asks whether LLMs [rescue customer support or ring its death knell](https://www.conf42.com/Large_Language_Models_LLMs_2024_Dmitry_Kindrya_customer_support_revolutionizing), the sceptic's take on the same question.
- [Reliable API Support: Human-in-the-Loop Agentic RAG for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human) by Vishal Shah, for the human handoff done in an engineering context.
- Ed Fullman's [product management view of LLMs for customer experience](https://www.conf42.com/Large_Language_Models_LLMs_2025_Ed_Fullman_customer_experience_product).

[Watch Rajanikant Vellaturi's talk](https://www.conf42.com/DevSecOps_2025_Rajanikant_Vellaturi_start_scale_succeed)

[Watch the talk on YouTube](https://youtu.be/Ry5i7ibI4MI).

## Watch the talk

[AI-Driven Customer Experience: How to Start, Scale, and Succeed in the Enterprise](https://www.conf42.com/DevSecOps_2025_Rajanikant_Vellaturi_start_scale_succeed) at Conf42 DevSecOps 2025.
