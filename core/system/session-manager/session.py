import subprocess

class SessionManager:
    def __init__(self):
        self.current_mode = None

    def launch(self, mode):
        self.current_mode = mode
        subprocess.call(f"/opt/shellos/bootshell/launchers/{mode}.sh", shell=True)

    def back_to_bootshell(self):
        subprocess.call("/opt/shellos/bootshell/bootshell.sh", shell=True)
