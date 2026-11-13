# A 1997 college graphics exercise, running inside Angular via WebAssembly

Conf42 Blog, 2020-10-01. https://www.conf42.com/blog/js2020/cpp-to-angular-emscripten-webassembly

In short: Alejandro Mercado (KMMX) at Conf42 JavaScript 2020 on compiling old C and C++ with Emscripten and wrapping the result as an Angular service

Old C and C++ code doesn't have to stay on the desktop: compile it with Emscripten and it runs in the browser, even inside a modern framework. At Conf42 JavaScript 2020, Alejandro Mercado, CEO of KMMX in Mexico, showed an experiment he wrote up on Medium as Back to the Future: taking C++ graphics code he first wrote at college and running it in an Angular app through WebAssembly.

He's upfront about the spirit of it. "It's about having some c plus plus code in web. Something a little weird I can say, but pretty fun," Alejandro Mercado said at Conf42 JavaScript 2020. It's a short, enthusiastic talk about an aha moment, not a production migration guide, and it's good at exactly that.

## Why would anyone put C++ in a web app?

Control, and the performance that comes with it. Alejandro points at game engines and graphics tools, where memory and rendering demand the kind of control C and C++ give you. For years, writing for the web in C++, Prolog or Perl sounded odd. WebAssembly changed that by acting as a bridge between those languages and the browser, which is everywhere.

## What does the first step look like?

Hello world, of course. He installs Emscripten (the C/C++-to-JavaScript compiler toolchain, garbled into several creative spellings by the transcript), checks the version, and compiles a classic C hello world with emcc; em++ does the same for C++. The output is two files: a.out.wasm, the compiled WebAssembly binary, and a.out.js, the JavaScript runtime support that loads and runs it. Run the JS file with Node and the greeting prints.

That moment carried the talk for him: joining code he wrote 20 years ago with the stack he uses today. To see it in a browser, Emscripten can also emit an HTML page, and a one-line Python simple HTTP server is enough to serve it on localhost.

## Can the old graphics code really run unchanged?

Mostly. At college, in a Graphics Programming 101 course, his class used SDL, the Simple DirectMedia Layer: a cross-platform library for low-level access to audio, keyboard, mouse, joystick and graphics hardware via OpenGL and Direct3D. They drew circles, donuts and toroids and made them move. The exercise he ports dates from 1997, and in his words it's still almost the same code. The demo is a C++ colour cube with gradient faces that rotates and changes, and the code is on GitHub for anyone who wants to replicate it.

## Where is the hard part?

The boundary between C++ and JavaScript. Emscripten ships helper methods that make calls between the module and JavaScript easier, and a conditional compilation symbol you can test to know whether the code is being built by Emscripten. The trap is name mangling. C++ allows overloaded functions, so the compiler rewrites function names with information about their parameters, and the method name your JavaScript wants to call no longer exists in the binary. The fix is to wrap the exported methods in an extern C block so the compiler leaves their names alone, then recompile.

He also flags that the HTML Emscripten generates is a learning aid rather than something you ship. For production you want the module inside your own UI.

## How does it end up in Angular?

Frameworks today are about components, so the compiled cube becomes one. He generates a component with the Angular CLI and loads the compiled C++ and its wasm file as a service. His practical tip, earned the hard way: make sure the compiled .js and .wasm files actually land in the component's folder after compilation, because he lost a lot of time to a missing pair. Emscripten can also generate a JavaScript glue file you include from HTML, if you'd rather let it build the UI elements.

## Will WebAssembly replace JavaScript?

The question he hears most. His answer is no: WebAssembly expands what the web can do and enables hybrid designs, with JavaScript staying put. He expects browsers to run renderers and games smoothly thanks to compiled code, and more languages to join in.

## Who should watch

Developers curious about WebAssembly who want to see the very first steps, from emcc to a framework component, without a wall of theory. If you're already shipping wasm, you'll know all of it. For more depth, pair it with [Tamas Piros on WebAssembly](https://www.conf42.com/JavaScript_2021_Tamas_Piros_Supercharge_Web_Assembly) at Conf42 JavaScript 2021 and [Robert Aboukhalil's interactive command-line tutorials with WebAssembly](https://www.conf42.com/JavaScript_2022_Robert_Aboukhalil_interactive_commandline_tutorials_webassembly) at Conf42 JavaScript 2022. At the same event, [Victor Lebrun's canvas mosaic talk](https://www.conf42.com/JavaScript_2020_Victor_Lebrun_canvas_pixel_transformation) ends by proposing WebAssembly for exactly the kind of pixel loop C++ is good at.

[Watch Alejandro Mercado's talk](https://www.conf42.com/JavaScript_2020_Alejandro_Mercado_back_to_the_future_c) from [Conf42 JavaScript 2020](https://www.conf42.com/js2020).

## From KMMX

Alejandro introduced himself as a web and mobile developer from Mexico with DevOps tools under his belt, and he writes about web technologies and DevOps on Medium, where the full Back to the Future article with every step lives.

- KMMX: [kmmx.mx](https://kmmx.mx)

[Watch the talk on YouTube](https://youtu.be/e84JsH0HHM0).

## Watch the talk

[Back to the Future! From C++ to JS](https://www.conf42.com/JavaScript_2020_Alejandro_Mercado_back_to_the_future_c) at Conf42 JavaScript 2020.
