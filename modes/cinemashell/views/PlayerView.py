import pygame
from core.api.media import play, pause

class PlayerView:
    def __init__(self, renderer, state, movie_name):
        self.renderer = renderer
        self.state = state
        self.movie_name = movie_name
        play(f"/opt/shellos/user/movies/{movie_name}")

    def draw(self):
        font = pygame.font.Font(None, 40)
        label = font.render("Lecture en cours... (Entrée = Pause)", True, (255, 255, 255))
        self.renderer.screen.blit(label, (200, 200))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pause()
