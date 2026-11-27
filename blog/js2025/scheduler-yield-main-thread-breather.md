# One await scheduler.yield() can unfreeze a page stuck on long tasks

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/scheduler-yield-main-thread-breather

In short: Aleksandr Tkachenko of Playtech at Conf42 JavaScript 2025 on scheduler.yield(), why setTimeout yielding loses its place, and a frozen banking demo.

A loop that spends 10 ms on each of 200 items sounds harmless, right up to the moment the page freezes for two full seconds. At Conf42 JavaScript 2025, Aleksandr Tkachenko, a front-end engineer at Playtech, showed how the experimental `scheduler.yield()` API lets a long task pause, hand the browser its turn, and resume ahead of the queue, often with a one-line change.

He is upfront about scope: the API is still early, not every browser supports it, and a polyfill exists. The talk is a careful explanation of why it behaves differently from the tricks we already use, plus a demo you will recognise from your own app.

## The event loop, briefly and correctly

Aleksandr starts with a refresher worth the time. Synchronous code runs on the call stack; async callbacks wait in the microtask queue (promises) or the task queue (timers); when the stack empties, the loop drains all microtasks, then picks one runnable task, and repeats. Task queues are not strict FIFO, and the event loop is defined in the HTML standard, not in ECMAScript. Anything holding the main thread past 50 ms is a long task, and while it runs the browser cannot repaint or respond.

## The two-second freeze you can feel

His toy demo makes it visceral. A `blockingTask(ms)` burns CPU on purpose, and a `heavyWork()` loop calls it for 10 ms on each of 200 items. Click OK and the button stays visually pressed; click Log four times and nothing happens until the work ends, then all four timestamps print at once; click the close icon three times and the window vanishes only afterwards. Events are queued, not lost, which is somehow worse for the user who keeps clicking.

## Why setTimeout(0) is a polite but unreliable pause

The classic fix is to chunk the loop and `await` a promise resolved by `setTimeout(fn, 0)` every so often, here about every 25% of the work. It helps, but your continuation goes to the back of the task queue. If something else on the page has a `setInterval` firing, those callbacks can run first, so you never know when you get control back. `requestAnimationFrame` has similar drawbacks, and `requestIdleCallback` suits background work, not resuming a user-triggered job.

`scheduler.yield()` changes the ordering. After the pending user input is handled, your continuation is prioritised and runs before already queued timer tasks. His diagram contrasts the three cases: no yielding (the click waits for the whole task), setTimeout (the click runs, then a queued timer, then your work), and `scheduler.yield()` (the click runs, then your work continues).

## Priorities made explicit

The Prioritized Task Scheduling API names three levels: `user-blocking` for input and critical UI, `user-visible` for things the user sees but that are not urgent, and `background` for work nobody is waiting on. `scheduler.yield()` defaults to user-visible, and when called inside a `scheduler.postTask()` callback it inherits that task's priority. Aleksandr deliberately stops short of a full postTask tour.

## The banking demo

The finale is a fictional banking app: hidden balance, a card that flips to show details, and a Generate report button that runs the heavy loop over 1,000 items. Without yielding, the button sticks and the card and balance controls ignore every click. With `scheduler.yield()` every 5% of the work, the button renders, a loading animation appears and the user can flip the card and reveal the balance while the report builds. Animations are a little less smooth, and he says so.

## Who should watch

Front-end engineers chasing Interaction to Next Paint (INP), anyone maintaining legacy code with heavy synchronous loops they can't rewrite this sprint, and people who have sprinkled `setTimeout(0)` around and wondered why it sometimes doesn't help. If you already use `postTask` in production, the event loop section will be review.

## Related Conf42 talks

- [Lorenzo Pieri's Node.js event loop fairytale](https://www.conf42.com/JavaScript_2023_Lorenzo_Pieri_nodejs_eventloop_fairytale) at Conf42 JavaScript 2023.
- [Aleksandr Tkachenko on Skeleton Mammoth reusable loaders](https://www.conf42.com/JavaScript_2023_Aleksandr_Tkachenko_skeleton_mammoth_reusable_loaders) at Conf42 JavaScript 2023.
- [Aleksandr Guzenko on breaking up a monolith with code splitting](https://www.conf42.com/JavaScript_2023_Aleksandr_Guzenko_breaking_monolith_code_splitting_techniques) at Conf42 JavaScript 2023.

[Watch Aleksandr Tkachenko's talk](https://www.conf42.com/JavaScript_2025_Aleksandr_Tkachenko_let_browser_take), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/N6M9wIBqFwY).

## Watch the talk

[Let Your Browser Take a Breather with a Scheduler.yield()](https://www.conf42.com/JavaScript_2025_Aleksandr_Tkachenko_let_browser_take) at Conf42 JavaScript 2025.
