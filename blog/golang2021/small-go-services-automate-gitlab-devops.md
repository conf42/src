# Six tiny Go services that run a team's release process

Conf42 Blog, 2021-06-24. https://www.conf42.com/blog/golang2021/small-go-services-automate-gitlab-devops

In short: Oliver Fuerst (Restorepoint) at Conf42 Golang 2021 on the small single-binary Go tools that automate releases, GitLab issues, data race reports and library tags

The most useful DevOps tooling is often a hundred lines of Go that nobody outside the team has heard of. At Conf42 Golang 2021, Oliver Fuerst, Lead Developer at Restorepoint, walks through the half-dozen small single-binary services his team wrote to glue GitLab, Freshdesk and their build servers together, including a nightly job that turns Go race detector output into GitLab issues.

It is a short talk and a practical one: every tool is something you could rebuild in an afternoon.

## What are they automating?

Restorepoint's product, also called Restorepoint, is a network device backup and restore system shipped as a single, highly concurrent Go monolith: its own scheduler, HTTP, FTP and TFTP servers and a Lua environment, inside a Linux box customers run on premises or in their own cloud. Per the slides it's roughly 120,000 lines of Go, not counting 2.8 million from external libraries.

The release shape is the interesting constraint: three release versions, two target environments, weekly production releases (customers prefer weekly, though they could ship daily) and continuous internal development releases. GitLab runs the whole life cycle.

## A release API instead of SSH

The first tool removes the need for the build server to SSH into the update server. The build server POSTs the release tarball with its MD5 sum, a set of metadata fields (product, version, tag, build, revision, commit, changelog) and a shared secret. The release API checks the required fields and the secret, writes the file while hashing it in the same pass with an `io.TeeReader`, aborts if the checksum doesn't match, writes the metadata to an env file and hands both to a per-product release script.

Oliver puts it at maybe 100 lines and uses it as his case for the language: Go lets you write a web server in very few lines. He's a fan in general.

"It's a great language to write, but especially to read when you have a large code base to get into," Oliver Fuerst said at Conf42 Golang 2021.

## Support escalations without exposing everyone to every ticket

First-line support lives in Freshdesk; developers only work in GitLab. A Tampermonkey script injects an escalate button into the Freshdesk UI. Clicking it copies the ticket's comments and attachments into a new GitLab issue, links both sides, and refuses to create duplicates. Support engineers decide what reaches developers, and developers don't wade through tickets that were never development problems.

## Webhooks that keep merge requests honest

With three live release versions, merging the wrong branch into the wrong one is an easy mistake. A webhook service receives every merge request event, uses the GitLab API to compare the versions of the source and target branches, and leaves a warning comment when they differ. Because GitLab won't merge while discussions are unresolved, the comment blocks the merge until someone deals with it.

The same webhook moves issues along the board. Issues go Open, To Do, In Development, In Review, To Test, Testing, Closed. Mention the issue number in a merge request and it jumps to In Review; merge it and it moves to To Test. Developers forget to update ticket status; the bot doesn't.

## Turning the race detector into a ticket queue

The idea most teams could copy tomorrow: every internal development build runs with Go's race detector enabled. It costs CPU and, Oliver recalls, roughly doubles memory, so it stays out of production builds. Races in a concurrent monolith tend to fire only when a particular code path is hit, so a fleet of internal machines replays common usage scenarios around the clock and logs any race reports.

Once a day a tool scans those logs. Each block from the WARNING: DATA RACE marker to the closing separator becomes a GitLab issue, titled with the function where the race occurred and labelled as a race condition. If the issue already exists it adds a comment instead, keeping it fresh. The low-hanging races are long fixed, Oliver says, and the setup has turned up a fair number in external libraries, which the team reported upstream.

## Patch versions nobody has to remember

Roughly 20 internal libraries are consumed as Go modules, which want semantic version tags. A tag job in each library's pipeline runs on merges to master, reads the existing tags, bumps the patch version (or creates the first tag), and uses the last commit message as the tag description. The job ships as a container image you drop into the pipeline.

## Who should watch?

Go teams on GitLab with a monolith, an on-prem product or a support desk that keeps pinging developers. It's an inventory rather than a deep technical talk, but the race-detector pipeline and the release API are both worth stealing. It ends with a hiring pitch for remote UK and EU Go engineers.

Pair it with [Piyush Verma on Go concurrency primitives and when not to use them](https://www.conf42.com/Golang_2021_Piyush_Verma_concurrency_primitives), [Robert Pajak on build automation in Go with goyek](https://www.conf42.com/Golang_2023_Robert_Pajak_goyek_automation), and [Francisco Daines on enforcing architecture rules in CI with arch-go](https://www.conf42.com/Golang_2021_Francisco_Daines_archgo_architecture_tooling_test_guidelines_automation).

[Watch Oliver Fuerst's talk](https://www.conf42.com/Golang_2021_Oliver_Fuerst_devops_automation) from [Conf42 Golang 2021](https://www.conf42.com/golang2021).

## From Restorepoint

Restorepoint builds network automation and device backup and restore software, written in Go and shipped weekly as an on-premises appliance.

- Restorepoint: [restorepoint.com](https://www.restorepoint.com)

[Watch the talk on YouTube](https://youtu.be/KaIbgrYIPQk).

## Watch the talk

[DevOps automation with Go](https://www.conf42.com/Golang_2021_Oliver_Fuerst_devops_automation) at Conf42 Golang 2021.
