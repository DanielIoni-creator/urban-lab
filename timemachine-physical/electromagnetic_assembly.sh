#!/bin/bash
# ⚡ URBAN LAB - Assemblaggio Sistema Elettromagnetico

echo "⚡ URBAN LAB - SISTEMA ELETTROMAGNETICO"
echo "======================================="
echo ""
echo "📋 COMPONENTI:"
echo "   - Bobina Tesla 100kV"
echo "   - 8 Magneti N52"
echo "   - 10 Condensatori 450V"
echo "   - Cavo rame 2.5mm²"
echo ""
echo "🔧 ISTRUZIONI:"
echo "1. Posiziona la bobina Tesla al centro"
echo "2. Installa i magneti agli angoli"
echo "3. Collega i condensatori in parallelo"
echo "4. Salda i cavi di collegamento"
echo "5. Verifica l'isolamento"
echo ""
read -p "✅ Sistema elettromagnetico completato? (s/n): " elettro

if [ "$elettro" = "s" ]; then
    echo "✅ Sistema elettromagnetico completato!"
    echo "📝 Aggiorna il diario:"
    ./assembly_log.sh
fi
