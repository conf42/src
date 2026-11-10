# LLMday Hamburg is about agents that have to ship, not demo

Conf42 Blog, 2026-11-09. https://www.conf42.com/2026-11-09-llmday-hamburg-agents-with-definition-of-done

In short: LLMday Hamburg, November 18 at House of AI - 15 talks from justtrack, vCluster Labs, ScyllaDB, DKB Code Factory and more. CONF42 = 42% off.

LLMday Hamburg runs on November 18, 2026, at House of AI, with fifteen talks on one track about getting agents and models through production instead of through a demo. Speakers come from justtrack, vCluster Labs, ScyllaDB, DKB Code Factory, OMR Reviews, HeyBreez AI, Adjoe and moebel.de, and the code **CONF42** gets Conf42 readers **42% off** the ticket.

## The keynote is honest about what broke

**Gabriel Awad (justtrack GmbH)** opens with *Design, Product, Engineering: What Our AI-Driven Design Workflow Fixed and What It Broke*. justtrack rebuilt its design workflow as scoped agent skills (requirements, research, design, critique, pre-handoff check), and a feature now goes from ticket to clickable prototype in a day. The title promises the other half too, which is the part worth the train ticket.

## Testing is the running theme

A surprising share of the day is about knowing whether the thing works.

- **Jan Kleine-Klatte (MoinMeister)**, *Testing AI Agents Like Self-Driving Cars*, brings nearly a decade of scenario-based testing and safety assurance from autonomous driving to agents.
- **Ebrahim Mirsafian (Lavan Labs)**, *Testing Voice When Your Coding Agent Can't Hear*. They build a voice co-worker with Claude Code, and the coding agent cannot tell whether the voice still works. Somebody has to listen.
- **Miroslav Dzunic (DKB Code Factory)**, *Build Your Own Agentic Factory: Agents Still Need a Definition of Done*. Fifteen years of hearing "done" from humans, now from agents.
- **Izabel Cvetkovic (OMR Reviews)**, *Hallucination Gating for multi-agentic systems*, on a grounding gate that stops a model from inventing a pricing tier the retrieved documents never mention.

## Platforms, serving and memory

**Piotr Zaniewski (vCluster Labs)** argues in *Your Platform Already Has AI Users* that MCP servers, RAG services and agents already hit your platform APIs and need their own identity, context budget and guardrails. **Philip Laine (Kvick)** covers *It's Time to Serve AI Models*: 20-minute cold starts, OOMing nodes and restarting downloads, solved level by level. **Attila Toth (ScyllaDB)** explains the infrastructure behind "For You" feeds at companies like Tripadvisor and Medium, and **Ivan Vokhmin (moebel.de)** walks *From RAG to memory decay*, including how to retire stale context in a vector store.

The rest of the bill covers voice agents in operations (**Faris Qatawneh, HeyBreez AI**), a company brain (**Shekhar Khandelwal, Adjoe**), indirect prompt injection (**Kristaps Pluto**), who owns the harness (**Lior Oren**), an agent-built code foundry (**Marcel Koert, MeloMar-IT**) and spec-driven agentic development (**Pedro Treuer, Netlight Consulting**).

## Why a Conf42 viewer should go

It overlaps neatly with [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026): the people building the platform and the people building the agents are in the same room, arguing about who gets paged. Harness sponsors the day alongside House of AI.

## Register

Doors open at 09:00. Get a ticket on [Luma](https://luma.com/event/evt-A6EmE2vrDywENqn) and enter **CONF42** at checkout for 42% off. The full schedule is on the [LLMday Hamburg page](https://llmday.com/2026-hamburg-q4).
