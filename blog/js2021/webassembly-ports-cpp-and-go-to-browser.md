# WebAssembly is JavaScript's helper, not its replacement

Conf42 Blog, 2021-10-29. https://www.conf42.com/blog/js2021/webassembly-ports-cpp-and-go-to-browser

In short: Tamas Piros (Cloudinary) at Conf42 JavaScript 2021 on using WebAssembly next to JavaScript, porting a C++ image tool and a Go analyser to the browser

Every few months someone announces that WebAssembly will replace JavaScript. At Conf42 JavaScript 2021, [Tamas Piros](https://www.conf42.com/JavaScript_2021_Tamas_Piros_Supercharge_Web_Assembly), Senior Developer Experience Engineer at Cloudinary, argues the opposite: the two complement each other through the WebAssembly JavaScript API, and the practical win is taking code that already exists in C++ or Go and running it in the browser. He shows it with two image tools, one ported from C++ and one written in Go.

## What problem does WebAssembly solve?

JavaScript was never meant to be the web's main language, and we now ask it to do video, heavy processing and CPU-bound work. V8 and the other engines optimise brilliantly, but some tasks stay too complex or too slow.

Tamas Piros said at Conf42 JavaScript 2021: "I'm going to rephrase it to say we push a language well outside its comfort zone."

His short history: asm.js from Mozilla in 2013, the WebAssembly announcement in 2015, an MVP in 2017, and an official W3C recommendation in 2019, alongside HTML, CSS and JavaScript. His one-line definition: it runs non-web code at near native speed on the web, and every modern browser supports it.

## How do you get C code into a web page?

The walkthrough is deliberately trivial, a C function that squares an integer, because the point is the pipeline. Install Emscripten, compile with emcc, and you get two files: a .wasm module and a .js glue file that ties the module to JavaScript. Load the glue code, wait for the runtime to initialise, then call the exported function from an ordinary click handler. His two reminders: always ship the glue code, and if you build a progressive web app, cache it with your offline assets.

Go works differently because it is not an LLVM language. It has its own WebAssembly compile target, you download the glue file from the Go project, and Go code can touch the DOM directly. His Go source has a line that reads almost exactly like document.getElementById followed by setting innerHTML.

## When is it worth it?

His list: reusing existing code (audio, video or image processing you do not want to rewrite), predictable performance and binary size thanks to static typing rather than on-the-fly JIT optimisation, and advanced system access such as threads, SIMD and shared memory. The number to remember: in a recent project he used two builds of OpenCV's WebAssembly module, with and without SIMD, and the SIMD one doubled the frames per second of a video project.

## The demos: SSIMULACRA and an image format inspector

The first demo is SSIMULACRA, a C++ tool that compares two images and returns a score for how visible the quality difference is. Cloudinary uses it to check whether a quality reduction will be noticed; scores below about 0.1 should be invisible to the human eye. He ported it with Emscripten, using the browser's virtual file system that WebAssembly exposes to write both images before comparing them. In the demo, a car photo served with Cloudinary's automatic quality setting drops from 1.4 MB to 732 KB, about half, and the tool reports no artifacts a person would see, while the deliberately ruined quality-1 version scores far higher.

The second is a Go project built on libwebp, libpng and other libraries to look inside what Cloudinary's automatic format setting returns. Chrome gets a lossy WebP in a VP8 container without alpha; a PNG source comes back as WebP with an alpha channel; switch the user agent to Safari in Chrome's network conditions panel and the same URL returns JPEG, or JPEG 2000 at full size. A neat trick for testing format negotiation without a second browser.

He closes with pointers: Doom and an NES emulator running through WebAssembly, and Google's Squoosh app, which uses WebAssembly modules for image compression.

## Who should watch?

JavaScript developers who have heard about WebAssembly but never compiled anything to it, and teams sitting on a C, C++ or Go library they would like to run client-side. It is an introduction with working demos, not a performance study.

## Related Conf42 talks

- Robert Aboukhalil on [interactive command-line tutorials with WebAssembly](https://www.conf42.com/JavaScript_2022_Robert_Aboukhalil_interactive_commandline_tutorials_webassembly) at Conf42 JavaScript 2022.
- Andrey Makarov on [WebAssembly for the web](https://www.conf42.com/Rustlang_2024_Andrey_Makarov_wasm_assembly_code_web) at Conf42 Rustlang 2024.
- Thorsten Hans on [serverless WebAssembly](https://www.conf42.com/Golang_2024_Thorsten_Hans_serverless_webassembly) at Conf42 Golang 2024.

[Watch Tamas Piros's talk](https://www.conf42.com/JavaScript_2021_Tamas_Piros_Supercharge_Web_Assembly), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Cloudinary

Cloudinary is a media platform for images and video; the automatic quality and automatic format settings shown in the demos are its features.

- [Cloudinary website](https://cloudinary.rocks/jyu)

[Watch the talk on YouTube](https://youtu.be/lMy1zXJstVU).

## Watch the talk

[Supercharge your JavaScript with Web Assembly](https://www.conf42.com/JavaScript_2021_Tamas_Piros_Supercharge_Web_Assembly) at Conf42 JavaScript 2021.
