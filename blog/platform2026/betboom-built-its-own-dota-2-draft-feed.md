# BetBoom's own Dota 2 draft feed took conversion from 8.4% to 31.2%

Conf42 Blog, 2026-10-14, updated 2026-11-09. https://www.conf42.com/blog/platform2026/betboom-built-its-own-dota-2-draft-feed

In short: Egor Kolovertnykh of BetBoom at Conf42 Platform Engineering 2026 on turning Dota 2 Game State Integration snapshots into a live draft feed.

A live widget that runs five minutes behind the game is a history lesson, not a live widget. At Conf42 Platform Engineering 2026, Egor Kolovertnykh, Senior Backend Developer at BetBoom, showed how his team stopped waiting on an external data provider for Dota 2 pick-and-ban updates and built their own source straight from the game client, in Go and Postgres, in about six weeks.

The payoff he reported is the kind product managers frame and hang on the wall: the widget fed by the in-house source got more than five million views during 2024, and its conversion rate was 31.2% against 8.4% for the partner-fed one.

## The data source is a person running Dota

Dota 2 has a feature called Game State Integration (GSI). Drop a config file into the game folder with your endpoint, and the client POSTs its current state as JSON, picks and bans included. So BetBoom's "telemetry platform" starts on an operator's computer: someone joins the match, the game talks, the backend listens.

That framing matters for the rest of the talk. Half the engineering is about the human in the loop. Configs ship with a signed JWT carrying BetBoom's event ID and config ID, because the Dota game ID doesn't exist yet when the operator prepares the file. One config covers a whole series of maps. A new config starts in test mode: the operator opens a replay of any match, the service confirms picks and bans arrive, and only then does the config go live. The replay's game ID is kept aside so yesterday's heroes never show up on today's match page.

## Snapshots are state; users want events

GSI doesn't send "team A banned Pudge". It sends the whole current board: pick and ban slots per team, filling up as the draft goes, with every earlier choice repeated in every request. Ten identical snapshots must produce the same widget, not ten new events.

Egor's fix was to encode the draft rules as an ordered list of steps (which side, pick or ban, which slot), infer which team went first by checking which ordering fits the observed slots, and then merge each snapshot into one array of actions. Known actions stay in place; new filled slots append. A neat side effect: if the operator joins late, the first snapshot already contains the earlier picks, so the draft can be rebuilt from it with no special catch-up path. State lived in a Go map behind a mutex, one entry per game, with configs and event links in Postgres.

Then production taught the usual lesson. Dota has both Captain's Mode and Captain's Draft, with different action orders, and to the backend they look nearly identical. The draft type went into the config, chosen by the operator. As Egor put it, when you work with a game you eventually have to check which rules the other side is playing by today.

## Keep the old contract, win on priority

The part platform engineers should steal: the new service spoke the exact contract the platform already used for partner data. Teams, ordered actions, widget state. To everything downstream it was just another source. New draft modes stayed inside Egor's backend; nothing else had to learn Dota rules.

That made rollout gradual. At first a source was chosen per event; later the in-house data became the first choice, with the partner feed as fallback when it wasn't available. No big-bang migration of every match page, and the partner contract stayed alive.

## Replays as a test harness

Replays did double duty in development. Change the code, reopen the same game, watch the draft again, compare. No waiting for the next tournament. Front-end developers and QA sat with the game on one screen and the website on the other, checking right hero, right team, right position, pick or ban. Watching Dota officially became part of the job, which is the most enviable acceptance-test setup at this conference.

## Who should watch

Anyone building a real-time pipeline from a source that only gives you snapshots: game telemetry, IoT devices, polling APIs. It's also a tidy case study in replacing a vendor feed without breaking the consumers of it. If you want deep Kafka or scale numbers, this isn't that talk; it's a focused, honest build story.

## Related Conf42 talks

- [Building a scalable ecosystem for high-loaded multiplayer game](https://www.conf42.com/Platform_Engineering_2023_Dmitrii_Ivashchenko_building_a_scalable_ecosystem_for_highloaded_multiplay) by Dmitrii Ivashchenko (MY.GAMES)
- [Pushing Your Streaming Platform to the Limit](https://www.conf42.com/Chaos_Engineering_2024_Elad_Leev_pushing_streaming_platform) by Elad Leev (Dojo)
- [Building Self-Healing Real-Time Streaming Pipelines with Go and AI](https://www.conf42.com/Golang_2026_Yogesh_Pugazhendhi_Duraisamy_Rajamani_building_self_healing) from Ford Motor Company

[Watch Egor's talk](https://www.conf42.com/Platform_Engineering_2026_Egor_Kolovertnykh_telemetry_game_conversion)

[Watch the talk on YouTube](https://youtu.be/kZwvx7hi5f0).

## Watch the talk

[Building an In-House Real-Time Telemetry Platform: From Raw Game State Integration to 31% Conversion Gains](https://www.conf42.com/Platform_Engineering_2026_Egor_Kolovertnykh_telemetry_game_conversion) at Conf42 Platform Engineering 2026.
