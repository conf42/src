# Keep the monolith, call it the app shell, and carve pages out of it

Conf42 Blog, 2021-10-28. https://www.conf42.com/blog/js2021/westwing-app-shell-module-federation

In short: Trishul Goel (Westwing) at Conf42 JavaScript 2021 on splitting a front-end monolith into micro frontends with webpack 5 Module Federation and an app shell

Westwing did not build a new shell for its micro frontends. It renamed the old front-end monolith the app shell and started moving pages out of it, one at a time. At Conf42 JavaScript 2021, [Trishul Goel](https://www.conf42.com/JavaScript_2021_Trishul_Goel_monolith_Microfrontends), Principal Engineer at Westwing, shows how that works with webpack 5 Module Federation, what ended up in the shell, and the four problems the team had to solve after the first demo worked.

## Why break up the front end at all?

Back ends were split into microservices years ago, but business logic kept moving into the browser, and the front end turned into a monolith of its own: one growing repository, more and more teams in the same code, a slower path from development to deploy. Worst of all, one team breaking production blocked every other team's deploy until the fix landed.

Micro frontends answer that with small apps, each with its own repository, CI pipeline and, the part he likes most, independent deployment, stitched together into a single page at runtime.

## What lives in the app shell?

At Westwing, an e-commerce site, every page became a micro frontend: home, product listing, product detail, cart, payments. The host, which they call the app shell, owns the header and footer plus the business logic that must stay identical everywhere:

- **Login**: a micro frontend sends a signal, the shell runs the login flow and returns the user.
- **Tracking**: third-party tracking goes through the shell, so there is one place to log and debug it.
- **System config**: environment and pipeline config, a single source of truth.
- **Routing**: the shell receives the request and renders the right micro frontend between header and footer.

For communication, same-stack apps pass props like any React component, functions included. Across stacks, or between micro frontends, they use custom DOM events: create a CustomEvent with a payload, dispatch it, and any subscriber on the page gets it. Plain browser JavaScript, no framework involved.

## How does Module Federation wire it up?

Their first attempt shipped components as npm packages, which still meant bumping versions and redeploying the main app, so the coupling was back. Module Federation lets webpack reference modules that do not exist at compile time and load them at runtime.

The remote's webpack config adds the ModuleFederationPlugin with a name (the namespace the host will use), a remoteEntry file (a manifest of what is exposed and how to load it), an exposes map pointing at the component, and shared libraries, here React and React DOM, which the remote takes from the host instead of loading a second copy. The host config lists its remotes and their addresses. Then it is one import from the remote's namespace and the component behaves like a local one. His demo passes a counter from the host's state into a component served from another port, and both counts move together.

## What hurt after the demo worked?

Trishul Goel was candid that it was not a piece of cake, and listed the fixes:

- **Design consistency**: a design system called UI Kit with a Storybook. New components go into the kit first, even if only one micro frontend needs them.
- **Starting a new micro frontend**: each needs GitLab pipelines, CI, Docker, Helm charts and S3 publishing scripts. A templating tool spins up a new one in about a minute, and an infrastructure change made in the template propagates to every micro frontend.
- **Decoupling code from the shell**: moving every UI component into the design system first removed most internal references. Static shared logic such as price and date formatting became small npm utility packages, created once a helper is used by more than two micro frontends.
- **Local development**: running the shell plus three micro frontends at once was heavy.

Trishul Goel said at Conf42 JavaScript 2021: "My laptop fan was really like I'm doing a coin mining or something."

The fix was a Docker image of the staging setup that takes micro frontend URLs from environment variables: everything runs from staging except the one micro frontend you are working on locally. Six months in, he called the move worth it, with more still to improve.

## Who should watch?

Front-end leads with several teams in one React codebase who want a concrete migration path rather than architecture diagrams. The webpack configs are short enough to copy, and the challenges section is the part most micro frontend talks skip.

## Related Conf42 talks

- Tomasz Krajewski on [micro frontends foundations](https://www.conf42.com/JavaScript_2021_Tomasz_Krajewski_Micro_Frontends_foundations) at Conf42 JavaScript 2021.
- Azizi Yazit on [design systems for micro frontends](https://www.conf42.com/JavaScript_2021_Azizi_Yazit_System_MicroFrontends) at Conf42 JavaScript 2021.
- Maksim Zemskov on [scaling a glorious monolith with micro frontends](https://www.conf42.com/JavaScript_2023_Maksim_Zemskov_glorious_monolith_scaling_application_microfrontends) at Conf42 JavaScript 2023.

[Watch Trishul Goel's talk](https://www.conf42.com/JavaScript_2021_Trishul_Goel_monolith_Microfrontends), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Westwing

Westwing is the home and living e-commerce company whose shop front end this talk describes.

- [Westwing website](https://www.westwing.com/home/)

[Watch the talk on YouTube](https://youtu.be/frregZU6ck0).

## Watch the talk

[Destructuring frontend monoliths with Microfrontends](https://www.conf42.com/JavaScript_2021_Trishul_Goel_monolith_Microfrontends) at Conf42 JavaScript 2021.
