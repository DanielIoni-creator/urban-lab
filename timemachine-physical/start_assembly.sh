#!/bin/bash
# 🌀 URBAN LAB - Avvia l'assemblaggio

clear
echo "🌀 URBAN LAB - MACCHINA DEL TEMPO"
echo "=================================="
echo ""
echo "📋 FASE DI ASSEMBLAGGIO"
echo ""
echo "1️⃣  Avvia checklist interattiva"
echo "2️⃣  Avvia test continuo componenti"
echo "3️⃣  Mostra piano assemblaggio"
echo "4️⃣  Avvia simulatore Macchina del Tempo"
echo "0️⃣  Esci"
echo ""
read -p "Scelta: " scelta

case $scelta in
    1) ./assembly_checklist.sh ;;
    2) python3 continuous_test.py ;;
    3) cat ASSEMBLY_PLAN.md ;;
    4) python3 timemachine_advanced_fixed.py ;;
    0) echo "Arrivederci! 🌀"; exit 0 ;;
    *) echo "Scelta non valida!" ;;
esac
