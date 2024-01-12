#!/usr/bin/env python3

from collections import defaultdict
import yaml

# load the context from the metadata file
context = dict()
with open('metadata.yml') as f:
    context = yaml.load(f, Loader=yaml.FullLoader)

events = context.get("events")
counts = defaultdict(dict)
for event in events:
    d = event.get("date")
    event["year"] = d.year
    for sponsor_lvl, sponsors in event.get("sponsors", {}).items():
        counts[event["year"]][sponsor_lvl] = counts[event["year"]].get(sponsor_lvl, 0) + len(sponsors)

for year, stats in counts.items():
    print(f"{year}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
