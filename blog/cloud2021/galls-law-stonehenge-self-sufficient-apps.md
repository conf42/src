# Grow a monolith until it hurts, then build a Stonehenge

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/galls-law-stonehenge-self-sufficient-apps

In short: Fabricio Buzeto (bxblue) at Conf42 Cloud Native 2021 on Gall's law, stretching simple systems, and splitting a Rails monolith into self-sufficient apps

Fabricio Buzeto, CTO of bxblue, used his Conf42 Cloud Native 2021 talk to apply Gall's law to startup architecture: every complex system that works evolved from a simple one that worked, and one designed complex from scratch never does. His evidence is two companies he helped build, one stretched from 1,000 tweets a day to a million, the other grown from a landing page into what he calls a Stonehenge: a ring of self-sufficient, context-focused applications.

## What does Gall's law actually say?

John Gall's 1975 book Systemantics gives the rule its two halves. A working complex system evolved from a simple working one. And a simple system may or may not work, so you need to know what working means. For Buzeto, software works when it fulfils its purpose, and for most software that purpose is business and the client is a user with a problem. He uses John Conway's Game of Life as the picture: three rules, mostly dead starting states, and occasionally something complex and beautiful.

## How far can you stretch a simple stack?

His first case is Qualcanal, a social TV analytics startup he joined in 2012 that read the Twitter stream about TV shows and turned it into insight. The first stack was Twitter's API, Django and MySQL at about 1,000 tweets a day. Twitter's API limits pushed them to the DataSift firehose, and at 10,000 tweets a day with peaks of 5,000 an hour the application froze.

A rewrite was not on the table, so they scaled what they had: more Django instances, then more MySQL, reaching 100,000 tweets a day with peaks of 15,000 a minute, until the database and code base were about to become unmaintainable. Only then did they move to Apache Storm and Cassandra, migrating one metric at a time over six months while the old application kept running. They ended above a million tweets a day with peaks of 50,000 a minute, and load stopped being an issue. The lesson he took: stretch the architecture as far as you can until it hurts.

## Why start bxblue as a monolith?

At bxblue the first MVP was an Unbounce landing page pointing to a Google Doc. Then came a Rails application, Pipedrive for the client pipeline, and MongoDB. Each step changed the architecture a little and answered one question: will users want to migrate their loans, how are loans sold, how can we do it faster, how can we do it properly.

"Monoliths are simple to develop, simple to test, simple to deploy and simple to use," Fabricio Buzeto said at Conf42 Cloud Native 2021. He is honest about the drawbacks, citing Chris Richardson: monoliths get hard to scale in tests, team, deploys, stack and changes. bxblue's Rails app talked to more than 15 external services, and going asynchronous with Sidekiq let it scale fast.

## Don't trust yourself, trust the machine

What made that safe, he argues, was automating everything: tests, code quality, deploys and monitoring. At bxblue that meant RSpec, FactoryBot and VCR for tests, SimpleCov, RuboCop, Reek and Brakeman for quality, Knapsack for test speed, LayerCI, GitHub and Heroku for delivery, and Sentry, New Relic, Logentries and Metabase for monitoring. If tests are slow, people stop running them; if a machine can check it, reviewers shouldn't.

## What is a Stonehenge?

bxblue's pain was never user load. It was context: user journeys, content marketing, landing pages, ETL, event handling and data analysis all piling into one monolith and slowing development. He lays out the options: microservices, DHH's Citadel (a big monolith with small specialised services around it) and Nitesh Gupta's macroservices.

bxblue's answer was to build each new context as its own application rather than another module, starting with a back office and then anti-fraud, each with its own MongoDB and Sidekiq. Integration with the legacy monolith was easy and development was fast, so they kept going to more than six applications. The Stonehenge is his name for the result: simple, self-sufficient, context-focused, service-enabled applications that each work alone but can integrate with the others.

He doesn't claim it removes complexity. Larry Tesler's law of conservation of complexity says it has to go somewhere. What he wants to avoid is dead code: he cites research finding around 30% of files unused, and CB Insights data that 70% of startups fail. Build only what serves the purpose.

## Who should watch?

Startup CTOs and early engineers under pressure to adopt microservices before they have the problems microservices solve. It is a short, opinionated architecture talk with real numbers from two companies.

## Related Conf42 talks

- Daniil Koshelev on [monolith to microservices transitions](https://www.conf42.com/DevSecOps_2024_Daniil_Koshelev_monolith_microservices_transitions) at Conf42 DevSecOps 2024.
- Maksim Zemskov on [the glorious monolith and micro-frontends](https://www.conf42.com/JavaScript_2023_Maksim_Zemskov_glorious_monolith_scaling_application_microfrontends) at Conf42 JavaScript 2023.
- Daniel Paulus on [weekly releases at a small startup](https://www.conf42.com/DevOps_2024_Daniel_Paulus_releases_weekly_small_startup) at Conf42 DevOps 2024.

[Watch Fabricio Buzeto's talk](https://www.conf42.com/Cloud_Native_2021_Fabricio_Buzeto_stonehenge_galls_law), part of [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From bxblue

bxblue is the Brazilian loans startup where Fabricio Buzeto is CTO, and the company behind the Stonehenge architecture in this talk.

- [bxblue website](https://bxblue.com.br)

[Watch the talk on YouTube](https://youtu.be/sNOP42Jb6XY).

## Watch the talk

[Building the Stonehenge using Gall’s law](https://www.conf42.com/Cloud_Native_2021_Fabricio_Buzeto_stonehenge_galls_law) at Conf42 Cloud Native 2021.
