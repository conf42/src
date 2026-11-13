# Offline reads are the easy half. Offline writes need Firestore

Conf42 Blog, 2020-09-29. https://www.conf42.com/blog/js2020/angular-pwa-firestore-offline-writes

In short: Francesco Leardini (Trivadis) at Conf42 JavaScript 2020 on PWA caching strategies in Angular and offline writes that sync with Cloud Firestore

An app that works offline is mostly a caching decision, until users want to change data while offline; then you need a local store that syncs. At Conf42 JavaScript 2020, Francesco Leardini, senior software engineer and Angular trainer at Trivadis, showed both halves: caching strategies configured in Angular's service worker, then Cloud Firestore's offline persistence, demoed on a phone in airplane mode with edits that sync the moment it reconnects.

His opening complaint is that few people know what PWAs can do and even fewer use them. The rest of the talk is an argument by demo.

## What does a PWA buy you over a native app?

Francesco frames it as differences, not a fight. No app store rules to satisfy: deploy to the server and everyone has it. One version, with features progressively hidden where a browser lacks them. Cheaper to build, because your web team already has the know-how. And a far smaller footprint on the device, which he shows with two near-identical apps side by side on his Android phone, where the native one is much bigger.

The offline experience is where it pays off. Instead of the browser's default offline page, a PWA can show your branding and some useful static data. His favourite example is Trivago, which offers a labyrinth game when you come back offline, keeping the user busy until the connection returns and the requested page loads.

## What goes into the manifest?

The web manifest tells the browser how to render the installed app: name and short name for the label, a display mode (browser, standalone without the address bar, or fullscreen for media-rich apps and games), a start URL so the app always opens on the same page, and icons. At minimum, provide 192x192 and 512x512.

He spends a moment on maskable icons, a detail people miss. Since Android Oreo introduced adaptive icons, manufacturers crop icons into their own shapes, and non-maskable icons get cut or land on a white background. A maskable icon keeps everything important inside a safe area: a circle whose radius is 40% of the image size.

## Which caching strategy, when?

A service worker caches nothing by default; you choose. Cache first answers from the cache and falls back to the network: the offline-first choice. Network first goes to the network for the freshest data (his example is a stock exchange API) and falls back to the cache. Stale-while-revalidate answers from the cache immediately and refreshes the cached copy in the background for next time.

Writing these by hand is some code; Workbox, the framework-agnostic set of libraries he calls the state of the art, does stale-while-revalidate for all your JavaScript and CSS in about three lines.

## How does Angular set this up?

Run ng add for @angular/pwa and it registers Angular's service worker (production builds only), adds a manifest with default icons, and creates ngsw-config.json, where the real configuration lives. Asset groups cover static files: install mode prefetch downloads the core files while the service worker installs (keep the list small, because one failed download aborts the install), and lazy caches the rest after first use.

For APIs you add data groups. His demo caches a dad-jokes API with the performance strategy (cache first), at most five entries and a 15-minute max age, and a cat-pictures API with the freshness strategy (network first) plus a timeout, after which the service worker assumes you're offline or on a slow network and serves the cache. In DevTools the joke comes from the service worker while cats come from the network. Go offline and both come from the cache.

## And writing while offline?

The Cache API covers GET requests, not PUT and POST. You could queue writes in IndexedDB and replay them on reconnect; Firestore does that for you. On the web you call enablePersistence, and from then on Firestore keeps documents and pending changes locally, with a default cache threshold of 40 MB that you can change, and ships the changes one by one when the connection is back.

The demo is a PWA for tracking restaurants and bars he visits with his wife. Edit an entry on the laptop and it appears on the phone through sockets. Put the phone in airplane mode, add and edit entries, reconnect, and the laptop updates within seconds. For the user, online and offline behave the same.

## Should PWAs replace native apps?

"Of course, there is no silver bullet," Francesco Leardini said at Conf42 JavaScript 2020. Apple didn't support many PWA features (web notifications, some manifest properties). PWAs can only do what the web can, so no device contacts beyond the experimental Contact Picker API. And for media-heavy apps and games, native performance still wins.

## Who should watch

Angular developers who want an offline mode without writing a service worker, and anyone deciding between cache strategies. It pairs naturally with [Michael Solati's Building (Progressive) Web Apps](https://www.conf42.com/JavaScript_2020_Michael_Solati_progressive_web_app) from the same event, and with Francesco's own follow-up a year later, [a tour of browser web APIs](https://www.conf42.com/JavaScript_2021_Francesco_Leardini_browser_web_APIs). For keeping the main thread free while all this runs, see [Majid Hajian's talk](https://www.conf42.com/JavaScript_2020_Majid_Hajian_main_thread).

[Watch Francesco Leardini's talk](https://www.conf42.com/JavaScript_2020_Francesco_Leardini_offline_web_apps) from [Conf42 JavaScript 2020](https://www.conf42.com/js2020).

## From Trivadis

Francesco works as a software engineer and consultant at Trivadis, a consultancy based in Switzerland, and the demo code from the talk is on GitHub.

- Trivadis: [trivadis.com](https://www.trivadis.com/en/index.html)

[Watch the talk on YouTube](https://youtu.be/lGba-z0yxqw).

## Watch the talk

[Offline web apps don't exist anymore!](https://www.conf42.com/JavaScript_2020_Francesco_Leardini_offline_web_apps) at Conf42 JavaScript 2020.
