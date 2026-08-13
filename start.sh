#!/bin/bash
echo "🛴 URBAN LAB SCOOTER - MENU PRINCIPALE"
echo "========================================"
echo ""
echo "1. 🧪 Test Sensori (Software)"
echo "2. 📡 Firmware ESP32 (Compila)"
echo "3. 🔌 Firmware ESP32 (Carica)"
echo "4. 🤖 AI Controller"
echo "5. 📊 Dashboard Monitor"
echo "6. 📁 Documentazione"
echo "0. Esci"
echo ""
read -p "Scegli: " choice

case $choice in
    1)
        python3 test_sensors.py
        ;;
    2)
        cd firmware/esp32 && pio run
        ;;
    3)
        cd firmware/esp32 && pio run -t upload
        ;;
    4)
        python3 ai_scooter_controller.py
        ;;
    5)
        echo "📊 Avvio dashboard in corso..."
        # python3 dashboard.py
        ;;
    6)
        ls -la docs/
        ;;
    0)
        echo "👋 Arrivederci!"
        exit 0
        ;;
    *)
        echo "❌ Scelta non valida"
        ;;
esac
