import pygame
from ui.renderer import Renderer
from views.HomeView import HomeView

class CinemaShellUI:
    def __init__(self, state):
        self.renderer = Renderer()
        self.state = state
        self.current_view = HomeView(self.renderer, self.state)

    def run(self):
        running = True

        while running:
            self.renderer.clear()
            self.current_view.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.current_view.handle_event(event)

            if self.state.next_view is not None:
                self.current_view = self.state.next_view
                self.state.next_view = None

            self.renderer.clock.tick(60)
