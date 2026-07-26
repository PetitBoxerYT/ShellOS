import pygame

class GameCard:
    def __init__(self, title, icon_path, position):
        self.title = title
        self.icon = pygame.image.load(icon_path)
        self.position = position

    def draw(self, renderer, focused=False):
        x, y = self.position

        size = (260, 260) if focused else (240, 240)
        icon = pygame.transform.scale(self.icon, size)

        renderer.screen.blit(icon, (x - size[0]//2, y - size[1]//2))

        font = pygame.font.Font(None, 40)
        label = font.render(self.title, True, (221, 230, 255))
        renderer.screen.blit(label, (x - 80, y + 150))
