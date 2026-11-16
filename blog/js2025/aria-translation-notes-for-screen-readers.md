# ARIA is translation notes for screen readers, so use it sparingly

Conf42 Blog, 2025-10-06, updated 2026-11-09. https://www.conf42.com/blog/js2025/aria-translation-notes-for-screen-readers

In short: Anisat Ahmed at Conf42 JavaScript 2025 introduces ARIA roles, properties and states, when native HTML is enough, and the mistakes to avoid.

A `div` styled to look like a button is, to a screen reader, just something clickable called "Click me". At Conf42 JavaScript 2025, Anisat Ahmed gave a beginner-friendly introduction to ARIA built around that gap, and her most useful advice was about when not to reach for it at all.

This is an intro talk and says so: half an hour, three core concepts, a handful of code examples, then best practices, common mistakes and testing tools. If you have shipped accessible custom widgets before, it is a refresher. If ARIA attributes feel like magic incantations copied from Stack Overflow, it is a good place to start.

## HTML speaks two languages

Anisat's framing is that every page speaks a visual language (colours, layout, hover effects) for sighted users and a semantic language (this is a button, a level-one heading, a navigation region) for assistive technology. Accessibility bugs happen when the two disagree: something looks like a button but doesn't say it is one. ARIA, Accessible Rich Internet Applications, exists to make them agree when plain HTML can't. Her analogy is translation notes for screen readers: they don't change how the code looks, they add meaning.

She is also clear on motivation. Building accessibly is not a compliance checkbox or lawsuit avoidance; a product people can't navigate is simply unfinished.

## Roles, properties, states

The three concepts in her own short definitions:

- **Role** says what an element is, such as `role='button'` or `role='dialog'`.
- **Properties** describe it, such as `aria-label='Close dialog'`, `aria-labelledby` and `aria-describedby`.
- **States** say what is happening now, such as `aria-pressed='true'`, `aria-expanded` or `aria-selected`.

## Native HTML first, always

Her golden rule is the one the W3C repeats too: no ARIA is better than bad ARIA. Use `button` for buttons, `nav` for navigation, `input` for inputs, and only add ARIA when no semantic element exists, such as for tabs, carousels, modals and notifications. Rebuilding built-in behaviour on a `div` and then patching it with ARIA usually creates more problems than it fixes.

## Two examples worth copying

The first is a toast. A `div` that says "Message sent successfully" is visible to sighted users and silent to screen reader users. Add `role='status'` and `aria-live='polite'` and the message is announced when it appears, without interrupting the user.

The second is a confirm-delete modal. Visually it is obvious; to a screen reader it may not exist. Give the container `role='dialog'`, point `aria-labelledby` at its heading and `aria-describedby` at the paragraph asking whether you are sure, and the user hears what the dialog is for before they reach the Cancel and Delete buttons.

## The mistakes she keeps seeing

- ARIA on every element, just in case.
- `aria-hidden='true'` on interactive elements, which tells the screen reader to ignore something the user needs.
- Assuming ARIA adds keyboard support. It doesn't: you still write the key handlers.
- Conflicting roles, such as a button given a dialog role.

For testing, she recommends unplugging the mouse and tabbing through the page, listening with NVDA on Windows or VoiceOver on a Mac, and running automated checkers like axe DevTools, WAVE and Lighthouse, then retesting by hand. Her workflow advice is to bake accessibility checks into pull requests and the design system so it stops feeling like extra work.

## Who should watch

Junior and mid-level front-end developers, designers who hand off component specs, and reviewers who want a shared vocabulary for why a modal is not being announced. Senior accessibility folks can skip it, or send it to the colleague who keeps writing `div onclick`.

## Related Conf42 talks

- [Raihan Nismara on React accessibility essentials](https://www.conf42.com/JavaScript_2024_Raihan_Nismara_52_react_accessibility_frontend) at Conf42 JavaScript 2024.
- [Nav Singh on accessibility in Android](https://www.conf42.com/Mobile_2022_Nav_Singh_accessibility__android) at Conf42 Mobile 2022.
- [Victoria Nduka on making accessibility observable as a fifth golden signal](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) at Conf42 Observability 2026.

[Watch Anisat Ahmed's talk](https://www.conf42.com/JavaScript_2025_Anisat_Ahmed_introduction_aria_guide), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/zXF8g0TkugI).

## Watch the talk

[Introduction to ARIA: A Developer's Guide](https://www.conf42.com/JavaScript_2025_Anisat_Ahmed_introduction_aria_guide) at Conf42 JavaScript 2025.
