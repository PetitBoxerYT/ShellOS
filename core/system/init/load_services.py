import json
import subprocess

BOOTSEQ = "/opt/shellos/core/system/init/boot_sequence.json"

with open(BOOTSEQ) as f:
    seq = json.load(f)

for svc in seq["services"]:
    print(f"[ShellOS] Chargement du service : {svc}")
    subprocess.call(f"python3 /opt/shellos/core/services/{svc}/start.py", shell=True)
