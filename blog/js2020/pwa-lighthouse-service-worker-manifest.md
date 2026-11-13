# From zero Lighthouse checks to a real PWA in three moves

Conf42 Blog, 2020-09-29. https://www.conf42.com/blog/js2020/pwa-lighthouse-service-worker-manifest

In short: Michael Solati (Google) at Conf42 JavaScript 2020 on turning a plain web app into a PWA with a service worker, server-side rendering and a manifest

A web app becomes a progressive web app when it is fast, integrated, reliable and engaging, and you can get there in three moves: a service worker, server-side rendering and a web app manifest. At Conf42 JavaScript 2020, Michael Solati, Developer Program Engineer at Google, took a small popular-movies app that failed every PWA check in Lighthouse and walked it, step by step, to a full row of green.

He works on web.dev, describes himself as an Angular person at heart, and promises a framework-agnostic talk. Angular, React and Vue each get a line; the rest is plain browser platform.

## Why bother being an app at all?

Michael's case is about the home screen. Users spend most of their time in native apps because those are predictable, one tap away, and can pull people back with push notifications. He quotes a figure of roughly 78% of phone time going to a user's three favourite apps, while the average user installs no new apps in a month. Asking for an install is asking for time and space. A PWA lowers that barrier: one site for every platform, and Chrome will prompt users to add it to the home screen once the PWA criteria are met.

His personal anecdote is storage. He kept both the native Twitter app and the Twitter PWA on his phone, and when he looked at the installed-apps list the native one was using roughly 250 MB. The PWA was a small fraction of that, and he moved to it and never went back.

## Start by failing Lighthouse

The demo app looks native enough. It follows Material Design and has some speed tricks under the hood. Lighthouse disagrees. There's no service worker, so nothing works offline and the page doesn't respond with a 200 when the network is gone. There's no manifest, so it isn't installable and has no splash screen or theme colour. And the page shows nothing useful with JavaScript disabled.

That last check gets a war story. At a web shop, his team spent ages failing to reproduce a client's complaint that the site didn't work on her iPhone; the boss bought everyone iPod touches. The cause turned out to be that she kept JavaScript disabled. Nobody did anything wrong, but a simple notice would have saved the hunt and kept her on the site.

## Reliable: the service worker

A service worker is JavaScript that acts like a client-side proxy: it decides how each request is answered and controls the cache. Michael shows the cache-first strategy for an offline-first experience: check the cache, fall back to the network, store the response for next time. Pre-cache the key assets and the app loads regardless of the network state.

The on-ramps are short. Angular has the @angular/pwa schematic you apply with ng add. Create React App has shipped service worker support since 2017, and the Vue CLI lets you tick PWA support when you create the project. Vue and React both build on Workbox, the library that bakes in service worker best practices, and he points to Jeff Posnick's Workbox article on web.dev for the details.

## Fast: mind what JavaScript costs

The numbers he quotes are the reason to care: an average mobile load of roughly 19 seconds on 3G, and "53% of users will abandon the site if it takes longer than 3 seconds to load," Michael Solati said at Conf42 JavaScript 2020. The service worker helps on repeat visits. The first load is about JavaScript cost, a point he credits to Addy Osmani.

"A 200 kb JavaScript file has a very different set of costs than a 200 kilobyte JPEG file," he said. Both take the same time over the wire, but the image is decoded and painted while the script is parsed, compiled and executed. The remedy is to move rendering to the server. Next.js and Nuxt.js do it for React and Vue; the framework-agnostic route is Puppeteer, the Node library that drives headless Chrome and can pre-render pages for you.

## Engaging: the manifest

The web app manifest controls how the app appears and launches: home-screen icons, start page, theme colour, splash-screen background, display mode and orientation. Michael fills one in live with a manifest generator (the icon step broke mid-demo, a very honest moment), then adds the two lines that matter in the HTML: the link to the manifest and the theme-color meta tag. Rerun Lighthouse and the app passes.

## Who should watch

Front-end developers who have heard the PWA pitch and never shipped one. It's an introductory talk, about 25 minutes, and its value is the order of operations plus the war stories. If you already run Workbox in production, skip it. For a deeper take on caching strategies and offline writes, pair it with [Francesco Leardini's Offline web apps don't exist anymore!](https://www.conf42.com/JavaScript_2020_Francesco_Leardini_offline_web_apps) from the same event, and with [Majid Hajian on getting work off the main thread](https://www.conf42.com/JavaScript_2020_Majid_Hajian_main_thread). Francesco came back a year later with [a tour of browser web APIs](https://www.conf42.com/JavaScript_2021_Francesco_Leardini_browser_web_APIs).

[Watch Michael Solati's talk](https://www.conf42.com/JavaScript_2020_Michael_Solati_progressive_web_app) from [Conf42 JavaScript 2020](https://www.conf42.com/js2020).

## From Google

Michael's talk points to web.dev, the Google site he works on, for the PWA and Workbox guides he mentions, and to Lighthouse, which runs in Chrome DevTools, as a browser extension, or as an npm module in your build.

- Google SRE: [sre.google](https://sre.google)
- web.dev: [web.dev](https://web.dev)

[Watch the talk on YouTube](https://youtu.be/MNkeHzckoJk).

## Watch the talk

[Building (Progressive) Web Apps](https://www.conf42.com/JavaScript_2020_Michael_Solati_progressive_web_app) at Conf42 JavaScript 2020.
