import json
import requests

def check_updates():
    with open("version.json") as f:
        local = json.load(f)

    remote = requests.get(local["update_url"]).json()

    return remote if remote["version"] != local["version"] else None
