# Rebuild one page when someone asks for it, not the whole site

Conf42 Blog, 2021-10-29. https://www.conf42.com/blog/js2021/isr-rebuild-one-page-not-the-site

In short: Facundo Giuliani (Storyblok) at Conf42 JavaScript 2021 on Next.js Incremental Static Regeneration, static pages rebuilt per page in the background

Static sites are fast, cheap and secure right up to the day a typo fix means rebuilding ten thousand product pages. At Conf42 JavaScript 2021, [Facundo Giuliani](https://www.conf42.com/JavaScript_2021_Facundo_Giuliani_Incremental_Static_Regeneration), Developer Relations Engineer at Storyblok, explains Incremental Static Regeneration (ISR) in Next.js: keep serving the cached static page, and regenerate just that page in the background once it is old enough. He then shows server-side rendering, static generation and ISR side by side on the same content.

It is a clear introduction for React developers, with the trade-off spelled out instead of buried.

## Why not just generate everything at build time?

He starts from definitions. A static page is delivered exactly as stored, the same files for every visitor, though JavaScript can still make it interactive. A dynamic page is generated when needed, either by the server (server-side rendering) or in the browser (client-side rendering, as in a React app). Static pages win on speed, cost, maintenance, security, scaling (add storage) and stability, which is why static site generation took off: templates plus data from APIs, databases or a headless CMS, compiled into HTML, CSS and JavaScript at build time.

Next.js supports all of these per page, so a blog can build its home page and newest posts statically and render the long tail on demand. The catch is build time, which grows with every page, and atomic deployment: if any page fails to build, the whole deploy rolls back so that no two versions of the site are live at once. For a blog that grows daily or a shop that keeps adding products, rebuilding everything on every edit stops scaling.

## How does ISR work?

You build and deploy version one of each page as usual, and Next.js caches it. A revalidate value, in seconds, sets how long that version is considered fresh. A visitor arriving after that window still gets the cached version one, while Next.js regenerates only that page in the background; once it is done, version two is cached and served to everyone after them.

The benefits from his summary: faster builds, a higher share of cached pages, and a natural fit with a headless CMS, where editors change content without anyone running a build. Generated pages also persist between deployments.

Facundo Giuliani said at Conf42 JavaScript 2021: "This is a problem that we have to evaluate because we are breaking the atomic deployment doing this."

Pages of different versions can be live at the same time. Whether that matters depends on your site, and he leaves the decision to you.

## What does it look like in code?

The demo is a create-next-app project with one home page rendered three ways, pulling content from Storyblok:

- **Server-side rendering**: getServerSideProps runs on every request and fetches the story, Storyblok's word for a page.
- **Static generation**: getStaticProps runs at build time, and getStaticPaths lists which pages to build, here just home.
- **ISR**: the same two functions, with fallback set to blocking and revalidate set to 10 seconds.

The page component is identical in all three; only the data functions change. He then edits a feature title in Storyblok's visual editor, which previews the change against localhost before saving it to the draft. The server-rendered page shows the edit immediately, the static page keeps the old text until the next build, and the ISR page shows the old text once, regenerates in the background, and shows the new text on refresh.

## Who should watch?

React developers choosing a rendering strategy for a content-heavy Next.js site, and anyone whose static builds are getting long. If you already use ISR in production, the talk will not add much beyond the clean side-by-side demo. The Next.js commerce demo and Learn course are his suggested next steps.

## Related Conf42 talks

- Rishi Raj Jain on [incremental static generation and regeneration with Layer0 and Nuxt.js](https://www.conf42.com/JavaScript_2021_Rishi_Raj_Jain_Incremental_Static_Regeneration_ISG_and_ISR_Layer0_Nuxtjs) at Conf42 JavaScript 2021.
- Colby Fayock on [scaling WordPress with Next.js](https://www.conf42.com/JavaScript_2021_Colby_Fayock_Scaling_WordPress_Nextjs) at Conf42 JavaScript 2021.
- Luciano Mammino on [a zero-cost website with Next.js and Airtable](https://www.conf42.com/JavaScript_2022_Luciano_Mammino_0cost_website_nextjs_airtable) at Conf42 JavaScript 2022.

[Watch Facundo Giuliani's talk](https://www.conf42.com/JavaScript_2021_Facundo_Giuliani_Incremental_Static_Regeneration), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Storyblok

Storyblok is the headless CMS used in the demo, with a real-time visual editor that previews content changes against your running front end.

- [Storyblok website](https://www.storyblok.com/)

[Watch the talk on YouTube](https://youtu.be/yyYEx9z2HIU).

## Watch the talk

[Incremental Static Regeneration: Static sites on steroids](https://www.conf42.com/JavaScript_2021_Facundo_Giuliani_Incremental_Static_Regeneration) at Conf42 JavaScript 2021.
