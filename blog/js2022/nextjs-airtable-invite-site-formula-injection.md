# A free invite-only site, and the Airtable injection hiding in it

Conf42 Blog, 2022-11-17. https://www.conf42.com/blog/js2022/nextjs-airtable-invite-site-formula-injection

In short: Luciano Mammino (fourTheorem) at Conf42 JavaScript 2022 on a zero-cost invite site with Next.js, Vercel and Airtable, plus the formula injection to avoid

You can host a private, personalised event site for nothing, as long as you remember that Airtable formulas can be injected like SQL. At Conf42 JavaScript 2022, Luciano Mammino, Senior Architect at fourTheorem, built an invite-only website from a Next.js app on Vercel with Airtable as the database, then showed the two ways an uninvited guest could still crash the party.

Luciano is a Microsoft MVP and co-author of Node.js Design Patterns, and the talk reads like a well-paced code review: types, API routes, a custom hook, a deploy, then the security bugs.

## What are we building, and why this stack?

Each guest gets a URL with a unique invite code in the query string. A valid code shows a page personalised for that guest (the demo invites the Teenage Mutant Ninja Turtles to a secret pizza party); a wrong or missing code shows access denied. Guests can RSVP, and the organisers, not all of them technical, can edit the guest list in a spreadsheet.

The requirements drive the choices. Next.js gives you a React single-page app and API routes in one project. Vercel, which builds Next.js, deploys straight from GitHub. Airtable is a spreadsheet with APIs, or as Luciano puts it, a dynamic CSV file with APIs. Airtable and Vercel both have generous free plans, so a low-traffic side project costs nothing to host.

## The data flow

The SPA boots showing nothing, reads the code from the URL and calls a backend API. The API looks the code up in Airtable and returns the invite or an error. Luciano used Next.js 12, noting that 13 had just come out.

In Airtable terms: a base (secret pizza party), a table (invites), fields (invite code, name, favourite colour, weapon) and records, one per guest, keyed by a UUID. A nice touch he highlights: Airtable's API docs are generated for your own base, with your table and field names already in the examples, even if the example code still uses var and callbacks.

The API route lives in pages/api/invite.ts thanks to file-based routing. It rejects anything but GET with a 405, returns a 400 when the code is missing, and takes only the first value if the query string repeats the code, because Next.js can hand you an array.

## Why a custom hook?

He tried three ways to manage the fetch lifecycle in React: a useEffect in a top-level component, a context provider, and a custom hook. The hook gave the most concise code for the component that uses it, so useInvite won. It reads the code, calls the API and returns the invite response and an error; the component renders an error, a loading state or the page.

He gives a quick refresher on the rules of hooks, since a custom hook is just a function whose name starts with use and follows them: call hooks only at the top level, never inside loops, conditions or nested functions, and in the same order on every render.

For RSVPs he adds a single-select coming field in Airtable, a helper that updates the record, a PUT-only pages/api/rsvp endpoint and a richer hook that also returns an updating flag and an update function. The component never sees the backend logic; it ticks yes or no and the spreadsheet changes in near real time.

## Security bug one: your secrets are in the bundle

The page shows invalid code, but anything written in JSX ends up in the compiled JavaScript bundle, which every visitor downloads. A curious uninvited guest can open the developer tools and read the venue and date. The fix: no sensitive text in templates. Return the messages from the API alongside a valid invite and interpolate them into placeholders on the client.

## Security bug two: formula injection

The better story is one Luciano says he found himself and reported to Airtable. The lookup builds an Airtable filter formula by interpolating the invite code from the query string. A crafted code can rewrite the formula into one that is true for every record, and the attacker is let in as whichever guest comes first (in the demo, Donatello).

"If you ever used SQL, you probably know of the term SQL injection," Luciano Mammino said at Conf42 JavaScript 2022, and this is that, in a spreadsheet. Airtable didn't provide an escape function, so he wrote his own, with the caveat that it might not be 100% bulletproof and should be reviewed.

## Limits and alternatives

The free Airtable plan allows five requests per second, and each RSVP costs two (look up, then update). Alternatives he lists include Google Sheets, DynamoDB with Amplify, Firebase, Supabase and Strapi. His closing warning is the right one: this is a case study for one use case, so take the lessons, not the code.

## Who should watch

React developers who haven't written a custom hook yet, anyone building a quick side project on a spreadsheet backend, and security-minded folks who enjoy a new flavour of injection. The code is all on GitHub and in a companion article, linked from the talk.

Related talks from Conf42: [Colby Fayock on scaling WordPress with Next.js](https://www.conf42.com/JavaScript_2021_Colby_Fayock_Scaling_WordPress_Nextjs), [Eric Burel on segmented rendering](https://www.conf42.com/JavaScript_2022_Eric_Burel_segmented_rendering) from the same event, and [Daniel Espino Garcia on React hooks](https://www.conf42.com/JavaScript_2024_Daniel_Espino_Garcia_18_reacthooks_improvement_development).

[Watch Luciano Mammino's talk](https://www.conf42.com/JavaScript_2022_Luciano_Mammino_0cost_website_nextjs_airtable) from [Conf42 JavaScript 2022](https://www.conf42.com/js2022).

## From fourTheorem

Luciano introduces fourTheorem as a service company focused on cloud and AWS, doing a lot of serverless work and cloud migrations, and says it is hiring.

- fourTheorem: [fourtheorem.com](https://fourtheorem.com/)

[Watch the talk on YouTube](https://youtu.be/soHRQVeZTDI).

## Watch the talk

[Let's build a 0-cost invite-only website with Next.js and Airtable!](https://www.conf42.com/JavaScript_2022_Luciano_Mammino_0cost_website_nextjs_airtable) at Conf42 JavaScript 2022.
