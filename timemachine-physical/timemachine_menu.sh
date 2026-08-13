#!/bin/bash
# 🌀 URBAN LAB - Macchina del Tempo - Menu Avanzato

cd ~/urban-lab-scooter/timemachine-physical

clear
echo "🌀 URBAN LAB - MACCHINA DEL TEMPO AVANZATA"
echo "==========================================="
echo ""
echo "🌌 MODALITÀ DI VIAGGIO:"
echo ""
echo "1. 🚀 Viaggio nel Tempo Base"
echo "2. 🌟 Viaggio Interstellare"
echo "3. ⚡ Viaggio Avanzato (con effetti)"
echo "4. 📊 Pianificatore Multi-Viaggio"
echo ""
echo "🔬 MODALITÀ DI STUDIO:"
echo ""
echo "5. 📈 Grafici Scientifici"
echo "6. 🌀 Simulatore Paradossi"
echo "7. 📚 Teorie Alternative"
echo ""
echo "🖥️ INTERFACCE:"
echo ""
echo "8. 🎮 Interfaccia GUI"
echo "9. 🌌 Visualizzazione 3D"
echo "10. 📅 Calcolatore Interattivo"
echo ""
echo "0. ❌ Esci"
echo ""
read -p "Scelta (0-10): " choice

case $choice in
    1) python3 simulator.py ;;
    2) python3 interstellar_travel.py ;;
    3) python3 timemachine_advanced.py ;;
    4) python3 timemachine_multi.py ;;
    5) python3 timemachine_graphs.py ;;
    6) python3 temporal_paradox.py ;;
    7) python3 alternative_theories.py ;;
    8) python3 timemachine_gui.py ;;
    9) python3 timemachine_3d.py ;;
    10) python3 calcola_viaggio.py ;;
    0) echo "Arrivederci! 🌀"; exit 0 ;;
    *) echo "Scelta non valida!" ;;
esac

echo ""
read -p "Premi ENTER per continuare..."
exec $0
