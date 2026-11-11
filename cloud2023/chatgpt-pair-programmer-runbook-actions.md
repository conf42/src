# ChatGPT as the pair programmer for your runbook automations

Conf42 Blog, 2023-03-31. https://www.conf42.com/cloud2023/chatgpt-pair-programmer-runbook-actions

In short: Doug Sillars (unSkript) at Conf42 Cloud Native 2023 on growing runbooks into automations, with ChatGPT drafting the Python actions that get you there

Nobody has seven months to write a runbook for every outage, but almost everyone has ten minutes to automate one step. At Conf42 Cloud Native 2023, [Doug Sillars](https://www.conf42.com/Cloud_Native_2023_Doug_Sillars_pairing_chatbot_building_devops_automations), Head of Developer Relations at unSkript, shows how to grow runbooks into automations gradually, with ChatGPT writing the first draft of the Python and a human fixing the bit it gets wrong.

It is a vendor talk, and the product is unSkript's open-source runbook automation, built on Jupyter notebooks. The ChatGPT part was recorded in the GPT-3 era, which makes its near misses more instructive, not less.

## Why treat runbooks as documentation first?

His starting point is that a runbook is internal documentation: the checklist you follow to provision something or bring a system back. And bad documentation hurts the same inside a company as outside it. His own example: pulling GitHub repository traffic into Postgres, following the docs to the letter, and getting a 403 that blamed the personal access token type when the token simply lacked a permission. Hours lost to one wrong error message. An outdated last step in a runbook does the same thing to an on-call engineer at the worst possible moment.

The cost is real. He quotes a figure that application support and operations take up to 55% of developer time, the manual, tedious work that lands in the inbox but isn't what matters most.

## The seven-month runbook programme most teams can't afford

Two blog posts frame the talk. The first is from an SRE at a gambling site, where downtime is lost money by definition. His boss gave him seven months to write a runbook for every issue and outage, about 1,800 of them, then 10% ongoing time to keep them current. The payoff list is long: faster resolution, simpler escalations (calling Tom becomes the last step of the runbook, not the first), easier onboarding, better training, and eventually automation.

Since few teams get seven months, the second post, Dan Slimmon's *Do Nothing Scripting*, supplies the realistic path: write all the steps down in a script that does nothing but prompt you, then automate one step whenever you have time. "So build the runbook and then as you get time, automate some of the steps," Doug Sillars said at Conf42 Cloud Native 2023. His one addition: put the runbooks where the whole team can reach them, or you stay the person who gets paged.

## What a notebook runbook looks like

That is where Jupyter fits. Markdown cells hold the do-nothing steps, Python cells hold the automated ones, and the notebook is shareable. unSkript ships a Docker image of the open-source version plus a cloud enterprise edition, with a library of pre-built actions for AWS, Google Cloud, Kubernetes, databases, Jira and more, around 30 integrations and a count of actions he puts near 400.

His example is a Kubernetes health check: three pre-built actions list the pods in a namespace and pull their logs, then a small hand-written glue action parses the logs for warnings and posts any it finds to Slack. Credentials are stored once and selected by name, so an action runs without anyone pasting the AWS key. When an action is missing, you extend one (change the open-pull-requests action to list closed ones by editing a single word), write a new one, or write glue.

## ChatGPT gets you close, the error message finishes the job

The two new actions he builds with ChatGPT are both practical. The first tags an EC2 instance with a cost centre, useful for knowing which machines can be shut down when a project ends. ChatGPT produced commented boto3 code that failed on the first run because the client had no region. The error said so, he asked for a region variable set to us-west-2, ChatGPT agreed it had made a mistake, and the call returned a 200. He then turned key, value and region into inputs, so the action behaves like a small API, and it went into the unSkript library.

The second lists Google Cloud VMs and flags which are publicly reachable, a security check he wants to run on a schedule. Here he had to steer ChatGPT to the Google Cloud library unSkript already uses. His closing claim is that ChatGPT can shave 80% off the time to write an action, giving you an almost working prototype to finish yourself.

## Who should watch

SREs and ops engineers with a wiki full of runbooks they don't trust, and anyone curious how an early LLM coding workflow looked when the human still had to supply the region. Doug Sillars also gave the Python-flavoured version of the runbook story, on [automating CloudOps with Jupyter](https://www.conf42.com/Python_2023_Doug_Sillars_automate_cloudops_operations), at Conf42 Python 2023.

Related Conf42 talks:

- Anurag Gupta on [generative AI to fix runbooks](https://www.conf42.com/Incident_Management_2023_Anurag_Gupta_generative_ai_fix_runbooks), Conf42 Incident Management 2023.
- Mandi Walls on [improving automation to reduce toil](https://www.conf42.com/DevOps_2024_Mandi_Walls_improve_automation_reduce_toil), Conf42 DevOps 2024.
- Dylan Etkin on [why not to toil and to automate instead](https://www.conf42.com/DevOps_2024_Dylan_Etkin_dont_toil_automate), Conf42 DevOps 2024.

## From unSkript

unSkript builds runbook automation on Jupyter notebooks, open source with a cloud edition, and the action library the talk draws on.

- [unSkript](https://unskript.com/)
- [Awesome-CloudOps-Automation on GitHub](https://github.com/unskript/Awesome-CloudOps-Automation)

[Watch the talk on YouTube](https://youtu.be/2pqv9UG0STM).

## Watch the talk

[Pairing with a ChatBot: Building DevOps Automations with a little help](https://www.conf42.com/Cloud_Native_2023_Doug_Sillars_pairing_chatbot_building_devops_automations) at Conf42 Cloud Native 2023.
