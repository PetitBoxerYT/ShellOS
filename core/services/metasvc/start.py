import tmdbsimple as tmdb

tmdb.API_KEY = "YOUR_API_KEY"

def search_movie(title):
    s = tmdb.Search()
    r = s.movie(query=title)
    return r["results"][0] if r["results"] else None
