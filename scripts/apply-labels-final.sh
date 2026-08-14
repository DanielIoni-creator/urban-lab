#!/bin/bash
# 🏁 URBAN LAB - Script per applicare i label finali

echo "🏁 URBAN LAB - APPLICAZIONE LABELS FINALI"
echo "=========================================="
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

# Repository
REPO="DanielIoni-creator/urban-lab"

echo "📌 Creazione labels finali per: $REPO"
echo ""

# STATO
echo "📊 Creazione labels stato..."
gh label create "final: hardware" --color "B60205" --description "🔧 Assemblaggio e montaggio hardware" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: firmware" --color "D93F0B" --description "📡 Caricamento e test firmware" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: testing" --color "FBCA04" --description "🧪 Test e calibrazione sistema" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: software" --color "1D76DB" --description "💻 Software e integrazione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: documentation" --color "0075CA" --description "📝 Documentazione e video" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: deployment" --color "0E8A16" --description "🚀 Deploy e collaudo finale" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# PRIORITÀ
echo ""
echo "🔴 Creazione labels priorità..."
gh label create "final: critical" --color "B60205" --description "🔴 Bloccante - Deve essere completato subito" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: high" --color "D93F0B" --description "🟡 Alta priorità - Da completare al più presto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: medium" --color "FBCA04" --description "🟢 Priorità media - Da pianificare" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: low" --color "0E8A16" --description "⚪ Bassa priorità - Quando c'è tempo" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# COMPLETAMENTO
echo ""
echo "✅ Creazione labels completamento..."
gh label create "final: ready" --color "0E8A16" --description "✅ Pronto per il test finale" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: in-progress" --color "FBCA04" --description "⏳ In corso di completamento" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: blocked" --color "B60205" --description "🚫 Bloccato - Serve aiuto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: done" --color "0E8A16" --description "🎉 Completato con successo" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# CATEGORIE
echo ""
echo "📂 Creazione labels categorie..."
gh label create "final: assembly" --color "5319E7" --description "🔧 Assemblaggio fisico" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: calibration" --color "F9D0C4" --description "📊 Calibrazione sensori" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: road-test" --color "1D76DB" --description "🛣️ Test su strada" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: performance" --color "A2EEEF" --description "📈 Test prestazioni" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: video" --color "7057FF" --description "🎥 Contenuti video" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "final: publish" --color "008672" --description "📤 Pubblicazione e condivisione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# MILESTONE
echo ""
echo "🏗️ Creazione labels milestone..."
gh label create "milestone: hardware" --color "B60205" --description "🏗️ Milestone Hardware" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: testing" --color "FBCA04" --description "🧪 Milestone Testing" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: validation" --color "0E8A16" --description "✅ Milestone Validazione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "milestone: release" --color "1D76DB" --description "🚀 Milestone Release" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

echo ""
echo "✅ LABELS FINALI CREATI CON SUCCESSO!"
echo ""
echo "📋 LISTA LABELS FINALI:"
gh label list --repo $REPO | grep "final:" || echo "   Nessun label finale trovato"
echo ""
echo "📊 STATISTICHE LABELS:"
echo "   📌 Stato: 6 labels"
echo "   🔴 Priorità: 4 labels"
echo "   ✅ Completamento: 4 labels"
echo "   📂 Categorie: 6 labels"
echo "   🏗️ Milestone: 4 labels"
echo "   📝 TOTALI: 24 labels"
