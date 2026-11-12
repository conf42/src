# 100% coverage, zero assertions, and the mutants that catch it

Conf42 Blog, 2021-03-26. https://www.conf42.com/blog/enterprise2021/mutation-testing-pit-assertionless-tests

In short: Rafał Leszko (Hazelcast) at Conf42 Enterprise Software 2021 on mutation testing with PIT, and why code coverage thresholds get gamed

Rafał Leszko, Cloud Native Team Lead at Hazelcast and formerly of Google and CERN, showed at Conf42 Enterprise Software 2021 how to test your tests without writing more tests. Mutation testing plants small bugs in your production code and checks whether any test fails. With PIT, the Java mutation testing tool, he takes a calculator test with 100% line coverage and no assertions, shows every mutant surviving, then runs the same check on Hazelcast's Kubernetes plugin in CI.

## Why isn't code coverage enough?

He opens with the Mars Climate Orbiter, launched in December 1998 and lost in September 1999 because ground software worked in pounds while the orbiter expected metric units. It cost more than 300 million dollars. Then the smallest possible example: a method returning a plus b, and a test that calls it and asserts nothing. Coverage reports 100% for class, method and line. As Uncle Bob puts it, paraphrased by Leszko, coverage proves you executed every line, not that you tested it.

## What is mutation testing?

Richard Lipton proposed it in 1971 by asking why we write tests at all: to catch bugs. So introduce a bug and see if the suite notices. Change a plus to a minus and you have a mutant. If a test fails, the mutant is killed, which is good; if every test still passes, it survived, and that code is effectively untested.

Real code needs more than one trick, so mutation operators come in families: math changes (plus to minus, multiply to divide), boundary changes (less than becomes less than or equal), negated conditions, removed if statements and method calls, modified return values and constants. A tool generates many mutants across the code base and reports which ones lived.

## What does PIT look like in practice?

PIT runs from the command line, from Maven or Gradle, or as an IntelliJ plugin, which is how Leszko uses it. On the assertion-free calculator test it generates two mutants and kills neither. Write a real test, given two values, when summed, assert the result, and the mutants die. The HTML report is the useful output: a coverage view by package and class, with each line showing how many mutants it produced and whether they were killed.

The bigger demo is the Hazelcast Kubernetes plugin, around 5,000 lines in twelve classes. Adding PIT took one Maven profile. A GitHub Action runs mutation coverage on every push to master, about two and a half minutes in his run, and publishes the report to GitHub Pages, where he points at a whole method no test catches when its return value is replaced.

## Why did it take 41 years to catch on?

Two problems kept mutation testing academic. The first is equivalent mutants: changes that don't alter behaviour, so no test can kill them, which shows up as noise. PIT doesn't solve that, but it disables by default the operators most likely to produce them. The second is speed: every mutant times every test is a lot of runs. PIT first runs normal coverage to learn which tests touch which lines, then runs only those tests against each mutant. That is the trick that made it practical.

## What should teams do with the score?

The best story is from his investment banking days, on a team spread across the US, Kraków and Hyderabad, with a hard requirement of 100% coverage. Leszko kept stalling at 95% because a module's main class can't be unit tested on its own. He went to see how another team had reached 100% and found tests with given and when, and no assertions at all.

"But the moral of the story is that the test coverage threshold doesn't make any sense, because if you do it for your project, people will try to work around it if they need to," Rafał Leszko said at Conf42 Enterprise Software 2021. His alternative: run PIT in the CI/CD pipeline and review the HTML report as a team every week or two, as a way to pay down technical debt rather than a gate. He notes it has been used at CERN and in Norway's voting system.

## Who should watch?

Java developers and leads who own a coverage target, and anyone who suspects their green build is greener than it should be. It is a compact introduction with two demos; nothing here needs Hazelcast.

## Related Conf42 talks

- Nahuel Garbezza on [Testy, a testing tool for teaching](https://www.conf42.com/JavaScript_2021_Nahuel_Garbezza_Testy_testing_tool_teaching) at Conf42 JavaScript 2021.
- Gil Zilberfeld on [TDD with legacy code](https://www.conf42.com/Python_2022_Gil_Zilberfeld_TDD_legacy_code) at Conf42 Python 2022.
- Joe Skeen on [learning to love unit testing](https://www.conf42.com/DevOps_2024_Joe_Skeen_love_unit_testing) at Conf42 DevOps 2024.

[Watch Rafał Leszko's talk](https://www.conf42.com/Enterprise_Software_2021_Rafa_Leszko_mutation_testing_pit), part of [Conf42 Enterprise Software 2021](https://www.conf42.com/enterprise2021).

## From Hazelcast

Hazelcast, where Rafał Leszko leads the cloud native team, makes the Hazelcast in-memory data grid for distributed computation and caching, Hazelcast Jet for stream processing, and Hazelcast Cloud, Hazelcast as a service. Its Kubernetes plugin is the demo code base here.

- [Hazelcast website](https://hazelcast.com)

[Watch the talk on YouTube](https://youtu.be/a9R9FRnkLu4).

## Watch the talk

[Mutation Testing with PIT](https://www.conf42.com/Enterprise_Software_2021_Rafa_Leszko_mutation_testing_pit) at Conf42 Enterprise Software 2021.
