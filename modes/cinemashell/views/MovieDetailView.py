import pygame
from logic.metadata_manager import MetadataManager
from views.PlayerView import PlayerView

class MovieDetailView:
    def __init__(self, renderer, state, movie_name):
        self.renderer = renderer
        self.state = state
        self.movie_name = movie_name
        self.meta = MetadataManager().get_metadata(movie_name)

    def draw(self):
        font = pygame.font.Font(None, 60)
        title = font.render(self.movie_name, True, (255, 255, 255))
        self.renderer.screen.blit(title, (200, 150))

        if self.meta:
            font2 = pygame.font.Font(None, 40)
            overview = font2.render(self.meta.get("overview", "Pas de description"), True, (200, 200, 200))
            self.renderer.screen.blit(overview, (200, 250))

        font3 = pygame.font.Font(None, 40)
        play = font3.render("▶ Lire", True, (255, 255, 255))
        self.renderer.screen.blit(play, (200, 450))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.state.switch_to(PlayerView(self.renderer, self.state, self.movie_name))
