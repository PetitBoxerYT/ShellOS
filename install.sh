#!/bin/bash

set -e

echo "==============================================="
echo "        Installation de ShellOS"
echo "==============================================="

# Chemin absolu du dossier où se trouve install.sh
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "[1/6] Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

echo "[2/6] Installation des dépendances système..."
sudo apt install -y python3 python3-pygame mpv git

echo "[3/6] Préparation du dossier /opt/shellos..."
sudo rm -rf /opt/shellos
sudo mkdir -p /opt/shellos

echo "[4/6] Copie des fichiers ShellOS dans /opt/shellos..."
sudo cp -r "$SCRIPT_DIR/bootshell" /opt/shellos/
sudo cp -r "$SCRIPT_DIR/core"      /opt/shellos/
sudo cp -r "$SCRIPT_DIR/modes"     /opt/shellos/
sudo cp -r "$SCRIPT_DIR/user"      /opt/shellos/
sudo cp -r "$SCRIPT_DIR/assets"    /opt/shellos/

echo "[5/6] Création de la commande 'shellos'..."
sudo bash -c 'cat > /usr/bin/shellos <<EOF
#!/bin/bash
/opt/shellos/bootshell/bootshell.sh
EOF'
sudo chmod +x /usr/bin/shellos
sudo chmod +x /opt/shellos/bootshell/bootshell.sh

echo "[6/6] (Optionnel) Création du service systemd ShellOS..."
sudo bash -c 'cat > /etc/systemd/system/shellos.service <<EOF
[Unit]
Description=ShellOS BootShell
After=network.target

[Service]
ExecStart=/usr/bin/shellos
Restart=always

[Install]
WantedBy=multi-user.target
EOF'

echo "==============================================="
echo "Installation terminée !"
echo "==============================================="
echo "Lancez ShellOS avec la commande : shellos"
echo "Pour activer le démarrage automatique :"
echo "  sudo systemctl enable shellos"
echo "Pour démarrer ShellOS maintenant :"
echo "  sudo systemctl start shellos"

