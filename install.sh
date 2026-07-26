#!/bin/bash

echo "==============================================="
echo "        Installation de ShellOS"
echo "==============================================="

# 1. Mise à jour du système
echo "[1/6] Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

# 2. Installation des dépendances système
echo "[2/6] Installation des dépendances système..."
sudo apt install -y python3 python3-pip mpv git

# 3. Installation des dépendances Python
echo "[3/6] Installation des dépendances Python..."
pip3 install pygame

# 4. Création du dossier /opt/shellos
echo "[4/6] Copie des fichiers ShellOS dans /opt/shellos..."
sudo rm -rf /opt/shellos
sudo mkdir -p /opt/shellos

# Copie des dossiers du projet
sudo cp -r bootshell /opt/shellos/
sudo cp -r core /opt/shellos/
sudo cp -r modes /opt/shellos/
sudo cp -r user /opt/shellos/
sudo cp -r assets /opt/shellos/

# 5. Création de la commande shellos
echo "[5/6] Création de la commande 'shellos'..."
sudo bash -c 'echo "#!/bin/bash" > /usr/bin/shellos'
sudo bash -c 'echo "python3 /opt/shellos/bootshell/main.py" >> /usr/bin/shellos'
sudo chmod +x /usr/bin/shellos

# 6. (Optionnel) Création du service systemd
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

echo "Pour activer le démarrage automatique :"
echo "  sudo systemctl enable shellos"
echo "Pour démarrer ShellOS maintenant :"
echo "  sudo systemctl start shellos"

echo "==============================================="
echo "Installation terminée !"
echo "Lancez ShellOS avec la commande : shellos"
echo "==============================================="
