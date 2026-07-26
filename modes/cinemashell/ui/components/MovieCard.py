import pygame

class MovieCard:
    def __init__(self, title, poster_path, position):
        self.title = title
        self.poster = pygame.image.load(poster_path)
        self.position = position

    def draw(self, renderer, focused=False):
        x, y = self.position

        size = (260, 380) if focused else (240, 360)
        poster = pygame.transform.scale(self.poster, size)

        renderer.screen.blit(poster, (x - size[0]//2, y - size[1]//2))

        font = pygame.font.Font(None, 40)
        label = font.render(self.title, True, (221, 230, 255))
        renderer.screen.blit(label, (x - 80, y + 200))
