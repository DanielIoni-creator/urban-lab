#!/bin/bash
# 🧠 URBAN LAB - Apri le issue di Pytho AI

echo "🧠 URBAN LAB - APERTURA ISSUE PYTHO AI"
echo "======================================"
echo ""

if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI non installato!"
    exit 1
fi

REPO="DanielIoni-creator/urban-lab"

open_issue() {
    local title="$1"
    local body="$2"
    local labels="$3"
    
    echo "📝 Creazione: $title"
    gh issue create --repo $REPO \
        --title "$title" \
        --body "$body" \
        --label "$labels" \
        --assignee DanielIoni-creator
    echo "   ✅ Issue creata!"
}

open_issue "[PA-01] Knowledge Base di Pytho AI" \
"## 📋 Descrizione
Creare la knowledge base di Pytho AI con tutte le informazioni sulla fisica e i viaggi nel tempo.

## 🎯 Obiettivi
- [ ] Aggiungere concetti di relatività
- [ ] Inserire formule fisiche
- [ ] Documentare teorie sui wormhole
- [ ] Aggiungere informazioni sui paradossi
- [ ] Creare database di conoscenza

## 📋 Contenuti
- [ ] Relatività Ristretta
- [ ] Relatività Generale
- [ ] Meccanica Quantistica
- [ ] Teoria delle Stringhe
- [ ] Wormhole e viaggi nel tempo" \
"pytho: critical,pytho: core,milestone: pytho-core"

# Altre issue...
echo ""
echo "✅ TUTTE LE ISSUE PYTHO AI CREATE!"
