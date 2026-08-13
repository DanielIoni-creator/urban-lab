# 🏷️ LABELS URBAN LAB

## 📋 CATEGORIE

### 🔴 PRIORITÀ
| Label | Colore | Descrizione |
|-------|--------|-------------|
| `priority: critical` | #B60205 | 🚨 Bloccante - Risolvere subito |
| `priority: high` | #D93F0B | 🔴 Alta priorità |
| `priority: medium` | #FBCA04 | 🟡 Priorità media |
| `priority: low` | #0E8A16 | 🟢 Bassa priorità |

### 📌 TIPOLOGIA
| Label | Colore | Descrizione |
|-------|--------|-------------|
| `type: bug` | #B60205 | 🐛 Bug da correggere |
| `type: feature` | #1D76DB | ✨ Nuova funzionalità |
| `type: enhancement` | #A2EEEF | 🔧 Miglioramento |
| `type: documentation` | #0075CA | 📝 Documentazione |
| `type: testing` | #F9D0C4 | 🧪 Test e QA |
| `type: research` | #5319E7 | 🔬 Ricerca |

### 📂 AREA
| Label | Colore | Descrizione |
|-------|--------|-------------|
| `area: 3d-printing` | #FBCA04 | 🖨️ Stampa 3D |
| `area: firmware` | #B60205 | 📡 Firmware ESP32 |
| `area: rl` | #1D76DB | 🧠 Reinforcement Learning |
| `area: app` | #0E8A16 | 📱 App mobile |
| `area: dashboard` | #5319E7 | 🌐 Dashboard web |
| `area: legal` | #F9D0C4 | ⚖️ Documentazione legale |
| `area: hardware` | #D93F0B | 🔧 Hardware |
| `area: documentation` | #0075CA | 📚 Documentazione |

### 📊 STATO
| Label | Colore | Descrizione |
|-------|--------|-------------|
| `status: done` | #0E8A16 | ✅ Completato |
| `status: in-progress` | #FBCA04 | ⏳ In corso |
| `status: blocked` | #B60205 | 🚫 Bloccato |
| `status: review` | #5319E7 | 👀 In revisione |
| `status: needs-help` | #D93F0B | 🆘 Serve aiuto |

### 💪 COMPLESSITÀ
| Label | Colore | Descrizione |
|-------|--------|-------------|
| `complexity: easy` | #0E8A16 | 😊 Facile |
| `complexity: medium` | #FBCA04 | 🤔 Media |
| `complexity: hard` | #B60205 | 💪 Difficile |

### 🎯 ALTRI
| Label | Colore | Descrizione |
|-------|--------|-------------|
| `good first issue` | #7057FF | 🎯 Per beginners |
| `help wanted` | #008672 | 🙏 Richiede contributi |

## 📝 COME USARE I LABEL

### Per le Issue
1. **Priorità**: Sempre presente
2. **Tipo**: Sempre presente
3. **Area**: Sempre presente
4. **Stato**: Opzionale (usato per tracking)
5. **Complessità**: Opzionale
6. **Altri**: Opzionale

### Esempio di Combinazione
cd ~/urban-lab-scooter

# 1. CREA LA DIRECTORY PER GLI SCRIPT
mkdir -p scripts

# 2. CREA LO SCRIPT CON NANO
cat > scripts/apply-labels.sh << 'EOF'
#!/bin/bash
# 🏭 Urban Lab - Script per applicare i label su GitHub

echo "🏭 URBAN LAB - APPLICAZIONE LABELS"
echo "==================================="
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

echo "📌 Creazione labels per: $REPO"
echo ""

# PRIORITÀ
echo "🔴 Creazione labels priorità..."
gh label create "priority: critical" --color "B60205" --description "🚨 Bloccante - Deve essere risolto immediatamente" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "priority: high" --color "D93F0B" --description "🔴 Alta priorità - Da risolvere al più presto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "priority: medium" --color "FBCA04" --description "🟡 Priorità media - Da pianificare" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "priority: low" --color "0E8A16" --description "🟢 Bassa priorità - Quando c'è tempo" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# TIPOLOGIA
echo ""
echo "📌 Creazione labels tipologia..."
gh label create "type: bug" --color "B60205" --description "🐛 Bug o errore da correggere" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "type: feature" --color "1D76DB" --description "✨ Nuova funzionalità" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "type: enhancement" --color "A2EEEF" --description "🔧 Miglioramento di funzionalità esistente" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "type: documentation" --color "0075CA" --description "📝 Documentazione o guide" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "type: testing" --color "F9D0C4" --description "🧪 Test e QA" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "type: research" --color "5319E7" --description "🔬 Ricerca e analisi" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# AREA
echo ""
echo "📂 Creazione labels area..."
gh label create "area: 3d-printing" --color "FBCA04" --description "🖨️ Stampa 3D e modelli" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: firmware" --color "B60205" --description "📡 Firmware ESP32 e sensori" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: rl" --color "1D76DB" --description "🧠 Reinforcement Learning e AI" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: app" --color "0E8A16" --description "📱 App mobile React Native" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: dashboard" --color "5319E7" --description "🌐 Dashboard web" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: legal" --color "F9D0C4" --description "⚖️ Documentazione legale" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: hardware" --color "D93F0B" --description "🔧 Hardware e componenti" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "area: documentation" --color "0075CA" --description "📚 Documentazione generale" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# STATO
echo ""
echo "📊 Creazione labels stato..."
gh label create "status: done" --color "0E8A16" --description "✅ Completato" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "status: in-progress" --color "FBCA04" --description "⏳ In corso" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "status: blocked" --color "B60205" --description "🚫 Bloccato" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "status: review" --color "5319E7" --description "👀 In revisione" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "status: needs-help" --color "D93F0B" --description "🆘 Serve aiuto" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# COMPLESSITÀ
echo ""
echo "💪 Creazione labels complessità..."
gh label create "complexity: easy" --color "0E8A16" --description "😊 Facile - Adatto per beginners" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "complexity: medium" --color "FBCA04" --description "🤔 Media - Richiede esperienza" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "complexity: hard" --color "B60205" --description "💪 Difficile - Richiede expertise" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

# ALTRI
echo ""
echo "🎯 Creazione labels altri..."
gh label create "good first issue" --color "7057FF" --description "🎯 Buona prima issue per contributori" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"
gh label create "help wanted" --color "008672" --description "🙏 Richiede contributi esterni" --repo $REPO 2>/dev/null || echo "   ⚠️ Label già esistente"

echo ""
echo "✅ LABELS CREATI CON SUCCESSO!"
echo ""
echo "📋 LISTA LABELS ATTUALI:"
gh label list --repo $REPO
