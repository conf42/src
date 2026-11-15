# Blue/green on AWS with Lambda@Edge, cookies and a cache that cooperates

Conf42 Blog, 2025-11-10, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/blue-green-on-aws-with-lambda-edge

In short: Rayenn Hamrouni of Lenstra at Conf42 DevSecOps 2025 on cookie-based blue/green routing with Lambda@Edge, SSM and CloudFront caching.

Rollbacks that take ages are the tax you pay for release days you dread. At Conf42 DevSecOps 2025, Rayenn Hamrouni, DevOps Engineer at the Paris cloud consultancy Lenstra, showed how his team built cookie-based blue/green deployments at the edge with Lambda@Edge, and then made it survive CloudFront caching. Since adopting it, he reports zero production incidents during releases and promotions or rollbacks in under a minute.

This is a field report from a client project, which makes it one of the more hands-on talks of the event.

## The starting point was ordinary

The architecture is textbook AWS: CloudFront serving a static front end from S3 and forwarding API calls to an Application Load Balancer in front of ECS on Fargate. It looked fine on a diagram, but production releases kept causing incidents, rollbacks were slow and painful, and deployments sometimes meant downtime.

Blue/green fixes that in principle: two identical environments, test the new release on green, switch traffic, flip back if it breaks. Rayenn is upfront about the costs too: you run two environments for a while, state and database schema changes need careful thought (his project had no database to manage, which helped), and routing gets more complex.

## Five ways to switch, one that fit

He walks through the AWS options before revealing the one they picked:

- **Route 53**, including weighted routing. Simple and works with any architecture, but DNS caching means the switch is never instant and you cannot route per request.
- **API Gateway**, flexible per header or cookie, but no help for a static S3 front end.
- **ALB weighted target groups**, fast to switch and roll back, again no S3 and less routing logic.
- **CodeDeploy**, a full blue/green workflow with health checks and automatic rollback, at a real setup cost.
- **Lambda@Edge**, functions that run in CloudFront edge locations and can rewrite the origin or S3 prefix before a request hits your backend.

They chose Lambda@Edge for per-user control and low latency.

## Cookies decide who sees which colour

Each colour gets its own ALB and ECS cluster, and the front ends live under different prefixes in the same bucket. A cookie, holding something hard to guess like the release commit hash, pins a user to a version so they do not bounce between releases mid-session. No cookie, or a full reload of the app, assigns the currently active release. A developer override cookie always wins, so QA can force a version in their browser.

The catch: changing the active version in the function code meant redeploying Lambda@Edge to every edge location, which is slow and unpredictable. Iteration two moved the active version to SSM Parameter Store and cached it in memory for a short time, so a switch is a parameter change, not a deploy.

## Make the cache work for you

The best part of the talk is the caching explanation. CloudFront has four hook points (viewer request, origin request, origin response, viewer response) and the cache sits between viewer and origin. If an object is cached, the origin hooks never run, so where you put your logic decides whether blue/green works at all.

Their final flow: at viewer request, a developer cookie injects a unique identifier to bypass the cache. On a miss, origin request routes to the right prefix using the cookie or the active release from SSM. Origin response sets the release cookie when the app loads. Every switch triggers a cache invalidation, so the next load reaches the origin hooks and gets assigned correctly. Getting caching right is half the design here.

He flags what the talk leaves out: coordinating colours across multiple backends and databases, progressive rollout to a subset of users, and CI/CD automation of promotion and rollback.

## Who should watch

Anyone running a CloudFront-fronted app on AWS who wants safer releases without adopting a full deployment platform. If your stack is all API Gateway or ALB, the comparison of options is still useful.

## Related talks

- [Your Rollback Is Untested and You Will Find Out at 3am](https://www.conf42.com/MLOps_2026_Artemis_Leonardou_rollback_untested_3am) by Artemis Leonardou.
- [Designing Staging Environments: A Blueprint for Pre-production](https://www.conf42.com/Cloud_Native_2023_Lucas_da_Costa_staging_environments_blueprint_preproduction) by Lucas da Costa.

[Watch Rayenn Hamrouni's talk](https://www.conf42.com/DevSecOps_2025_Rayenn_Hamrouni_deployments_aws)

[Watch the talk on YouTube](https://youtu.be/5e2GLJX8IQ8).

## Watch the talk

[From Blue to Green Without Seeing Red: Mastering Deployments on AWS](https://www.conf42.com/DevSecOps_2025_Rayenn_Hamrouni_deployments_aws) at Conf42 DevSecOps 2025.
