# Chaos engineering is deliberately practising being wrong

Conf42 Blog, 2020-01-22. https://www.conf42.com/blog/ce2020/chaos-engineering-practice-being-wrong

In short: Russ Miles (ChaosIQ) at Conf42 Chaos Engineering 2020 on dark debt, surprises over incidents, and chaos engineering as verifying objectives

Everyone is wrong all the time, so the useful skill is being wrong safely and on purpose. At Conf42 Chaos Engineering 2020 in London, Russ Miles, CEO of ChaosIQ, opened the day by recasting chaos engineering as deliberately practising being wrong, and by suggesting a better name for it: system verification, anchored to an objective the business already cares about.

It's a keynote told through motorcycle trips, a heckler and jokes about naming things, with a tight argument underneath.

## Why are fire drills the wrong analogy?

People often justify chaos engineering as a fire drill: practise, and you'll be ready. "Fire drills are a terrible analogy for chaos engineering," Russ Miles said at Conf42 Chaos Engineering 2020. Drills make you complacent. When an alarm goes off at 11am, everyone checks their watch and assumes it's a drill, smoke or no smoke. His warning: treat chaos engineering as a practice, and stay alert to the complacency that practice can breed.

A road in Tibet, ridden on the way to Everest, supplies the second warning. The tarmac had washed off the corners, so to mark the hazard someone ringed them with small boulders, turning a mildly dangerous corner into a lethal one. Software does that too: a fragile spot gets a README nobody reads. Making something safer can make it more dangerous.

## Why say surprise instead of incident?

Because an incident sounds like something you caused and should have predicted. A surprise is what it is. Russ wants the boss to ask why that surprise happened, which leaves room to learn. Production is a sociotechnical system (people, practices, processes, infrastructure, applications) with turbulence from users, cloud providers and admins. Using the Cynefin framework, he places most of us not in obvious or complicated but in complex, and with frequent change, chaotic, where small changes can have large effects.

## What is dark debt?

Technical debt is the shortcut you know you took. Dark debt is its evil cousin: present however right you think you are, camouflaged as working software, unknown until it surfaces. You can't measure it and you can't design it out in a review. You can only find evidence of it.

The business reason to care is cost. Russ cites roughly $100,000 per hour of downtime for 95% of enterprise systems, and those are back-office systems, email and the issue tracker, not streaming platforms, before anyone sues. Speed isn't the enemy, though: citing Accelerate, he notes the fastest teams also ship fewer failures.

He tested a room of bankers. Almost everyone had a systems failure in the last two months; many had a disaster recovery programme exercised in the last month. Asked how many exercised it on purpose, most hands went down.

## Is the world's first chaos engineer a child?

Russ's favourite story, from the preface of the Google SRE book: Margaret Hamilton, lead of the Apollo onboard software, brought her daughter Lauren to work, Lauren crashed the mission simulator with a key combination that wiped navigation data, and NASA said trained astronauts would never do that. On a later mission one did. Margaret had kept a backup procedure, so in Russ's telling Lauren was the first chaos engineer and Margaret a resilience engineer.

## Why is blame the wrong shortcut?

At a talk in Norway, an attendee leapt on stage to confess he had destroyed the master node of a university's grid cluster and lost about three weeks of research processing. The instinctive fix is to take away his keyboard. The real cause: the command he typed differed by one character from the one he meant, and nothing asked for confirmation. It was a trap built into the system, and blame skips straight past it.

## What should chaos engineers actually do?

Think like a motorcyclist. Drivers are taught to assume others can't see them; riders assume others can see them and want them dead. Production, says Russ, hates you. So add compensating practices and learn to tell two words apart: "Robustness is for the stuff you know can happen. Resilience is for the stuff you don't know is going to happen."

His recipe avoids the word chaos. Start with what you care about (availability, durability, the home page being up), make it measurable, set a target such as 99%. Then choose conditions to verify against it: a pod dying, the network degrading. Without the objective, breaking things tells you nothing about what to fix first. With it, the results give prioritised actions. There are only two techniques, game days and automated experiments, so small fires replace big ones, and learning moves from postmortem to pre-mortem.

His closer: he claimed there are no best practices in complex systems, then admitted he lied. Chaos engineering is the one, he said: just do it.

## Who should watch

Anyone who needs to explain chaos engineering to a business that hears the word chaos and reaches for the budget veto. Practitioners will find the objective-first framing useful for choosing experiments. Related talks from the same event: [Adrian Hornsby on getting out of the starting blocks](https://www.conf42.com/Chaos_Engineering_2020_Adrian_Hornsby_getting_out_of_the_starting_blocks), [Matty Stratton on the psychology of chaos](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology), and [Yury Nino on postmortem culture](https://www.conf42.com/Chaos_Engineering_2020_Yury_Nino_postmortem_culture).

[Watch Russ Miles's talk](https://www.conf42.com/Chaos_Engineering_2020_Russ_Miles_how_to_be_wrong) from [Conf42 Chaos Engineering 2020](https://www.conf42.com/ce2020).

## From ChaosIQ

Russ named two tools at the end: the Chaos Toolkit, the open-source experiment tool he created with a friend and where many companies start, and ChaosIQ, which he described as a software-as-a-service verification tool. He also wrote Learning Chaos Engineering.

- ChaosIQ: [chaosiq.io](https://chaosiq.io)
- Chaos Toolkit: [chaostoolkit.org](https://chaostoolkit.org)

[Watch the talk on YouTube](https://youtu.be/7k6gYZa6BVg).

## Watch the talk

[How to be WRONG](https://www.conf42.com/Chaos_Engineering_2020_Russ_Miles_how_to_be_wrong) at Conf42 Chaos Engineering 2020.
