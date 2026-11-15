# Good SAST matches the shape of your code, not the text

Conf42 Blog, 2025-11-30, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/semgrep-sast-matches-code-shape-not-text

In short: Safeer C M of MoEngage at Conf42 DevSecOps 2025 explains how SAST works via abstract syntax trees and how to write and roll out Semgrep rules without drowning devs.

Grep finds strings; a SQL injection is a structure. At Conf42 DevSecOps 2025, [Safeer C M](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep), principal engineer at MoEngage, opened the black box of static application security testing: how tools turn source into abstract syntax trees, why that beats text matching, and how to write and roll out rules with the open-source Semgrep engine without burying developers in false positives.

Safeer brings 20-plus years in SRE, infrastructure and platform engineering, and the talk has that flavour: less about vulnerability taxonomy, more about building a tool developers will actually keep turned on. It's a foundations talk, so start here if SAST has always been somebody else's dashboard.

## Why SAST, and why it got a bad name

Manual security review of every change doesn't scale, so shifting left is the only way. Because SAST is white-box testing with full access to the source, it can cover the whole codebase before anything is built, and catch classics like SQL injection, exposed secret keys and buffer overflows.

Safeer is candid about the history. First-generation tools were clumsy: slow scans, complex setup, results nobody could act on, and developers who decided the tools were useless. Later tools improved, but false positives remain the big problem, and SAST still struggles with authentication and authorisation flaws, weak cryptography and configuration issues, since it only reads code.

## Abstract syntax trees are the whole trick

Under the hood, source is tokenised, parsed by the language grammar into a hierarchical tree, and then analysed for control flow and data flow before rules are applied. The tree is abstract because it drops what doesn't change meaning: comments, whitespace, formatting. His slide shows four print statements that look different as text but produce the same tree. He uses Python's built-in ast module to show the structure, then compares a direct call with one that goes through a variable assignment to show how quickly trees grow.

## Semgrep rules look like the code they catch

Semgrep, the name a blend of semantic and grep, works directly on source, no compiled artefacts needed. Rules are YAML, and patterns look like ordinary code with placeholders. Even rules are parsed into trees, so matching stays deterministic. A rule carries an ID, the pattern, a message for the developer, target languages, severity and metadata such as CWE links or internal docs, which lets a rule set double as your organisation's coding standard.

He walks through the combinators: pattern, patterns (all must match), pattern-either (any can match), pattern-regex, and nestable operators like pattern-inside and pattern-not. Metavariables capture part of the code so later conditions can inspect it, for example a URL passed to a requests call. He also distinguishes structural rules from data-flow and taint analysis, noting that the community edition focuses on rules within a single file while the commercial Pro engine adds cross-file and deeper taint support.

The demos keep it concrete: a hello-world rule, an SQL injection rule with three alternatives (variables concatenated, interpolated or percent-formatted into a cursor's execute call) that flags two of them in a sample, a rule that checks that functions call the company's standard input-validation helper before processing input, and an AWS credentials rule that uses metavariable regexes for the 20-character access key ID and the 40-character secret.

## Roll it out softly or nobody will look at it

The adoption advice is the part teams usually get wrong. Start with the community registry, which Safeer puts at more than 3,000 open-source rules, using the auto config that detects your languages and frameworks, then fork and tweak rules locally. Integrate in layers: IDE plugins so the tool teaches rather than gates, pre-commit hooks scanning only changed code, CI with SARIF output into GitHub code scanning or other dashboards, and PR comments that turn tribal knowledge into rules over time.

Begin with warnings rather than blocks, except for critical issues. Scan the baseline, focus on new findings, use ignore files to cut noise, and don't switch on every rule at once. Work with security engineers to tune rules as you go.

## Who should watch

Developers and platform engineers about to introduce SAST, or stuck with a scanner everyone ignores. AppSec veterans will know the theory but may like the rollout playbook.

## Related Conf42 talks

- [Why We Need to Think of Adopting Static Analysis in Dependency Tools](https://www.conf42.com/DevSecOps_2022_Joseph_Hejderup_going_beyond_metadata_adopting_static_analysis_dependency_tools) applies the same idea to dependencies.
- [Vulnerability Management that developers won't hate](https://www.conf42.com/DevSecOps_2024_Anthony_Laiuppa_vulnerability_management_developers) shares the developer-experience-first view.
- [Purple Teaming with OWASP PurpleTeam](https://www.conf42.com/Chaos_Engineering_2022_Kim_Carter_owasp_purpleteam) covers the dynamic testing SAST can't do.

[Watch Safeer C M's talk](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep)

[Watch the talk on YouTube](https://youtu.be/_RRV8SY2ED0).

## Watch the talk

[Understanding SAST Foundations with Open-Source Semgrep](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep) at Conf42 DevSecOps 2025.
