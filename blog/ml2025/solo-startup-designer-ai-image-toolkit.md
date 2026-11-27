# How a solo startup designer used Midjourney, Sora and Figma

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/solo-startup-designer-ai-image-toolkit

In short: Nikita Poloznikov, Head of Design at Jazari, at Conf42 Machine Learning 2025 on the AI image tools that let one designer cover a whole startup.

Being the only designer at a startup means owning pitch decks, ad creatives, user flows and the app UI at the same time, plus the occasional backend logic discussion. Nikita Poloznikov, Head of Design at Jazari, a remit-now-pay-later financial service, told the story at [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) of how he stopped trying to work harder and built an AI image toolkit instead: Stable Diffusion first, then Midjourney 6.1, then OpenAI's image generation in ChatGPT, with Figma for the cleanup.

This is a practitioner's experience report, not an ML talk. There are no benchmarks; there are honest notes on what each tool was good and bad at, from someone who shipped the results in real campaigns.

## Stable Diffusion: good enough for the first pitch deck

In early 2024, Midjourney's web interface was still in closed beta and the main way in was a Discord chat, which Poloznikov found stiff for creative work. He settled on DreamStudio, running Stable Diffusion XL 1.0, for its clean interface and easy prompt experiments. It produced the first assets for early pitch decks and a mock-up of the company's first limited-edition payment card, a prototyping step he calls pivotal for the brand.

The limits were real. Even with negative prompts, getting realistic, non-stereotyped images of people was hard, and outputs came with broken hand anatomy and awkward details that needed heavy retouching. A start, but not something that scaled with a growing company.

## Midjourney 6.1: taste becomes a setting

Version 6.1 and the move to a full web app changed the experience. Two features stand out in his account. Personalisation: rating images during onboarding teaches the model your taste. Aesthetic tuning: stylisation, weirdness and variety controls set how unusual results get. Style references, each with a code, work like a Pinterest board the model can read, so a whole folder of visual DNA can steer new images.

One of his early Midjourney images went into a performance ad on Meta and, by his account, clearly beat the team's standard creatives on click-through. That result pushed the team toward a broader generative content strategy.

The frustration is just as candid. Midjourney often misreads specific instructions about objects, their relationships and textures. At one point he wondered whether hiring a photographer and buying cricket balls would be faster than persuading the model, and the usable image arrived after around 120 variants. Anyone who has argued with a prompt for an afternoon will feel seen.

## Retouch in Figma, because speed matters

Whatever the generator, Poloznikov says the output always needs fixing: weird hands, awkward shadows, inconsistent textures. His advice is to skip heavyweight tools and do quick fixes directly in Figma, which is lightweight and collaborative, since the value comes from iterating quickly rather than perfecting one image. Figma's built-in background remover helps too.

## ChatGPT images: the tool that finally got the brief

OpenAI's image generation, built into ChatGPT, was the breakthrough in his story. With a minimal interface (dimensions, number of outputs, references) and Midjourney-style prompts adapted for it, he found it captured natural skin tones, intentional camera angles, believable expressions and coherent backgrounds without endless re-prompting. That mattered because the brand had shifted toward representing people from many backgrounds. It still struggled with complex scenes of several people interacting in motion, but once controlled it produced polished marketing assets with little editing, plus upscaling and transparent PNG output.

## Lessons that outlast the tool versions

His closing lessons are the reason to watch. Models change fast, so your mindset has to change faster. AI tools empower designers rather than replace them; what separates experts from dabblers is how well they use them. Do not get attached to one tool. And creative intuition, not the gadget, is where a designer's value lies.

## Who should watch

Designers and founders at early-stage companies who need marketing and product visuals without a team, and engineers curious how generative image tools hold up in daily production work. Tool versions will date; the workflow advice will not.

## Related Conf42 talks

- [Design think before you create your next AI product](https://www.conf42.com/Machine_Learning_2024_Arushi_Srivastava_design_think_create), Arushi Srivastava, Conf42 Machine Learning 2024
- [Building a design system in limited timeframes](https://www.conf42.com/Machine_Learning_2024_Elena_Shabanova_building_design_system), Elena Shabanova, Conf42 Machine Learning 2024
- [Easy mode full stack with Figma and AWS Amplify](https://www.conf42.com/JavaScript_2023_Arundeep_Nagaraj_easy_mode_fullstack_figma_aws_amplify), Arundeep Nagaraj, Conf42 JavaScript 2023

[Watch Nikita Poloznikov's talk](https://www.conf42.com/Machine_Learning_2025_Nikita_Poloznikov_toolkit_startup_designer)

[Watch the talk on YouTube](https://youtu.be/Oc8rkzoFHco).

## Watch the talk

[AI-Powered Startup Toolkit for a Product Designer](https://www.conf42.com/Machine_Learning_2025_Nikita_Poloznikov_toolkit_startup_designer) at Conf42 Machine Learning 2025.
