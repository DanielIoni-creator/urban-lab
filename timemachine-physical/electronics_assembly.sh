#!/bin/bash
# 💻 URBAN LAB - Assemblaggio Elettronica

echo "💻 URBAN LAB - ELETTRONICA DI CONTROLLO"
echo "======================================="
echo ""
echo "📋 COMPONENTI:"
echo "   - Raspberry Pi 5 8GB"
echo "   - Arduino Mega 2560"
echo "   - Display OLED 7\""
echo "   - Alimentatore 5V 3A"
echo ""
echo "🔧 ISTRUZIONI:"
echo "1. Monta Raspberry Pi sul supporto"
echo "2. Fissa Arduino accanto al Raspberry"
echo "3. Collega il display via HDMI"
echo "4. Cabla l'alimentazione"
echo "5. Collega Arduino via USB"
echo ""
read -p "✅ Elettronica completata? (s/n): " elettronica

if [ "$elettronica" = "s" ]; then
    echo "✅ Elettronica completata!"
    echo "📝 Aggiorna il diario:"
    ./assembly_log.sh
fi
