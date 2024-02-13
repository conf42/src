import os
import csv

from .shared import (
    read_talk_csv,
)

SOURCE_DIRECTORY = "./previews"

def get_sources(src=SOURCE_DIRECTORY):
    return [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(src) for f in filenames]

def process_preview(source):
    mapping = dict(
        Title="title",
        Abstract="description",
        Name1="name",
        Company1="organisation",
        url="url",
    )
    talks = read_talk_csv(source)
    for k in mapping:
        if k in talks:
            print("Already processed")
            return
    with open(source, "w") as f:
        writer = csv.DictWriter(f, fieldnames=mapping.keys())
        writer.writeheader()
        for item in talks:
            if item.get("state") != "accepted":
                continue
            writer.writerow({
                key: item.get(value)
                for key, value in mapping.items()
            })

def process_all_previews(src=SOURCE_DIRECTORY):
    for source in get_sources(src):
        if not source.endswith(".csv"):
            continue
        print("Overriding", source)
        process_preview(source)

if __name__ == "__main__":
    process_all_previews()
