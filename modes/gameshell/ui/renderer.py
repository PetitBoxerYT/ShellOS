import pygame
from core.api.theme import get_color

class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

    def clear(self):
        bg = get_color("background")
        r = int(bg[1:3], 16)
        g = int(bg[3:5], 16)
        b = int(bg[5:7], 16)
        self.screen.fill((r, g, b))
