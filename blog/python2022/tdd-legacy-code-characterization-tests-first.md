# TDD works on legacy code once you pin down what already works

Conf42 Blog, 2022-01-28. https://www.conf42.com/blog/python2022/tdd-legacy-code-characterization-tests-first

In short: Gil Zilberfeld (TestinGil) at Conf42 Python 2022 on TDD in messy legacy Python, starting with characterization tests that lock in what works

Every TDD tutorial starts with a fresh calculator class and an empty file, which is exactly why nobody believes it works on their codebase. At Conf42 Python 2022, Gil Zilberfeld, the testing consultant and trainer behind TestinGil and author of *Everyday Unit Testing*, took a deliberately messy calculator from his workshops and did TDD on it live in PyCharm: one bug fix, one new feature, and a lot of refactoring in between. The takeaway: before you write the first red test, lock in what the old code already does.

## Why does TDD look useless on legacy code?

Gil's list of real-world complaints is short and familiar. The textbook examples are too simple. Real dependencies cause havoc, so you end up mocking half the world and the tests get coupled to the code. The code resists change, and changing it just to make it testable feels risky when there are no tests to tell you what you broke.

He reframes the whole thing around time rather than code quality. TDD, code reviews, design reviews and test automation all exist so you spend less time staring at logs and reading code you are afraid to touch. "TDD included in that, it's about respecting your time," Gil Zilberfeld said at Conf42 Python 2022.

## What does the messy calculator look like?

Two APIs: a press method that takes a string of keys and a display getter. Inside press sits what Gil calls arrow code, a nest of if/else branches that points right across the screen. Plus and divide work, minus and multiply do not exist yet, and a few behaviours are just wrong. It fits on one screen because it is Python, which is about the only nice thing to say about it.

## Characterization tests are the safety net

The first move is not a unit test. It is a set of characterization tests: operate the system, write down what comes out, and assert it. Gil describes the idea plainly: "A characterization test is not a unit test or integration test."

He builds them with a small fluent wrapper, so a test reads like pressing three, plus, one, plus, four, and then asserting the display. The passing ones go into a characterization suite that must stay green. The failing ones are the interesting part: pressing plus at the start should show zero and does not; typing zero then three should show three and does not. Now he knows what works, what does not, and what must still work at the end.

## Fixing a bug test-first

The bug: pressing plus at the start crashes with an invalid literal for int, because the code casts an empty display to an integer. Gil writes the failing test, adds the simplest guard that makes it pass, then notices the same pattern in the divide and equals branches. Instead of copy-pasting the fix, he writes one test per branch first, makes them pass, and only then extracts the check into a small parse helper.

Then he refactors the tests too: a base test class holds the setup and the fluent helpers, both suites inherit from it, and the bug-fix tests move into a class named for the scenario, so the method names get shorter and read better.

## Adding a feature by refactoring first

For the minus key he flips the order: refactor the existing code under the tests he already has, so the new feature lands somewhere safe. Three moves:

- **Guard clauses** replace the trailing else, which flattens the arrow.
- **Python 3.10's match statement** replaces the if/elif chain. Gil stresses this one is manual; no tool does it with a guarantee, so lean on the characterization tests and add more if you feel exposed.
- **Extract method**: the plus and divide branches were the same code apart from the operation, so they become one handler that takes the operation enum.

After that, the minus feature is a test plus one enum value, and it passes. "It's like magic really. We worked hard at this magic, but it just works," he said. A final round of extractions leaves the press method reading at one level of abstraction, in the user's language rather than the implementation's.

## Who should watch

Python developers who have tried TDD on a kata, liked it, and then hit a sprawling module at work. The talk is short and code-first; the principles (lock in behaviour, change one thing at a time, refactor both code and tests) carry over to any language.

## Related Conf42 talks

- Ivan Pesenti on [TDD in a complex Go application](https://www.conf42.com/Golang_2023_Ivan_Pesenti_complex_app_tdd) at Conf42 Golang 2023.
- Joe Skeen on [learning to love unit testing](https://www.conf42.com/DevOps_2024_Joe_Skeen_love_unit_testing) at Conf42 DevOps 2024.
- Muhammad Ahsan Ayaz on [refactoring Angular projects](https://www.conf42.com/DevOps_2025_Muhammad_Ahsan_Ayaz_angular_refactoring_projects) at Conf42 DevOps 2025.

[Watch Gil Zilberfeld's talk](https://www.conf42.com/Python_2022_Gil_Zilberfeld_TDD_legacy_code) from [Conf42 Python 2022](https://www.conf42.com/python2022).

## From TestinGil

Gil Zilberfeld runs TestinGil, which trains developers and testers in unit testing, TDD and test automation, and wrote *Everyday Unit Testing*.

- TestinGil: [testingil.com](http://www.testingil.com/)
- Everyday Unit Testing: [everydayunittesting.com](https://www.everydayunittesting.com/)

[Watch the talk on YouTube](https://youtu.be/kxWvP-y49sw).

## Watch the talk

[How to TDD in legacy code](https://www.conf42.com/Python_2022_Gil_Zilberfeld_TDD_legacy_code) at Conf42 Python 2022.
