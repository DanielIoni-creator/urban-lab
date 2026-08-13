#!/bin/bash
# 🌀 URBAN LAB - Avvia il Portale del Tempo Fisico

echo "🌀 URBAN LAB - Portale del Tempo Fisico"
echo "========================================"
echo ""

# Attiva ambiente
source ~/urban-lab-scooter/activate_urbanlab.sh

# Avvia il server
cd ~/urban-lab-scooter/portal
python3 server.py
