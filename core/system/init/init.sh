#!/bin/bash

echo "[ShellOS] Initialisation du Core..."

python3 /opt/shellos/core/system/init/load_services.py

echo "[ShellOS] Démarrage de BootShell..."
exec /opt/shellos/bootshell/bootshell.sh
