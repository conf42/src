# TypeScript strict true is a start, not the whole rulebook

Conf42 Blog, 2021-10-29. https://www.conf42.com/blog/js2021/typescript-strict-true-is-not-everything

In short: Daniel Danielecki (Capgemini) at Conf42 JavaScript 2021 on what each TypeScript strict compiler option catches, and what strict mode still leaves off

Turning on strict in tsconfig.json feels like flipping every safety switch TypeScript has. It is not. At Conf42 JavaScript 2021, [Daniel Danielecki](https://www.conf42.com/JavaScript_2021_Daniel_Danielecki_TypeScripts_Strict_Compiler), Software Engineer at Capgemini, walks through the compiler options one at a time, each with a small broken snippet and its fix, then shows how differently Angular, React, Vue.js and Svelte set them up for you out of the box.

It is a reference-style talk: one option, one error, one fix, repeated. That makes it easy to watch with your own tsconfig open in the other window.

## Which strict options catch real bugs?

The best example in the talk is strictFunctionTypes. A callback typed for strings is passed somewhere that hands it a number, and the code calls toLowerCase on it. With the flag off, the compiler says nothing and the bug ships; his demo compiles it and shows the runtime error a user would get. With it on, TypeScript points at the parameter mismatch first and, once fixed, at the real problem: toLowerCase only exists on strings.

The rest of the tour, in the order he covers it:

- **noImplicitAny**: parameters without a type become errors.
- **noImplicitThis**: the confusing one. Fix it with an arrow function or by typing this explicitly in the parameter list.
- **noImplicitOverride**: a subclass method that overrides must say override, a habit Java developers will recognise.
- **strictNullChecks**: assigning null to a string is now an error. strictPropertyInitialization only works together with it and flags class properties that are never initialised.
- **noFallthroughCasesInSwitch**: his compiled demo shows a missing break printing both even and odd for zero.
- **exactOptionalPropertyTypes**: an optional number no longer silently accepts an explicit undefined unless you say so in the type. It also needs strictNullChecks.
- **useUnknownInCatchVariables**: the caught error becomes unknown, so reading its message needs an instanceof Error check first. He admits he is not sure how big the risk is without it.

He skips strictBindCallApply, reasoning that bind, call and apply are rare since ES6, and points to the docs.

## What does strict leave off?

strict enables a family of type checks plus alwaysStrict, which emits JavaScript in strict mode rather than sloppy mode. It does not enable the options the docs file elsewhere, such as noImplicitReturns, noFallthroughCasesInSwitch, noPropertyAccessFromIndexSignature and noUncheckedIndexedAccess. The last two are the advanced ones: the first forces bracket access for properties that come from an index signature, so a reviewer can see which ones the interface does not declare; the second types such access as possibly undefined.

He also covers the options that protect you by default and should stay that way, like suppressExcessPropertyErrors and suppressImplicitAnyIndexErrors, where turning them on, or reaching for a ts-ignore, is a bad idea. skipLibCheck is a genuine trade-off between build speed and checking conflicting types in dependencies.

## How do the frameworks set it up?

Comparing default generated configs, in his summary table: React and Vue.js 2 ship with strict on, Svelte ships with it off, and Angular asks during project generation whether you want strict, the only CLI that does. Counting the extra linter-style checks outside strict, Angular adds two out of seven, React one, Vue.js and Svelte none. His verdict on Svelte is that its TypeScript support still had some catching up to do.

## Is it worth the friction?

He cites a study that found TypeScript catching about 15% of bugs, done in the TypeScript 2.0 era and before the newer strict flags, and an Airbnb review that estimated 38% of their bugs could have been prevented with TypeScript. His argument is that stricter settings should push those numbers up, not down.

Daniel Danielecki said at Conf42 JavaScript 2021: "It's the same as you saying you don't need tests because you don't write bug code".

## Who should watch?

Developers who turned on strict once, saw a wall of errors and turned it off again, and teams deciding on a shared tsconfig. The demos are small enough to replay in any editor.

## Related Conf42 talks

- Serhii Bilyk on [writing safer TypeScript](https://www.conf42.com/JavaScript_2022_Serhii_Bilyk_safer_typescript) at Conf42 JavaScript 2022.
- Austin Gil on [type safety with JSDoc and TypeScript](https://www.conf42.com/JavaScript_2022_Austin_Gil_jsdocs_typescript) at Conf42 JavaScript 2022.
- Kacper Szewczyk on [improving TypeScript developer experience](https://www.conf42.com/JavaScript_2024_Kacper_Szewczyk_31_typescript_developerexperience_improvement) at Conf42 JavaScript 2024.

[Watch Daniel Danielecki's talk](https://www.conf42.com/JavaScript_2021_Daniel_Danielecki_TypeScripts_Strict_Compiler), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Capgemini

Capgemini is the consulting and technology services company Daniel Danielecki works for as a Software Engineer.

- [Capgemini website](https://www.capgemini.com/gb-en/)

[Watch the talk on YouTube](https://youtu.be/o0HEbXdCyKg).

## Watch the talk

[TypeScript's Strict Compiler Options](https://www.conf42.com/JavaScript_2021_Daniel_Danielecki_TypeScripts_Strict_Compiler) at Conf42 JavaScript 2021.
