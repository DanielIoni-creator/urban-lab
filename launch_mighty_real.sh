#!/bin/bash
# 🏭 Urban Lab - Lancia MIGHTY sul monopattino reale

echo "🏭 URBAN LAB - MIGHTY sul Monopattino Reale"
echo "==========================================="
echo ""

# Attiva ambiente
source ~/urban-lab-scooter/activate_urbanlab.sh

# Verifica connessione ESP32
if [ -e /dev/ttyUSB0 ]; then
    echo "✅ ESP32 trovato su /dev/ttyUSB0"
    PORT="/dev/ttyUSB0"
elif [ -e /dev/ttyUSB1 ]; then
    echo "✅ ESP32 trovato su /dev/ttyUSB1"
    PORT="/dev/ttyUSB1"
else
    echo "⚠️ ESP32 non trovato! Usa modalità simulata."
    PORT=""
fi

# Avvia il bridge hardware
if [ -n "$PORT" ]; then
    echo "🔌 Avvio bridge con ESP32..."
    python3 ~/urban-lab-scooter/mighty/scripts/hardware_bridge.py --port $PORT
else
    echo "🔄 Avvio bridge in modalità simulata..."
    python3 ~/urban-lab-scooter/mighty/scripts/hardware_bridge_simple.py
fi
