#!/usr/bin/env python3

import pprint
import csv

MAPPING = {
    "SRE": ["sre", "site reliability engineer", "devops", "devops engineer", "ops", "system administrator", "system analist", "system and network supervisor", "sysadm", "admin"],
    "software engineer": ["analyst", "software eng.", "software eng", "developer", "software designer", "web designer", "sde", "consultant", "dev", "sw", "sw eng", "swe", "programmer", "golang dev", "freelancer", "engineer", "qa", "se", "sse", "it", "software"],
    "tech leader": ["architect", "technical lead", "tech lead", "sre lead", "architech", "cto", "c.t.o", "lead", "sa", "cio"],
    "people leader": ["vp", "vice president", "director", "ceo", "team lead", "head", "founder", "manager"],
    "product": [],
    "research": ["professor", "student"],
    "security": ["infosec", "security"],
    "teacher": ["teacher", "coach"],
    "data scientist": ["data scientist", "data"]
}
REVERSED_MAPPING = {}
for base, variants in MAPPING.items():
    REVERSED_MAPPING[base] = base
    for variant in variants:
        REVERSED_MAPPING[variant] = base

def read_csv(path):
    """ Read the pre-process the CSV """
    items = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            item = dict(item)
            items.append(item)
    return items

def preprocess(title):
    title = title.lower()
    title = title.replace("senior ", "")
    title = title.replace("sr ", "")
    title = title.replace("sr. ", "")
    title = title.replace("cloud ", "")
    for general_form in [
        "student",
        "manager",
        "tech lead",
        "architect",
        "analyst",
        "engineer",
        "team lead",
        "developer",
        "consultant",
        "product",
        "head",
        "director",
        "coach",
        "cto",
        "sde",
        "research",
        "devops",
        "lead",
        "founder",
        "ceo",
        "security",
        "professor"
    ]:
        if general_form in title:
            return general_form
    return title

def process_list(raw_list, others):
    counts = dict()
    for member in raw_list:
        title = member.get("Job title")
        title = preprocess(title)
        if title in ["", "-", "n/a", "none", "self", "no", "no job"]:
            normalized_title = "none"
        else:
            normalized_title = REVERSED_MAPPING.get(title, "other")
            if normalized_title == "other":
                others.append(title)
        count = counts.get(normalized_title, 0)
        counts[normalized_title] = count + 1
    return counts

community_list = read_csv("./list.csv")

others = []
counts = process_list(community_list, others)

# remove the ones with less than 1% of the scale
counts_filtered = {
    key: value for key, value in counts.items()
    if value >= len(community_list) / 100
}
counts_filtered = counts

# pprint.pprint(counts_filtered)

print("#"*80)
print(f"People: {len(community_list)}")
people_total = 0
for title in counts_filtered:
    if title != "none":
        people_total += counts_filtered.get(title)
print(f"People with titles: {people_total}")
print(f"Unique titles: {len(counts)}")
print(f"Unique titles filtered: {len(counts_filtered)}")

# calculate the percentages
print("#"*80)
for title in sorted(counts_filtered.keys(), key=counts_filtered.get, reverse=True):
    count = counts_filtered.get(title)
    print(f"{title}: {count} ({count/people_total*100}%)")

print("#"*80)
for title in sorted(counts_filtered.keys(), key=counts_filtered.get, reverse=True):
    if title == "none":
        continue
    print(f"{title}")

print("#"*80)
for title in sorted(counts_filtered.keys(), key=counts_filtered.get, reverse=True):
    if title == "none":
        continue
    count = counts_filtered.get(title)
    print(f"{count}")

# print("#"*80)
# for title in sorted(others):
#     print(title)
