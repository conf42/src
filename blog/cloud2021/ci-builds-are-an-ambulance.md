# A CI build is an ambulance, not a race car

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/ci-builds-are-an-ambulance

In short: Zan Markan (CircleCI) at Conf42 Cloud Native 2021 on measuring slow builds, then fixing them with resources, test splitting, caching and less scope

The worst build Zan Markan ever worked with didn't just run long; it stayed red for days, maybe weeks, while a queue of finished features waited behind it. At Conf42 Cloud Native 2021, the CircleCI developer advocate used that story to argue that a slow, painful pipeline is a signal to fix rather than bypass, and walked through the fixes in order: measure, add horsepower, go parallel, cache, cut scope, and get the team on board.

The advice is tool-agnostic; the examples use CircleCI configuration.

## The build that wouldn't go green

Around 2015 Markan was on a mobile team doing everything by the book: SOLID, clean architecture, TDD, and functional UI tests agreed with the product manager before any feature was built. Everything was, as far as they were concerned, 100% tested. Then a build failed overnight. He pushed a fix in the morning; it failed again by evening. And again the next day. Releases stopped.

He compares it to the ship that had just blocked the Suez Canal: do you wait, or turn around and sail round Africa, which in CI terms means switching it off and going manual? His answer is to remember why the red light exists: every failing build, however agonising, is still sending you a signal.

## How do you know your builds are too slow?

The obvious case is when someone suggests turning CI off. The usual case is gradual: builds don't slow down overnight, they slow down over months of features and commits. Watch how often builds break, and how long they stay broken; if fixing a build took five minutes a month ago and takes 20 now, find out why. His favourite detector needs no tools at all: the team complains about CI at every retro and every one-on-one.

Then measure. Whole pipeline duration, per-job times, time from red to green, failure rates, and ideally per-test timings to find the slowest and flakiest suites. A spreadsheet will do if nothing else is available. CircleCI's Insights dashboard shows trends over the last 90 days or so, success rates per workflow and, then in preview, per-test data.

## Add horsepower first

The cheapest fix: give jobs more resources. Out-of-memory errors are the clear tell. The subtler one is a build that takes three to five minutes on a developer laptop (his example: an i7 with 16 GB of RAM) and 20 minutes on CI with 2 to 4 GB and fewer cores. In CircleCI that is a resource class setting.

## Go parallel, twice

Run independent jobs at the same time (unit tests, security scans, functional tests) and only move on to build and deploy once they're all green. Then split a single big suite, such as hundreds of functional tests, across parallel containers. His preferred split is by timing data from a previous run, so each container gets roughly equal work.

## Cache what you need and what you build

Markan splits caching in two. What you need: dependencies (anyone who has installed create-react-app knows the npm wait), keyed on the lock file so they are reloaded only when it changes; and custom Docker images with your tools baked in instead of installing them every run. What you build: artifacts reused by later jobs, intermediate build outputs such as Android modules, and Docker layer caching, which reuses every layer up to the first changed instruction.

## Then run less

Once the technical fixes are done, cut scope. In a shopping app, registration and checkout tests must run on every build; profile picture tests can run later or asynchronously. Match workflows to how you work: a subset on feature branch commits, more on merges to main, the full suite on a release tag.

And make CI a team job. DevOps is a cultural movement first, he says, and one person maintaining the pipeline is a bottleneck; a single config file that tells the whole story also makes onboarding easier.

## What is the right build time?

He won't give a number, since it depends on your team and your software, and points to CircleCI's State of Software Delivery report, where time to recovery tends to matter more than raw build time. His closing image is the ambulance: it should go fast, but its job is to arrive with the cargo intact.

"Your signal, your CI CD's cargo, if you will, is the most precious cargo," Markan said at Conf42 Cloud Native 2021. A 5-second build that skips the tests you need is fast and useless.

## Who should watch

Any team whose pipeline has quietly crept past the point of patience. Most of the fixes are known; the value is the order to try them in and the reminder to measure first.

## Related Conf42 talks

- Efi Merdler-Kravitz on [CI/CD in the serverless era](https://www.conf42.com/Cloud_Native_2021_Efi_MerdlerKravitz_cicd_serverless) at Conf42 Cloud Native 2021.
- Matt Jarvis on [continuous security in pipelines](https://www.conf42.com/Cloud_Native_2021_Matt_Jarvis_conunuous_security_pipelines) at Conf42 Cloud Native 2021.
- Ricardo Castro on [CI/CD build and deploy automation](https://www.conf42.com/Cloud_Native_2023_Ricardo_Castro_cicd_builddeploy_automation) at Conf42 Cloud Native 2023.

[Watch Zan Markan's talk](https://www.conf42.com/Cloud_Native_2021_Zan_Markan_need_for_speed_cicd_setup)

## From CircleCI

CircleCI is a CI/CD platform: pipelines defined in one config file in your repository, with jobs, reusable orbs and workflows.

- [circleci.com](https://circleci.com/)

[Watch the talk on YouTube](https://youtu.be/wPMr6j-Dav4).

## Watch the talk

[The Need for Speed (in your CI/CD setup)](https://www.conf42.com/Cloud_Native_2021_Zan_Markan_need_for_speed_cicd_setup) at Conf42 Cloud Native 2021.
