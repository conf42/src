# A detailed prompt still doesn't make the answer correct

Conf42 Blog, 2026-10-20, updated 2026-11-09. https://www.conf42.com/blog/prompt2026/prompt-engineering-is-evaluating-the-output

In short: Emmanuela Opurum (SoftNet Technologies) at Conf42 Prompt Engineering 2026 on templates, .md rule files and evaluating every AI response.

Claude builds your first page beautifully, so you trust it with the second, and the second quietly pulls in a package your project never uses. That scenario sits at the centre of Emmanuela Opurum's talk at Conf42 Prompt Engineering 2026. Emmanuela, a Solutions Architect at SoftNet Technologies, argues that prompt engineering is the evaluation around the prompt as much as the prompt itself: a good result yesterday earns no trust for today's output.

It's a practical, beginner-friendly talk aimed at people using Claude, Codex and similar tools day to day, not a framework or tooling showcase.

## Prompting vs prompt engineering

Her definitions are simple. Prompting is the instruction you give an agent to get a response. Prompt engineering adds the workflow around it: knowing the project's requirements and standards, and checking every result against them. The trap she names is believing that more detail in the prompt makes the output automatically correct. It doesn't; it only makes it more likely to be shaped the way you want.

Her corollary is blunt: if you don't know what success looks like for the project before you start, you have no business handing the work to an AI, because you'd have nothing to evaluate against.

## Keep the stable parts in a file

The most reusable habit is how she structures prompts. The things that never change in a project (the role, coding style, rules, policies) go into a template, or into the .md instruction files that Claude and Codex read. The chat box then carries only the task at hand. You stop repeating yourself, and the agent stops guessing your standards.

She's careful to add that a reusable template saves prompting time but doesn't produce identical results. Every output still gets checked.

## Relevant context beats more context

Detailed doesn't mean dumping everything. Her example is the CV request: paste a job description and ask the model to build your CV around it, without giving it your experience or skills, and it will invent a candidate for you. The fix is the missing context plus an example, such as an existing CV in the format you like. Irrelevant context, on the other hand, confuses the agent. The model will happily fill any gap you leave, which is the problem.

## Test the cases you didn't think about

Evaluation, for her, is more than the happy path. Test missing fields, partial changes, conflicting instructions and edge cases, and keep running the same test cases every time you update a prompt. She credits that discipline with stopping a prompt that looked fine in several tries from reaching her production build. It's also what lets you answer a lead who asks why you shipped that code.

## Drift: change one line at a time

Her approach to prompt drift is small-step debugging. When the generated page is great except the footer you asked for is missing, she edits only the line that describes the footer, re-runs, and re-evaluates, rather than rewriting the whole prompt. Once it works, the prompt gets saved as a template for similar tasks.

## Secrets never go in the chat box

She closes on security: no API keys, client data, or personal or bank details pasted into a prompt. Keys belong in the platform's secret store; she uses GitHub's secrets for the integrations in her projects.

## Who should watch

Developers and analysts who've moved from occasional chats to relying on an agent for real project work and want a sane routine, and team leads looking for plain-language guidance to hand to newer colleagues. If you already run eval suites and versioned prompts in CI, this will be familiar ground; the related talks below go further into the tooling.

## Related Conf42 talks

- [Harness Engineering for Production LLMs: Eval-as-Code From Day One](https://www.conf42.com/MLOps_2026_Anwar_Khan_eval_llms_harness) by Anwar Khan (John Deere) at Conf42 MLOps 2026.
- [AI-Driven Testing for Conversational AI: LLM-as-Judge, Generative QA, and Scalable Automation](https://www.conf42.com/Prompt_Engineering_2025_Yash_Panjari_testing_conversational_automation) by Yash Panjari (Apple) at Conf42 Prompt Engineering 2025.
- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz (Arato.ai) at Conf42 Large Language Models 2025.

[Watch Emmanuela Opurum's talk](https://www.conf42.com/Prompt_Engineering_2026_Emmanuela_Opurum_workflows_production_reliable) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/tgmh_ecPkh0).

## Watch the talk

[Beyond Better Prompts: Designing Reliable Prompt Engineering Workflows for Production AI](https://www.conf42.com/Prompt_Engineering_2026_Emmanuela_Opurum_workflows_production_reliable) at Conf42 Prompt Engineering 2026.
