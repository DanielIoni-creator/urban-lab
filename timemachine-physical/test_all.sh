#!/bin/bash
# 🧪 URBAN LAB - Test Completo della Macchina del Tempo

cd ~/urban-lab-scooter/timemachine-physical

echo "🧪 URBAN LAB - TEST COMPLETO MACCHINA DEL TEMPO"
echo "==============================================="
echo ""

echo "1️⃣ Test Simulatore Base..."
python3 simulator.py

echo ""
echo "2️⃣ Test Viaggio Interstellare..."
python3 interstellar_travel.py << EOF
1
3
