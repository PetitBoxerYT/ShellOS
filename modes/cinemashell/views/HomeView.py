import pygame
from ui.components.MovieCard import MovieCard
from views.LibraryView import LibraryView
from views.PlaylistView import PlaylistView
from views.SettingsView import SettingsView

class HomeView:
    def __init__(self, renderer, state):
        self.renderer = renderer
        self.state = state

        self.cards = [
            MovieCard("Bibliothèque", "/opt/shellos/modes/cinemashell/assets/posters/library.png", (350, 300)),
            MovieCard("Playlists", "/opt/shellos/modes/cinemashell/assets/posters/playlist.png", (650, 300)),
            MovieCard("Paramètres", "/opt/shellos/modes/cinemashell/assets/posters/settings.png", (950, 300)),
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
            self.state.switch_to(PlaylistView(self.renderer, self.state))
        elif self.selected == 2:
            self.state.switch_to(SettingsView(self.renderer, self.state))
