# Abstract proofreading pass

A daily pass (cloud routine "Abstracts - proofreading pass", 03:00 UTC, Fable) over the talk abstracts of
SREday, LLMday, PLATFORMday and Conf42. PEC is not included.

The Google Sheets are the source of truth. A fix is written into the sheet cell first; only then is the same
text copied into the repo CSV (`<event>/_db/talks.csv`, `_db/<EVENT>_<year>.csv`). An abstract is read once:
`state.json` holds a hash of every abstract text already dealt with, so a cell comes back only when its text
changes.

## What to fix

- Typos, spelling, grammar, missing or doubled words, punctuation and spacing slips.
- Broken markdown: unclosed `**`/`_`, bullets glued into one line (`• a • b`, `- a - b`), `-item` / `##Title`
  without the space, literal `\n`, HTML entities or tags, stray escape characters, mojibake.
- Walls of text: a paragraph of roughly 6+ sentences, or one with several distinct parts (problem, approach,
  takeaways), gets blank lines between the parts. Do not reorder sentences.
- A list written as running text or as bare lines ("You will learn: X, Y; Z" stays; "1) ... 2) ... 3) ..." or
  lines that are clearly list items become a markdown list). Abstracts render as markdown on every site:
  a paragraph break is an empty line, a bullet is `- `. A single newline renders as a space, so lines the
  author meant as separate lines need a blank line or a bullet.
- Leading/trailing blank lines, runs of 3+ newlines, trailing spaces.

## What never to do

- No rewording, tightening, restructuring or "improving" the style. The author's voice, claims, hype,
  first person, jokes and emoji stay exactly as written.
- Nothing added, nothing removed: no new sentences, headings, bold or summaries; no cut sentences.
- Keep the author's spelling variant (British or American), their terminology, product names and numbers.
  Fix a brand's capitalisation only when it is plainly a slip (kubernetes -> Kubernetes).
- Keep the language: a Portuguese or Spanish abstract is proofread in that language, never translated.
- Links, code and names are copied character for character.
- Only the abstract column. Titles, bios, names, every other cell and every formula stay untouched.
- When unsure whether something is a mistake, leave it. A clean abstract is left exactly as it is.

`finish` enforces this: a cell whose words changed by more than a proofread would explain is refused and
must be put back (`restore.json`).

## Procedure (the routine follows this; a person can too)

Checkouts side by side: `conf42` (github.com/conf42/src, may be called `src`), `website` or `sreday`
(sreday/sreday), `llmday`, `platformday`. `git pull --rebase` each one on main first.

1. `python3 proofread/proofread.py scan --limit 60` (from the conf42 checkout; add `--root <dir>` if the
   checkouts are not next to each other). 0 pending = nothing to do, stop.
2. `python3 proofread/proofread.py show` and read every abstract against the rules above.
3. For each abstract that needs a fix, write the corrected text into its cell with the Google Sheets
   connector: `update_values`, spreadsheet = the id shown by scan, range = the one printed by show
   (for example `'Amsterdam 2026 Q4'!M12`), values = `[[<whole corrected text>]]`. One cell per call, the
   abstract cell only. Paragraph breaks are real newlines inside the string. Leave clean abstracts alone.
4. `python3 proofread/proofread.py finish`. It re-reads the sheets, records clean cells, refuses rewrites and
   patches the CSVs (abstract field only, byte-safe). If it lists refused cells, write each `value` from
   `proofread/restore.json` back into its range, then run `finish` again. If it says a cell still holds the
   old text right after you wrote it, wait a minute and run `finish` again (the export lags a little).
5. Commit and push main in every repo that changed (site repos: only `*/_db/talks.csv`; conf42:
   `_db/*.csv` and `proofread/state.json`). Message: `Proofread abstracts: <events>`. Never force-push; if
   the push is rejected, `git pull --rebase` and push again.
6. Append one line per run to `proofread/LOG.md` (date, events, fixed / clean / refused counts) in the same
   conf42 commit.

Never edit a CSV by hand, never write to the sheet outside the abstract cells listed by `show`, and never
touch `past/` folders.
