# How to Make SPA Apps SEO Friendly

Conf42 Blog, 2022-08-04. https://www.conf42.com/blog/2022-08-04-spa-apps-seo-friendly

In short: a guest blogpost by Sammy Lin

## How to Make SPA Apps SEO Friendly
The evolution of web apps has recently brought about an interesting twist. As developers became ever more reliant on client-side Javascript for creating dynamic web pages, a new pattern of development emerged. This new pattern was great for developers and clients alike.
However, Googlebot wasn’t so fond of it. This client heavy pattern, known as the single page application (SPA), essentially builds and renders an entire website on the client. In most cases, the only real work happening on the server is client-side API calls for data retrieval.

### Why Are SPAs Bad for SEO?
SPAs and SEO don’t always play well together, and it’s common for poorly configured [SPA
SEO](https://www.ohmycrawl.com/spa-seo) to rank poorly with Google or other search
engines. To understand why, we need a quick refresher on how an SPA works. SPAs use an
empty shell pattern, which means that an empty HTML shell is sent to the client at initial page
load.

### What the Client Receives When They Request an SPA
When you request a page that utilizes the SPA pattern of development, you’ll receive something that looks like this:
```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Example SPA Shell&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div id=&#39;root&#39;&gt;
&lt;/div&gt;
&lt;script src=”/spa-script.js”&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

After the initial page load, the **spa-script.js** script is ran, which populates the `root div` tag
with all the guts of the site. This means the navigation bar, footer, images, and everything else
isn’t rendered until the browser finishes processing this script.
It’s a simple concept that works well at first glance. However, Google wants content fast, and
the extra time it takes to process all that Javascript before the content is displayed hurts page
rank for a number of Google SEO web metrics.

### Ways to Load Content More Efficiently in an SPA to Enhance SEO
SPA frameworks like React have devised a number of ways to increase SEO performance while
leveraging all the benefits that come with the SPA pattern. These techniques can be broken
down into 3 main categories:

1. CDN caching and prerendering services.
2. Dynamic loading.
3. Isomorphic development.

These techniques are often used in conjunction with one another to increase SEO performance,
which usually has the added benefit of enhancing user experience.
Let’s take a closer look at each technique and how they solve our SEO woes.

#### CDN Caching and Pre-Rendering Services
One popular and fairly simple technique is to utilize caching services, which saves a pre-
rendered copy of our SPA that is ready for the client (and search engines) to consume. This
improves SEO because the Javascript is already processed into static content, which is readily
available for crawler consumption.
The workflow for this solution looks something like this:

1. The SPA website is built and launched.
2. A prerender service such as prerender.io is used to store and serve a static “prerendered” copy of the website.
3. This new endpoint is configured with a CDN such as Cloudflare to serve the content even faster.

For small sites that utilize content that doesn’t change frequently, such as a blog or small business page, this solution works great. However, this option comes with limitations that make it a poor choice for sites more dynamic in nature.

The prerender.io service will only render your page one to three times per day. So, if you have
content that is changing rapidly, such as an auction site or social media platform, three renders
a day isn’t even close to keeping up with the rapidly changing data.

#### Dynamic Loading of Components
Most SPA frameworks come equipped with some form of dynamic or “lazy” loading
functionality. Since React is the most popular SPA framework to-date, we’ll use it for our
example.

When using React, code is broken up into components. Each component usually consists of
some bit of code that is eventually rendered into pure HTML. The problem is, all these
components are indiscriminately packaged up into a code bundle that’s processed on the client.
Instead of loading all of this code as one linear chunk, we can gain significant SEO performance
gains if we prioritize the order in which our code is loaded.
As an example, we can load our navigation bar and footer first, then load the body content
once these two components are rendered. This helps boost an SEO metric called first contentful
paint (FCP), which is an important Google ranking factor.
Here’s an example of what this would look like in a simple React implementation:

```
import React, { Suspense, lazy } from &#39;react&#39;;
import Navbar from &#39;./Navbar&#39;;
import Footer from &#39;./Footer&#39;;
 const MainContent = lazy(() =&gt; import(&#39;./MainContent&#39;));
 const App = () =&gt; {
        
    return(
        &lt;&gt;
            &lt;NavBar/&gt;
            &lt;Suspense fallback = {&lt;div&gt;Content is loading...&lt;/div&gt;}&gt;
                &lt;MainContent/&gt;

            &lt;/Suspense&gt;
            &lt;Footer/&gt;
        &lt;/&gt;
    );
    
}
 export default App;

```
As can be seen in the above code, we are importing the `lazy` and `Suspense` components from
the React framework. We then wrap our `MainContent` component, telling React to __only
load__ this component once all other components on the page are finished rendering.
This is a simple technique often overlooked by novice React developers that can significantly
increase SEO performance in React apps.

### Isomorphic Development for Increasing SEO Performance

Isomorphic development is just a fancy way of saying “what can be done on the client can also be done on the server.” In the case of React, this means that we can utilize React code on the server. This opens the door for two patterns of development that can increase SEO performance; static site generation (SSG) and server side rendering (SSR). Each technique can be defined as follows:

- **Static Site Generation (SSG)**: SSG is similar in concept to prerendering, but it is much more powerful. SSG is implemented by creating server code that renders all of your SPA code into pure HTML at build-time. This means the developer can code the entire site using a framework like React, then run a “build”, which essentially converts all that code into static HTML files which are then served from a hosting provider.
- **Server Side Rendering (SSR)**: SSR is similar to SSG because most of the work happens on the server. However, instead of everything being processed at build-time, it is processed at “run-time”, during each request that is made by the client. This means that when you request a page, the server converts all of the code into HTML on the fly, then sends the result to the client.

SSG is typically faster than SSR, but it comes with the same pitfalls as the prerendering option. Although SSG can handle more dynamic data than a prerendering service, you are still limited

by the number of builds your server can process before the overhead becomes too cumbersome. SSR is currently the most scalable solution because you can handle much of the rendering on the server real-time, while dictating which code you’d like to process on the client.

### Overview SPA Technology and SEO Implications

Leveraging SPA technology is beneficial for both the developer and end-user. For this reason, developers have worked hard to come up with solutions for the inherent SEO pitfalls of this design pattern.

The techniques mentioned in this article can be used to significantly increase SEO performance, while leveraging all the great features that come with SPA frameworks such as React. As usual, if the problem is understood, it can be overcome.

The SPA paradigm is here to stay. While it can be tricky understanding which implementation is best for you, the payoff is usually worth the hard work.

To learn more about Javascript SEO, visit [OhMyCrawl.com](https://www.ohmycrawl.com) for more information.
