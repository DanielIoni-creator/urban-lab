#!/bin/bash
# 📊 URBAN LAB - Tracker Progresso Macchina del Tempo

echo "🌀 URBAN LAB - PROGRESSO MACCHINA DEL TEMPO"
echo "==========================================="
echo ""

# Fasi
declare -A fasi=(
    ["Preparazione"]="0"
    ["Struttura"]="0"
    ["Elettromagnetica"]="0"
    ["Elettronica"]="0"
    ["Software"]="0"
    ["Test"]="0"
)

# Mostra progresso
echo "📊 STATO ATTUALE:"
for fase in "${!fasi[@]}"; do
    progresso=${fasi[$fase]}
    barra=$(printf "%${progresso}s" | tr ' ' '█')
    echo "   $fase: [$barra${progresso}%]"
done
echo ""
echo "📋 Prossima fase: ${!fasi[@]}"
echo ""
echo "🔄 Aggiorna progresso:"
read -p "Fase completata: " fase_completata
read -p "Progresso (%): " progresso_nuovo
echo "✅ Aggiornato!"
