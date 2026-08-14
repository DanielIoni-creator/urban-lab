#!/bin/bash
# 🧲 URBAN LAB - Sensori e Cablaggio

echo "🧲 URBAN LAB - SENSORI E CABLAGGIO"
echo "=================================="
echo ""
echo "📋 COMPONENTI:"
echo "   - 4 Sensori Hall A1324"
echo "   - 4 Sensori DS18B20"
echo "   - Cavi e connettori"
echo ""
echo "🔧 ISTRUZIONI:"
echo "1. Posiziona i sensori Hall (N/S/E/O)"
echo "2. Installa i sensori temperatura"
echo "3. Collega i cavi ad Arduino"
echo "4. Fissa i cablaggi con fascette"
echo "5. Verifica le connessioni"
echo ""
read -p "✅ Sensori e cablaggio completati? (s/n): " sensori

if [ "$sensori" = "s" ]; then
    echo "✅ Sensori completati!"
    echo "📝 Aggiorna il diario:"
    ./assembly_log.sh
fi
