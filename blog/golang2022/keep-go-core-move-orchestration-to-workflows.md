# Keep the Go services stable, move the business glue into a workflow

Conf42 Blog, 2022-04-01. https://www.conf42.com/blog/golang2022/keep-go-core-move-orchestration-to-workflows

In short: Walter Demian Schroeder (Globant) at Conf42 Golang 2022 on keeping core logic in Go microservices and orchestrating business processes as workflows

One client wants order status from your public endpoint, another wants a webhook, a third wants a file over SFTP. Walter Demian Schroeder, Go Developer Architect at Globant, argued at Conf42 Golang 2022 that the worst answer is a pile of conditionals in your Go services, and the better one is to keep the core in Go and hand the orchestration of each business process to a workflow layer that a dedicated team can change at any time.

A note on scope before you press play: despite the title, there is almost no Go on screen. It is a short architecture talk with a demo of Google Cloud's workflow service, and its value is the argument for where business logic should live.

## Why do integrations rot?

His example is a ride-hailing app. A passenger requests a trip and pays; a driver gets notified, accepts and bills for the trip. Simple, until you draw every subsystem, every microservice and every external system it touches.

Then take one requirement, telling a client the status of an order, and watch it fork into three implementations depending on the client. You can build all of them into the integration, a branch per case, and end up with a big custom solution for everyone. With new integrations arriving constantly on top of rapid updates, that code gets harder to maintain until someone has to rework it to make it small and stable again. Workflows are his way to prevent that, or at least slow it down.

## Where does the workflow layer sit?

Schroeder's team practice comes first. Understand the business areas and organise teams around them, so a new requirement goes to the team whose area it touches, and that team can size it and decide which microservices change, or whether a new one is needed at all.

That decoupling raises the integration question. Every process starts from a trigger: a schedule, a data change, a user action. You can wire the steps together by hand through a message broker or direct API calls, but without good documentation those links become hard to maintain, and it takes time just to find who owns each one.

"Using a workflows tool we can create a flow of the business process using existing microservices started by an event trigger or a batch schedule," Walter Demian Schroeder said at Conf42 Golang 2022.

The split he proposes:

- **Go services keep the core functionality**, the part that needs Go's performance and benefits from staying stable.
- **A workflow layer owns the orchestration**: each step defined, full visibility of what is happening, changeable whenever a case needs it.
- **A specific team owns the workflows**, making sure requirements are met and that microservices are integrated the same way everywhere.

He adds two side benefits. The business gets a readable picture of each process when it asks for new functionality, and some workflow tools integrate directly with databases and third-party applications, which cuts development time for those steps.

## What does the demo show?

He builds a workflow in Google Cloud. Creating one asks for a name, a description, a deployment region, a service account and an optional trigger. The first definition calls a dummy URL, sets some values and returns a message, written in YAML and then shown again as the same logic in JSON.

The second branches on the date: one message on Fridays, another at weekends, a third for the working week. He runs it with logging off (one switch turns on per-step detail for debugging), and since it is Tuesday it reports a working week, with the execution detail underneath.

The third version takes the current day and searches Wikipedia for related entries, returning a list of results. As the definition grows, the console draws a diagram of every step and branch beside the code, which is the part that makes his maintainability point: you can see what a process does without reading the services behind it.

## Who should watch

Architects and tech leads whose Go services have started sprouting per-client branches, and teams weighing a managed workflow service against hand-rolled broker choreography. It is short and conceptual; if you want depth on durable execution or failure handling, pair it with one of the talks below.

## Related Conf42 talks

- Oskar Neumann on [modern application architecture with AWS Step Functions](https://www.conf42.com/Cloud_Native_2023_Oskar_Neumann_modern_application_architecture_aws_step_functions) at Conf42 Cloud Native 2023.
- David Joyce on [scalable data pipelines with Argo Workflows](https://www.conf42.com/Kube_Native_2022_David_Joyce_scalable_data_pipelines_argo_workflows) at Conf42 Kube Native 2022.
- Siri Varma Vegiraju on [Dapr workflows and failure](https://www.conf42.com/Cloud_Native_2025_Siri_Varma_Vegiraju_workflow_dapr_failure) at Conf42 Cloud Native 2025.

[Watch Walter Demian Schroeder's talk](https://www.conf42.com/Golang_2022_Walter_Demian_Schroeder_workflows)

## From Globant

Globant is a digitally native technology services company; Schroeder works there as a Go architect.

- [Globant](https://bit.ly/3pYFWRA)

[Watch the talk on YouTube](https://youtu.be/inPkJkPBfas).

## Watch the talk

[Go with Workflows](https://www.conf42.com/Golang_2022_Walter_Demian_Schroeder_workflows) at Conf42 Golang 2022.
