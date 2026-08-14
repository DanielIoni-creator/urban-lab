#!/bin/bash
# 🌀 URBAN LAB - Applica labels per Macchina del Tempo

echo "🌀 URBAN LAB - APPLICAZIONE LABELS MACCHINA DEL TEMPO"
echo "======================================================"
echo ""

# Verifica se gh è installato
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) non installato!"
    echo "   Installa: sudo apt install gh"
    echo "   Oppure: https://cli.github.com/"
    exit 1
fi

# Verifica autenticazione
if ! gh auth status &> /dev/null; then
    echo "❌ Non autenticato su GitHub!"
    echo "   Esegui: gh auth login"
    exit 1
fi

REPO="DanielIoni-creator/urban-lab"

echo "📌 Creazione labels Macchina del Tempo per: $REPO"
echo ""

# PRIORITÀ
echo "🔴 Creazione labels priorità..."
gh label create "tm: critical" --color "B60205" --description "🔴 Bloccante - Essenziale per il funzionamento" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: high" --color "D93F0B" --description "🟡 Alta priorità - Da completare al più presto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: medium" --color "FBCA04" --description "🟢 Priorità media - Da pianificare" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: low" --color "0E8A16" --description "⚪ Bassa priorità - Quando c'è tempo" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# AREA
echo ""
echo "📂 Creazione labels area..."
gh label create "tm: hardware" --color "B60205" --description "🔧 Componenti fisici e struttura" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: electronics" --color "1D76DB" --description "⚡ Circuiti e componenti elettronici" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: firmware" --color "D93F0B" --description "📡 Firmware per microcontrollori" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: software" --color "A2EEEF" --description "💻 Software e interfacce" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: testing" --color "FBCA04" --description "🧪 Test e calibrazione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: documentation" --color "0075CA" --description "📝 Documentazione e guide" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# STATO
echo ""
echo "📊 Creazione labels stato..."
gh label create "tm: todo" --color "FBCA04" --description "⏳ Da fare" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: in-progress" --color "5319E7" --description "🔧 In corso" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: review" --color "F9D0C4" --description "👀 In revisione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: done" --color "0E8A16" --description "✅ Completato" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: blocked" --color "B60205" --description "🚫 Bloccato - Serve aiuto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# COMPLESSITÀ
echo ""
echo "💪 Creazione labels complessità..."
gh label create "tm: easy" --color "0E8A16" --description "😊 Facile - Per tutti" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: medium" --color "FBCA04" --description "🤔 Media - Richiede esperienza" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: hard" --color "B60205" --description "💪 Difficile - Richiede expertise" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: expert" --color "D93F0B" --description "🔥 Esperto - Alto livello di competenza" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# CATEGORIE SPECIFICHE
echo ""
echo "🔧 Creazione labels categorie specifiche..."
gh label create "tm: mechanical" --color "5319E7" --description "⚙️ Lavori meccanici e struttura" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: electrical" --color "1D76DB" --description "⚡ Lavori elettrici e cablaggio" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: magnetic" --color "A2EEEF" --description "🧲 Campi magnetici e bobine" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: programming" --color "F9D0C4" --description "💻 Programmazione e codifica" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: safety" --color "B60205" --description "🛡️ Sicurezza e protezione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "tm: integration" --color "FBCA04" --description "🔗 Integrazione dei componenti" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# MILESTONE
echo ""
echo "🏗️ Creazione labels milestone..."
gh label create "milestone: hardware-base" --color "B60205" --description "🏗️ Milestone Hardware Base" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: electronics" --color "D93F0B" --description "⚡ Milestone Elettronica" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: software" --color "1D76DB" --description "💻 Milestone Software" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: testing" --color "FBCA04" --description "🧪 Milestone Testing" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: deployment" --color "0E8A16" --description "🚀 Milestone Deploy" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

echo ""
echo "✅ LABELS MACCHINA DEL TEMPO CREATI!"
echo ""
echo "📊 STATISTICHE LABELS:"
echo "   🔴 Priorità: 4 labels"
echo "   📂 Area: 6 labels"
echo "   📊 Stato: 5 labels"
echo "   💪 Complessità: 4 labels"
echo "   🔧 Categorie: 6 labels"
echo "   🏗️ Milestone: 5 labels"
echo "   📝 TOTALI: 30 labels"
echo ""
echo "📋 LISTA LABELS:"
gh label list --repo $REPO | grep "tm:" || echo "   Nessun label trovato"
