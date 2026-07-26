import pygame
from ui.components.GameCard import GameCard
from views.LibraryView import LibraryView
from views.ProjectsView import ProjectsView
from views.SettingsView import SettingsView

class HomeView:
    def __init__(self, renderer, state):
        self.renderer = renderer
        self.state = state

        self.cards = [
            GameCard("Jouer", "/opt/shellos/modes/gameshell/assets/icons/play.png", (300, 300)),
            GameCard("Bibliothèque", "/opt/shellos/modes/gameshell/assets/icons/library.png", (600, 300)),
            GameCard("Création", "/opt/shellos/modes/gameshell/assets/icons/dev.png", (900, 300)),
            GameCard("Paramètres", "/opt/shellos/modes/gameshell/assets/icons/settings.png", (1200, 300)),
        ]

        self.selected = 0

    def draw(self):
        for i, card in enumerate(self.cards):
            card.draw(self.renderer, focused=(i == self.selected))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.selected = max(0, self.selected - 1)
            elif event.key == pygame.K_RIGHT:
                self.selected = min(len(self.cards) - 1, self.selected + 1)
            elif event.key == pygame.K_RETURN:
                self.activate()

    def activate(self):
        if self.selected == 0:
            self.state.switch_to(LibraryView(self.renderer, self.state))
        elif self.selected == 1:
            self.state.switch_to(LibraryView(self.renderer, self.state))
        elif self.selected == 2:
            self.state.switch_to(ProjectsView(self.renderer, self.state))
        elif self.selected == 3:
            self.state.switch_to(SettingsView(self.renderer, self.state))
