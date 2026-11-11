# Skip the paid speech API, call whisper.cpp from Go

Conf42 Blog, 2023-04-20. https://www.conf42.com/golang2023/whisper-cpp-go-bindings-transcription

In short: Pratim Bhosale (SurrealDB) at Conf42 Golang 2023 on building an open source transcription CLI in Go with whisper.cpp and its Go bindings

Subtitles for your own meetings should not need a cloud contract. At Conf42 Golang 2023, Pratim Bhosale, Developer Advocate at SurrealDB, showed how she replaced paid speech-to-text APIs with OpenAI's open source Whisper model, run through whisper.cpp and called from a small Go CLI via the project's Go bindings, ending with a live transcription of a YouTube clip.

It is a short, practical intro rather than a benchmark study. SurrealDB sponsored the slot, but the talk is about Whisper and Go, not the database.

## Why not just use a cloud API?

She started out wanting subtitles for her meetings, found most tools were paid, and did what developers do: decided to build one. The managed options from Google and Amazon looked fine until she worked out the bill. By her calculation for Google's speech-to-text API, crossing the free threshold could mean at least $1,000 a month in transcription fees, which pushed her towards an open source model she could run herself.

## What is Whisper, and where does whisper.cpp fit?

Whisper is OpenAI's open source automatic speech recognition system, trained on a large amount of multilingual, multitask supervised data from the web. "It is one of the most underrated models of OpenAI," Pratim Bhosale said at Conf42 Golang 2023, noting that companies such as Snap Inc. and Shopify already use the Whisper API.

Her walkthrough of the architecture is the useful kind of brief. Audio is cut into 30-second chunks and converted into a visual representation of its features. A transformer encoder processes the speech and a decoder turns it into text. Special tokens tell the model which task to perform, so the same model can identify the language, timestamp phrases, transcribe many languages and translate speech into English.

whisper.cpp is a lightweight C/C++ implementation of the model, built for faster execution and lower resource use than the reference version. That is what makes it practical on an ordinary machine.

## How does Go talk to C?

Through bindings. Go bindings let your Go code call functions and use data structures from a library written in another language, bridged through that language's foreign function interface. whisper.cpp ships its own Go bindings, so the Go application stays Go and the heavy lifting stays in C.

## What does the code do?

Her CLI downloads the audio of a YouTube video and transcribes it. The core is one transcribe function:

- Load the Whisper model with the bindings' constructor, passing the model path.
- Create a context for the model. She explains context in the speech sense too: surrounding words help the model predict and interpret what is being said, which improves accuracy.
- Decode the WAV file, the format Whisper accepts, into a slice of samples, after checking that the sample rate and channel count match what Whisper expects (otherwise return an error).
- Hand the samples to the context's process call, which does the transcription, then print the result.

The dependencies are dockerised to avoid cross-platform build problems with the C code.

## Did the demo work?

Yes, after the Docker build, which she narrates as finishing 10,000 years later, a feeling anyone who has compiled C inside a container will recognise. The clip is a 32-second coffee-shop advert, and the output matches it word for word, including the fresh coffee and bagels. Longer videos simply take longer, so she kept it short.

Use cases she lists: meetings, interviews, podcasts, customer support calls, voice assistants and real-time closed captions.

## Who should watch

Go developers who want speech-to-text in their stack without a per-minute API bill, and anyone curious how Go code drives a C library through bindings. It is a starting point, not a production guide: there is no discussion of throughput, GPUs or accuracy tuning. Pair it with [Alexandre Evangelista de Souza on LangChain with Go](https://www.conf42.com/Golang_2024_Alexandre_Evangelista_de_Souza_langchain), [Murali Krishna Reddy Mandalapu on AI inference at the edge](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge) and [Waseem Syed on multimodal audio and video models](https://www.conf42.com/Large_Language_Models_LLMs_2025_Waseem_Syed_multimodal_audio_video).

[Watch Pratim Bhosale's talk](https://www.conf42.com/Golang_2023_Pratim_Bhosale_speechtotext_transcriptions_whisper)

## From SurrealDB

- [SurrealDB](https://surrealdb.com/): the database company Pratim Bhosale represented at Conf42 Golang 2023.

[Watch the talk on YouTube](https://youtu.be/wGkaYfcHDfs).

## Watch the talk

[Whispering into the Future: Reinventing Speech-to-Text Transcriptions with Go and Whisper](https://www.conf42.com/Golang_2023_Pratim_Bhosale_speechtotext_transcriptions_whisper) at Conf42 Golang 2023.
