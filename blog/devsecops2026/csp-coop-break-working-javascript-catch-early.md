# When CSP and COOP break working JavaScript, and how to catch it first

Conf42 Blog, 2026-09-27, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/csp-coop-break-working-javascript-catch-early

In short: At Conf42 DevSecOps 2026, SAP's Elena Darevskaya shows how browser security headers break popups, eval and blob workers, plus ESLint and Playwright fixes.

Your login popup works for years, then one morning it hangs with nothing in the console. At Conf42 DevSecOps 2026, Elena Darevskaya, Senior Platform Engineer at SAP who builds a web SDK customers embed in their own pages, showed how browser security policies quietly break correct JavaScript, and how to catch that in design, lint, build, test and production rather than in a customer's bug report.

## A header you did not set broke your code

Darevskaya's angle is unusual for a security talk. Most CSP talks ask how to make the policy as strict as possible. She asks how to keep your code compatible with policies you do not control, because her SDK runs inside other people's sites with other people's headers.

Even if you own the environment, she gives three reasons to care: catching it early is cheaper than a redesign, CSP blocks things at execution time rather than load time (so an untested flow can hide an eval for months), and AI-generated code makes guardrails that stop risky patterns before commit more valuable.

Her demo is a sign-in popup with a third-party provider. Click sign in, click continue, nothing happens. Hours of debugging later: the provider added Cross-Origin-Opener-Policy, which severs the popup from its parent, so `window.opener` is null and the `postMessage` that used to report login goes nowhere. The design assumed the popup would always see its opener, and tightening browser security broke that assumption.

## Ask what the API assumes before you use it

At design time she suggests asking whether an API depends on window relationships or specific origins, whether a header can block it, whether it needs a secure context, and whether a permissions policy can restrict it. The answers might change the design: a redirect flow instead of a popup, or a broadcast channel that does not depend on the opener. She also mentions an experimental MDN MCP server as a way to give AI coding agents real API documentation instead of hallucinated behaviour.

## ESLint is a policy engine you already have

Most JavaScript projects run ESLint for style, and she argues it is underused. Out of the box it bans eval and its cousins: `new Function` and `setTimeout` with a string. With `no-restricted-syntax` you can forbid `innerHTML` and `outerHTML` unless wrapped in a sanitiser, which her live demo shows failing on exactly one unsafe file. With Trusted Types now available in modern browsers, CSP can block that sink outright.

The architectural trick is more interesting. Blob workers are blocked by typical CSP unless explicitly allowed, and the blob URL may be created in a different file from the worker. So make one worker factory module the only place allowed to call `new Worker` and own URL creation, and let everything else call its function. The same approach can restrict `window.open` to calls with noopener and noreferrer, or `fetch` to approved URLs.

## Your bundler can add the eval back

Her favourite gotcha: she removed every eval from the source, lint was clean, and the page still threw a CSP eval error. The culprit was a webpack devtool source map setting starting with "eval", which injects eval into the build. Vite has its own surprises. Her fixes: lint the bundler config itself to forbid eval-based devtool values, and add a thin scanner over build artifacts for eval, blob and data resources, inline styles and dynamic scripts. Source code is not the thing that runs.

## Test under the policy you mean

Staging and production headers often differ, so she runs the same Playwright tests as separate projects, one with a permissive CSP that allows blob workers and one strict, injecting the header in a fixture and attaching CSP violation reports as test annotations. A worker test passes under permissive and fails with a clear violation under strict. She also writes tests that are expected to fail: under `frame-ancestors 'none'`, embedding the page in an iframe should break, and the report shows that as a pass.

## Watch production with report-only

Finally, report-only headers and reporting endpoints let you trial a stricter policy or keep watching violations after rollout. Two warnings: the endpoint is public, so validate and rate-limit what it accepts, and reported URLs can contain tokens you should not store. If you ship a third-party script and cannot set headers, the SecurityPolicyViolation event and ReportingObserver can capture violations from inside the page, with different coverage and browser support.

## Who should watch

Front-end and platform engineers shipping embeddable SDKs or widgets, and security teams rolling out CSP who want developers on side. Lots of live demos, and the example code is on GitHub.

## Related Conf42 talks

- [Srinivasa Rao Gunda on a framework for front-end and Node.js vulnerability management](https://www.conf42.com/JavaScript_2025_Srinivasa_Rao_Gunda_securing_framework_frontend).
- [Gil Zilberfeld's Playwright in an hour](https://www.conf42.com/JavaScript_2024_Gil_Zilberfeld_26_playwright_automation_testing), if the test half is new to you.
- [Safeer C M on open-source SAST with Semgrep](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep), for static checks beyond ESLint.

[Watch Elena Darevskaya's talk](https://www.conf42.com/DevSecOps_2026_Elena_Darevskaya_csp_browser_javascript)

[Watch the talk on YouTube](https://youtu.be/OD1T6D9jhqo).

## Watch the talk

[When Working JavaScript Breaks: Browser Security Policies in Practice](https://www.conf42.com/DevSecOps_2026_Elena_Darevskaya_csp_browser_javascript) at Conf42 DevSecOps 2026.
