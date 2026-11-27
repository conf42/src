# CO-STAR prompts turn generic LLMs into e-commerce seller tools

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/costar-prompts-for-ecommerce-seller-tools

In short: Sureshkumar Karuppuchamy (eBay) at Conf42 Prompt Engineering 2025 on CO-STAR prompts for personalization, forecasting, pricing, listings and shopping chatbots.

The model every seller can rent is the same one their competitors rent; the difference is in what you tell it. At Conf42 Prompt Engineering 2025, Sureshkumar Karuppuchamy of eBay walked through prompt engineering for e-commerce seller tools, built around the CO-STAR checklist, and applied it to personalization, demand forecasting, dynamic pricing, product listings and conversational commerce, ending with a view of seller tools in 2030.

It's a broad survey talk with a practical core: the prompt patterns are concrete enough to copy, while most of the business numbers are industry figures he cited rather than results from one system.

## CO-STAR is a checklist, not magic

The prompt-writing section is the most reusable part. CO-STAR stands for context, objective, style, tone, audience and response format, and Sureshkumar uses it as a pre-flight check: did you give background, say what outcome you want, set the voice, name who the answer is for, and specify a list, paragraph or JSON?

Around it he adds habits that apply well beyond retail. State constraints up front (length limits, content to avoid). Treat prompting as iteration, not a one-shot. Give the model a role and the context it needs. His before-and-after example: instead of asking what product to recommend, tell the model it's a virtual assistant helping a customer who likes outdoor activities, based on their browsing history, and ask for a recommendation with a reason. And show an example of the output shape you want. The model can only do what you ask, so ask precisely.

## Personalization is context injection

His personalization example is a prompt that carries the customer's recent history: they bought running shoes and have been browsing trail-running gear, so suggest three more products with a one-sentence rationale each. That's the whole technique. The model doesn't know your shopper; the prompt does. He paired this with industry figures on revenue, retention and order value from good personalization.

## Forecasting and pricing want more signals

For demand forecasting, the argument is that AI can mix unstructured signals (social media buzz, weather, news) with historical sales. His sample prompt asks for next month's demand per category given last year's sales data plus recent social media mentions. He cited forecast accuracy rising from around 60% to 80% and stockouts falling by up to 65% in AI-driven setups.

Dynamic pricing applies the same idea: inventory levels, market trends, competitor prices and review sentiment feed a suggested price. Overstocked and slow? Discount. Scarce and in demand? Hold steady or nudge up.

## Listings, reviews and chatbots that sell

Content generation gets the most vivid example: one small business reportedly cut listing creation from 60 minutes per item to 15, and a retailer saw more organic traffic after switching to AI-written listings, because the copy naturally included relevant keywords. AI review summaries turn thousands of reviews into a highlight reel of pros, cons and recurring themes.

On conversational commerce, he's clear that a good shopping bot needs two things: well-designed prompts and access to real-time data such as product details, order status and customer profile. His techniques: inject relevant data into the prompt, use system roles and personas, give the bot a conversational blueprint rather than letting it wing it, and keep feeding the conversation history so context survives. The example of a bot finding a science kit for a 10-year-old niece shows the shift from support desk to sales assistant.

## The 2030 bet

His outlook: natural-language interfaces replacing dashboards, digital twins of individual shoppers, autonomous workflows, AI coworkers for operations teams, and prescriptive analytics that say what to do next, not just what happened. The competitive edge, he argues, is your proprietary data plus a library of prompts refined over time.

## Who should watch

Product managers and engineers building seller-facing or shopper-facing AI features, and anyone who wants a clean, copyable prompt checklist with retail examples. If you're after evaluation methodology or a production architecture, look elsewhere; this one is about framing and use cases.

## Related Conf42 talks

- [Optimizing Retail Forecasting Through Advanced AI Models: The Role of Prompt Engineering](https://www.conf42.com/Prompt_Engineering_2024_Sijo_Valayakkad_Manikandan_retail_forecasting_ai) by Sijo Valayakkad Manikandan at Conf42 Prompt Engineering 2024.
- [Hyper-Personalization: Using AI & Analytics to Fuel Digital Transformation & Growth](https://www.conf42.com/Machine_Learning_2025_Lakshmi_Narayana_Gupta_Koralla_hyper_personalization) by Lakshmi Narayana Gupta Koralla at Conf42 Machine Learning 2025.
- [Ecommerce OMNI Channel optimization using AI](https://www.conf42.com/Machine_Learning_2024_Jubin_Thomas_ecommerce_omni_channel_optimization) by Jubin Thomas at Conf42 Machine Learning 2024.

[Watch Sureshkumar Karuppuchamy's talk](https://www.conf42.com/Prompt_Engineering_2025_Sureshkumar_Karuppuchamy_ecommerce_tools_ai) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/qEPNReNZRhM).

## Watch the talk

[Prompt Engineering for E-commerce AI: Transforming Seller Tools by 2030](https://www.conf42.com/Prompt_Engineering_2025_Sureshkumar_Karuppuchamy_ecommerce_tools_ai) at Conf42 Prompt Engineering 2025.
