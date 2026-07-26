import time
from ui.renderer import Renderer

def show_splash(renderer: Renderer):
    renderer.clear()
    font = pygame.font.Font(None, 120)
    label = font.render("ShellOS", True, (221, 230, 255))
    renderer.screen.blit(label, (500, 300))
    pygame.display.flip()
    time.sleep(1.5)
