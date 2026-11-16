# Accessible JavaScript comes down to three types and ten principles

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/js2025/accessible-javascript-ten-principles

In short: Gian Wild of AccessibilityOz at Conf42 JavaScript 2025 on making forms and scripted widgets accessible, from keyboard traps to error messages.

If you only remember one thing from Gian Wild's talk, she would like it to be this: don't use CAPTCHA. At Conf42 JavaScript 2025, the AccessibilityOz founder walked through a compact framework for accessible JavaScript, three types of functionality and ten principles, illustrated with real sites that get it right and very real sites that get it wrong.

The talk is dense on purpose. Gian says so up front and points to the AccessibilityOz JavaScript fact sheet, which carries the same principles, a testing checklist, developer examples and a live demo appendix with copy-paste code. Think of the video as the guided tour of that fact sheet.

## Three kinds of JavaScript, three obligations

Her taxonomy is the useful frame. Type one binds behaviour to elements that are already interactive (links, buttons, text fields), so assistive technology can read their attributes and text. Type two presents information without interaction, such as a progress meter, and must have a text equivalent like a percentage. Type three builds custom widgets that are both, and those must be made from elements assistive tech already understands: a calendar widget with a label, a trigger button and table markup underneath.

## The keyboard is the test that catches most things

Principle two (everything works with every input device) gets a lot of airtime, because assistive technologies such as joysticks, head wands and switches usually mimic a mouse or keyboard. Her rules are concrete: tab moves between actionable items, escape closes, arrow keys move within menus, focus is always visible, and there are no keyboard traps. Except inside a modal, where focus must be trapped until the user closes it.

Her horror story is the late-2000s Firefox video player, which swallowed the tab key. Users who tabbed into it had to close the browser, reopen the page and try to steer around the video.

## Order, time and surprise

Several principles are about predictability:

- **Source order, focus order and visual order should agree.** Insert dynamic content in the DOM right after the element that triggered it. Never put information after a submit button: her examples include a ticket site that hides the accessible-tickets option below it, and a bookshop page that only mentions a title is unavailable in a corner nobody reads.
- **Timed activity can be controlled.** Warn before a session expires and let people extend it. A donation form with a 20-minute timeout gets the eye-roll it deserves.
- **Movement can be paused.** Carousels need pause controls, animated GIFs should stop within five seconds, and the blink and marquee elements stay buried. For flashing content she recommends the free PEAT analysis tool, with the 1997 Pokemon episode as the cautionary tale.
- **No unexpected changes.** No navigation on a select's change event, no timed client-side redirects, no popups that vanish after a few seconds.

## Forms are where JavaScript most often breaks things

Labels must be programmatically tied to fields (she inspects Amazon's sign-in field to show the `for`/`id` pairing). Fieldsets group fields that only make sense together, like an area code plus a phone number. Errors must be in text, not just red, because screen readers don't announce colour and red-blind users can't see it.

Validation gets specific rules: validate on submission, not per field; bind to the form's submit event, not the button's click; move focus to the first invalid field; insert the error message right after the field and in its label; and never force focus to stay in an invalid field.

## Who should watch

Front-end developers who build forms, menus, modals or carousels, which is most of them. Some parts are an intro (there is a pointer to her Accessibility Basics material if terms like "assistive technology" are new), but the form-validation and focus-order rules are the sort of checklist senior engineers get wrong too. Have the fact sheet open in another tab.

## Related Conf42 talks

- [Taslan A. Graham on web accessibility testing with Playwright and axe-core](https://www.conf42.com/JavaScript_2023_Taslan_A_Graham_web_accessibility_testing_playwrightjs_axecore) at Conf42 JavaScript 2023.
- [Erissa Duvall's accessibility testing 101](https://www.conf42.com/Kube_Native_2023_Erissa_Duvall_accessibility_testing_101) at Conf42 Kube Native 2023.
- [Gian Wild on why security and accessibility can be friends](https://www.conf42.com/DevOps_2026_Gian_Wild_accessibility_security_inclusion) at Conf42 DevOps 2026.

[Watch Gian Wild's talk](https://www.conf42.com/JavaScript_2025_Gian_Wild_accessible_easier_than), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/6X7JtkEhRX8).

## Watch the talk

[Accessible JavaScript: it's easier than you think!](https://www.conf42.com/JavaScript_2025_Gian_Wild_accessible_easier_than) at Conf42 JavaScript 2025.
