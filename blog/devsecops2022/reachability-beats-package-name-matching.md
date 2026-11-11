# Your scanner matches names; the vulnerability lives in a method

Conf42 Blog, 2022-12-01. https://www.conf42.com/blog/devsecops2022/reachability-beats-package-name-matching

In short: Henrik Plate (Endor Labs) at Conf42 DevSecOps 2022 on code-centric vulnerability management with Eclipse Steady - fix commits, call graphs and bloat

Most dependency scanners decide you are vulnerable by matching a package name and version against an advisory. Henrik Plate, security researcher at Endor Labs, argued at Conf42 DevSecOps 2022 that the question worth answering is different: is the vulnerable code actually in your build, and can your application reach it? He demonstrated the approach with Eclipse Steady, the open source tool he spent several years building with fellow researchers, and was clear that the talk is about the technique, not Endor Labs' own product.

## Why is name matching not good enough?

The numbers are familiar: open source makes up about 80% of a typical application, with dozens to hundreds of dependencies, most of them transitive. His example, a Maven plugin, has 8 direct and 34 transitive dependencies in a tree seven levels deep. Most vulnerabilities live in those transitive ones, and often only a few of their functions are used, sometimes none.

Advisories don't help much. His case is a 2018 CVE in Eclipse Mojarra: two sentences of description, a CVSS score and CPE identifiers. Searching Maven Central for Eclipse Mojarra gives 36 hits, none of them the artifact that actually ships the vulnerable code, which is published under a GlassFish name. Henrik Plate said at Conf42 DevSecOps 2022: "So this demonstrates the problem of mapping names given by people to each other in the hope to find the right match." When his team checked the bytecode, two versions the CVE did not list still contained the vulnerable code; NVD updated the entry after their report.

Metadata tools such as OWASP Dependency-Check are light and easy to run, but they can only help with detection. They know nothing about your code, so triage and impact assessment stay manual.

## Two easier questions than exploitability

Whether a vulnerability is exploitable depends on configuration, deployment and architecture, which no tool fully knows. Eclipse Steady answers two easier questions instead. Is the vulnerable code contained? And is it executable in this application? The assumption: if your app runs code that later got a security fix, there is a real risk.

For the first question it starts from the fix commit and builds a change list of the methods and constructors that were added, deleted or modified, then looks for those signatures in every archive, whatever the archive is called. That also catches rebundled classes copied into other JARs, which name matching misses.

For the second it chains three analyses: a static call graph from the application's own methods; dynamic tracing of what actually runs during JUnit or integration tests; then a second static pass starting from the traced methods. That last step bridges reflection and the runtime-generated calls that frameworks like Spring Boot rely on, where static analysis gives up. In their study, around 10% of reachable vulnerable code was found only through that combination.

## The demo: Apache Commons Text

The example is the Apache Commons Text string substitution vulnerability disclosed in October 2022: interpolators enabled by default, including one for JavaScript, allowed remote code execution before version 1.10.0, but only if your code or a dependency calls the substitution. A sample app with Commons Text and JUnit runs the advisory's proof of concept, which creates a file.

Steady's Maven plugin builds a method-level bill of materials and flags Commons Text based on vulnerable method signatures, not coordinates. The call graph goal then draws the path from main to the vulnerable constructor, and the instrumented test run confirms it dynamically. The mitigation view lists the touch points where the app calls into the library and checks each against the fixed releases; going from 1.9 to 1.10.0, 170 of the 171 methods in the call graph keep the same body, so the upgrade is low risk.

It also measures bloat: of 3,671 and 1,149 methods in the two compile-time dependencies, tests executed 10 and 130. A dependency where nothing is reachable or executed is a candidate for deletion, and a deleted dependency never shows up in a scan report again.

## Where does it stop working?

He is upfront about the limits. A fix that only changes a default configuration or properties file is invisible to code analysis. Reachable is not exploitable, and the reverse holds too: with Java deserialization, a gadget class sitting anywhere on the classpath is enough, call graph or not. And Steady specifically needs fix commits, which public databases don't collect; its Project KB lists them for about 700 vulnerabilities. It supports Java, with Python in beta, and runs as a Docker Compose application.

## Who should watch

AppSec engineers triaging scanner output, Java teams shipping on-premise software where every patch release costs customers effort, and anyone curious how reachability analysis works under the hood. If you follow one triage rule from it, make it his: "If yes, fix it now, if no, fix it later, reduce the priority, look at the things that matter more." Pair it with his colleague [Joseph Hejderup on static analysis in dependency tools](https://www.conf42.com/DevSecOps_2022_Joseph_Hejderup_going_beyond_metadata_adopting_static_analysis_dependency_tools), [Magno Logan's software composition analysis 101](https://www.conf42.com/DevSecOps_2021_Magno_Logan_software_composition_analysis_101) and [Anthony Laiuppa on vulnerability management for developers](https://www.conf42.com/DevSecOps_2024_Anthony_Laiuppa_vulnerability_management_developers).

[Watch Henrik Plate's talk](https://www.conf42.com/DevSecOps_2022_Henrik_Plate_opensource_vulnerability_management_source)

## From Endor Labs

- [Endor Labs](https://www.endorlabs.com/endor-labs-demo-request): open source dependency risk and vulnerability management based on program analysis.

[Watch the talk on YouTube](https://youtu.be/lR_Ib7CX_hU).

## Watch the talk

[Open-source vulnerability management? Use the source, Luke!](https://www.conf42.com/DevSecOps_2022_Henrik_Plate_opensource_vulnerability_management_source) at Conf42 DevSecOps 2022.
