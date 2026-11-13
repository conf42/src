# Haskell on the JVM, or how to refactor without the fear

Conf42 Blog, 2021-03-25. https://www.conf42.com/blog/enterprise2021/eta-haskell-on-the-jvm-refactoring

In short: Abdu Códigos (Kulkul Technology) at Conf42 Enterprise Software 2021 on why pure FP makes refactoring safe, from Elm in the browser to Eta on the JVM

Every Java developer knows the moment after a big refactor when the code compiles and nobody is sure the app still works. At Conf42 Enterprise Software 2021, Abdu Códigos, founder of Kulkul Technology, argues that a strict functional language shrinks that gap until "it compiles" nearly means "it works", using Elm on the frontend as the success story and Eta, a Haskell for the JVM, as the experiment. The takeaway is honest: learn pure FP for how it changes your code, but think twice before putting Eta in production.

It is an introductory talk for Java programmers, part pep talk for functional programming, part live demo.

## Why does refactoring feel so risky?

He tells it as the story of John, a software engineer who builds a web app in his favourite language (Java), opens a pull request, and meets the senior reviewer. Abdu Códigos said at Conf42 Enterprise Software 2021: "ten lines of code, ten issue. But if it's 500 lines of code, it looks fine."

John refactors as asked, sweats through it, and the app no longer works. The lesson Abdu draws: building reliable software takes code review, unit tests and refactoring, and refactoring in particular gets complex. His proposed shortcut is functional programming, which he dates back to 1978 and describes as an old concept that keeps proving itself, unlike frontend ideas that get invented overnight.

## What does pure FP actually buy you?

The pitch is composition of pure functions, immutable data and no shared state. That brings easier concurrency (he quotes Uncle Bob on race conditions and deadlocks coming from mutable variables), lazy evaluation, and above all code that is easy to change: keep the interface, rework the inside, and lean on the compiler.

He sorts languages into pure (Haskell, Elm, Mercury, Clean), impure (Scala, Clojure, F#, OCaml), and multi-paradigm languages like JavaScript and Ruby that keep borrowing FP ideas.

## Elm is the proof he has lived

His own success story is Elm on the frontend. The claims on Elm's site read like a scam, he jokes, until you use it: follow the compiler errors and you come out the other end with a working app. He points to NoRedInk, which reports almost zero runtime exceptions in production; the one they hit was a compiler bug, since fixed. Open the devtools console on almost any big web app and you see the contrast.

He also credits Elm's friendly compiler messages, which name the mismatched types and offer a hint. Fast, readable feedback is what turns a long refactor into a checklist.

## What is Eta, and should you use it?

Eta brings Haskell to the JVM. Its selling points, as he lists them: a strongly typed foreign function interface for safe Java interop, global type inference that feels like a dynamic language with a strict type system underneath, and several concurrency strategies, including software transactional memory and fibers.

The demo is a small web service in Haskell source files, built with Eta's own tooling inside Docker: a Fibonacci endpoint on port 9000 and a hello endpoint that reads a name from a query parameter and returns an error if it is missing. The API is declared as a type, and everything has to match it. A patched version of a Haskell web library runs on Jetty underneath.

Then the caveats, which he does not hide. Eta is not actively maintained, many packages are no longer hosted (he had to run the Docker image to get it going), and keeping Haskell dependencies compatible is hard. His recommendation: use it to learn, especially if you come from Java and want to run Haskell with Gradle instead of learning a new build tool, not for production.

## Who should watch

Java developers curious about pure functional programming and tech leads choosing a stack for a new service. The FP half is a gentle introduction; the Eta half is a field report on a language whose momentum had stalled.

## Related Conf42 talks

- Jordane Grenat on [Elm for the frontend](https://www.conf42.com/JavaScript_2021_Jordane_Grenat_Elm_frontend) at Conf42 JavaScript 2021.
- Daniel Danielecki on [TypeScript's strict compiler](https://www.conf42.com/JavaScript_2021_Daniel_Danielecki_TypeScripts_Strict_Compiler) at Conf42 JavaScript 2021.
- Joe Zhou on [type safety across the full stack](https://www.conf42.com/JavaScript_2024_Joe_Zhou_76_typesafety_fullstack) at Conf42 JavaScript 2024.

[Watch Abdu Códigos's talk](https://www.conf42.com/Enterprise_Software_2021_Abdu_Cdigos_typesafe_web_development_eta)

## From Kulkul Technology

Kulkul Technology is the software company Abdu founded and the team behind this talk.

- Kulkul Technology: [kulkul.tech](https://kulkul.tech)

[Watch the talk on YouTube](https://youtu.be/xGcQK0VCngI).

## Watch the talk

[Enjoy Typesafe Web Development with Eta](https://www.conf42.com/Enterprise_Software_2021_Abdu_Cdigos_typesafe_web_development_eta) at Conf42 Enterprise Software 2021.
