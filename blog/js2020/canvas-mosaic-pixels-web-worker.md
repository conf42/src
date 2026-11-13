# Five million pixels, five seconds, and why the worker saved the UI

Conf42 Blog, 2020-09-30. https://www.conf42.com/blog/js2020/canvas-mosaic-pixels-web-worker

In short: Victor Lebrun (Theodo) at Conf42 JavaScript 2020 on turning Mapbox maps into colour mosaics with the Canvas API, and moving the work to a web worker

Paint every area between the roads of a map in its own colour and you get a mosaic; do it pixel by pixel in JavaScript and you get a frozen browser tab. At Conf42 JavaScript 2020, Victor Lebrun, a lead developer at Theodo in Paris, live-coded (well, pre-recorded and "pseudo live") the whole pipeline in a React and TypeScript app: read a Mapbox map's pixels, run an area-detection algorithm over them, paint the result on a 2D canvas, then move the heavy part into a web worker so you can still drag the map.

The idea came during lockdown, while he was drawing road-bounded maps by hand and decided a browser should do it for him.

## What is a pixel, to the Canvas API?

Victor builds up from nothing. A magenta rectangle on a canvas element (300 by 150 pixels, the default size). Then getImageData, which hands back a Uint8ClampedArray: four numbers per pixel, red, green, blue and alpha, each clamped between 0 and 255, indexed from top left to bottom right. Fill that array with random values, write it back with putImageData, and you have a noise mosaic that regenerates every time Mapbox renders.

Two gotchas come next, and they're the bits worth stealing. First, sizing: he sets the mosaic canvas to the Mapbox WebGL context's drawing buffer width and height, gets a canvas twice the size he wanted, and learns that on retina screens Mapbox renders twice the pixels per direction. The fix is to set the element's CSS size to half the buffer size; canvas width and style width are different things. Second, orientation: he copies the map with readPixels on the WebGL context and the town name comes out mirrored, because WebGL starts counting from the bottom left. A small helper converts each index to an x/y point, flips y, and converts back.

## How do you find the areas?

The source is effectively a two-colour image: roads and everything else. The algorithm walks every pixel from top left to bottom right. For each pixel not yet visited, it starts a paint routine with a to-visit stack: pop a pixel, paint it with the target colour, mark it visited, push any neighbours of the same source colour. When the stack is empty, one area is done, and the scan moves on to the next unvisited pixel with a new colour. It's a flood fill, wrapped in a CanvasDataTransformer class that takes the source and target arrays and the size.

It works on satellite imagery only up to a point, because the threshold that tells white areas from the rest isn't smart. So he switched to a custom road style built in Mapbox's style editor, which gives the algorithm clean, binary input. Cheating by choosing your input is a respectable engineering technique.

## Why does the UI freeze, and what fixes it?

Because the algorithm runs on the main thread, every map render blocks interaction; dragging the map to another region becomes a struggle. Web workers run scripts in background threads, so the transformation moves there. The main thread posts a payload (the target array, the Mapbox pixels and the canvas size), the worker runs the transformer and posts back the painted array, and the main thread puts it on the canvas.

The setup has friction he shows honestly: webpack's worker-loader, a TypeScript module declaration so the import type-checks, an ejected Create React App to override the webpack config, and an eslint-disable for a rule Create React App adds. The second fix is subtler. Mapbox fires many renders while you pan, and the worker keeps grinding through outdated jobs. Calling terminate on the worker before each new render, and creating a fresh one, means only the latest render gets computed.

## Is it fast now?

No, and he says so. "So for example, for the 5 million pixels I have on my full screen, it takes up to 5 seconds, so it's very long indeed," Victor Lebrun said at Conf42 JavaScript 2020. The worker keeps the page responsive; it doesn't make the maths faster.

His closing ideas are where the next talk would start. Mapbox itself is fast because it draws layers (background, roads, forests) as shapes with WebGL vertex arrays instead of filling pixels one by one, so a better algorithm might follow road geometry, find intersections, and draw areas as vertices. Or, guessing at why Photoshop's area detection is so quick, compile the pixel loop to WebAssembly and measure the gain.

## Who should watch

Anyone who has wanted to do per-pixel work in a browser and needs a careful tour of the traps: ImageData layout, retina buffers, WebGL's flipped origin, and worker plumbing in a Create React App project. It's a coding session, so expect to watch code being typed. Pair it with [Renaldi Gondosubroto's custom graphics library](https://www.conf42.com/JavaScript_2020_Renaldi_Gondosubroto_custom_graphics_library) and [Majid Hajian on the main thread](https://www.conf42.com/JavaScript_2020_Majid_Hajian_main_thread) from the same event, and [Dmitrii Ivashchenko's WebGL to WebGPU](https://www.conf42.com/JavaScript_2023_Dmitrii_Ivashchenko_webgl_to_webgpu) for where GPU drawing in the browser went next.

[Watch Victor Lebrun's talk](https://www.conf42.com/JavaScript_2020_Victor_Lebrun_canvas_pixel_transformation) from [Conf42 JavaScript 2020](https://www.conf42.com/js2020).

## From Theodo

Victor introduced himself as a lead developer at Theodo's Paris office, and the project grew out of a personal side project rather than client work.

- Theodo: [theodo.co.uk](https://www.theodo.co.uk)

[Watch the talk on YouTube](https://youtu.be/L6rQtGDxCXk).

## Watch the talk

[Canvas pixels transformation: beauty comes slowly](https://www.conf42.com/JavaScript_2020_Victor_Lebrun_canvas_pixel_transformation) at Conf42 JavaScript 2020.
