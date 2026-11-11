# A 202 Accepted proves nothing, so Form3 load tests the queue

Conf42 Blog, 2022-03-31. https://www.conf42.com/blog/golang2022/f1-load-testing-async-in-go

In short: Adelina Simion and Andy Kuszyk (Form3) at Conf42 Golang 2022 on F1, their open source Go load tester for asynchronous systems

When a payments API answers 202 Accepted, the real work has barely started. Adelina Simion, Tech Evangelist, and Andy Kuszyk, Head of International Engineering, both at Form3, used their Conf42 Golang 2022 talk to show F1, the open source load testing tool Form3 wrote because neither JMeter nor k6 could easily test an asynchronous system, write tests in Go, or push load hard enough.

The first half is a crisp primer on performance testing; the second is a live demo in which Kuszyk builds a service, an SQS mock and a load test from an empty folder.

## Load, spike or soak?

Simion sets the vocabulary. Performance testing checks stability, scalability and reliability, and starts with your business needs, so you know what good looks like. For a high-volume payments platform it also means testing against anticipated future load to see the growth runway.

Load tests tell you how many concurrent users or transactions the system handles, and different scenarios need different tests.

"Load tests should be performed all the time in order to ensure that your system is always on point, which is why it should be integrated into your continuous integration cycles," Adelina Simion said at Conf42 Golang 2022.

Stress tests probe the upper limits and look for memory leaks, slowdowns, security issues and data corruption. A sudden ramp-up is a spike test; a slow ramp over a long period is a soak test. Run them before your Black Friday. And before any of it, have monitoring and a failure threshold agreed: average and peak response time, error rate, concurrent users, throughput, CPU.

## Why weren't JMeter and k6 enough?

Form3's systems lean on events, queues and asynchronous processing. The example service exposes one payments endpoint, does background work, and publishes to an SQS queue when it finishes. The 202 makes the request look instant, so a useful test has to connect each request to its eventual message.

JMeter, the open source Java tool, configures tests through a recording GUI and templates, handles async with long polling or follow-up requests, and needs a plugin for step and spike ramp-ups. k6, the open source Go project run by Grafana, uses JavaScript-like scripts with no support for promises or asynchronous execution, working around it with virtual users. Form3 used k6 first. But its platform is entirely Go, writing async tests in JavaScript was awkward, and k6's single mode (a pool of virtual users) wasn't aggressive enough for some cases. So they wrote their own and open-sourced it.

## How does F1 work?

F1 is a Go package, not a separate binary you feed scripts to. You create the F1 type in your own main function, call execute, and you get a full command line interface. Then you register scenarios. Each scenario function runs setup code once and returns a run function that executes on every iteration; at 100 iterations a second, it runs 100 times a second. Its testing type looks much like Go's own testing.T.

That is where Go pays off. In Kuszyk's demo, the setup creates an SQS client against goaws (a local SQS mock in Docker Compose) and starts a goroutine that polls the queue and pushes messages into a channel. Each iteration then posts to the payments endpoint, checks for a 202, and waits up to 10 seconds for a message on the channel, failing if none arrives. In real tests Form3 matches the message to the request by IDs carried through the background processing.

## Why does the load mode matter?

The demo's two runs show the difference. Constant mode at one iteration per second for 10 seconds: each takes about 1.5 milliseconds and passes. A pool of one virtual user instead: close to 1,000 requests per second, each taking three or four milliseconds, because the user fires again the moment it finishes.

Kuszyk's point is what happens when virtual users saturate. Ten users waiting 2 seconds each on an async process can only deliver five requests per second, however much you want ten. Constant mode ignores users and applies the rate you asked for, which is a big part of why they built F1.

## How does Form3 use it?

Every day, Kuszyk says, sending hundreds or thousands of synthetic payments per second into pre-production environments, where it catches bottlenecks and scalability problems well before production.

"It shouldn't be an afterthought and it should be part of the way you're developing your applications," Andy Kuszyk said at Conf42 Golang 2022.

## Who should watch

Go teams testing anything with a queue in the middle, and anyone whose k6 virtual users run out before the target rate does. The primer is useful on its own for people new to load testing. Code for the demo is in the f1-example repo.

## Related Conf42 talks

- Hari Krishnan on [shift-left performance testing](https://www.conf42.com/Site_Reliability_Engineering_2021_Hari_Krishnan_shift_left_performance_testing) at Conf42 SRE 2021.
- Kaye Alvarado on [a load testing pipeline](https://www.conf42.com/DevOps_2024_Kaye_Alvarado_loadtesting_pipeline) at Conf42 DevOps 2024.
- Samir Akarioh on [load testing and optimisation with Gatling](https://www.conf42.com/JavaScript_2024_Samir_Akarioh_61_loadtesting_optimization_gatling) at Conf42 JavaScript 2024.

[Watch Adelina Simion and Andy Kuszyk's talk](https://www.conf42.com/Golang_2022_Adelina_Simion_Andy_Kuszyk_load_testing_f1)

## From Form3

Form3 is a payments technology provider with an all-Go codebase; at the time of the talk it had around 260 employees, about 130 of them engineers, and was fully remote. F1 lives in its open source organisation.

- Form3: [form3.tech](https://www.form3.tech/)
- F1 on GitHub: [github.com/form3tech-oss/f1](https://github.com/form3tech-oss/f1)
- Demo code: [github.com/form3tech-oss/f1-example](https://github.com/form3tech-oss/f1-example)
- Form3 engineering: [engineering.form3.tech](https://engineering.form3.tech)

[Watch the talk on YouTube](https://youtu.be/yKJ_h0K6liM).

## Watch the talk

[Load testing with F1](https://www.conf42.com/Golang_2022_Adelina_Simion_Andy_Kuszyk_load_testing_f1) at Conf42 Golang 2022.
