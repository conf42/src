# Try the framework before you install a state library

Conf42 Blog, 2021-10-29. https://www.conf42.com/blog/js2021/try-the-framework-before-a-state-library

In short: Joshua Arvin Lat (NuWorks Interactive Labs) at Conf42 JavaScript 2021 on when React, Angular and Vue.js apps really need Redux, NgRx or Vuex.

Two months into a new e-commerce build, the shiny state management library is everywhere, nobody fully understands it, and ripping it out would cost another month or two. That is the opening scenario of Joshua Arvin Lat's talk at [Conf42 JavaScript 2021](https://www.conf42.com/js2021). The CTO of NuWorks Interactive Labs argues that most basic to medium-sized React, Angular and Vue.js apps can manage state with what the framework already ships, and that a library such as Redux, NgRx, MobX, Recoil or Vuex should be a deliberate choice, made for the team you have and the deadline you face.

## When does prop drilling justify a library?

He builds it up with a component tree. A child telling its sibling something goes through the parent: easy to read, easy to debug, no extra layer. Add grandchildren that need to talk across branches and you get prop drilling, data passed through components that don't use it, and code that starts to look like spaghetti. The common mistake, in his view, is that teams jump straight from prop drilling to a state management library, when other solutions exist.

The cost is boilerplate. His illustration: 20 lines of logic become 20 plus 10 plus 10 plus 10, about 50 lines, for even a simple feature. In a small app that is a fridge organised with a shipping-container system, mostly empty space.

## What does the framework already give you?

His first rule is to make the most of what you have:

- **React**: useContext, useState, useEffect and useRef carry basic to medium projects without Redux.
- **Angular**: a shared service with dependency injection before NgRx; bring in NgRx once many interconnected components in a single-page app need managed data flow.
- **Vue.js**: the fundamentals plus a simple global store or a global event bus, before Vuex.

Every new tool is something every developer on the project has to learn, so the fewer the better until one is needed. When Redux is justified, Redux Toolkit trims the boilerplate.

## More magic or less magic?

MobX means less boilerplate and more magic: fine for a smaller team, but less explicit, so bugs are harder to trace. Redux is explicit: more files, but when something breaks you know where to look. He sums the trade-off as strong assumptions yield strong guarantees: rules such as immutability cost code but prevent or contain whole classes of issues, which matters in complex apps. A small app that will stay small can accept more risk and more magic. Knowing one-way versus two-way data binding, and using devtools features such as time travel, is part of being able to debug either.

## Time, team and the types of state

Time drives the choice because it drives budget, launch dates and debugging. A 30-person team and a five-person team have very different costs of complexity, and a launch next month may call for something between quick and elegant. Then check skill honestly: a hello-world with Angular and NgRx does not make an expert. His suggestion is a hands-on exam, building an isolated clone of the target app in about 8 hours, to see whether the team can really deliver on that stack.

Not all state belongs in the store. He separates URL or router state, server state, client state and local UI state; a form that only posts to the server doesn't need the full store machinery, and local UI state can stay in its component.

## Don't learn on production

Whatever you pick, stick with it: switching from Recoil to Redux midway means refactoring from scratch. Watch for performance chain reactions and flicker, clean up to avoid memory leaks, and learn each library's own antipatterns. And experiment elsewhere. "Don't use your real projects as a playground," Joshua Arvin Lat said at Conf42 JavaScript 2021. Build a pet project for the new tool instead of adding it to a client's codebase for your resume.

## Who should watch

Tech leads choosing a stack for a new frontend, and teams that suspect their state library is costing more than it saves. It is a decision-making talk across three frameworks, not a code walkthrough. Pair it with:

- [Sergii Zhuravel on ducks, re-ducks and Redux Toolkit](https://www.conf42.com/JavaScript_2021_Sergii_Zhuravel_Reduxtools_ReactRedux_apps) at Conf42 JavaScript 2021.
- [Abdelrahman Awad on Vue.js form validation with vee-validate v4](https://www.conf42.com/JavaScript_2021_Abdelrahman_Awad_Vuejs_form_validation_veevalidate_v4) at Conf42 JavaScript 2021.
- [Assaf Krintza on React performance](https://www.conf42.com/JavaScript_2021_Assaf_Krintza_React_Performance) at Conf42 JavaScript 2021.

[Watch Joshua Arvin Lat's talk](https://www.conf42.com/JavaScript_2021_Joshua_Arvin_Lat_State_Management_React__Angular_Vuejs) from Conf42 JavaScript 2021.

## From NuWorks Interactive Labs

NuWorks Interactive Labs builds websites and applications on React, Angular and Vue.js, the experience this talk draws on.

- [NuWorks Interactive Labs website](https://ecommerce.nuworks.ph)

[Watch the talk on YouTube](https://youtu.be/CI2224SyEZ4).

## Watch the talk

[Pragmatic State Management in React, Angular, and Vue.js Applications](https://www.conf42.com/JavaScript_2021_Joshua_Arvin_Lat_State_Management_React__Angular_Vuejs) at Conf42 JavaScript 2021.
