# Your Rust crate declares 17 transitive dependencies and calls about 6

Conf42 Blog, 2022-11-30. https://www.conf42.com/devsecops2022/metadata-is-not-source-code

In short: Joseph Hejderup (Endor Labs) at Conf42 DevSecOps 2022 on why dependency tools should use lightweight static analysis instead of manifest metadata

Joseph Hejderup, Research Engineer at Endor Labs, brought numbers from his PhD research to Conf42 DevSecOps 2022: across the Rust ecosystem, packages resolve a median of 17 transitive dependencies according to metadata, but a call graph shows them actually using about 6. His argument is that dependency tools, from vulnerability scanners to update bots, should look at how code calls code instead of trusting what the manifest declares.

This is a design discussion with research behind it, not a product pitch, and it is honest about where static analysis loses.

## What are package managers actually good at?

He starts with a 1986 US Department of Commerce guideline on software reuse: reuse should improve productivity and cut development time, cost and risk. Package managers deliver the first two brilliantly. One npm install gives you thousands of libraries, and publishing is just as easy.

Risk is another matter. One install can pull in hundreds of packages (one build in his example compiles 307), the tree can hold two versions of the same library, and version ranges mean the same install gives a different tree three days later. Lock files fix the moving target. Everything else (vulnerabilities, updates, audits, deprecation) is left to analyzer bots and plugins that walk the dependency tree and flag any path from a bad package to your app, with plenty of false positives and warnings you can't act on.

## Is it just alert fatigue?

He says no: the problem is the quality of the analysers. His first rule: "metadata is not source code". A declaration is not usage, and two clients use the same library in completely different ways. His second rule: make code a first-class citizen. Saying package green 1.2 is vulnerable tells you little; saying function bar in it is vulnerable, and there is or isn't a reachable path from your main, is something a developer can act on and estimate.

The usual objection is that program analysis is expensive and doesn't scale to hundreds of dependencies. His third rule answers it: aim for lightweight techniques. His team built call graphs for the Rust ecosystem in 10 days; the slides put it at 23,767 packages and 142,301 releases.

## What did the Rust numbers show?

The study (Präzi, published in Empirical Software Engineering in 2022) compared dependency counts from crates.io and docs.rs metadata with a call-based network. For direct dependencies the two roughly agree: if you declared it, you probably use it. For transitive dependencies they don't: 17 versus 6, with packages on average not calling around 60% of the transitive dependencies they resolve.

To check whether the static analysis was wrong, he went through 34 cases by hand. He found dependencies declared but never imported (3), imported but never used (4), one used only under conditional compilation, derive macro libraries that generate code at compile time and are not runtime dependencies at all (2), and a test dependency declared in the runtime section. The biggest group, 16 cases, were transitive dependencies with no reachable path: your app calls lib one, lib one calls one function in lib two, and that function never touches lib three, even though another function in lib two does. Joseph Hejderup said at Conf42 DevSecOps 2022: "And this really shows that context really matter."

## So should every dependency tool use static analysis?

His answer depends on scope:

- **Direct dependencies**: metadata is good enough, needs no program analysis and has higher recall, which matters for security-sensitive uses. It still misses unused imports and code-generation-only crates.
- **Transitive dependencies**: prefer static analysis. It captures actual usage, cuts false positives and saves the tedious manual walk from your code to GitHub and down the tree. Think of a parser that depends on a regex library you never trigger.

The costs are real. Static analysis has false negatives, which security teams won't love. Package repositories mix libraries that use static dispatch with ones built on dynamic class loading, which call graphs handle badly. Recall depends on language coverage; of the Java call graph generators WALA, OPAL and Soot, he notes OPAL handles Java 11 features better. Handling dynamic dispatch means linking a call site to every possible implementation, and the algorithms that narrow that down, such as points-to analysis, don't scale to a whole dependency tree. For Python and JavaScript he points to hybrid static and dynamic analysis.

## Who should watch

People building or choosing SCA and dependency tools, Rust developers curious how much of their tree they really use, and anyone who wants evidence for why reachability should drive triage. Watch it next to his Endor Labs colleague [Henrik Plate on Eclipse Steady and code-centric vulnerability management](https://www.conf42.com/DevSecOps_2022_Henrik_Plate_opensource_vulnerability_management_source), [Andrew Robinson on dependency management and health checks](https://www.conf42.com/Cloud_Native_2021_Andrew_Robinson_improving_reliability_health_check_dependency_management) and [Ciara Carey on actionable SBOMs](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable).

[Watch Joseph Hejderup's talk](https://www.conf42.com/DevSecOps_2022_Joseph_Hejderup_going_beyond_metadata_adopting_static_analysis_dependency_tools)

## From Endor Labs

- [Endor Labs](https://www.endorlabs.com/endor-labs-demo-request): dependency risk and vulnerability management built on program analysis.

[Watch the talk on YouTube](https://youtu.be/Ct-qukdHdj0).

## Watch the talk

[Going Beyond Metadata: Why We Need to Think of Adopting Static Analysis in Dependency Tools](https://www.conf42.com/DevSecOps_2022_Joseph_Hejderup_going_beyond_metadata_adopting_static_analysis_dependency_tools) at Conf42 DevSecOps 2022.
