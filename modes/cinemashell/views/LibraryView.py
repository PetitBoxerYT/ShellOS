import pygame
from logic.movie_manager import MovieManager
from views.MovieDetailView import MovieDetailView

class LibraryView:
    def __init__(self, renderer, state):
        self.renderer = renderer
        self.state = state
        self.manager = MovieManager()
        self.movies = self.manager.list_movies()
        self.selected = 0

    def draw(self):
        font = pygame.font.Font(None, 50)
        y = 150

        for i, movie in enumerate(self.movies):
            color = (255, 255, 255) if i == self.selected else (180, 180, 180)
            label = font.render(movie, True, color)
            self.renderer.screen.blit(label, (200, y))
            y += 60

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = max(0, self.selected - 1)
            elif event.key == pygame.K_DOWN:
                self.selected = min(len(self.movies) - 1, self.selected + 1)
            elif event.key == pygame.K_RETURN:
                self.state.switch_to(MovieDetailView(self.renderer, self.state, self.movies[self.selected]))
