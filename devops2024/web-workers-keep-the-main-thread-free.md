# Move the heavy loop to a Web Worker and the button clicks again

Conf42 Blog, 2024-01-24. https://www.conf42.com/devops2024/web-workers-keep-the-main-thread-free

In short: Kevin Uehara (iFood) at Conf42 DevOps 2024 on Web Workers - moving heavy client-side processing off the main thread in plain vanilla JavaScript.

A loop that runs for a few seconds on the main thread is a few seconds in which your user cannot click anything. At Conf42 DevOps 2024, Kevin Uehara, Staff Frontend Engineer at iFood, showed the fix in its smallest possible form: take the heavy function, move it into a Web Worker, talk to it with postMessage, and the page stays responsive while the work runs.

It is a beginner-friendly talk, his first in English, and it does exactly what the abstract promises: a vanilla JavaScript app built twice, once blocking and once not.

## Why does the page freeze?

Uehara starts with the basics. JavaScript in the browser is single-threaded; the event loop, callback queue and call stack let it juggle asynchronous work, but a CPU-bound function still occupies the one thread that also handles clicks and repaints. Browsers ship many APIs alongside the language (storage, IndexedDB, PWA features, performance tooling), and Web Workers are the one built for this case: run an operation away from the main thread so the UI is never blocked.

Context matters here. He works in iFood's logistics tribe on two Maps Platform teams, Location Areas and Location Geo, where geoprocessing, delivery areas and routes are the daily diet. Heavy computation in a web app is not hypothetical for them.

## The blocking version

No framework, no library: an index.html, an index.js and a stylesheet, served with the VS Code Live Server extension. The page has two buttons and a pre element. The first button calls a function that loops many millions of times, multiplying as it goes, then prints the result. The second toggles the background between dark and white.

Click the first, then try the second, and nothing happens until the loop finishes. "I can't click on the second button because the main thread is blocked," Kevin Uehara said at Conf42 DevOps 2024. It is the kind of demo that makes the problem obvious in about four seconds.

## The worker version

The refactor is small enough to remember:

1. Create worker.js and move the heavy function into it.
2. In the worker, define an onmessage handler that checks the incoming message name, runs the function and posts the value back with postMessage.
3. In index.js, create the worker with the Worker constructor and the file path, send it a message with postMessage, and handle the result in the worker's onmessage callback by writing it into the pre element.

Run it again, start the long job, and the background toggle works throughout. In his words, the main thread is free for the user to interact with the page while the work happens on the worker. He then live-codes the whole thing from an empty folder, which is useful if you want to follow along at the keyboard.

## What the talk leaves out

Uehara is clear that this is one solution among many, and the demo stays at the hello-world level. You will not get transferable objects, worker pools, SharedArrayBuffer or the cost of copying large payloads between threads; those are the next things to read about once the basic pattern clicks. His dev.to article on introducing JavaScript Web Workers covers the same example in more detail.

## Who should watch

Frontend developers who have never used a Web Worker, and backend or DevOps folks who want to understand why a dashboard freezes when it crunches data in the browser. Experienced frontend engineers can skip it.

## Related Conf42 talks

- Majid Hajian on [the main thread](https://www.conf42.com/JavaScript_2020_Majid_Hajian_main_thread) at Conf42 JavaScript 2020.
- Atila Fassina on [multi-threading in JavaScript, demystified](https://www.conf42.com/JavaScript_2021_Atila_Fassina_MultiThread_demystified) at Conf42 JavaScript 2021.
- Assaf Krintza on [React performance](https://www.conf42.com/JavaScript_2021_Assaf_Krintza_React_Performance) at Conf42 JavaScript 2021.

[Watch Kevin Uehara's talk](https://www.conf42.com/DevOps_2024_Kevin_Uehara_webworkers_heavy_processing)

## From iFood

iFood is a Brazilian food delivery company; its logistics engineers build the maps, geolocation and delivery-route systems behind the app.

- [iFood website](https://www.ifood.com.br/)

[Watch the talk on YouTube](https://youtu.be/RXZ46Ury5sw).

## Watch the talk

[Web Workers: Handling Heavy Processing on the Client Side](https://www.conf42.com/DevOps_2024_Kevin_Uehara_webworkers_heavy_processing) at Conf42 DevOps 2024.
