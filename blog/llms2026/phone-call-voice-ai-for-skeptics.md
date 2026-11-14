# Voice AI over a plain phone call, for users who distrust AI

Conf42 Blog, 2026-05-21, updated 2026-11-09. https://www.conf42.com/blog/llms2026/phone-call-voice-ai-for-skeptics

In short: Pavel Shchekotov (Denk Solutions) at Conf42 LLMs 2026 on running an LLM voice agent over phone calls and SMS for users aged 55+, and what broke.

The easiest way to onboard someone who will never install your app is to let them call a phone number. At Conf42 Large Language Models (LLMs) 2026, Pavel Shchekotov, co-founder of Denk Solutions, shares what happened when his team at Sofi Connect, where he was founding engineer, built an LLM voice agent for a dating service aimed at people aged 55 and over, delivered over ordinary phone calls and text messages.

The bet was that a concierge-style voice experience would lift retention, and that a phone call would remove app installs, accounts and registration from the funnel. It did remove them. It also surfaced a long list of problems that never show up in a chatbot demo.

## Trust is a design problem before it is a model problem

Many people don't want to talk to robots, and some react to the word AI itself. Accents tripped speech-to-text. And an unexpected call from an unknown number about a new service looks a lot like a scam.

Users also went off script: related questions, personal stories, and in a few cases flirting with the bot. Every off-script minute costs money, but you can't simply hang up on a person.

The team's responses were small and deliberate:

- A calm, pleasant voice: a neutral female voice from the latest ElevenLabs models at the time, because it sounded less robotic.
- A neutral human name, Sophie, while still disclosing up front that it is AI (US rules require it). The wording was tuned to be transparent without scaring people off.
- No picture of Sophie anywhere, for the same reason Siri and Alexa don't have faces: any face wins some users and loses others.
- Caller identification: users were asked to save the number, and calling name presentation showed who was calling even when they hadn't.
- Memory, via Mem0, so Sophie could bring back small details from earlier conversations. Pavel calls this the difference between a script and a personal experience.

Scripts were written to be heard. A sentence that looks short on screen can drag when spoken, so every phrase was replayed out loud, and a guardrail layer politely steered off-topic conversations back on track.

## The phone network has opinions

Latency at least has known fixes: optimise networking and code, move infrastructure closer to users, pick faster providers, and run speech-to-text locally if you can. Pavel's benchmark is roughly 500 to 700 milliseconds end to end, from voice activity detection to the first audio chunk of text-to-speech, on top of phone network latency.

Other problems have no clean fix. Local carriers block calls. Landlines can't receive SMS. Calls drop.

The surprise was voicemail. Undetected voicemail wastes money at best and can ruin a user's journey at worst. Twilio's built-in answering machine detection was a start but not perfect, so the team layered heuristics on top (a voice reading out a string of digits, phrases like "you have reached") and, once they had collected enough real examples, an LLM-based detector.

## SMS is billed by the segment

The text agent had its own constraints. SMS is charged per segment of about 160 characters, and some punctuation and emoji eat more space, so the agent had to count characters. Delivery rates depend on opt-out phrasing and on not looking spammy or sensitive, which is easy to trip in dating. Payment links sent by SMS had low delivery, which is understandable: a payment link in a text looks scammy. Without an app, that's an extra drop-off on top of the usual paywall.

And every interaction has a marginal cost: each minute, each message, each failed delivery.

## Who should watch

Product engineers considering voice for audiences that mainstream AI products ignore, and anyone who has only built voice agents for browsers. It's a practitioner's war story more than an architecture talk, and the voicemail and SMS details alone will save someone a sprint.

## Related Conf42 talks

- [Building Trust in Conversational AI: The Role of Explainable AI in Enhancing Chatbot Transparency](https://www.conf42.com/DevSecOps_2024_Shradha_Kohli_conversational_ai_trust) by Shradha Kohli, on trust from the explainability side.
- [Scaling Conversational AI in Production: MLOps Strategies for Contact Center Transformation](https://www.conf42.com/MLOps_2025_Manoj_Kumar_Vunnava_scaling_conversational_ai) by Manoj Kumar Vunnava, for running conversational AI at contact-centre scale.
- [How To Use Voice AI For Incident Reporting, Monitoring and Alerts](https://www.conf42.com/Site_Reliability_Engineering_2021_Arthur_Grishkevich_voice_AI_Incident_reporting_monitoring_alerts) by Arthur Grishkevich, an earlier take on phone-first interfaces.

[Watch Pavel Shchekotov's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Pavel_Shchekotov_voice_ai_trust)

[Watch the talk on YouTube](https://youtu.be/f2pBELR8CaI).

## Watch the talk

[Building Voice AI for People Who Don’t Trust AI](https://www.conf42.com/Large_Language_Models_LLMs_2026_Pavel_Shchekotov_voice_ai_trust) at Conf42 Large Language Models (LLMs) 2026.
