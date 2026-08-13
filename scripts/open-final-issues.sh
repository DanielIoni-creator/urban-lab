#!/bin/bash
# 🏁 URBAN LAB - Apri le issue finali su GitHub

echo "🏁 URBAN LAB - APERTURA ISSUE FINALI"
echo "===================================="
echo ""

# Verifica se gh è installato
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) non installato!"
    echo "   Installa: sudo apt install gh"
    exit 1
fi

# Verifica autenticazione
if ! gh auth status &> /dev/null; then
    echo "❌ Non autenticato su GitHub!"
    echo "   Esegui: gh auth login"
    exit 1
fi

REPO="DanielIoni-creator/urban-lab"

echo "📌 Apertura issue per: $REPO"
echo ""

# Funzione per aprire una issue
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
    echo ""
}

# ISSUE F1: Assemblaggio Telaio
open_issue "[F1] Assemblaggio Telaio Monopattino" \
"## 📋 Descrizione
Assemblare tutti i componenti stampati in 3D per formare il telaio del monopattino.

## 🎯 Obiettivi
- [ ] Preparare tutti i pezzi stampati
- [ ] Incollare i 3 pezzi del telaio
- [ ] Montare il sistema pieghevole
- [ ] Installare gli attacchi ruota
- [ ] Verificare la solidità della struttura

## 📋 Checklist Materiali
- [ ] Telaio (3 pezzi in PETG)
- [ ] Pieghevole (ABS)
- [ ] Attacchi ruota x4 (PETG)
- [ ] Colla epossidica
- [ ] Viti e bulloni M3-M8

## ⏱️ Tempo Stimato: 4 ore

## 📎 Risorse
- Guida: 3d-printing/assembly-guide.md
- Pezzi: 3d-printing/stl-files/

## ✅ Criteri di Accettazione
- [ ] Telaio solido e stabile
- [ ] Sistema pieghevole funzionante
- [ ] Tutti i bulloni serrati
- [ ] Struttura senza gioco" \
"final: critical,final: hardware,final: assembly"

# ISSUE F2: Montaggio Elettronica
open_issue "[F2] Montaggio Elettronica e Sensori" \
"## 📋 Descrizione
Montare tutti i componenti elettronici sul telaio del monopattino.

## 🎯 Obiettivi
- [ ] Montare il box batteria
- [ ] Installare ESP32 e sensori
- [ ] Collegare display OLED
- [ ] Installare GPS e IMU
- [ ] Collegare antenna NFC
- [ ] Cablaggio e gestione cavi

## 📋 Componenti
- [ ] ESP32 DevKit
- [ ] Batteria LiFePO4 48V 20Ah
- [ ] Controller VESC 60A
- [ ] GPS NEO-6M
- [ ] IMU MPU6050
- [ ] NFC RC522
- [ ] OLED 1.3\"
- [ ] Sensore prossimità HC-SR04

## ⏱️ Tempo Stimato: 3 ore

## ✅ Criteri di Accettazione
- [ ] Tutti i sensori fissati saldamente
- [ ] Cablaggi protetti e ordinati
- [ ] Connessioni salde
- [ ] Alimentazione corretta" \
"final: critical,final: hardware,final: assembly"

# ISSUE F3: Caricamento Firmware
open_issue "[F3] Caricamento Firmware ESP32" \
"## 📋 Descrizione
Caricare e verificare il firmware sul ESP32.

## 🎯 Obiettivi
- [ ] Installare PlatformIO
- [ ] Configurare il progetto
- [ ] Caricare il firmware
- [ ] Verificare il boot
- [ ] Testare connessione seriale

## 🔧 Comandi
\`\`\`bash
cd firmware/esp32
pio run -t upload
pio device monitor
\`\`\`

## ⏱️ Tempo Stimato: 1 ora

## ✅ Criteri di Accettazione
- [ ] Firmware caricato con successo
- [ ] Serial monitor mostra output
- [ ] LED di stato funzionante
- [ ] Comandi seriali rispondono" \
"final: critical,final: firmware"

# ISSUE F4: Test Sensori
open_issue "[F4] Test Sensori e Elettronica" \
"## 📋 Descrizione
Testare tutti i sensori e i componenti elettronici.

## 🎯 Obiettivi
- [ ] Test GPS (acquisizione segnale)
- [ ] Test IMU (lettura accelerometro)
- [ ] Test OLED (visualizzazione)
- [ ] Test NFC (lettura tag)
- [ ] Test prossimità (rilevamento ostacoli)
- [ ] Test batteria (lettura voltaggio)

## 📋 Test da Eseguire
| Sensore | Test | Verifica |
|---------|------|----------|
| GPS | Acquisizione segnale | ✅ Dati validi |
| IMU | Lettura movimento | ✅ Dati in tempo reale |
| OLED | Display funzionante | ✅ Testo visibile |
| NFC | Lettura tag | ✅ Tag rilevato |
| Prossimità | Rilevamento | ✅ Distanza misurata |

## ⏱️ Tempo Stimato: 2 ore

## ✅ Criteri di Accettazione
- [ ] Tutti i sensori funzionanti
- [ ] Dati letti correttamente
- [ ] Nessun errore di comunicazione" \
"final: high,final: testing"

# ISSUE F5: Calibrazione Sistema
open_issue "[F5] Calibrazione Sistema e Sensori" \
"## 📋 Descrizione
Calibrare tutti i sensori e il sistema di controllo.

## 🎯 Obiettivi
- [ ] Calibrare IMU (offset e scale)
- [ ] Calibrare GPS
- [ ] Calibrare batteria
- [ ] Configurare PID
- [ ] Settare parametri MIGHTY

## 🔧 Strumenti
\`\`\`bash
python3 calibrate_sensors.py
\`\`\`

## ⏱️ Tempo Stimato: 2 ore

## ✅ Criteri di Accettazione
- [ ] Sensori calibrati
- [ ] Dati stabili
- [ ] Nessun drift anomalo" \
"final: high,final: testing,final: calibration"

# ISSUE F6: Test MIGHTY Hardware
open_issue "[F6] Test MIGHTY su Hardware Reale" \
"## 📋 Descrizione
Testare MIGHTY sul monopattino reale.

## 🎯 Obiettivi
- [ ] Collegare bridge hardware
- [ ] Testare evitamento ostacoli
- [ ] Testare traiettorie
- [ ] Verificare risposta in tempo reale
- [ ] Ottimizzare parametri

## 🔧 Comandi
\`\`\`bash
./launch_mighty_real.sh
\`\`\`

## ⏱️ Tempo Stimato: 3 ore

## ✅ Criteri di Accettazione
- [ ] MIGHTY risponde in tempo reale
- [ ] Ostacoli evitati con successo
- [ ] Traiettorie fluide
- [ ] Nessuna collisione" \
"final: high,final: software"

# ISSUE F7: Test App Mobile
open_issue "[F7] Test App Mobile su Dispositivo Reale" \
"## 📋 Descrizione
Testare l'app mobile sul dispositivo reale.

## 🎯 Obiettivi
- [ ] Installare app su Android
- [ ] Testare connessione BLE
- [ ] Verificare dashboard
- [ ] Testare controlli
- [ ] Testare notifiche

## ⏱️ Tempo Stimato: 2 ore

## ✅ Criteri di Accettazione
- [ ] App si connette
- [ ] Dati visualizzati correttamente
- [ ] Comandi funzionanti
- [ ] UI reattiva" \
"final: medium,final: software"

# ISSUE F8: Collaudo Finale
open_issue "[F8] Collaudo Finale del Monopattino" \
"## 📋 Descrizione
Eseguire il collaudo finale del monopattino completo.

## 🎯 Obiettivi
- [ ] Test in condizioni reali
- [ ] Verificare autonomia
- [ ] Testare velocità massima
- [ ] Verificare stabilità
- [ ] Testare frenata

## 📋 Test da Eseguire
- [ ] Percorso in piano
- [ ] Percorso in salita
- [ ] Frenata d'emergenza
- [ ] Autonomia reale
- [ ] Comfort di guida

## ⏱️ Tempo Stimato: 4 ore

## ✅ Criteri di Accettazione
- [ ] Monopattino funzionante
- [ ] Performance soddisfacenti
- [ ] Nessun problema di sicurezza" \
"final: medium,final: deployment,final: road-test"

# ISSUE F9: Video Dimostrativo
open_issue "[F9] Creazione Video Dimostrativo" \
"## 📋 Descrizione
Creare un video dimostrativo del monopattino in azione.

## 🎯 Obiettivi
- [ ] Riprendere assemblaggio
- [ ] Riprendere test su strada
- [ ] Mostrare app e dashboard
- [ ] Mostrare AI in azione
- [ ] Montare e pubblicare

## 📋 Contenuti Video
- [ ] Introduzione al progetto
- [ ] Assemblaggio (time-lapse)
- [ ] Test sensori
- [ ] Navigazione con MIGHTY
- [ ] Controllo via app
- [ ] Conclusioni

## ⏱️ Tempo Stimato: 3 ore" \
"final: low,final: documentation,final: video"

# ISSUE F10: Documentazione Finale
open_issue "[F10] Documentazione Finale del Progetto" \
"## 📋 Descrizione
Completare la documentazione finale del progetto.

## 🎯 Obiettivi
- [ ] Aggiornare README
- [ ] Completare post DEV.to
- [ ] Documentare performance
- [ ] Creare guida utente
- [ ] Archiviare progetti

## 📋 Documenti da Completare
- [ ] README aggiornato
- [ ] Post DEV.to pubblicato
- [ ] Specifiche finali
- [ ] Guida utente
- [ ] BOM (Bill of Materials)
- [ ] Gallery foto

## ⏱️ Tempo Stimato: 2 ore" \
"final: low,final: documentation,final: publish"

echo ""
echo "✅ TUTTE LE ISSUE FINALI CREATE!"
echo ""
echo "📋 RIEPILOGO ISSUE FINALI:"
echo "   🔴 Critical: 3 (F1, F2, F3)"
echo "   🟡 High: 3 (F4, F5, F6)"
echo "   🟢 Medium: 2 (F7, F8)"
echo "   ⚪ Low: 2 (F9, F10)"
echo ""
echo "🔗 VEDI LE ISSUE SU GITHUB:"
echo "   https://github.com/DanielIoni-creator/urban-lab/issues"
