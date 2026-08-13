#!/bin/bash
# 🌀 URBAN LAB - Macchina del Tempo - Menu Super Avanzato

cd ~/urban-lab-scooter/timemachine-physical

clear
echo "🌀 URBAN LAB - MACCHINA DEL TEMPO ULTIMATE"
echo "==========================================="
echo ""
echo "🚀 VIAGGI NEL TEMPO:"
echo ""
echo "1.  ⏳ Viaggio nel Futuro (avanzato)"
echo "2.  📜 Viaggio nel Passato (teorico)"
echo "3.  🌟 Viaggio Interstellare"
echo "4.  ⚛️ Viaggio Quantistico"
echo "5.  🌌 Multiverso"
echo ""
echo "🔬 STRUMENTI DI ANALISI:"
echo ""
echo "6.  📊 Calcolatore Viaggi"
echo "7.  📈 Grafici Scientifici"
echo "8.  🌀 Simulatore Paradossi"
echo "9.  📚 Teorie Alternative"
echo ""
echo "🖥️ INTERFACCE:"
echo ""
echo "10. 🎮 Interfaccia GUI"
echo "11. 🌌 Visualizzazione 3D"
echo "12. 📅 Calcolatore Interattivo"
echo ""
echo "0.  ❌ Esci"
echo ""
read -p "Scelta (0-12): " choice

case $choice in
    1) python3 timemachine_advanced_fixed.py ;;
    2) python3 past_travel.py ;;
    3) python3 interstellar_travel.py ;;
    4) python3 quantum_time.py ;;
    5) python3 multiverse.py ;;
    6) python3 calcola_viaggio.py ;;
    7) python3 timemachine_graphs.py ;;
    8) python3 temporal_paradox.py ;;
    9) python3 alternative_theories.py ;;
    10) python3 timemachine_gui.py ;;
    11) python3 timemachine_3d.py ;;
    12) python3 calcola_viaggio.py ;;
    0) echo "Arrivederci! 🌀"; exit 0 ;;
    *) echo "Scelta non valida!" ;;
esac

echo ""
read -p "Premi ENTER per continuare..."
exec $0
