# Your APM finds the crime scene, not the line of code

Conf42 Blog, 2021-10-28. https://www.conf42.com/blog/js2021/lightrun-logs-without-a-redeploy

In short: Shai Almog (Lightrun) at Conf42 JavaScript 2021 on adding logs, snapshots and metrics to running Node.js servers instead of a redeploy cycle

A dashboard can tell you that a web service is slow or failing; it cannot tell you why, or which line. At Conf42 JavaScript 2021, [Shai Almog](https://www.conf42.com/JavaScript_2021_Shai_Almog_Debug_NodeJS_Lightrun), Developer Advocate at Lightrun, describes the loop most teams fall into after that point, add a log, go through CI/CD and QA, wait for the bug to happen again, and shows Lightrun injecting logs and snapshots into running Node.js and Java servers instead.

He starts by saying he loves APMs, and means it: he remembers checking a server by kicking it and listening for the hard drive.

Shai Almog said at Conf42 JavaScript 2021: "We're truly at the golden age of monitoring hell."

## Why don't logs and debuggers solve this already?

Logs only help if you knew in advance where the bug would be, and you cannot log everything without the bill and the performance going through the roof. He compares the decision to writing comments: noise today, or a lifesaver at 2am. A missing log means hours through the pipeline and a reproduction with fingers crossed, then rinse and repeat.

Debuggers have the right features, breakpoints, stack traces, variables, but they were not built for production. Remote debugging is insecure, a breakpoint blocks the server, an expensive condition can take it down, and a debugger attaches to one machine when the bug may appear on a random node of a polyglot cluster. Then there is the line between developers and ops, drawn for good reason: developers with direct production access did not end well. Ops can see the alarm but often cannot fix a developer's bug.

## How does Lightrun keep developers out of production?

The developer works in an IDE plugin (WebStorm and IntelliJ IDEA at the time, with a Visual Studio Code plugin announced; there is also a command line). Actions go to a management server, which forwards them to a small agent running inside the service, and results flow back to the IDE. Developers never touch production directly, so the ops line holds. Setup for Node.js is an npm install of the agent plus a snippet with your Lightrun secret at the top of the main file.

There are three kinds of action. A **snapshot** works like a breakpoint, capturing the stack and variables without stopping the process. A **log** is added at runtime, without a restart, and is merged into your existing logs so you read it in context. A **metric** counts line hits or times a block or method, and can go to Prometheus or StatsD, which fills the gap where an APM names the slow entry point but not the slow block. He notes metrics were available for JVM languages only at the time, with Node.js and Python promised.

## The to-do app bug

The demo is the classic to-do app, a Node.js front end and part of the back end, with storage in Spring Boot. He stumbled on a real bug while preparing: clear completed did nothing. A snapshot on the Node.js handler showed the method was reached; an injected log showed it finished without an exception. On the Java side, a log with an expression printing the size of the response list said two items came back. Changing it to print the first element showed the completed field was false on the server. The cause: the Node.js code that should toggle that field was never written, so it was only ever set on creation.

Note the expression detail: he printed the list's size, not the list. Expressions run in a sandbox with a limit on operations, so an expensive one may be dropped instead of eating the CPU.

## What about safety and privacy?

His closing list: actions run in a sandbox so they cannot change the program's state; the agent pulls from the server, not the other way round as with JDWP, so services can stay behind firewalls; PII redaction rules can mask patterns such as card numbers before they reach logs; blocklists can stop developers placing actions in particular files, classes or methods, for example where passwords live. It runs as cloud or on-premise, on containers, microservices or serverless, and supports JVM languages, Node.js (JavaScript and TypeScript) and Python.

## Who should watch?

Node.js and Java developers who have redeployed just to add one log line, and platform teams deciding how much production access developers should get. It is a product demo, but the to-do bug walkthrough is a good lesson in validating assumptions one step at a time.

## Related Conf42 talks

- Shai Almog again on [a polyglot cloud-native debugger beyond the APM](https://www.conf42.com/Python_2022_Shai_Almog_polyglot_cloudnative_debugger_beyond_apm) at Conf42 Python 2022.
- Finbar Fleming on [debugging errors in production](https://www.conf42.com/JavaScript_2022_Finbar_Fleming_debugging_errors_in_production) at Conf42 JavaScript 2022.
- Elinor Sapir on [debugging differently](https://www.conf42.com/Cloud_Native_2023_Elinor_Sapir_debugging_debugging_differently) at Conf42 Cloud Native 2023.

[Watch Shai Almog's talk](https://www.conf42.com/JavaScript_2021_Shai_Almog_Debug_NodeJS_Lightrun), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Lightrun

Lightrun makes the production debugging tool shown in the talk: logs, snapshots and metrics added to running services from the IDE.

- [Lightrun website](https://lightrun.com/)

[Watch the talk on YouTube](https://youtu.be/lqLu5VhF-_0).

## Watch the talk

[Debug NodeJS Applications in Production with Lightrun](https://www.conf42.com/JavaScript_2021_Shai_Almog_Debug_NodeJS_Lightrun) at Conf42 JavaScript 2021.
