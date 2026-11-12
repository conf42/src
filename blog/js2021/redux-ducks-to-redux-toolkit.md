# Redux Toolkit slices are ducks that finally won

Conf42 Blog, 2021-10-28. https://www.conf42.com/blog/js2021/redux-ducks-to-redux-toolkit

In short: Sergii Zhuravel (Absio) at Conf42 JavaScript 2021 on structuring React/Redux apps by feature, from ducks and re-ducks to Redux Toolkit slices.

The classic React/Redux project has an actions folder, a reducers folder, a sagas folder and a selectors folder, and adding one entity means touching all four. At [Conf42 JavaScript 2021](https://www.conf42.com/js2021), Sergii Zhuravel, Lead Software Engineer at Absio, traced how the community fixed that: ducks, then re-ducks, then Redux Toolkit. His argument is that they are one idea, bundle everything a reducer needs in one place, and Redux Toolkit's slices are its most opinionated form.

## Why is anyone still talking about Redux?

He opens with the obvious objection. Every new arrival, the Context API included, was announced as the end of Redux, and Redux is still the most-starred and most-downloaded React state library on Openbase's list, while scoring lower on user rating. The usual complaint is boilerplate, and he argues much of that pain is structural.

He also splits state into types first: component local state, shared component state (often lifted to a common parent), and global app state, which itself holds UI state (theme, configuration) and a cache of API responses. Many teams now ask whether that cache belongs in the same store at all, a question he raises without settling.

## The folder-per-function trap

Function-first folders look professional in a small app. "Now my application looks professional, but later when we need to maintain and support such project, it can become a nightmare to support it," Sergii Zhuravel said at Conf42 JavaScript 2021. Adding, changing or deleting an entity means visiting the same set of folders every time, so the approach scales badly.

His alternative leans feature-first, with one extra rule: move state management away from the UI entirely, ideally into something you could put in a shared library. Think of the day you move from React to another library, or run React Native alongside the web app, and keep the state layer portable.

## Ducks: one file per reducer

Erik Rasmussen's ducks proposal puts action types, action creators, the reducer, selectors and even sagas for one reducer into a single file. The rules: export the reducer as default, export action creators as functions, and name action types in the form app/reducer/ACTION_TYPE. The name comes from the last syllable of redux, after Java's jars and Ruby's gems. You still import reducers and actions the usual way, so the rest of the app barely notices.

Sergii liked it for small apps and pitched it to colleagues, who were wary at first. Its weakness shows as a feature grows: one file holding everything becomes hard to maintain.

## Re-ducks: one folder per concept

Re-ducks keeps the bundle but turns the file into a folder per concept (product, cart, session) with separate files for types, actions, operations, reducers, selectors, utils and tests, plus an index that exports according to the original duck rules. Operations hold chained logic through middleware such as redux-thunk or redux-saga; selectors, which he builds with reselect, never change state. Tests live in the same folder, so deleting a feature deletes its tests with it.

## Redux Toolkit as the end of the saga

Redux Toolkit's createSlice, in his view, implements the duck idea directly. configureStore wraps createStore in a few lines, supports redux-thunk by default (he wires in sagas instead) and the Redux DevTools extension, alongside createReducer and createAction. The bigger win is opinion: Angular and Vue give newcomers a structure, while React and Redux let them build anything, including bad layouts. Redux Toolkit narrows the choice.

His companion repository for the talk starts from a basic Redux app and refactors it in separate branches, improved classic, ducks, re-ducks and Redux Toolkit, so you can diff the approaches side by side.

## Who should watch

Developers maintaining a Redux codebase that grew by folder, or deciding whether to migrate an older app to Redux Toolkit. It is a history-and-structure talk rather than an API tour, around 20 minutes. Pair it with:

- [Joshua Arvin Lat on state management in React, Angular and Vue.js](https://www.conf42.com/JavaScript_2021_Joshua_Arvin_Lat_State_Management_React__Angular_Vuejs) at Conf42 JavaScript 2021.
- [Assaf Krintza on React performance](https://www.conf42.com/JavaScript_2021_Assaf_Krintza_React_Performance) at Conf42 JavaScript 2021.
- [Daniel Afonso on testing state](https://www.conf42.com/JavaScript_2025_Daniel_Afonso_state_testing_tech) at Conf42 JavaScript 2025.

[Watch Sergii Zhuravel's talk](https://www.conf42.com/JavaScript_2021_Sergii_Zhuravel_Reduxtools_ReactRedux_apps) from Conf42 JavaScript 2021.

## From Absio

Absio sponsored Conf42 JavaScript 2021 and sent one of its engineering leads to give this talk.

- [Absio website](https://www.absio.com)

[Watch the talk on YouTube](https://youtu.be/8T_oB4KgsA4).

## Watch the talk

[Ducks, Re-ducks, Redux-tools - modular approaches for structuring React/Redux apps](https://www.conf42.com/JavaScript_2021_Sergii_Zhuravel_Reduxtools_ReactRedux_apps) at Conf42 JavaScript 2021.
