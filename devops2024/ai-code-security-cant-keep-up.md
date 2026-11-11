# AI writes code faster than security can read it

Conf42 Blog, 2024-01-25. https://www.conf42.com/devops2024/ai-code-security-cant-keep-up

In short: Arshan Dabirsiaghi (Pixee) at Conf42 DevOps 2024 on why LLM coding tools outrun AppSec, and three ways to scale - paved roads, RASP and fix-bots.

If autocomplete-style coding assistants already give developers 25 to 60% more throughput, and the security team was outnumbered before any of this, who reviews the extra code? At Conf42 DevOps 2024, Arshan Dabirsiaghi, CTO of Pixee, laid out why LLMs will not secure their own output and proposed three things that can scale with the robots: paved roads, runtime protection and a security tools copilot that triages and fixes findings.

He has spent around 20 years in application security, and the talk reads like it: specific about vulnerability classes, sceptical of hand-waving.

## The robots are coming in three waves

Fill-in-the-middle autocomplete (GitHub Copilot and friends) has the adoption and the studies: 25 to 60% more throughput, depending on how you measure. Drafting assistants that write whole components are newer, with no numbers yet; he guesses 100% purely for argument's sake. Then unguided agents that take an issue, plan, change multiple files and fix their own compile errors, which GitHub had just demoed. Each wave multiplies the code arriving at review.

## Why can't the models just write secure code?

The studies he cites (NYU, Stanford) found that people using assistants produced more insecure code and, worse, were more confident it was secure; one found that about 40% of programs written with Copilot across 89 scenarios had potentially exploitable vulnerabilities. In his own testing, models handle SQL injection because the internet is full of it, but fall apart on slightly rarer classes. They are trained on human code, bugs included.

The deeper problem is the shape of a vulnerability. Untrusted input enters, bounces through custom code, libraries, frameworks, runtime and third-party services, and finally lands where it shouldn't. Most of that path is not in your repo. Codebases do not fit in a context window, embeddings give you search rather than reasoning, and models get confused tracking several variables across many steps. "We've tried to build static analysis tools, code analysis tools, that are purpose built for exactly this problem, and they can't do this fast and accurately," Arshan Dabirsiaghi said at Conf42 DevOps 2024.

## Security is already outnumbered

Even a security-mature lifecycle is full of manual steps: threat modelling, then triaging every SAST, SCA, DAST, IAST and container scan finding, ticket management, product trade-offs. Developers outnumber security around 100 to 1, and he says it is drastically worse at big banks. The two groups are not cross-skilled. So AppSec runs its full programme on maybe 10% of apps, the internet-facing ones, and attackers walk in through the rest; his example is the retailer breached via a contractor HVAC portal.

## Three things that scale

**Make it hard to be insecure.** Paved roads, Netflix's term: frameworks and types that enforce authentication automatically, compile-time demands for access control roles, REST plus JSON only to make XSS patterns harder, one pipeline that forces static analysis on every build. Copilot tends to follow the patterns around it, so if the codebase is paved, the robot uses the pavement. It needs strong DevEx and platform teams, fewer technology stacks and security champions.

**Make insecure code hard to exploit.** A WAF guesses from traffic, far from where the damage happens. RASP puts sensors inside the app and judges behaviour: it sees the actual SQL query, notices user input crossing a token boundary into code and a clause that is always true. Teams running RASP were protected when the Log4j exploits arrived. Business logic flaws remain out of reach.

**Remove the human interruptions.** Most manual work is responding to code scanning results. The vision: a scanner such as Sonar finds a SQL injection, a security copilot triages it and opens a PR with the fix, a human approves, and the next scan is clean. This is where Pixee sits, alongside others he lists. Under it is Codemodder, Pixee's open source codemod library for Java and Python, which orchestrates tools that are good at finding code (Semgrep, Sonar, Fortify, Checkmarx, Contrast) with tools good at changing it (JavaParser, LibCST). His example codemod finds calls to Python's random module and swaps in the secrets module's SystemRandom. The aim is 50 to 100 such codemods.

## Who should watch

AppSec leads planning for Copilot rollouts, platform teams building paved roads, and anyone who suspects the vulnerability backlog is about to grow faster than headcount.

## Related Conf42 talks

- Pixee's Dan D'Avella on [writing Python codemods for fun and profit](https://www.conf42.com/Python_2024_Dan_DAvella_writing_python_codemods_fun_profit) at Conf42 Python 2024.
- Eugene Neelou with [a gentle introduction to LLM security](https://www.conf42.com/Large_Language_Models_LLMs_2024_Eugene_Neelou_gentle_introduction_llm_security) at Conf42 LLMs 2024.
- Safeer C M on [open source SAST with Semgrep](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep) at Conf42 DevSecOps 2025.

[Watch Arshan Dabirsiaghi's talk](https://www.conf42.com/DevOps_2024_Arshan_Dabirsiaghi_army_of_robots)

## From Pixee

Pixee builds an automated fixer for security tool findings and maintains the open source Codemodder library shown in the talk.

- [Pixee website](https://www.pixee.ai/)
- [Codemodder](https://codemodder.io/)
- [Pixeebot GitHub app](https://github.com/apps/pixeebot)

[Watch the talk on YouTube](https://youtu.be/0_MiJkthRwg).

## Watch the talk

[Who Secures Our Code When an Army of Robots Is Writing It?](https://www.conf42.com/DevOps_2024_Arshan_Dabirsiaghi_army_of_robots) at Conf42 DevOps 2024.
