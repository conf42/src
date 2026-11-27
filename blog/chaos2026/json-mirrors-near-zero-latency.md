# Two JSON files, no round trips: the zero-latency UX trick

Conf42 Blog, 2026-11-27. https://www.conf42.com/blog/chaos2026/json-mirrors-near-zero-latency

In short: Haim Michael (Zindell Technologies) at Conf42 Chaos Engineering 2026 on serving a big and a tiny JSON mirror so filtering never touches the backend.

Every filter click in a typical web app is a request, a database query and a render. Haim Michael of Zindell Technologies asks, at Conf42 Chaos Engineering 2026, whether you can skip all of that for read-heavy pages: have the server publish its data as JSON and let the browser do the querying. His case study is nana.events, a conference-discovery site that feels instant on a perfectly ordinary PHP and MySQL stack.

This is a pragmatic web-performance talk rather than a chaos-engineering one, and Haim is upfront that it isn't an architecture to apply to a whole application. It is a pattern for the part of the app where reads dominate.

## What's the "interaction tax"?

Haim's term for the usual loop: the user presses a button or ticks a checkbox, the browser calls the server, the server queries the database, and the client renders the reply. Every filter, navigation or search pays that tax. His alternative is to ship the data the queries need to the browser once and run filtering client-side, while the database stays the single source of truth.

## How does nana.events do it?

The site pulls in tech and business conferences from sources such as python.org's list of upcoming Python events, via a crawler, plus events people submit through an Add Event button. An AI agent on the server validates each submission as a legitimate event before it reaches the database. The backend is RESTful PHP with MySQL, and the front end is a single-page app in vanilla JavaScript, chosen to keep the code and file sizes small and the platform maintainable over the long run.

Whenever the database changes, the server regenerates JSON. There are two files:

- `tiny.json`: only what's needed to paint something on first visit, which helps people on a weak mobile connection.
- `events.json`: the full dataset. It arrives while the visitor is still working out the interface, after which filtering, search and the world map view with its date range slider all run in the browser.

The front end also stores the data in local storage so the next visit renders without waiting.

## Is it really zero latency?

Haim doesn't claim it is. "It's almost, but not zero latency," he says. Filtering and querying skip the network, but you still pay to download the file and run JavaScript on the main thread, and adding an event is a normal round trip. His point is that for the interactions people repeat most, the cost is gone.

## When does it fit, and when doesn't it?

It fits when the dataset is public and not huge, when most interaction is reading and filtering, and when slightly stale data is tolerable. A visitor on an older JSON file isn't a disaster for an events directory. It's a poor fit for large datasets, private data, or anywhere every client must see exactly the same data at the same moment.

His three takeaways: do it intentionally and bundle the data simply, "Don't make it difficult for the client side"; give weak connections a smaller first file; and remember the browser is now doing the computing, so check that the cost is acceptable for what you build. The talk gives no benchmark numbers or measurements of browser memory, so treat "fast" as demonstrated live rather than measured.

## Who should watch

Frontend and full-stack engineers with a read-heavy directory, catalogue or dashboard on a conventional backend, and anyone tempted to reach for a search service before trying a static file. If you work with large or private datasets, skim it for the trade-off list and move on.

Related Conf42 talks: [Surviving a 300% Flash Crowd: State-Safe Autoscaling With Zero Split-Brain Events](https://www.conf42.com/Chaos_Engineering_2026_Amit_Singh_Negi_autoscaling_crowd_brain) by Amit Singh Negi of T-Mobile, and [Chaos Engineering Is Not Just Killing Pods](https://www.conf42.com/Chaos_Engineering_2026_Akbar_Dizaji_net_pods_resilience) by Akbar Dizaji of Skedda, both at the same event.

[Watch Haim Michael's talk](https://www.conf42.com/Chaos_Engineering_2026_Haim_Michael_json_latency_ux) from [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026).

[Watch the talk on YouTube](https://youtu.be/Sem8hEPWi1M).

## Watch the talk

[Zero-Latency UX with JSON Mirrors: Rethinking Data Access Beyond the Backend](https://www.conf42.com/Chaos_Engineering_2026_Haim_Michael_json_latency_ux) at Conf42 Chaos Engineering 2026.
