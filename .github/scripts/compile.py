#!/bin/env python

import glob
import json
from os import path

root = path.join(path.dirname(__file__), "../..")

def handle_badges(file):
    with open(file) as f:
        id = path.splitext(path.basename(file))[0]
        badges = json.load(f)
        return (id, badges)

def main():
    guildFiles = glob.glob(path.join(root, "guilds/*.json"))
    userFiles = glob.glob(path.join(root, "users/*.json"))
    
    guilds = dict([handle_badges(f) for f in guildFiles])
    users = dict([handle_badges(f) for f in userFiles])

    data = {
        "guilds": guilds,
        "users": users,
    }

    with open(path.join(root, ".builds/badges.json"), "w") as f:
        json.dump(data, f)
    with open(path.join(root, ".builds/badges.pretty.json"), "w") as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()
