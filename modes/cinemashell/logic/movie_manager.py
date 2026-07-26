import os
from core.api.files import scan

class MovieManager:
    def __init__(self):
        self.movies = scan("/opt/shellos/user/movies")

    def list_movies(self):
        return self.movies
