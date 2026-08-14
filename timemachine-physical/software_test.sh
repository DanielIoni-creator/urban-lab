#!/bin/bash
# 📡 URBAN LAB - Software e Test

echo "📡 URBAN LAB - SOFTWARE E TEST"
echo "==============================="
echo ""
echo "📋 OPERAZIONI:"
echo "1. Carica firmware su Arduino"
echo "2. Installa software su Raspberry Pi"
echo "3. Configura la comunicazione seriale"
echo "4. Avvia il sistema di test"
echo ""
echo "🔧 COMANDI:"
echo "   Arduino: carica arduino_firmware.ino"
echo "   Raspberry: python3 pi_controller.py"
echo "   Test: python3 continuous_test.py"
echo ""
read -p "✅ Software e test completati? (s/n): " software

if [ "$software" = "s" ]; then
    echo "✅ Software e test completati!"
    echo "📝 Aggiorna il diario:"
    ./assembly_log.sh
fi
