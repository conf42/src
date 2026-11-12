# A test with no assertions should fail, and Testy makes sure it does

Conf42 Blog, 2021-10-27. https://www.conf42.com/blog/js2021/testy-testing-tool-fails-empty-tests

In short: Nahuel Garbezza (10Pines) at Conf42 JavaScript 2021 on Testy, a zero-dependency JavaScript testing tool built with students to teach TDD

Most JavaScript test runners will happily report a test as green when it never asserted anything. At Conf42 JavaScript 2021, [Nahuel Garbezza](https://www.conf42.com/JavaScript_2021_Nahuel_Garbezza_Testy_testing_tool_teaching), Software Craftsman at 10Pines and a teacher of object-oriented design and test-driven development in Buenos Aires, presents Testy, a minimal testing tool he started building with his students, which treats that case as an error, along with a second trap every JavaScript beginner falls into.

## How do you end up writing your own test runner?

In 2018 he was moving his Object-Oriented Programming 2 course at Universidad Católica Argentina from Smalltalk, which he had taught with for six or seven years, to JavaScript. One day he ran out of exercises and, inspired by Kent Beck building a testing framework test-first in Test-Driven Development by Example, started writing one with the class. The walking skeleton was a single assert function that compared two values and printed ok or failure. Everything since has been built on top of it, test-driven, with coverage above 95%.

## What does simple mean for a testing tool?

His guide is the essay Design Principles Behind Smalltalk, and he names three properties:

- **Zero dependencies.** Jest pulls in 328 dependencies and 42 MB of node_modules, per his count in October 2021. Testy is a few kilobytes, so students on a poor connection can install it for a kata in seconds.
- **Readable code.** No metaprogramming unless strictly necessary, and currently none at all, so students can read the source and even change it.
- **Only the features it needs.** It is not trying to copy other test runners.

Nahuel Garbezza said at Conf42 JavaScript 2021: "There should be no dark magic behind this tool".

To keep complexity in check he generates a dependency graph of the tool's modules with Madge. There are fewer than 20 modules, and a change that makes the chart hard to read, or adds a circular dependency, is a signal to rethink it.

## What does Testy do that Jest and Mocha do not?

The common features are there: suites and tests with a name and a function body, a fluent assertion language (equality, inclusion, emptiness, null, undefined, raised exceptions), coloured console output in English or Spanish, pending tests, a fail-fast mode and random ordering, which he recommends enabling by default to keep tests independent. A test ends in one of five states: success, failure, error, pending, or skipped when fail-fast stops the run.

Two behaviours are there for learners. A test with no assertions is reported as an error saying so, instead of passing. And comparing undefined with undefined is a failure, reported as an indetermination. His demo shows why: misspell a property on two objects, both sides come back undefined, and a normal runner says the names are equal. If you really mean to check for undefined, there is an explicit assertion for that.

## How do you make a small project easy to contribute to?

For him it was the first project that attracted outside contributors, 13 by the time of the talk. What helped: documentation in English and Spanish, issue and PR templates, a changelog following Keep a Changelog, semantic versioning, CI on GitHub Actions with CodeClimate for coverage, automated releases to npm (version 5.1.0 then), badges, good-first-issue labels, and the all-contributors bot to credit people in the README. The demo runs Testy's own suite, 213 tests, written in Testy.

## Who should watch?

Teachers running TDD or object-oriented courses in JavaScript, and anyone who wants a small, readable codebase to learn how a test runner works. Production teams will stay on their runner, but the two beginner traps are worth a lint rule anywhere.

## Related Conf42 talks

- Tal Doron on [why tests should not be left for last](https://www.conf42.com/JavaScript_2021_Tal_Doron_only_tests_left) at Conf42 JavaScript 2021.
- Gil Zilberfeld on [TDD with legacy code](https://www.conf42.com/Python_2022_Gil_Zilberfeld_TDD_legacy_code) at Conf42 Python 2022.
- Ivan Pesenti on [building a complex app with TDD](https://www.conf42.com/Golang_2023_Ivan_Pesenti_complex_app_tdd) at Conf42 Golang 2023.

[Watch Nahuel Garbezza's talk](https://www.conf42.com/JavaScript_2021_Nahuel_Garbezza_Testy_testing_tool_teaching), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From 10Pines

10Pines is the software company where Nahuel Garbezza works as a software craftsman.

- [10Pines website](https://www.10pines.com)

[Watch the talk on YouTube](https://youtu.be/iDPyFa6HV4o).

## Watch the talk

[Testy: a minimal testing tool designed for teaching](https://www.conf42.com/JavaScript_2021_Nahuel_Garbezza_Testy_testing_tool_teaching) at Conf42 JavaScript 2021.
