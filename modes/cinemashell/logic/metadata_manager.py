# TODO: implement
from core.api.meta import search_movie

class MetadataManager:
    def get_metadata(self, title):
        return search_movie(title)
