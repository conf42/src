# Sentiment analysis that never leaves the browser

Conf42 Blog, 2025-10-18, updated 2026-11-09. https://www.conf42.com/blog/js2025/sentiment-analysis-that-never-leaves-the-browser

In short: Ujjwala Modepalli of Wells Fargo showed at Conf42 JavaScript 2025 how TensorFlow.js, Web Workers and IndexedDB run text analytics client-side.

Your analytics know a user clicked "Contact support". The message they typed afterwards knows they were furious. At Conf42 JavaScript 2025, Ujjwala Modepalli, Senior Credit Risk Specialist at Wells Fargo, showed how to read that text with NLP that runs entirely in the browser, so the raw words never reach your servers.

## Clicks tell you what, text tells you why

Her starting point: traditional analytics track clicks, scrolls and time on page, but every form, chat message, search query and feedback comment carries signals about emotion, intent, confusion and satisfaction. Those signals have mostly been ignored because processing language meant expensive server-side pipelines.

Moving the work to the client gives three wins in her framing: privacy (the text stays on the device, which simplifies compliance), real-time feedback (sentiment can update as the user types, so the interface can offer help), and efficiency (users "bring their own compute", with GPU acceleration in the browser, so server costs and latency drop).

## The toolkit and the architecture

The libraries are small and familiar:

- **Natural** and **Compromise** for tokenisation, part-of-speech tagging and entity recognition, with no external dependencies.
- **TensorFlow.js**, using WebGL for GPU acceleration, for sentiment scoring and text classification with pre-trained models.
- **Web Workers** to keep NLP off the main thread so the UI never freezes, and **IndexedDB** to store results locally across sessions.

Service workers cache models for offline use, and results flow into a state layer (Redux or Context API) that updates React components. She described it as distributed computing at the browser level.

## Real-time sentiment without analysing every keystroke

The pipeline loads a lightweight pre-trained model (a small transformer or LSTM variant) at startup. Input events are debounced so analysis runs after the user pauses, not on every key. Text is normalised, tokenised (stop words removed, stemming applied) and vectorised with TF-IDF or embeddings, then scored. The score shows up in the UI as a colour, an emoji or a gauge.

On top of that she showed topic modelling with k-means or hierarchical clustering on vectorised snippets, so clusters like billing issues or feature requests form and update as new messages arrive. Custom React hooks talk to the workers, context providers share results across the app, and D3.js draws timelines, word clouds and cluster graphs.

## Four kinds of users hiding in your text boxes

The segmentation section is the most product-friendly part. Language separates hesitant users ("maybe", "I think", lots of questions), competitive switchers who name other products or pricing, high-intent prospects with decisive phrasing, and at-risk users whose negative sentiment and cancellation words signal churn early. She layers that into features (polarity, readability, emotional intensity), behavioural metrics (how often and how fast people write, whether their tone shifts) and finally scores such as a satisfaction index or churn probability.

## Performance and consent are part of the design

Client-side models are heavy, so she lazy-loads TensorFlow models only when needed, batches inference to use the GPU better, debounces input and caches results in IndexedDB under hashed keys so repeated text isn't re-analysed. On privacy: explicit opt-in that explains what's analysed, users can view, export or delete their data, stored text is encrypted, and analytics switch off in private browsing.

Use cases she listed: routing frustrated or urgent support chats to live agents, finding content gaps from search intent, and auto-tagging feedback as bugs, feature requests or praise.

## Who should watch

Frontend and product engineers who want sentiment or intent signals without building a data pipeline, and anyone whose privacy review blocks sending free text to a server. It's an architecture and pattern talk rather than a live coding session.

## Related talks

- [AI with JS: The Future is on the Browser](https://www.conf42.com/JavaScript_2024_Danielle_Maxwell_19_ai_browser) is a broader look at running models client-side.
- [Leveraging NLP for Enhanced Incident Management: Sentiment Analysis and Language Generation](https://www.conf42.com/Incident_Management_2024_Vishal_Khadake_49_nlp_sentiment_language) applies sentiment analysis to a very different kind of text.
- [Data analytics in browser with AlaSQL.JS](https://www.conf42.com/JavaScript_2022_Gaurab_Patra_Bhagyajit_Jagdev_data_analytics_browser_alasqljs) is another take on keeping analytics work on the client.

[Watch Ujjwala Modepalli's talk](https://www.conf42.com/JavaScript_2025_Ujjwala_Modepalli_client_side_nlp)

[Watch the talk on YouTube](https://youtu.be/zVvGB5Jp88I).

## Watch the talk

[Client-Side NLP: JavaScript Text Analytics for User Behavior Intelligence](https://www.conf42.com/JavaScript_2025_Ujjwala_Modepalli_client_side_nlp) at Conf42 JavaScript 2025.
