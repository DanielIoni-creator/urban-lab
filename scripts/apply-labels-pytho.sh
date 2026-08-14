#!/bin/bash
# 🧠 URBAN LAB - Applica labels per Pytho AI

echo "🧠 URBAN LAB - APPLICAZIONE LABELS PYTHO AI"
echo "==========================================="
echo ""

if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI non installato!"
    echo "   Installa: sudo apt install gh"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "❌ Non autenticato su GitHub!"
    echo "   Esegui: gh auth login"
    exit 1
fi

REPO="DanielIoni-creator/urban-lab"

echo "📌 Creazione labels Pytho AI per: $REPO"
echo ""

# PRIORITÀ
echo "🔴 Creazione labels priorità..."
gh label create "pytho: critical" --color "B60205" --description "🔴 Essenziale per Pytho AI" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: high" --color "D93F0B" --description "🟡 Alta priorità" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: medium" --color "FBCA04" --description "🟢 Priorità media" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: low" --color "0E8A16" --description "⚪ Bassa priorità" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# AREA
echo ""
echo "📂 Creazione labels area..."
gh label create "pytho: core" --color "1D76DB" --description "🧠 Nucleo dell'assistente AI" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: chat" --color "A2EEEF" --description "💬 Interfaccia conversazionale" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: physics" --color "5319E7" --description "🔬 Fisica e calcoli" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: integration" --color "F9D0C4" --description "🔗 Integrazione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: ui" --color "0075CA" --description "🎨 Interfaccia utente" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: documentation" --color "0E8A16" --description "📚 Documentazione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# STATO
echo ""
echo "📊 Creazione labels stato..."
gh label create "pytho: todo" --color "FBCA04" --description "⏳ Da implementare" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: in-progress" --color "5319E7" --description "🔧 In sviluppo" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: review" --color "F9D0C4" --description "👀 In revisione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: done" --color "0E8A16" --description "✅ Completato" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: blocked" --color "B60205" --description "🚫 Bloccato" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# COMPLESSITÀ
echo ""
echo "💪 Creazione labels complessità..."
gh label create "pytho: easy" --color "0E8A16" --description "😊 Facile" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: medium" --color "FBCA04" --description "🤔 Media" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: hard" --color "B60205" --description "💪 Difficile" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: expert" --color "D93F0B" --description "🔥 Esperto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# CATEGORIE SPECIFICHE
echo ""
echo "🔧 Creazione labels categorie specifiche..."
gh label create "pytho: knowledge" --color "5319E7" --description "📚 Knowledge base" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: personality" --color "A2EEEF" --description "🧠 Personalità" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: forecasting" --color "1D76DB" --description "🔮 Previsioni" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: safety" --color "B60205" --description "🛡️ Sicurezza" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "pytho: performance" --color "FBCA04" --description "⚡ Performance" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# MILESTONE
echo ""
echo "🏗️ Creazione labels milestone..."
gh label create "milestone: pytho-core" --color "1D76DB" --description "🧠 Nucleo Pytho" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: pytho-chat" --color "A2EEEF" --description "💬 Chat Interattiva" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: pytho-integration" --color "F9D0C4" --description "🔗 Integrazione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: pytho-release" --color "0E8A16" --description "🚀 Rilascio Pytho" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

echo ""
echo "✅ LABELS PYTHO AI CREATI!"
echo ""
echo "📊 STATISTICHE:"
echo "   🔴 Priorità: 4"
echo "   📂 Area: 6"
echo "   📊 Stato: 5"
echo "   💪 Complessità: 4"
echo "   🔧 Categorie: 5"
echo "   🏗️ Milestone: 4"
echo "   📝 TOTALI: 28"
