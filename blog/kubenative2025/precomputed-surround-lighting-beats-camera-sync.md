# Pre-computed surround lighting beats the camera pointed at your TV

Conf42 Blog, 2025-10-07, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/precomputed-surround-lighting-beats-camera-sync

In short: Chandan Kumar (Google) at Conf42 Kube Native 2025 on pre-computing ambient light signals from the video stream to sync smart lights in ~60 ms.

Anyone who has set up sync lighting knows the scene: the police chase ends, and only then does the room start flashing red and blue. At Conf42 Kube Native 2025, Chandan Kumar, a software engineer at Google, presented a fix: stop watching the screen with a camera, and pre-compute the light signals from the video signal itself, ahead of time. His benchmark put the result at about 60.7 ms end to end, against the 200 to 300 ms he measured for conventional systems.

This is a design talk based on a defensive publication he wrote under the same name. It sits a long way from Kubernetes, and it is one of the more fun talks on the event's IoT track.

## Why today's sync lights lag

Chandan's critique of the conventional setup is precise. A camera points at the screen, a small box processes what it sees, decides on colours and brightness, then sends commands to bulbs, usually over Zigbee. Every step happens live, so every step adds latency. Worse, because heavier computation would add even more delay, those boxes play it safe: a limited palette of mostly primary colours and conservative brightness. The system is boxed in by physics and its own processing budget.

The result, in his experience and the internal test users he surveyed, is lighting that feels disconnected from what's on screen, the opposite of immersion.

## Read the signal, look ahead

The core idea is to process the content from the signal pass-through instead of from a camera, and to use a predictive buffer that looks a few seconds ahead. If the system knows the next scene is a police chase, it can prepare the red-and-blue sequence and send it so it lands as the scene starts. He describes buffering the light state about two seconds before the scene appears, which also smooths transitions when a stream rebuffers.

Because the work is decoupled from the display, frame rate stops being the limit. A 120 Hz or 240 Hz monitor that outruns a camera-based system is fine when the lights are computed from the content in advance. Game engines could even pre-encode lighting for parts of a map: head towards snow and the room goes white, towards the sea and it goes blue.

## Smarter than the dominant colour

Two refinements make the output better, not just faster. Scene classification picks the subject instead of the dominant colour: a character looking at a rainbow in a blue sky should get rainbow light in the room, not sky blue. And because the system checks its own predictions, it can use the full RGB gamut and the full zero-to-100% brightness range: properly dark for a horror game, fully bright for a colourful blockbuster.

Distance calibration is another neat trick. If a bulb at the back of a large room takes a second to receive its signal, the system just sends that bulb's command a second earlier. A camera-based system can't do that, because it only knows what's on screen now.

## The architecture and where it goes

The pipeline has four parts: content input, a frame analysis engine that decodes content into light states, the predictive buffer, and a node controller that sends commands to strips, bulbs or virtual devices for testing. Better GPUs deepen the look-ahead.

Chandan's bigger vision is an ecosystem like surround sound mixing, where content producers pre-compute a lighting track once and every viewer's device simply plays it, the same way subtitles ship with a film. He sketches uses from home theatres and consoles to commercial cinemas converted cheaply with smart lights, plus calmer focus modes and accessibility for viewers with impaired vision.

## Who should watch

Smart-home and IoT engineers, game and media developers, and anyone who likes a clean latency argument: move the work out of the critical path and into a buffer. Kubernetes operators won't find their cluster in it, but they will recognise the pattern.

## Related Conf42 talks

- [Why IoT Devices Mandate a Zero Tolerance Security Architecture](https://www.conf42.com/DevOps_2024_Antoinette_Hodes_iot_devices_saving_toasters) is the security counterweight to a house full of connected bulbs.
- [Empowering Cloud-Native Solutions with Software-Defined Networking for IoT and 5G](https://www.conf42.com/Cloud_Native_2025_Sai_Charan_Madugula_networking_iot_5g) covers the network side of device latency.

[Watch Chandan Kumar's talk](https://www.conf42.com/Kube_Native_2025_Chandan_Kumar_lighting_immersion_responsive)

[Watch the talk on YouTube](https://youtu.be/ziBZmNXIlW4).

## Watch the talk

[Beyond Ambilight: Pre-Computed Surround Lighting for Sub-100ms Reactive Immersion](https://www.conf42.com/Kube_Native_2025_Chandan_Kumar_lighting_immersion_responsive) at Conf42 Kube Native 2025.
