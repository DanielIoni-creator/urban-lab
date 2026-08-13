#!/bin/bash
# 🌀 URBAN LAB - Lancia la Macchina del Tempo

echo "🌀 URBAN LAB - Macchina del Tempo"
echo "=================================="
echo ""
echo "Scegli la versione:"
echo "1. Simulatore base (testuale)"
echo "2. Visualizzazione 3D"
echo "3. Interfaccia GUI"
echo "4. Calcolatore interattivo"
echo ""
read -p "Scelta (1-4): " choice

case $choice in
    1)
        python3 simulator.py
        ;;
    2)
        python3 timemachine_3d.py
        ;;
    3)
        python3 timemachine_gui.py
        ;;
    4)
        python3 calcola_viaggio.py
        ;;
    *)
        echo "Scelta non valida"
        ;;
esac
