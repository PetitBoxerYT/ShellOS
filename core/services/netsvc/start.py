import requests

def fetch_json(url):
    return requests.get(url).json()
