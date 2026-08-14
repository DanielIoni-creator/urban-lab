#!/bin/bash
# 🌀 URBAN LAB - Assemblaggio Completo Macchina del Tempo

clear
echo "🌀 URBAN LAB - ASSEMBLAGGIO COMPLETO"
echo "===================================="
echo ""
echo "📋 SEQUENZA DI ASSEMBLAGGIO:"
echo ""
echo "1️⃣  Preparazione postazione"
echo "2️⃣  Struttura Meccanica"
echo "3️⃣  Sistema Elettromagnetico"
echo "4️⃣  Elettronica di Controllo"
echo "5️⃣  Sensori e Cablaggio"
echo "6️⃣  Software e Test"
echo "7️⃣  Test Finale"
echo ""
echo "===================================="
echo ""

# Esegui ogni fase
echo "🏗️ FASE 1: POSTAZIONE"
cat workstation_check.md
read -p "Premi ENTER quando la postazione è pronta..."

echo "🔧 FASE 2: STRUTTURA"
./assembly_log.sh
read -p "Premi ENTER per continuare..."

echo "⚡ FASE 3: ELETTROMAGNETICA"
./electromagnetic_assembly.sh
read -p "Premi ENTER per continuare..."

echo "💻 FASE 4: ELETTRONICA"
./electronics_assembly.sh
read -p "Premi ENTER per continuare..."

echo "🧲 FASE 5: SENSORI"
./sensors_assembly.sh
read -p "Premi ENTER per continuare..."

echo "📡 FASE 6: SOFTWARE"
./software_test.sh
read -p "Premi ENTER per continuare..."

echo "🧪 FASE 7: TEST FINALE"
python3 continuous_test.py

echo ""
echo "🎉 ASSEMBLAGGIO COMPLETATO!"
echo "🌀 La Macchina del Tempo è pronta!"
