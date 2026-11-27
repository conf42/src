# Deploy apps to Lambda, not fifty single-purpose functions

Conf42 Blog, 2022-03-30. https://www.conf42.com/blog/golang2022/fiber-on-lambda-apps-not-functions

In short: Savas Ziplies (elipZis) at Conf42 Golang 2022 on running a full Fiber app on AWS Lambda with AWS SAM, one codebase that also runs locally

Serverless tutorials start with one hello-world function, and by function number fifty you are testing a distributed system on your laptop. At Conf42 Golang 2022, Savas Ziplies, Managing Director and founder of elipZis, showed the alternative he calls framework as a service: write an ordinary Go web app with Fiber, run it locally, and let AWS SAM deploy the same code to Lambda as a handful of apps instead of a swarm of functions.

He is upfront that this is not a sales pitch for serverless. His last answer to whether you need it is: try it and find out.

## What is wrong with function-by-function serverless?

Nothing, for small jobs. Savas walks through the native path first: a Google Cloud Function is just an HTTP handler with no main, while AWS Lambda needs lambda.Start and requests proxied in from API Gateway. Then the AWS CLI routine: build for Linux, zip, create an IAM role, create the function, invoke it, rinse and repeat per user story.

His list of pros: quick to start, simple development, an easy single-purpose pattern. His list of cons: the code differs per vendor so you are locked in immediately, single-purpose functions can be too micro-service for an app, local development and testing get tedious once there are dozens of functions with dependencies on each other, and familiar structure such as routing is gone.

## Think in apps, route in your own code

The fix is to keep routing inside the application. His template repository (elipZis/go-serverless on GitHub) has a build folder for provider configuration, a cmd folder where each serverless app lives as a full Go program (an API, a queue handler, a web app), shared code alongside, plus environment files and Docker Compose for local work. Every cmd becomes one configurable Lambda function, so you can start with one app and split out an endpoint later, for example when it needs more memory.

The single point of entry is main.go. It reads a SERVER_ENV variable: on AWS it starts the Lambda handler, anywhere else it starts a normal local Fiber server. AWS's own aws-lambda-go-api-proxy library supplies the adapter that turns the Lambda event back into a Fiber context, and it has adapters for Gin and Echo too. After that line, it is just Fiber development.

## What does AWS SAM do here?

SAM, the Serverless Application Model, models the application rather than the infrastructure. In template.yaml, each app is an AWS::Serverless::Function whose code URI points at its cmd folder, with memory size and timeout set per app (his advice: start low, because low is cheap). One API event with a catch-all proxy path sends every request into the app, so the app does the routing, not API Gateway.

Because the template is CloudFormation underneath, it can also declare an RDS database, SQS queues, DynamoDB or Redis and inject their endpoints as environment variables, so nobody copies URLs out of the console. For extra binaries, his example adds a Chromium build as a versioned Lambda layer for scraping JavaScript-heavy pages. samconfig.toml then holds the deployment settings, with separate profiles for default, dev, staging and production in one file. Savas said at Conf42 Golang 2022: "So you're now deploying apps instead of functions."

## What does it cost you?

The honest part. The ops layer is tied to SAM, though it is swappable for another vendor's tooling. A framework adds boot and execution overhead, which matters when you pay per millisecond of reserved memory. You get no insight into the hardware, and on AWS you cannot set CPU directly: at the time, you got one vCPU per 768 MB of memory, so more CPU means paying for more memory. A runaway invocation with a five-minute timeout and 1 GB reserved bills you for all of it, every time, so monitoring and limits are mandatory. Constantly busy endpoints may be cheaper on warm, classic instances. And you are only as scalable as your smallest resource: Lambda may absorb a marketing spike that your smallest database cannot.

## Who should watch

Go developers with an existing web app who want to try Lambda without rewriting it into functions. Teams already deep into Lambda will find the SAM template walkthrough and the cost caveats the most useful parts.

## Related Conf42 talks

- Thorsten Hans on [serverless WebAssembly with Go](https://www.conf42.com/Golang_2024_Thorsten_Hans_serverless_webassembly) at Conf42 Golang 2024.
- Gunnar Grosch on [chaos for serverless with AWS Fault Injection Simulator](https://www.conf42.com/Chaos_Engineering_2022_Gunnar_Grosch_serverless_aws_fault_injection_simulator) at Conf42 Chaos Engineering 2022.
- Luciano Mammino on [writing Lambdas in Rust](https://www.conf42.com/Cloud_Native_2023_Luciano_Mammino_lambdas_rust) at Conf42 Cloud Native 2023.

[Watch Savas Ziplies's talk](https://www.conf42.com/Golang_2022_Savas_Ziplies_serverless)

## From elipZis

elipZis is the software company Savas founded and runs. The serverless template from the talk is on GitHub as elipZis/go-serverless.

- elipZis: [elipzis.com](https://elipzis.com)
- The go-serverless template: [github.com/elipZis/go-serverless](https://github.com/elipZis/go-serverless)

[Watch the talk on YouTube](https://youtu.be/dO6hM1PsyZk).

## Watch the talk

[Go Serverless!](https://www.conf42.com/Golang_2022_Savas_Ziplies_serverless) at Conf42 Golang 2022.
