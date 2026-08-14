#!/bin/bash
# 📝 URBAN LAB - Diario di Bordo Assemblaggio

LOG_FILE="assembly_log_$(date +%Y%m%d).txt"

echo "📝 URBAN LAB - DIARIO DI BORDO ASSEMBLAGGIO"
echo "==========================================="
echo ""
echo "📅 Data: $(date)"
echo "⏰ Ora: $(date +%H:%M)"
echo ""
echo "📋 Inserisci il tuo aggiornamento:"
read -p "> " update

echo "[$(date +%H:%M)] $update" >> $LOG_FILE
echo ""
echo "✅ Aggiornamento salvato!"
echo ""
echo "📊 ULTIMI AGGIORNAMENTI:"
tail -5 $LOG_FILE
