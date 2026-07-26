import pygame
from logic.game_manager import GameManager

class LibraryView:
    def __init__(self, renderer, state):
        self.renderer = renderer
        self.state = state
        self.manager = GameManager()
        self.games = self.manager.list_games()
        self.selected = 0

    def draw(self):
        font = pygame.font.Font(None, 50)
        y = 150

        for i, game in enumerate(self.games):
            color = (255, 255, 255) if i == self.selected else (180, 180, 180)
            label = font.render(game, True, color)
            self.renderer.screen.blit(label, (200, y))
            y += 60

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = max(0, self.selected - 1)
            elif event.key == pygame.K_DOWN:
                self.selected = min(len(self.games) - 1, self.selected + 1)
            elif event.key == pygame.K_RETURN:
                print(f"Lancer le jeu : {self.games[self.selected]}")
