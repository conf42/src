# Drop the CAPTCHA, and other ways security and accessibility agree

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/security-and-accessibility-can-be-friends

In short: Gian Wild of AccessibilityOz at Conf42 DevOps 2026 on why PDFs are not secure, every CAPTCHA is inaccessible, and WCAG already makes room for security.

Security people get told accessibility will weaken their controls; accessibility people get told security means accessibility must give. At Conf42 DevOps 2026, Gian Wild, founder and CEO of AccessibilityOz, took both claims apart with two examples every web team has met (the "secure" PDF and the CAPTCHA), then walked through the WCAG form requirements that explicitly leave room for security.

Gian brings unusual credentials: she worked on Australia's first accessible website, built the country's first automated accessibility testing tool, spent six years as an invited expert on the W3C WCAG 2 working group, and chairs the Mobile Accessibility Testing Guidelines. She also points out that at least 60% of her staff have always had a significant disability, and that the largest group of disabled web users have cognitive disabilities, not only vision impairments.

## A PDF is not a security control

The first story is about a doctored PDF. As Gian tells it, an Australian politician circulated a version of the City of Sydney's annual report showing a $15 million travel budget; the council's report actually showed $6,000 of international travel, and it could prove the document on its website had never changed because its CMS showed one upload, untouched.

The lesson: people pick PDF because "nobody can change it", yet anyone can edit a PDF. An HTML page on your own site is the harder thing to tamper with, and it is the more accessible format too. Australian guidance already says security features must not block assistive technology, and that if authenticity matters you should state which format is authoritative.

## Every CAPTCHA is inaccessible

Gian's position is blunt, and she backs it with the W3C's own words. WCAG 1.1.1 allows CAPTCHA if alternatives in different sensory modes exist, but the W3C's note on CAPTCHA admits every type will be unsolvable by some disabled users; the requirement exists because banning CAPTCHA outright would push sites to ignore WCAG altogether.

Google's reCAPTCHA gets special attention: it challenges you when you look like a bot, and screen readers look like bots. Audio CAPTCHAs fail too, because they are distorted to beat bots that understand speech, and they are transient, so anyone who cannot hold six characters in memory is stuck. WCAG 2.2's accessible authentication criterion, 3.3.8, then bans cognitive function tests in login unless there is an alternative or an exception such as object recognition, an exception that seems to permit reCAPTCHA's image grids while the W3C still calls them inaccessible.

Her advice is to avoid CAPTCHA entirely. If you truly must, offer more than two working modalities, make audio repeatable, or provide a human who can bypass it. Better options from her list:

- multi-factor authentication
- very simple human test questions (is fire hot or cold?)
- honeypot fields hidden from everyone, screen reader users included
- server-side spam filtering and validation
- timestamping forms, since submissions faster than humanly possible are probably bots
- a confirmation step, proof-of-work JavaScript and limited-use accounts

## WCAG already thought about security

The forms section is a tour of success criteria with good and bad examples: 2.2.1 Timing Adjustable (warn and let the user extend, with an exception for real-time events like auctions), 3.3.1 Error Identification (an error that reads out a long product hash to a screen reader user is not identification), 3.3.3 Error Suggestion, 3.3.4 Error Prevention for legal and financial actions, and 3.3.7 Redundant Entry.

Her point is that several of these carry explicit security carve-outs. Error suggestions are not required if they would jeopardise security; redundant entry is not required where re-entry is needed for security. Autocomplete for email, password and address fields helps a lot of users and costs little security.

## Who should watch

Security engineers who own login and signup flows, and anyone who has added a CAPTCHA because a form got spammed. It is not a DevOps pipeline talk, which is the point: the people who build the gate should hear from the people it locks out. Slides and links are on the AccessibilityOz conferences page.

## Related Conf42 talks

- [Accessible JavaScript: it's easier than you think!](https://www.conf42.com/JavaScript_2025_Gian_Wild_accessible_easier_than) is Gian's companion talk for front-end developers.
- [Automated Web Accessibility testing with playwright.js and axe-core](https://www.conf42.com/JavaScript_2023_Taslan_A_Graham_web_accessibility_testing_playwrightjs_axecore) by Taslan A Graham puts accessibility checks into the pipeline.
- [The Fifth Golden Signal: Making Accessibility Observable](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) by Victoria Nduka treats accessibility as an SLO you monitor.

[Watch Gian Wild's talk](https://www.conf42.com/DevOps_2026_Gian_Wild_accessibility_security_inclusion)

[Watch the talk on YouTube](https://youtu.be/7YMbQhtXQeU).

## Watch the talk

[Security and Accessibility can be friends!](https://www.conf42.com/DevOps_2026_Gian_Wild_accessibility_security_inclusion) at Conf42 DevOps 2026.
