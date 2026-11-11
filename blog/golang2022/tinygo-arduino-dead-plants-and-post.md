# TinyGo turns a Go developer into an IoT hobbyist without learning C

Conf42 Blog, 2022-03-30. https://www.conf42.com/blog/golang2022/tinygo-arduino-dead-plants-and-post

In short: Liam Hampton (Microsoft) at Conf42 Golang 2022 on using TinyGo to put plain Go on an Arduino, from a soil moisture sensor to a letterbox alarm

A year before his talk, Liam Hampton knew nothing about IoT, had never written C or MicroPython, and owned a pile of freshly bought Arduinos. At Conf42 Golang 2022 the Microsoft Cloud Advocate showed how TinyGo let him skip learning a new language entirely: the code he flashes onto the boards is ordinary Go, plus one package.

It is a beginner-friendly, hobbyist talk with a live demo, not a deep compiler tour, and it is honest about that.

## Where does a Go developer even start with microcontrollers?

On Google, like everyone else. Liam said at Conf42 Golang 2022: "I didn't want to learn a new language, so I ended up like every other developer would, went onto Google and said, how do I put go on an Arduino?"

The answer was TinyGo, whose tagline he says you will see on the website, the GitHub repo and every blog post about it. In his words, "it is a compiler for small places, it's still a go compiler." It keeps the parts of the standard library that make sense on tiny hardware (bytes, archive and zip, for example) and drops what does not, such as html/template and the net package. Under the hood it uses LLVM to target architectures like x86, ARM and PowerPC.

## What is TinyGo actually used for?

Liam names three uses, in order of how often you will meet them:

- **Microcontrollers**: Arduino, micro:bit, Adafruit boards, even a smartwatch. TinyGo supported over 70 boards at the time of the talk, up from about 50 when he started a year earlier.
- **WebAssembly**: compile TinyGo to Wasm and have the browser run it, for example a dashboard.
- **Small CLIs**: less common by 2022, he says, but still around.

## The projects: dead plants and a long walk downstairs

His motivation was domestic. After a month away he came home to a wilted plant, so he built a soil moisture sensor that reports a reading through the Arduino in human-readable form (71% on the day he showed it; the plant wants 50% or more). The next phase is a self-watering pump he can trigger remotely from a dashboard.

The second project fixes a problem anyone in a tall block of flats will recognise: walking down every day to check a letterbox that is often empty. Phase one is an Arduino Uno R3 on a breadboard with a photoresistor and a few LEDs. When the postie opens the letterbox, light gets in, and that is the trigger. Phase two is sending the notification somewhere useful, through something like Azure IoT Hub or a pub/sub setup.

## What does the code look like?

Exactly like Go, which is the point. The demo ran in Visual Studio Code with the TinyGo extension, Go 1.17 and TinyGo 0.22. The extension's status bar lets you pick the target board from a long dropdown. The one unusual import is the machine package, which gives you the pins: the light sensor on ADC0 and LEDs on D7 to D10, all configured as outputs in a loop over a slice.

The logic is a plain if/else: above a light reading of 8000 (a threshold he tuned to his room, unit unconfirmed) the LEDs go off, otherwise on, followed by a one-second sleep so the sensor does not flood him with data. To flash it, he listed the serial ports under /dev, found the USB modem, and ran tinygo flash with the Arduino target, the port and the file. Flashing took a second or two, and covering the sensor lit the LEDs on camera.

## What's next on the bench

Three more projects: a macro pad on an RP2040 board for streaming shortcuts, a spinning Lego wheel for GitHub notifications (because emails and texts are too easy to ignore), and a hallway dashboard tying the home sensors, the plant and the letterbox together. If you do not want to buy hardware first, the TinyGo playground at play.tinygo.org simulates boards in the browser, much like the Go playground.

## Who should watch

Go developers curious about embedded work who have been put off by C toolchains. If you already ship firmware, this is a pleasant 20 minutes rather than new material.

## Related Conf42 talks

- Thorsten Hans on [serverless WebAssembly with Go](https://www.conf42.com/Golang_2024_Thorsten_Hans_serverless_webassembly) at Conf42 Golang 2024.
- Pradeep Kumar Vattumilli on [TinyML at the edge](https://www.conf42.com/Golang_2025_Pradeep_Kumar_Vattumilli_edge_tinyml_ai) at Conf42 Golang 2025.
- Antoinette Hodes on [IoT devices and saving toasters](https://www.conf42.com/DevOps_2024_Antoinette_Hodes_iot_devices_saving_toasters) at Conf42 DevOps 2024.

[Watch Liam Hampton's talk](https://www.conf42.com/Golang_2022_Liam_Hampton_to_the_edge)

## From Microsoft

Liam is a Microsoft Regional Cloud Advocate based in the UK. For the cloud end of projects like his letterbox alarm, he points to Azure IoT Hub.

- Microsoft: [microsoft.com](https://www.microsoft.com/en-ie/)

[Watch the talk on YouTube](https://youtu.be/xM8myEOM2yQ).

## Watch the talk

[Go to the Edge](https://www.conf42.com/Golang_2022_Liam_Hampton_to_the_edge) at Conf42 Golang 2022.
