# We made our API twice as fast and paged someone else's on-call

Conf42 Blog, 2021-02-26. https://www.conf42.com/blog/ce2021/faster-endpoint-paged-someone-else

In short: Lisa Karlin Curtis (GoCardless) at Conf42 Chaos Engineering 2021 on why almost any API change can break an integrator, and how to ship them more safely

A developer at GoCardless fixes an N+1 problem, halves an endpoint's latency, and admires the cliff in the graph. Somewhere else, another engineer gets paged because their database CPU just spiked. At Conf42 Chaos Engineering 2021, Lisa Karlin Curtis, Tech Lead at GoCardless, uses that story to show that a breaking change is not a property of the change but of what your integrators assumed, and walks through how to find those assumptions, shrink them, and release risky changes without wrecking anyone's night.

## How does a performance fix break someone?

The integrator's webhook handler received a webhook, called back to the very endpoint that had just been fixed, then wrote to its own database. GoCardless webhooks come from batch processes, so they arrive in big spikes a couple of times a day. Faster responses meant the handler pushed more and more load into its database during each spike, until someone was paged. The fix was easy (scale down the handlers, or the database up); seeing it coming was not.

Her catalogue of other real breaks: introducing a rate limit (Docker's, she notes, was clearly communicated and still hurt); changing an error string that someone was matching with a regex to pick the message shown to users; fixing an endpoint that ignored the Accept-Language header, which broke an integrator who relied on always getting English; splitting the database transaction that always created a state transition and its event together; and moving the time of a daily batch run that some integrators create payments just ahead of.

Lisa Karlin Curtis said at Conf42 Chaos Engineering 2021: "it may indeed be their fault, but it's often your problem."

Assumptions are inevitable, she argues, since you can't write code without making hundreds of them, and unless you are Google or AWS, your integrators' pain is your pain.

## Where do assumptions come from?

Some are explicit: API docs (which people skim straight to the examples), support articles and third-party blog posts, and ad hoc answers from presales, solutions engineers, support tickets or a friend who used to work there. Some are implicit: industry standards, like a JSON response keeping its content-type header. GoCardless had a bad incident when an HAProxy upgrade began lowercasing outgoing HTTP headers. By the book, header names are case-insensitive. A couple of key integrators relied on the old casing anyway, and because their requests succeeded but the responses could not be parsed, the outage was worse.

The biggest source is observed behaviour. Developers spot an undocumented header, a batch that always runs at the same time, or a latency figure, and build on it, because humans pattern-match aggressively. Her historical example is MS-DOS: developers reverse-engineered undocumented calls Microsoft used in its own software, Ralf Brown's Interrupt List spread them widely, and Microsoft could no longer change the internals without breaking the applications that made the platform worth having. The modern equivalent, she says, is a Medium post titled ten things you didn't know an API could do.

## How do you stop integrators assuming the wrong things?

- **Document edge cases**, and make them findable through site search and SEO, since developers google everything.
- **Never leave something undocumented on purpose** because you might change it. Say plainly that it will change. She puts it bluntly: "if you don't document something, you can end up just as locked in as if you do."
- **Keep guides current and versioned**, and chase incorrect third-party posts.
- **Centralise ad hoc communication**: PDFs and shared Slack channels engineers can't search mean nobody can tell what was promised.
- **Name things honestly.** An account number ending field breaks expectations when Australian account numbers contain letters; numbers with leading zeros, like company registration numbers, lose them in a numeric column. Put the edge case in the example itself.
- **Restrict your own behaviour, and document the limit**: events per webhook, payload size, request rate. Otherwise a future optimisation can quietly multiply the events in every webhook.

## How do you ship a change that might break someone?

Treat breaking as a probability, not a yes-or-no. Empathise, rubber-duck with colleagues who know the system less well, talk to integrators, and have new engineers integrate against your API during onboarding to find tripwires. Measure where you can: GoCardless sees the daily spike of payment creation just before its payment run, and rising 5xx responses to your webhooks point to a broken integration on the other side.

Then scale the communication to the risk: a changelog first, targeted emails only to those affected (and never mixed with marketing), and explicit acknowledgement from a few key integrators for the scariest changes. Make breaking changes often, so the muscle and the contact list stay current. Roll out incrementally, by percentage of requests or a slowly rising number of events per webhook, so an outage becomes a degradation; use the sandbox as a canary; and keep a kill switch and know each change's point of no return.

## Who should watch

Anyone who owns a public or internal API, and anyone on the other side who has been surprised by one. It is the most practical API-evolution talk you will find at a chaos engineering conference.

## Related Conf42 talks

- Arlemi Turpault on [API-first design](https://www.conf42.com/Chaos_Engineering_2022_Arlemi_Turpault_how_to_win_friends_and_influence_people_with_api_first) at Conf42 Chaos Engineering 2022.
- Navendu Pottekkat on [SRE best practices for API design](https://www.conf42.com/Site_Reliability_Engineering_2022_Navendu_Pottekkat_sre_best_practices_api_design) at Conf42 SRE 2022.
- Marvin Collins Hosea on [building secure, scalable webhooks](https://www.conf42.com/Golang_2023_Marvin_Collins_Hosea_building_secure_scalable_webhooks) at Conf42 Golang 2023.

[Watch Lisa Karlin Curtis's talk](https://www.conf42.com/Chaos_Engineering_2021_Lisa_Karlin_Curtis_breaking_things)

## From GoCardless

GoCardless runs the bank payment API every example in the talk comes from: its webhooks, its daily payment run and the integrators building on both.

- GoCardless: [gocardless.com](https://gocardless.com)

[Watch the talk on YouTube](https://youtu.be/PPoQSa_6Dko).

## Watch the talk

[How to avoid breaking other people's things](https://www.conf42.com/Chaos_Engineering_2021_Lisa_Karlin_Curtis_breaking_things) at Conf42 Chaos Engineering 2021.
