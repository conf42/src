# A visual builder that keeps regenerating your React code, and stays out of your logic

Conf42 Blog, 2020-09-30. https://www.conf42.com/blog/js2020/plasmic-visual-react-components-sync

In short: Yang Zhang (Plasmic) at Conf42 JavaScript 2020 on building React components visually and keeping design and code in sync with Plasmic

Most product teams have two copies of their UI: the designer's drawing and the developer's code, and they drift apart from day one. At Conf42 JavaScript 2020, Yang Zhang, co-founder of Plasmic, built a slice of TodoMVC from scratch in Plasmic's visual editor, pulled it into a Create React App project as real components, then restyled it in the editor while the change streamed into the running app.

It's a vendor talk and he says so: he works on one of the tools in a young category he lists alongside others. The second half, on what made the tool hard to build, is the part that will interest engineers who never plan to use it.

## What's wrong with designing in drawings?

Design tools like Sketch and Figma are vector drawing tools: fast for exploring ideas, but what they produce is freeform drawings. Engineers then rebuild the UI by hand, things get lost in translation, and there's a lot of back and forth. "And ultimately you have these two sources of truth that by most teams admission are never truly in sync," Yang Zhang said at Conf42 JavaScript 2020.

Visual UI builders are normal on iOS, Android and Windows, but not on the web, where they're seen as clunky. Website builders like Webflow target static sites. For a web app with a database, user accounts and custom business logic, he points to an emerging category of UI builders for web apps, each with a different take.

## What does the workflow look like?

Start rough. He draws boxes and text on the canvas for a task row and its checkbox, then right-clicks to turn the row into a reusable component called task, so every pasted copy is an instance of one primary. Styling comes next: a thin title in light red, an off-white page, and a text colour saved as a reusable colour token. Tokens, spacing tokens and mixins are how the design stays maintainable.

Layout is where Plasmic tries hardest. Lasso the tasks into a vertical stack (Flexbox underneath), snap to top-left, auto-size by double-clicking an edge. Text that should vary becomes a slot, a hole in the component you can fill with any content from each instance.

States are modelled as variants. He creates a states group with completed, editing and high-priority variants and designs completed: a pasted check mark, strike-through text, a lighter colour. Variants are overrides on top of the base, not copies, so base changes bleed through. They combine, too: a built-in hover variant darkens the checkbox border and switches the cursor, and preview mode shows completed and hover together.

## How does it get into code?

Two commands: plasmic init once per codebase, then plasmic sync to pull the components. The generated split is the interesting design choice. Each component gets a presentational Plasmic component that Plasmic owns and regenerates, plus a thin wrapper file generated once that you own. Yang replaces the mock tasks with real state in the wrapper, overriding the named task list element with his own data and task components. Then plasmic watch streams edits live: in the editor he turns the vertical list into wrapping tiles with gaps in both directions, and the app on the right updates as he works.

## What made it hard to build?

State management at scale. Smooth drags at 60 frames per second mean "you typically have a frame budget of around 16 milliseconds," Yang said, and a canvas with hundreds of artboards can't re-render synchronously on every change. Plasmic splits updates into small chunks and schedules them: the artboard you're manipulating first, nearby ones next, off-screen ones last.

Code components are the other hard problem: bringing your own React components, or a library like Material UI, into the canvas. That means bundling them without making users webpack experts, loading foreign code into the canvas securely and in isolation, and crawling the codebase to reflect component interfaces from TypeScript or prop types into controls, while children props stay editable by drag and drop.

The product challenges are just as concrete: distilling CSS layout into a small set of controls with escape hatches down to flex-basis, and importing from Figma, whose model (layers, masks, blend modes, centred borders) doesn't map neatly onto CSS. Underneath it all, the rule is that developers control the component API, so generated code helps and never hinders.

## Does the team use it?

They build Plasmic with Plasmic. The effects he names: a design-first habit that forces you to define the end product before the code; the occasional magic of running plasmic sync and finding a nicer landing page in the repo; and dropping a whole class of visual regression tests, since what you see in the editor is what ships. At the time the team was five people, three on engineering.

## Who should watch

Front-end developers tired of translating mockups pixel by pixel, and engineers interested in editor architecture. Related Conf42 talks: [Andrew Knight on visually testing components](https://www.conf42.com/JavaScript_2022_Andrew_Knight_visually_testing_components), [Arundeep Nagaraj on going from Figma to full stack with AWS Amplify](https://www.conf42.com/JavaScript_2023_Arundeep_Nagaraj_easy_mode_fullstack_figma_aws_amplify), and [Assaf Krintza on React performance](https://www.conf42.com/JavaScript_2021_Assaf_Krintza_React_Performance).

[Watch Yang Zhang's talk](https://www.conf42.com/JavaScript_2020_Yang_Zhang_react_frontend) from [Conf42 JavaScript 2020](https://www.conf42.com/js2020).

## From Plasmic

The talk demoed the Plasmic editor, the plasmic CLI (init, sync and watch), a CodeSandbox integration for spinning up a project straight from the editor, and the Figma plugin for importing existing designs.

- Plasmic: [plasmic.app](https://www.plasmic.app)

[Watch the talk on YouTube](https://youtu.be/BdCwJiHlDnE).

## Watch the talk

[Building React frontends visually](https://www.conf42.com/JavaScript_2020_Yang_Zhang_react_frontend) at Conf42 JavaScript 2020.
