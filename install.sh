#!/bin/bash

echo "========================================"
echo "      Installation de ShellOS"
echo "========================================"

# Vérification des droits
if [ "$EUID" -ne 0 ]; then
    echo "Veuillez lancer ce script avec sudo."
    exit 1
fi

echo "[1/6] Mise à jour du système..."
apt update && apt upgrade -y

echo "[2/6] Installation des dépendances système..."
apt install -y python3 python3-pip python3-venv \
               mpv libmpv-dev \
               libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
               git curl wget

echo "[3/6] Installation des dépendances Python..."
pip3 install pygame requests tmdbsimple

echo "[4/6] Copie de ShellOS dans /opt/shellos..."
mkdir -p /opt/shellos
sudo cp -r bootshell core modes user assets /opt/shellos/

echo "[5/6] Création du lanceur global /usr/bin/shellos..."
cat <<EOF > /usr/bin/shellos
#!/bin/bash
python3 /opt/shellos/core/system/init/init.sh
EOF

chmod +x /usr/bin/shellos

echo "[6/6] (Optionnel) Création du service systemd ShellOS..."
cat <<EOF > /etc/systemd/system/shellos.service
[Unit]
Description=ShellOS Interface
After=network.target

[Service]
ExecStart=/usr/bin/shellos
Restart=always
User=root
 
[Install]
WantedBy=multi-user.target
EOF

echo "Pour activer le démarrage automatique :"
echo "    sudo systemctl enable shellos"
echo "Pour démarrer ShellOS maintenant :"
echo "    sudo systemctl start shellos"

echo "========================================"
echo "Installation terminée !"
echo "Lancez ShellOS avec la commande : shellos"
echo "========================================"
