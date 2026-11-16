# TypeScript is a serious language for building games on the web

Conf42 Blog, 2025-09-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/typescript-game-dev-hology

In short: Annie Tsai and Adam Ringhede of Hology at Conf42 JavaScript 2025 on why TypeScript, WebGPU and WebAssembly make browser games a real platform.

If your mental picture of a browser game is a Flash puzzle you hid from your parents in 2008, Annie Tsai and Adam Ringhede of Hology Interactive would like a word. At Conf42 JavaScript 2025 the two co-founders, who have spent around two years building a game engine on web technologies, made the case that TypeScript and JavaScript are now a sensible default for web and mobile games, not a compromise.

It is a short talk, closer to a well-argued pitch than a tutorial. Annie covers the market side, Adam the engineering side, and the whole thing fits in a coffee break.

## The audience already lives in the browser

Annie's opening argument is distribution. Traditional studios think in PC and console terms, while a huge number of players sit on phones, social platforms and web portals. She points to platforms like Poki, with players from over 100 countries, and CrazyGames, which recently published an FPS. Discord activities are another door: you ship the game to people who are already hanging out there.

The pitch is about friction. A web game needs no install, no 100 GB download and no new graphics card. The same stack also stretches beyond games into education, marketing, rapid prototypes and interactive overlays for live streams, where the chat can play along.

## The GPU is no longer locked behind a native app

Adam takes over with the platform. WebGL 2 has been in the big browsers for years, and WebGPU is now supported in all major ones too. His take is that WebGL already gets you surprisingly close to native graphics and that its capabilities have not been used to the full. WebGPU narrows the gap further and adds parallel compute on the GPU, which games can use for more than drawing triangles.

## Types are the bridge from C++ habits

The language argument is where the talk earns its title. JavaScript gives you fast iteration: no long compile step, easy sharing as a website or an itch.io upload, a good fit for prototypes. TypeScript adds what bigger game codebases need: static types that make a large codebase readable, behave a bit like self-documentation, and catch type errors before runtime. For developers coming from C# or C++, Adam frames TypeScript as a bridge between JavaScript's dynamic nature and the compile-time safety they are used to, with strictness you can dial up or down.

The detail engine builders will enjoy is hot reloading. Because it is a scripting language, Hology's editor watches your code, transpiles it on change and runs it inside the already-running application in a couple of hundred milliseconds. Anyone who has waited for a C++ engine to rebuild knows exactly what that is worth.

## Open source beats proprietary toolchains

Adam contrasts the npm world with traditional game development, where engines often ship their own languages, version control and file formats that resist diffing or integration with other tools. With TypeScript you get millions of packages, tools that transfer to non-game work, and an open source culture that makes collaboration easier.

On performance, he pushes back on the usual doubt. Written carefully, with typed array buffers and C-like patterns, JavaScript optimises very well under the JIT. When you need more, WebAssembly lets you compile C, C++ or AssemblyScript (a TypeScript-like language) and bring in pathfinding or physics libraries of the kind AAA engines use. Most game code never has to touch it, but the escape hatch exists.

## Who should watch

Web developers curious about games, game developers wondering whether the browser is worth a look, and anyone choosing a language for a small team's first 3D project. It is an overview with a clear point of view, and it is upfront that Hology builds an engine on this stack. If you want code-level detail on rendering or physics, treat it as the starting map, not the territory.

## Related Conf42 talks

- [Dmitrii Ivashchenko on moving from WebGL to WebGPU](https://www.conf42.com/JavaScript_2023_Dmitrii_Ivashchenko_webgl_to_webgpu) at Conf42 JavaScript 2023.
- [Griffin Solot-Kehl on building 3D environments with Babylon.js](https://www.conf42.com/JavaScript_2022_Griffin_SolotKehl_babylonjs_create_3d_metaverse_environments) at Conf42 JavaScript 2022.
- [Andrey Makarov on building a battleship game](https://www.conf42.com/JavaScript_2023_Andrey_Makarov_battleship_game) at Conf42 JavaScript 2023.

[Watch Annie Tsai and Adam Ringhede's talk](https://www.conf42.com/JavaScript_2025_Annie_Tsai_Adam_Ringhede_level_why_typescript), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/coA-a5c5-hI).

## Watch the talk

[Level Up: Why TypeScript/JavaScript for game development?](https://www.conf42.com/JavaScript_2025_Annie_Tsai_Adam_Ringhede_level_why_typescript) at Conf42 JavaScript 2025.
