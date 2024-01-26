#!/bin/bash

echo "Mise à jour des paquets et installation de dépendances..."

# Mise à jour des paquets
sudo apt update

# Installation de software-properties-common pour add-apt-repository
sudo apt install -y software-properties-common

# Ajout du PPA deadsnakes pour Python
sudo add-apt-repository -y ppa:deadsnakes/ppa

# Mise à jour des paquets après l'ajout du PPA
sudo apt update

echo "Installation de Python 3.9.2..."
# Installation de Python 3.9.2
sudo apt install -y python3.9

echo "Installation du toolkit..."
python3 setup.py install --user

echo "Vérification des dépendances avec pip..."
# Installation des dépendances avec pip
pip install -r requirements.txt

echo "Script terminé."
