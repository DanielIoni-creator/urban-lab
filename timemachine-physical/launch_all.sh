#!/bin/bash
# 🌀 URBAN LAB - Macchina del Tempo - Menu Completo

cd ~/urban-lab-scooter/timemachine-physical

clear
echo "🌀 URBAN LAB - MACCHINA DEL TEMPO"
echo "=================================="
echo ""
echo "Seleziona una modalità:"
echo ""
echo "1. 🚀 Viaggio Avanzato (con effetti)"
echo "2. 📊 Pianificatore Multi-Viaggio"
echo "3. 📈 Grafici Scientifici"
echo "4. 🖥️ Simulatore Base"
echo "5. 🎮 Interfaccia GUI"
echo "6. 🌌 Visualizzazione 3D"
echo "7. 📅 Calcolatore Interattivo"
echo "0. ❌ Esci"
echo ""
read -p "Scelta (0-7): " choice

case $choice in
    1) python3 timemachine_advanced.py ;;
    2) python3 timemachine_multi.py ;;
    3) python3 timemachine_graphs.py ;;
    4) python3 simulator.py ;;
    5) python3 timemachine_gui.py ;;
    6) python3 timemachine_3d.py ;;
    7) python3 calcola_viaggio.py ;;
    0) echo "Arrivederci! 🌀"; exit 0 ;;
    *) echo "Scelta non valida!" ;;
esac

echo ""
read -p "Premi ENTER per continuare..."
exec $0
