import pygame

class ModeIcon:
    def __init__(self, name, icon_path, position):
        self.name = name
        self.icon = pygame.image.load(icon_path)
        self.position = position

    def draw(self, renderer, focused=False):
        x, y = self.position
        if focused:
            icon = pygame.transform.scale(self.icon, (260, 260))
        else:
            icon = pygame.transform.scale(self.icon, (240, 240))

        renderer.screen.blit(icon, (x - 120, y - 120))

        font = pygame.font.Font(None, 50)
        label = font.render(self.name, True, (221, 230, 255))
        renderer.screen.blit(label, (x - 80, y + 150))
