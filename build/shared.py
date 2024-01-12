import textwrap
import csv

def read_csv(path):
    """ Read the pre-process the CSV """
    items = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            items.append(dict(item))
    return items

def read_talk_csv(path):
    """ Read the pre-process the CSV """
    items = read_csv(path)
    for item in items:
        if "Abstract" in item:
            item["Abstract_s"] = textwrap.shorten(item.get("Abstract",""), 200-len(item.get("title","")), placeholder="...")
            item["Abstract_m"] = textwrap.shorten(item.get("Abstract",""), 400-len(item.get("title","")), placeholder="...")
            items.append(item)
    return items
