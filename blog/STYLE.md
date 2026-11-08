# Conf42 blog: house style

Who we write for: engineers who'd rather watch a good talk than read a press release. The post earns its place by
telling them, fast and accurately, why *this* talk is worth 30 minutes, and by sounding like someone who actually
watched it.

## The voice

- **Witty, nerdy, smart.** Dry humour that comes from the subject (a pager at 3am, a YAML indent, a cache that
  remembers too much), never stock jokes about coffee or Mondays. One joke per section at most.
- **Concrete beats clever.** Name the tool, the version, the number, the failure. "Their p99 went from 4s to 300ms"
  beats "dramatic performance gains". If the source has no number, don't invent one; say what was done instead.
- **Answer-first.** The first two sentences carry who spoke, at which Conf42 event, and the single most useful idea.
  Search snippets and AI answers lift exactly that passage.
- **Peer to peer.** Explain like a senior engineer to a colleague: assume competence, skip the 101 unless the talk is
  a 101 (then say so: "a good first talk on eBPF").
- **Short paragraphs, plain verbs.** Uses, cuts, breaks, ships, pages. Not leverages, empowers, unlocks.
- **Honest scope.** If the talk is an intro, say it's an intro. If it's a vendor talk, say whose product it shows.

## Anatomy by type

**talk** (500-900 words)
1. Lede (2-3 sentences): the claim/idea, the speaker with role and company, "at Conf42 <Event> <Year>".
2. The problem it tackles, in the speaker's framing.
3. The sharpest idea(s) - 2-4 short sections with `##` headings that are statements, not labels
   ("Retries are a load test you didn't schedule", not "Retries").
4. Who should watch (and who can skip it).
5. Related: 2-3 other Conf42 talks (linked) that pair with it.
6. Link to the talk page: `[Watch <Speaker>'s talk](https://www.conf42.com/<short_url>)`.

**sponsored** (600-1,500 words): the same anatomy as talk, then a closing `## From <Sponsor>` block with their links
(site, the product page the talk showed if the source names it, docs). Informative first; the product appears where
the talk put it.

**roundup** (600-2,000 words): what the event was about in one paragraph; 3-6 themes, each carried by the talks
that made it (linked, speaker + company); sponsors who joined in (linked); playlist + event page; a closing line on
what's next in the series.

**plug** (350-900 words): what the in-person event is, when and where (venue as "X HQ"), who's speaking (companies,
a few talk titles from the lineup), why a Conf42 viewer would care (the topical overlap), how to register (Luma link),
and for paid events the code: **CONF42 for 42% off**. Free events: say it's free.

**webinar** (400-1,300 words): what was covered, in order; the questions people asked and the answers; next steps
promised; the recording link if there is one; the next webinar if one is scheduled.

## Good vs slop

Slop (do not write like this):

> In today's fast-paced world of cloud-native development, observability is no longer just a nice-to-have - it's
> a game-changer. In this insightful talk, the speaker delves into the ever-evolving landscape of monitoring,
> unlocking powerful strategies to seamlessly supercharge your reliability journey.

Why it's slop: no person, no company, no event, no claim you could disagree with, nine stock phrases.

Good (shape to aim for - the facts here are illustrative, yours come from the source):

> Most teams find out their alerting is broken during the incident it should have caught. At Conf42 SRE 2026,
> Jane Doe, Staff SRE at Example Corp, walks through how her team deleted 70% of their alerts in a quarter and saw
> pages per on-call week drop from 41 to 9 - and which three alerts they had to bring back.

Why it works: a claim in sentence one, full name + role + company + event, real numbers from the talk, a hook
("which three") that makes you want the video.

## Mechanics

- Markdown only; `##` for sections (the page prints the Title as H1). No tables wider than 4 columns.
- Link the first mention of each talk/speaker/sponsor, not every mention.
- Quotes: verbatim from the transcript or abstract, in straight or curly double quotes; the linter checks them.
- Description (meta): one sentence, <=160 chars, with the speaker/company/event and the idea - not "Read more".
- Title: the talk's real claim in plain words, <=70 chars where possible; no clickbait, no "You won't believe".
- Tags: 3-6 lowercase topics (kubernetes, incident-response, llm-evals).
- British or American spelling: follow the speaker's; be consistent within a post.
