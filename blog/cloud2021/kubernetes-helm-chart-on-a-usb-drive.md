# Kubernetes won't fix a problem you framed wrong

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/kubernetes-helm-chart-on-a-usb-drive

In short: Lian Li (Container Solutions) at Conf42 Cloud Native 2021 on why cloud native transformations fail on culture and problem framing, not on Kubernetes

Lian Li, Cloud Native Engineer and Engineering Manager at Container Solutions in Amsterdam, opened her Conf42 Cloud Native 2021 talk by disappointing both camps in the room: Kubernetes won't save you, and serverless won't either. Her argument is that cloud native transformations stall on two attitudes, towards technology and towards people, and that no orchestrator fixes either.

Her claim is that the problem is culture: how an organisation solves problems, adapts to change and builds trust. The rest of the talk is a consultant's field guide to what that means in practice, with the war stories to back it.

## Has Kubernetes become boring, and is that a problem?

She starts with the state of play. Using a Container Solutions white paper built on Geoffrey Moore's Crossing the Chasm, she argues Kubernetes has already crossed into the mainstream. The headlines she pulls in show both sides of that: Kubernetes called the new Java, Google telling developers it has become boring, and the Ford and Pivotal write-down story. Her reading is that teams are waking up from the dream that Kubernetes would magically solve everything. You still have to put in the elbow grease.

The CNCF charter definition of cloud native does not help much here. It is purely technical, and it lists examples rather than saying what cloud native is. Container Solutions uses its Cloud Native Maturity Matrix instead, which scores an organisation on culture, architecture, infrastructure, provisioning and more. The point of the matrix is that the axes interact: microservices inside a waterfall culture will not give you the speed you bought them for.

## What does solving the wrong problem look like?

The best story in the talk is a client project. The customer built a camera with a chip doing object and face detection, and Container Solutions built the highly available, highly scalable platform behind it: microservices on Kubernetes, Kotlin migrated to TypeScript halfway through, AI and IoT. Then a demo for investors changed the use case. Now it had to run on a single physical server. That server could never be connected to the internet.

So the customer shipped a server to them, they installed the platform from a Helm chart on a USB drive, and posted it back. "We did the most physical handover of a cloud application that I've ever seen," Lian Li said at Conf42 Cloud Native 2021. A single Java app on Tomcat would have done the job, but the cloud native version already existed, so it shipped. She calls it the sunk cost fallacy, illustrated with the XKCD automation strip.

Her fix is design's old rule, form follows function. Tech is a byproduct of solving a customer problem; some companies adopt AI, blockchain or Kubernetes because everyone else is. Most companies, she notes, do not need to run their own Kubernetes cluster, yet many feel they must. Simon Sinek's Golden Circle is her tool for finding the purpose first, and she quotes Tatiana Mac: a solution is only as good as your framing of the problem.

## Why does psychological safety matter for cloud native teams?

The people half of the talk borrows from agile. Kubernetes is only about seven years old, so nobody is a twenty-year expert, and the work runs on fail fast, fail often loops such as Scrum retrospectives. Running that loop forever without burning people out takes intent.

She uses the accountability versus psychological safety grid. Low on both is the apathy zone; high accountability with low safety is the anxiety zone, where burnout lives; high safety with low accountability is the comfort zone. The learning zone needs both high. Container Solutions takes this seriously enough to employ an in-house psychologist, Andrea Dobson, partly because consulting is about coaching clients and partly because the work is stressful and often has a lot of money riding on it.

## Should teams collaborate less?

Her last section is Team Topologies by Matthew Skelton and Manuel Pais, with its three interaction modes: collaboration, facilitation and X as a service. Collaboration moves at the speed of its slowest member. X as a service costs more up front but is the fastest once built, because consuming a service can be automated. Her example is a platform team running the cluster: emailing manifests for manual deploys is slow, explaining the steps is better, and a self-service API with clear contracts is where delivery speeds up.

She closes on a line lifted from that book: don't do a transformation because you want Kubernetes; use Kubernetes because you are transforming.

## Who should watch?

Engineering managers and platform leads about to sell, or rescue, a cloud migration. There is no YAML here; it is a talk about why the YAML doesn't matter as much as the org chart.

## Related Conf42 talks

- Zach Gardner on [why digital transformations fail and how to succeed](https://www.conf42.com/Cloud_Native_2023_Zach_Gardner_digital_transformation_fails__how_to_succeed) at Conf42 Cloud Native 2023.
- Matty Stratton on [the psychology of chaos engineering](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology) at Conf42 Chaos Engineering 2020.
- Amir Shaked on [building a learning culture](https://www.conf42.com/Chaos_Engineering_2021_Amir_Shaked_learning_culture) at Conf42 Chaos Engineering 2021.

[Watch Lian Li's talk](https://www.conf42.com/Cloud_Native_2021_Lian_Li_kubernetes_wont_save_you), part of [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Container Solutions

Container Solutions is the Amsterdam consultancy, focused on programmable infrastructure, where Lian Li works. Its Cloud Native Maturity Matrix assessment and the Cloud Native Transformation book come up in the talk.

- [Container Solutions website](https://www.container-solutions.com/)
- [Cloud Native Maturity Matrix assessment](https://www.container-solutions.com/maturity-matrix-assessment)

[Watch the talk on YouTube](https://youtu.be/xfDDpCNt3LQ).

## Watch the talk

[Kubernetes won't save you](https://www.conf42.com/Cloud_Native_2021_Lian_Li_kubernetes_wont_save_you) at Conf42 Cloud Native 2021.
