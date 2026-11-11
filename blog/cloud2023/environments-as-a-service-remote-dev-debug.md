# When QA has less than one environment, give everyone their own

Conf42 Blog, 2023-03-31. https://www.conf42.com/blog/cloud2023/environments-as-a-service-remote-dev-debug

In short: Sorin Dumitrescu (Bunnyshell) at Conf42 Cloud Native 2023 on environments as a service, from Docker Compose to remote development and debugging in Kubernetes

Some QA engineers shift their working hours just to get the shared test environment to themselves. At Conf42 Cloud Native 2023, Sorin Dumitrescu, VP of Engineering at Bunnyshell, argued that the fix is self-service, production-like environments on demand: one per feature, per pull request or per developer, with remote development and debugging inside the Kubernetes container so the feedback loop shrinks from a pipeline run to a file save.

The first half is about the problem and is product-neutral. The second half is a Bunnyshell demo.

## What does the status quo cost?

He breaks it down by role. Software engineers work against simulated dependencies on their laptops, so integration bugs surface late, a ticket gets filed with all the context, and the fix comes back after the developer has lost focus. Limited laptop resources mean partial environments that perform badly, and keeping the local setup working eats time nobody tracks.

QA engineers get too few environments. "Or in many teams, it's less than one because they share an environment," Sorin Dumitrescu said at Conf42 Cloud Native 2023. Shared environments rush exploratory testing, drift out of sync, and bundle unrelated features together, which makes isolating a strange bug harder. The results are long testing queues and blocked releases.

His point is that this used to be treated as the cost of doing business, and it no longer has to be: containers and orchestration that works at scale make per-change environments practical.

## What does the solution look like?

Five properties, in his framing:

- **Self-service**, so developers stop depending on DevOps engineers for pre-production systems and DevOps can focus on production.
- **On-demand environments**, as many as needed.
- **Preview environments**, so code and UI get reviewed on a running instance.
- **Remote development**, code running in a Kubernetes container that reflects changes in real time, with your usual IDE and debugger.
- **Cost-consciousness**, only running the environments you need.

The before-and-after is the feedback loop. Before: code, commit, push, build, deploy, preview, and repeat when it fails. "I know you feel like life is going past you when you wait for a pipeline to finish with fingers being crossed," he said; Bunnyshell calls that idle time. After: code and see the change live, then commit.

The benefits he lists follow: more time for architecture, code and automated tests; no QA bottleneck; one broken feature no longer blocks unrelated ones; better reviews, because reviewers can use the change rather than read it; earlier stakeholder feedback; and onboarding on a working copy of the product rather than a half-broken local setup.

## What does the demo show?

He creates an environment in Bunnyshell from a GitHub repo containing a Docker Compose file: a Node.js backend, PostgreSQL with a persistent volume, and a React frontend that takes the backend URL as a build argument. Kubernetes manifests, Helm charts and Terraform modules work too, mixed within one environment. Bunnyshell turns the Compose file into its own YAML environment definition, with hostnames interpolated from an environment-based domain.

He deploys it to a connected dev cluster under a custom URL. Builds are cached, so a redeploy of unchanged components is quick. The settings include availability rules, such as running only from 9am to 6pm Monday to Friday, which is the cost-consciousness point made concrete. From the pipeline view he opens the backend Deployment to see live container logs, Kubernetes events and the deployed manifest, then adds a book through the app and refreshes to show persistence.

## How does remote development work?

From WebStorm, with the Bunnyshell CLI installed and authenticated, he starts a remote development session for the backend with local files: a local path and the remote path inside the container. Bunnyshell changes the pod definition and syncs files with Mutagen, dropping him into a shell in the container, where he runs the dev server. Edit the welcome message in server.js, save, the file syncs, the app restarts, and the browser shows the change.

For debugging he restarts the session with a port forward for the Node.js inspector on port 9229, runs the dev script with the inspect flag, attaches an attach-to-Node.js configuration in WebStorm with the local backend folder mapped to the container path, and hits a breakpoint on the next request: call stack, variables, step over and into, the usual.

## Who should watch

Teams with one shared staging environment and a queue to use it, platform engineers designing preview environments, and developers whose laptops wheeze under a local stack. He notes it is not a CI replacement: it plugs into existing pipelines to give end-to-end tests isolated environments that live only as long as the run. Pair it with [Lucas da Costa on a blueprint for staging environments](https://www.conf42.com/Cloud_Native_2023_Lucas_da_Costa_staging_environments_blueprint_preproduction), [Natalie Lunbeck on ephemeral environments](https://www.conf42.com/Cloud_Native_2024_Natalie_Lunbeck_ephemeral_environments) and [Edidiong Asikpo on closing the developer experience gap](https://www.conf42.com/Kube_Native_2023_Edidiong_Asikpo_closing_developer_experience_gap).

[Watch Sorin Dumitrescu's talk](https://www.conf42.com/Cloud_Native_2023_Sorin_Dumitrescu_environments_aas_improve_dx)

## From Bunnyshell

- [Bunnyshell](https://www.bunnyshell.com/): environments as a service platform for on-demand, preview and remote development environments on Kubernetes.

[Watch the talk on YouTube](https://youtu.be/zSb2KiDKtZY).

## Watch the talk

[Environments as a Service: Increase developer productivity and improve DX](https://www.conf42.com/Cloud_Native_2023_Sorin_Dumitrescu_environments_aas_improve_dx) at Conf42 Cloud Native 2023.
