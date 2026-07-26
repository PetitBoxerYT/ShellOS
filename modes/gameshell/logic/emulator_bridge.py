import subprocess
import json

class EmulatorBridge:
    def __init__(self):
        self.config = json.load(open("/opt/shellos/modes/gameshell/config/emulators.json"))

    def launch(self, game_path):
        emulator = self.config["default_emulator"]
        subprocess.call(f"{emulator} {game_path}", shell=True)
