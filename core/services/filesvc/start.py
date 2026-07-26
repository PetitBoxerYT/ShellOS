import os

def scan(path):
    if not os.path.exists(path):
        return []
    return [f for f in os.listdir(path)]
