# Read the import block, because that's where Go tech debt starts

Conf42 Blog, 2025-04-02, updated 2026-11-09. https://www.conf42.com/blog/golang2025/go-dependency-rabbit-hole-delivery-hero

In short: Andrii Raikov of Delivery Hero at Conf42 Golang 2025 on hidden Go dependencies, breaking v2 libraries and the helpers package that ate a codebase.

Can you name the indirect dependencies of the Go service you work on, and say why each one is there? At Conf42 Golang 2025, [Andrii Raikov](https://www.conf42.com/Golang_2025_Andrii_Raikov_dependencies_code_management), Principal Software Engineer at Delivery Hero, opened with that question and spent the rest of the talk showing why most of us can't, and how small package decisions turn into years of tech debt.

Delivery Hero runs a lot of Go, and Andrii's examples come from its own code base, good and bad. The talk has two halves: a set of binary-size experiments that make hidden dependencies visible, and three patterns from production that he has watched go wrong more than once.

## Your binary knows what you imported

Andrii starts with a hello world that prints with the built-in print function, then swaps in `fmt` and recompiles. The binary grows noticeably. Then he adds `os` to read a name from the arguments, and the size barely moves. The reason is in `fmt` itself: it already pulls in `io`, `os`, `reflect`, `strconv`, `sync` and `unicode`, so by the time you ask for `os` you already have it. Moving the code into an external module on GitHub changes almost nothing either.

The bigger experiment uses the AWS SDK to list S3 buckets in a few lines of code, and the binary jumps several times over. Andrii then had ChatGPT write the same call by hand, signing the request against the S3 API using only the standard library. That version is about six megabytes smaller, but still around eight. Commenting out imports one by one, he finds `crypto` and `encoding` barely matter on their own. A tiny program that only calls a URL with `net/http` already lands at about five megabytes.

He is explicit that the lesson isn't "rewrite net/http". The lesson is that nobody looks. You add one small library and have no idea what it drags in, or what its dependencies drag in.

## A v2 that breaks v1 can trap a team for years

The second half is about culture, and the first story will be familiar to anyone in a large company. A platform team owns a global service-to-service token service and ships client libraries in several languages, Go included. Version one works. Then version two changes the interfaces without a new module path.

Service teams look at the migration cost, decide "if it works, don't touch it", and stay on v1. The platform team has no capacity to support both and deprecates v1, so no more fixes or security updates. Then a different team builds a new shared library on top of v2. Any service still on v1 that tries to use it gets a conflict: two implementations under the same name. Andrii says he has seen this happen several times, and it takes a year or two to build up, by which point untangling it can cost more than a greenfield rewrite.

The fix he points to is the one the Go ecosystem already expects: a breaking change gets a separate major-version path with its own `go.mod`, so v1 and v2 can live side by side.

## The helpers package is a dependency magnet

The other two patterns are about DRY applied without thought. A `helpers` package grows a function that prints details of a `Gopher` type, so helpers now depends on the gopher package. The day the gopher package needs a helper, you have a cycle, and the usual workaround is a second helpers package, which brings back the duplication you were trying to remove. His fix is plain: that function should be a method on the type, with private fields if you like.

Scale the same habit across services and you get his worst case: the same helper code living in a service's own package, in a newly extracted shared library and again in a third dependency, with three slowly diverging implementations and three sets of vulnerabilities.

## What to do on Monday

Andrii's closing list is short: write a dependency policy and actually follow it, audit dependencies and update versions regularly, scan for vulnerabilities in transitive packages too, and work with product to prioritise the debt. His most practical tip: don't skip the import block during PR review. Several of his horror stories would have been caught there.

## Who should watch

Go developers in teams with more than a handful of services, and anyone maintaining a shared internal library. It's a good talk for mid-level engineers who haven't yet been burned by a breaking minor version. Seniors may know the theory, but the binary-size experiments are worth a look before your next `go get`.

## Related Conf42 talks

- [Going Beyond Metadata: Why We Need to Think of Adopting Static Analysis in Dependency Tools](https://www.conf42.com/DevSecOps_2022_Joseph_Hejderup_going_beyond_metadata_adopting_static_analysis_dependency_tools) by Joseph Hejderup (Endor Labs), on knowing which dependency code you actually call.
- [Supply Chain Attacks: Focused on NPM attacks](https://www.conf42.com/DevSecOps_2023_Danish_Tariq_Hassan_Khan_Yusufzai_supply_chain_npm_attacks), for what an unnoticed transitive dependency can do.
- [Compelling Code Reuse in the Enterprise](https://www.conf42.com/DevOps_2023_Travis_Gosselin_compelling_codecreuse_enterprise) by Travis Gosselin (SPS Commerce), on sharing code without the helpers trap.

[Watch Andrii Raikov's talk](https://www.conf42.com/Golang_2025_Andrii_Raikov_dependencies_code_management).

## From Delivery Hero

Delivery Hero sponsored Conf42 Golang 2025, and Andrii closed by saying the team is hiring engineers to help build a better dependency management culture.

- [Delivery Hero careers](https://careers.deliveryhero.com/deliveryhero-jobs)

[Watch the talk on YouTube](https://youtu.be/jntHMm3mLVA).

## Watch the talk

[The "Rabbit Hole" of Dependencies in Golang](https://www.conf42.com/Golang_2025_Andrii_Raikov_dependencies_code_management) at Conf42 Golang 2025.
