# A platform team of one runs side projects with AI, not on AI

Conf42 Blog, 2026-10-20, updated 2026-11-09. https://www.conf42.com/platform2026/platform-team-of-one-ai-side-projects

In short: Shem Magnezi (Lemonade) at Conf42 Platform Engineering 2026 on running many AI-built side projects alone with minimal launches, recoverable paths and agents.

Coding agents made building cheap. They did not make running a product cheap. At Conf42 Platform Engineering 2026, Shem Magnezi, Senior Staff Engineer at Lemonade and former CTO of the startup Wilco, framed his habit of shipping a side project almost every month as a platform-engineering problem with a team size of one: cut repeated work, make delegation usable, and decide what actually deserves a human.

It's a personal, practical talk, and the most useful parts are his failures.

## The agent will give you the average idea

Shem tested the beach-and-beer fantasy directly. He asked an agent to brainstorm fifty product ideas, pick the best one and run with it, with a small budget and no involvement from him. After more than 24 hours it came back with very basic ideas that got no traction and no income. His conclusion: AI is good at proposing and building, but its ideas, designs and go-to-market plans gravitate to the average. Judgment and context stay with you.

So he pivoted to building things he needed himself, which also supplies the motivation to finish. One example: a Chrome extension to find FIFA World Cup tickets. Scraping FIFA's site turned into a cat-and-mouse game that FIFA won every time, and the agent was (rightly) conservative about workarounds. Shem's own fix was to make it a portal where almost a thousand users each looked up their own data, and the aggregate gave everyone a picture of availability. No agent proposed that.

## Ship the minimum, but protect the recoverable path

His second lesson is about where to spend scarce attention. He used to polish every feature (load, non-English users, power users) for projects that then got no users. Now the first version should take an hour if possible. For a service that turns an old photo into an emotional video, version one was a landing page asking for an email and an image, with Shem doing the work by hand.

Only after a few dozen real orders did he build automation and run ads. Then one TikTok campaign took off overnight, the site fell over under the load, and he lost orders. He still thinks the trade was worth it, but he wished he had load-tested with an agent first and kept the emails so he could follow up.

He learned. On a later Disney World queue-time assistant, the very first paying user hit a broken billing flow, paid and got nothing. Because the email was captured, Shem could fix it and make it right. The rule: things will break, so make sure the paths that matter are recoverable. And every project gets a back office he can drive from his phone: contact users, edit what they received, see and fix errors from a bus.

## Act like a CEO, let the reports find you

The third lesson is the operating model. Shem built a board, somewhere between Trello and Slack, where his agents work. He sets goals at the level of five features by the end of the week, agents break them down, and he approves direction rather than reviewing PRs or Helm chart diffs. Recurring work (say, five new articles every Monday) runs on a schedule as a cron or weekly worker in Claude Code instead of waiting for a reminder.

Guardrails are non-negotiable: caps on cost and tokens, because nobody wants a surprise four-figure bill from a hobby. Agents propose, he gives a thumbs up or down. And information flows the other way from usual: he doesn't open logs, alerts or Datadog; daily and weekly reports push to him, mostly quiet, ideally empty.

## Who should watch

Engineers with a day job and a folder of half-finished ideas, and platform people curious how golden-path thinking scales down to one person and a fleet of agents. Shem is candid that he hasn't quit his job or got rich; the payoff he describes is skills, tools he brought back to work, and World Cup tickets. If you want hard benchmarks on agent frameworks, look elsewhere.

## Related Conf42 talks

- [One flag, no deploy: switching diagnostics and providers at runtime in a one-person production app](https://www.conf42.com/Feature_Flags_2026_Fuad_Laguda_flag_diagnostics_runtime) by Fuad Laguda
- [How to keep your startup's cloud secure when your security team is just you](https://www.conf42.com/DevSecOps_2021_Ryder_Damen_keep_your_startups_cloud_secure_solo) by Ryder Damen
- [The Harness Decides What to Trust: Running AI Coding Loops Without Shipping Fiction](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence) by Ruben Marcus Luz Paschoarelli (MultiVM Labs)

[Watch Shem's talk](https://www.conf42.com/Platform_Engineering_2026_Shem_Magnezi_team_one_ai)

[Watch the talk on YouTube](https://youtu.be/-O8L8q-YggE).

## Watch the talk

[A Platform Team of One, With AI](https://www.conf42.com/Platform_Engineering_2026_Shem_Magnezi_team_one_ai) at Conf42 Platform Engineering 2026.
