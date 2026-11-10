# MazeWall lets a JVM app sandbox its own threads with seccomp

Conf42 Blog, 2026-10-24, updated 2026-11-09. https://www.conf42.com/platform2026/mazewall-lets-jvm-apps-sandbox-themselves

In short: Leanid Piliptsevich (EPAM) at Conf42 Platform Engineering 2026 introduces MazeWall, using seccomp and Landlock to restrict pieces of an app from inside.

Your image-resizing function has the same right to read secrets as the rest of your process. At Conf42 Platform Engineering 2026, Leanid Piliptsevich, Java developer at EPAM, introduced MazeWall, an experimental open-source research project that lets JVM applications restrict individual threads and processes with Linux kernel tools, so a bug in one small piece of logic can't take the whole app with it.

It's a short talk, and an introduction rather than a production case study. Leanid is clear about that, and about the limits.

## Containers see one big app

Leanid's starting point: applications talk to Linux constantly, and Linux has strong security subsystems, but it can only act on the information the app gives it. Containers use those same subsystems and you should keep using them. Yet a container sees your service as one monolith and applies one policy to all of it.

Developers don't see their apps that way. We think in modules, classes and methods. He compares the goal to a warship's compartments: a breach in one shouldn't sink the vessel. Today, to the kernel and to an attacker, one flaw is enough to compromise everything. Take that image resizer: there's no code in it that reads secrets, until a crafted input exploits a bug and adds some.

## Profile first, then lock the thread

MazeWall's workflow has two halves. First, profile the logic you'll run in production and record every Linux system call it makes, in the new Software Bill of Behavior format, which Leanid clearly enjoys. Second, turn that bill of behaviour into a policy and apply it to the thread or process that runs the logic. Anything the profile saw keeps working; anything it didn't, fails.

Enforcement then belongs to the kernel, through seccomp for syscalls and Landlock for filesystem access. MazeWall's job ends once the policy is applied, which removes the confused-deputy problem of a userspace guard. One property shapes how you design with it: once a policy is applied you can't relax or remove it. Need different permissions? Start a new thread or process with a new policy. Per the abstract, the JDK Foreign Function and Memory API is how a Java or Kotlin app reaches those kernel interfaces.

## Threads are convenient, processes are safer

Leanid lays out three scopes. Process isolation is the proven one; he points out that the Elastic team has used it internally for about ten years and credits that approach with limiting Log4j-style attacks. Thread scope is the developer-friendly option and lets you restrict really small units of logic, since an app has one process but many threads. Its fundamental weakness is shared memory, so some attacks get through. The third option, spawning a dedicated worker process for the risky logic, trades convenience for that stronger isolation. His recommendation is to combine thread and process restrictions rather than pick one.

## Who should watch

JVM engineers who parse untrusted input (documents, images, archives) and security-minded platform teams who already squeezed what they can out of container policies. It's a brief, basic tour; the details live in the MazeWall repository, linked from the talk. Don't expect benchmarks or a deployment story yet.

## Related Conf42 talks

- [Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) by Karan Bansal (ArmorCode)
- [A Python Sandbox for Dynamic Rule Execution](https://www.conf42.com/Python_2024_Zhiya_Zang_sandbox_dynamic_rule_execution) by Zhiya Zang (TikTok)
- [How Kernel Programming Escaped the Kernel](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking) by Anais Dotis (groundcover)

[Watch Leanid's talk](https://www.conf42.com/Platform_Engineering_2026_Leanid_Piliptsevich_sandbox_app_make)

[Watch the talk on YouTube](https://youtu.be/Qi7BeKM3NRw).

## Watch the talk

[Make your app its own sandbox](https://www.conf42.com/Platform_Engineering_2026_Leanid_Piliptsevich_sandbox_app_make) at Conf42 Platform Engineering 2026.
