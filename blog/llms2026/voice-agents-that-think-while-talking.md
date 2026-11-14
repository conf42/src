# Voice agents that think while they talk, with a Thinker and a Speaker

Conf42 Blog, 2026-05-20. https://www.conf42.com/blog/llms2026/voice-agents-that-think-while-talking

In short: Bohdan Snisar (Solea AI) at Conf42 LLMs 2026 builds a voice pipeline layer by layer, then splits reasoning from speech to fit a 500 ms budget.

A voice agent gets about 500 milliseconds to answer before the conversation feels wrong, and that leaves almost no room for a model to think. At Conf42 Large Language Models (LLMs) 2026, Bohdan Snisar, founding engineer at Solea AI (an AI operating system for home service businesses), builds the classic voice pipeline layer by layer, shows where it hits the wall, and then moves the reasoning off the critical path entirely.

## Voice is not a chat with audio

Text is asynchronous: you can edit before sending, and the system answers request by request. Voice is synchronous. The user hears it once, timing carries meaning, and there is no undo. Pause too long and you sound confused; answer too fast and you cut someone off.

So the simple loop of listen, understand, reason, act and speak gets hard as soon as it must happen in real time.

## The cascade, and everything before the first token

The usual production stack is three models in a row: speech-to-text, an LLM, text-to-speech. It is modular and observable, and you can swap providers per language or pick an ElevenLabs voice. Each stage waits for the previous one, so in practice everything streams chunk by chunk. Speech-to-speech models like GPT Realtime or Gemini Live cut latency but cost you control and observability.

Before any model runs, there is plain real-time engineering: WebRTC, jitter, echo cancellation, packet loss, audio arriving in 20 ms frames. Bohdan's advice is to let platforms handle most of it.

Then comes turn-taking, which he treats as one of the hardest problems. Voice activity detection only answers whether someone is speaking right now (Silero is his balanced default). Endpointing and turn detection answer the more important question: has the user finished the thought? Get it wrong and the agent talks over people, or leaves them hanging.

Tool calls make the budget worse. A CRM lookup or calendar check can take 500 ms to five seconds. His rule: never let a tool call block the conversation. Cover it with filler speech, run it asynchronously, and inject the result when it is ready. That background-then-inject pattern is the seed of everything that follows.

## Separate the Thinker from the Speaker

Fast models keep the SLA but reason shallowly; reasoning models think well but blow the budget. Voice needs both. The LTS voice agent architecture splits them into two tracks.

The foreground Speaker streams the conversation and never blocks. In the background, a semantic trigger decides when the transcript holds enough meaning to be worth thinking about, so you don't pay for reasoning on every word. The Thinker, a stronger model, maintains a structured delta-state (new address, new time, the intent of the call) and injects it into the Speaker, which steers mid-conversation.

His example: a caller starts talking about cancelling. The trigger fires, the Thinker combines intent, sentiment, account data and company policy, and the Speaker gets a state update suggesting a 20% discount offer. If the user changes topic, the coordinator kills the Speaker and keeps the Thinker's state. The Speaker is disposable; the Thinker is durable. Barge-in handling is where Bohdan locates most of the difficulty in good voice agents.

## From one Thinker to a team of sidecars

The last step replaces the single Thinker with parallel sidecars: small, cheap models that each watch the live transcript for one thing (intent, complaint detection, retrieval, notes). An expensive reducer merges their outputs and produces one compact state object with a clear next action.

The catch is freshness. Background reasoning takes time, and guidance that lands after the conversation moved on is worse than none. He lists the controls: a TTL on state, turn identifiers so state matches the turn it was computed for, and never letting a stale snapshot replace a fresh one.

## Who should watch

Engineers building or evaluating voice agents who already know the STT, LLM, TTS diagram and want the next layer. The tool survey (LiveKit, Silero, Deepgram, ElevenLabs, Retell, Vapi) is a handy map, and the Thinker and Speaker split applies to any latency-bound agent. Bohdan also spoke at Conf42 earlier, on [GepAI in development processes and dev tools](https://www.conf42.com/Prompt_Engineering_2024_Bohdan_Snisar_gepai_development_tools).

## Related Conf42 talks

- [Building a Production-Ready Voice AI Agent with LangGraph, RAG and Evaluation](https://www.conf42.com/MLOps_2026_Arjun_Thakur_voice_langgraph_rag) by Arjun Thakur, for evaluation and retrieval in a voice stack.
- [Whispering into the Future: Reinventing Speech-to-Text Transcriptions with Go and Whisper](https://www.conf42.com/Golang_2023_Pratim_Bhosale_speechtotext_transcriptions_whisper) by Pratim Bhosale, on the first box of the cascade.
- [LLM-Enhanced Multimodal AI for Audio and Video Interaction](https://www.conf42.com/Large_Language_Models_LLMs_2025_Waseem_Syed_multimodal_audio_video) by Waseem Syed, the speech-to-speech side of the trade-off.

[Watch Bohdan Snisar's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Bohdan_Snisar_httpsyoutube5XSR13KHev4)

## Watch the talk

[Voice Agents That Think While They Talk: From STT–LLM–TTS Pipelines to Realtime Parallel Reasoning](https://www.conf42.com/Large_Language_Models_LLMs_2026_Bohdan_Snisar_httpsyoutube5XSR13KHev4) at Conf42 Large Language Models (LLMs) 2026.
