# Microservices broke the inner loop, so move it into the cluster

Conf42 Blog, 2022-10-19. https://www.conf42.com/blog/kubenative2022/microservices-broke-the-inner-loop

In short: Arsh Sharma (Okteto) at Conf42 Kube Native 2022 on why microservices made local dev miserable and how cloud dev environments restore hit-save feedback.

We split the monolith to make production scale, and quietly made every developer's afternoon worse. At Conf42 Kube Native 2022, Arsh Sharma, a DevEx engineer at Okteto and a contributor to the Kubernetes project, makes that case in a short, sharp talk: CI pipelines and staging environments never fixed the inner development loop, and the fix is to develop inside a Kubernetes cluster using the same manifests as production.

It's a vendor talk from a company that builds exactly this, and Arsh doesn't hide it. But most of its 15-odd minutes is a clear diagnosis of a problem every microservices team recognises, told through one developer called Jane.

## What actually broke when the monolith went away?

A couple of years earlier, Jane's loop was simple: open the editor, run a command or two, write code, hit save, see the change, open a pull request. Then containers became the norm, the monolith became microservices, and Kubernetes ran them in production.

Now Jane has two bad options. She can run the one service she is changing on its own, which tells her nothing about how it talks to the rest. Or she can bring up the whole application locally, which means reading READMEs written by the infra team and running bash scripts that break and need debugging of their own. With two or three services that's tolerable. With ten or fifteen it isn't.

And even after all that effort, Arsh points out, local still isn't production: the way services come up on a laptop is not the way they come up in the production cluster, so Jane still can't be sure her change behaves the same there.

## Why CI and staging didn't save Jane

The industry's answer was to push verification later: work on one service locally, push, and let the CI pipeline or a shared staging environment tell you if it works. Arsh's objection is distance. That feedback arrives only after commit and push, and bringing up an environment in CI can take minutes, or hours for a big application.

He's careful not to throw them out. CI and staging keep their place; they just sit too far from the moment the code is written to serve as the inner loop.

## How does a cloud development environment work?

The mechanism is the most useful part of the talk. Take a toy movies app with a frontend and an API:

1. Deploy both services to a Kubernetes cluster with the same manifests you use in production.
2. Replace the running API container with a development container.
3. That container syncs your local code into the cluster, so you see the result as soon as you hit save.

Because the dev container inherits the original container's configuration, the rest of the application keeps working as before. You edit in your own IDE; the code runs in a production-shaped environment.

## What you get for it

Arsh groups the payoff into three points:

- **Mirror production.** Same manifests, so the bugs that usually surface late in the cycle, the ones you couldn't reproduce locally, show up before you push.
- **Instant feedback.** No build, commit, push and wait for CI; save and look.
- **One-time configuration.** The dev environment lives in a single file, every developer brings up the whole app with one command, and a broken environment gets destroyed and recreated in minutes.

That first point carries the most weight. "Working in an environment which doesn't mimic production is the most common cause of bugs which creep in late in the dev cycle and are hard to debug," Arsh Sharma said at Conf42 Kube Native 2022.

He adds two smaller benefits: you're no longer limited by your laptop's resources, and you don't have to give up your tools. His closing line sums up the pitch: "If everything is happening in the cloud, then why should your dev environments not be there too?"

## Who should watch

Platform and DevEx engineers who have to justify why developers need something better than a docker-compose file and a prayer. It's an introduction, not a hands-on demo: there's no CLI walkthrough or numbers from a real rollout, so if you already run remote dev environments you'll know most of it. If your team still waits on staging to find out whether a change works, it's 15 minutes well spent.

For more on the same problem, see [Edidiong Asikpo on closing the developer experience gap](https://www.conf42.com/Kube_Native_2023_Edidiong_Asikpo_closing_developer_experience_gap) at Conf42 Kube Native 2023 and [Anita Ihuman on remocal development for Kubernetes](https://www.conf42.com/Kube_Native_2024_Anita_Ihuman_local_machine_mirror_dev_environment) at Conf42 Kube Native 2024.

[Watch Arsh Sharma's talk](https://www.conf42.com/Kube_Native_2022_Arsh_Sharma_shifting_microservices) from [Conf42 Kube Native 2022](https://www.conf42.com/kubenative2022).

## From Okteto

Okteto builds cloud development environments for Kubernetes applications, the approach Arsh describes in the talk: deploy with your production manifests, swap in a dev container, sync code on save.

- Okteto: [okteto.com](https://www.okteto.com/)

[Watch the talk on YouTube](https://youtu.be/vi8EJ1vflf0).

## Watch the talk

[Did We Actually Make Developers Happy by Shifting to Microservices?](https://www.conf42.com/Kube_Native_2022_Arsh_Sharma_shifting_microservices) at Conf42 Kube Native 2022.
