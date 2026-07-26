import pygame
import json
from ui.renderer import Renderer
from ui.components.ModeIcon import ModeIcon
from splash import show_splash

CONFIG = json.load(open("/opt/shellos/bootshell/config.json"))

def launch_mode(mode):
    import subprocess
    subprocess.call(f"/opt/shellos/bootshell/launchers/{mode}.sh", shell=True)

def main():
    renderer = Renderer()
    show_splash(renderer)

    modes = [
        ModeIcon("gameshell", "/opt/shellos/bootshell/assets/icons/gameshell.png", (400, 350)),
        ModeIcon("cinemashell", "/opt/shellos/bootshell/assets/icons/cinemashell.png", (800, 350))
    ]

    selected = 0
    running = True
    timeout = CONFIG["timeout_seconds"] * 60

    while running:
        renderer.clear()

        for i, mode in enumerate(modes):
            mode.draw(renderer, focused=(i == selected))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = max(0, selected - 1)
                elif event.key == pygame.K_RIGHT:
                    selected = min(len(modes) - 1, selected + 1)
                elif event.key == pygame.K_RETURN:
                    launch_mode(modes[selected].name)
                    running = False

        timeout -= 1
        if timeout <= 0:
            launch_mode(CONFIG["default_mode"])
            running = False

        renderer.clock.tick(60)

if __name__ == "__main__":
    main()
