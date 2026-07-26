import os
from core.api.files import scan

class GameManager:
    def __init__(self):
        self.games = scan("/opt/shellos/user/games")

    def list_games(self):
        return self.games
