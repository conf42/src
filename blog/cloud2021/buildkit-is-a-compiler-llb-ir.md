# docker build is a compiler, and BuildKit's LLB is its LLVM IR

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/buildkit-is-a-compiler-llb-ir

In short: Adam Gordon Bell (Earthly) at Conf42 Cloud Native 2021 on BuildKit as a compiler with front ends, an IR called LLB and back ends, with live demos

Every `docker build` you have ever run went through a compiler, whether or not you thought of it that way. At Conf42 Cloud Native 2021, Adam Gordon Bell, Developer Advocate at Earthly and host of a software engineering podcast, explains BuildKit, the engine behind Docker builds, by mapping it onto LLVM: front ends, an intermediate representation called LLB, and back ends. Then he writes LLB by hand in Go and ships a joke Dockerfile dialect inspired by INTERCAL.

It's the rare container talk that makes you understand the tool better rather than just use it.

## Image is to container as executable is to process

He starts with the analogy that frames everything else. An executable is a program you can launch as many processes from; an image is something you run as many containers from. Unlike a VM image, a Docker image is immutable: changes inside a running container don't flow back. And as executables come from compilers, images come from BuildKit.

The comparison holds closely. A C hello world goes through clang and LLVM into x86 assembly; a Dockerfile (from Alpine, copy a README, echo into a file) goes through BuildKit into layers packaged as an image. One difference: a compiler takes source code, while a Docker build also takes the build context, a file system, which is how `COPY` can pull in files.

## Why compilers grew an intermediate representation

The history detour is worth it. Dennis Ritchie's first C compiler on the PDP-11 translated C straight to PDP-11 assembly, which meant a new compiler for every new machine: the VAX-11, and eventually Apple's M1. Compiler authors split the work into a front end (tokenise, parse, build an AST), an optimiser and a back end that emits machine code. Once every back end speaks the same intermediate representation (LLVM IR), adding a CPU means one new back end, and adding a language means one new front end.

That's why, he argues, the last decade saw a Cambrian explosion of ahead-of-time compiled languages on LLVM, with back ends reaching WebAssembly and GPUs. "The secret is just this intermediate representation," Adam Gordon Bell said at Conf42 Cloud Native 2021.

## BuildKit has the same shape

BuildKit's IR is LLB, the low-level builder representation, chosen because containers also have to run on many architectures. With LLB in the middle, front ends multiply: the Dockerfile syntaxes are the common ones, and projects such as OpenFaaS, Rancher Rio and buildpacks use BuildKit too.

The demos make it concrete. First, the same Dockerfile built with plain `docker build`, then with `buildctl` against a `buildkitd` daemon running as a container (installed with Homebrew on his Mac), choosing the front end and an output back end (an image pushed to a registry; a tar file is another option).

Second, LLB written programmatically. LLB is a protobuf, so any language with protocol buffers can produce it; he uses Go because BuildKit is written in Go and ships a client library. The Go program reproduces the Dockerfile explicitly: the image from `docker.io/library/alpine`, a copy from the local context, and a run wrapped in a shell, since `echo` and redirects are shell features. Piping the output through `buildctl debug dump-llb` and jq shows the raw operations, and piping it to `buildctl build` produces an image that runs anywhere. His point: in a real language you get control flow, libraries and less duplication than a Dockerfile allows.

## A Dockerfile front end that says please

Third, a full front end. Docker's `syntax` directive lets a Dockerfile name a front end image that Docker pulls and runs, so users install nothing. He took an existing Dockerfile front end, kept its parser and LLB conversion, and swapped the keywords for INTERCAL-style ones: `COME FROM` instead of FROM, `STASH` for COPY, `PLEASE` for RUN, and "are you okay" for HEALTHCHECK. He doesn't recommend using it, but the repo is a decent template if you want your own syntax.

## What would you build on it?

The real examples are more sober. A Lambda-style service that takes JavaScript in a POST request and builds a container programmatically is, he estimates, a couple of hundred lines as a proof of concept. Mockerfile replaces long apt-get lines with a YAML list of packages, each issued as LLB. And BuildKit is more than a pure-function compiler: workers that power Docker Buildx for multi-architecture images, aggressive incremental caching (he compares it to Scala's slow cold start but fast incremental builds), parallel execution of independent steps, and distribution across a cluster because the layers talk gRPC.

His broader lesson: compiler problems hide everywhere, and spotting one gives you decades of literature to solve it with.

## Who should watch

Anyone who writes Dockerfiles daily and wants a mental model of what happens underneath, and platform engineers considering generating images from code instead of templates.

## Related Conf42 talks

- Gaspare Vitta on [reproducible builds with Bazel](https://www.conf42.com/Python_2021_Gaspare_Vitta_Reproducible_Builds_Bazel) at Conf42 Python 2021.
- Haseeb Majid on [reproducible environments with Nix](https://www.conf42.com/Golang_2024_Haseeb_Majid_using_nix_reproducible) at Conf42 Golang 2024.
- Sohan Maheshwar on [WebAssembly and the future of the cloud](https://www.conf42.com/Cloud_Native_2024_Sohan_Maheshwar_future_cloud_webassembly) at Conf42 Cloud Native 2024.

[Watch Adam Gordon Bell's talk](https://www.conf42.com/Cloud_Native_2021_Adam_Gordon_Bell_compiling_containers) from [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Earthly

Earthly builds on BuildKit features for reproducible builds such as CI pipelines; it's on GitHub and at earthly.dev.

- Earthly: [earthly.dev](https://earthly.dev/)

[Watch the talk on YouTube](https://youtu.be/RHqNNTqmfEA).

## Watch the talk

[Compiling Containers](https://www.conf42.com/Cloud_Native_2021_Adam_Gordon_Bell_compiling_containers) at Conf42 Cloud Native 2021.
