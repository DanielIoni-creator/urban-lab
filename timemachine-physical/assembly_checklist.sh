#!/bin/bash
# 🌀 URBAN LAB - Checklist Assemblaggio Interattiva

echo "🌀 URBAN LAB - ASSEMBLAGGIO MACCHINA DEL TEMPO"
echo "==============================================="
echo ""
echo "📋 CHECKLIST INTERATTIVA"
echo "========================"
echo ""

# Array delle fasi
declare -A fasi=(
    ["1_STRUTTURA"]="🏗️ Struttura Meccanica"
    ["2_ELETTROMAGNETICA"]="⚡ Sistema Elettromagnetico"
    ["3_ELETTRONICA"]="💻 Elettronica di Controllo"
    ["4_SENSORI"]="🧲 Sensori e Cablaggio"
    ["5_SOFTWARE"]="📡 Software e Firmware"
    ["6_TEST"]="🧪 Test e Calibrazione"
)

# File di progresso
PROGRESS_FILE="assembly_progress.txt"

# Inizializza se non esiste
if [ ! -f "$PROGRESS_FILE" ]; then
    for fase in "${!fasi[@]}"; do
        echo "$fase:0" >> "$PROGRESS_FILE"
    done
fi

# Funzione per mostrare progresso
show_progress() {
    clear
    echo "🌀 URBAN LAB - ASSEMBLAGGIO MACCHINA DEL TEMPO"
    echo "==============================================="
    echo ""
    echo "📊 PROGRESSO COMPLETAMENTO:"
    echo ""
    
    totale=0
    completate=0
    
    for fase in "${!fasi[@]}"; do
        progresso=$(grep "^$fase:" "$PROGRESS_FILE" | cut -d: -f2)
        if [ -z "$progresso" ]; then
            progresso=0
        fi
        
        if [ "$progresso" -eq 100 ]; then
            stato="✅"
            ((completate++))
        else
            stato="⏳"
        fi
        
        barra=$(printf "%${progresso}s" | tr ' ' '█')
        printf "   %s %-25s [%-10s] %3d%%\n" "$stato" "${fasi[$fase]}" "$barra" "$progresso"
        ((totale++))
    done
    
    totale_fasi=${#fasi[@]}
    percentuale=$((completate * 100 / totale_fasi))
    echo ""
    echo "📈 COMPLETATO: $completate/$totale_fasi ($percentuale%)"
    echo "==============================================="
}

# Funzione per aggiornare progresso
update_progress() {
    echo ""
    echo "📋 Seleziona la fase da aggiornare:"
    i=1
    for fase in "${!fasi[@]}"; do
        progresso=$(grep "^$fase:" "$PROGRESS_FILE" | cut -d: -f2)
        echo "   $i) ${fasi[$fase]} ($progresso%)"
        ((i++))
    done
    echo "   0) Torna al menu"
    echo ""
    read -p "Scelta: " scelta
    
    if [ "$scelta" -eq 0 ]; then
        return
    fi
    
    # Trova la fase selezionata
    i=1
    for fase in "${!fasi[@]}"; do
        if [ "$i" -eq "$scelta" ]; then
            read -p "Nuovo progresso (0-100): " nuovo_progresso
            if [ "$nuovo_progresso" -ge 0 ] && [ "$nuovo_progresso" -le 100 ]; then
                sed -i "s/^$fase:.*/$fase:$nuovo_progresso/" "$PROGRESS_FILE"
                echo "✅ Aggiornato!"
            else
                echo "❌ Valore non valido!"
            fi
            break
        fi
        ((i++))
    done
}

# Menu principale
while true; do
    show_progress
    echo ""
    echo "📋 COMANDI:"
    echo "   1) Aggiorna progresso"
    echo "   2) Mostra istruzioni fase"
    echo "   3) Resetta progresso"
    echo "   0) Esci"
    echo ""
    read -p "Scelta: " cmd
    
    case $cmd in
        1) update_progress ;;
        2) 
            echo ""
            echo "📖 FASI DI ASSEMBLAGGIO:"
            echo "   1. 🏗️ Struttura: Montare telaio e base"
            echo "   2. ⚡ Elettromagnetica: Bobine e condensatori"
            echo "   3. 💻 Elettronica: Raspberry Pi e Arduino"
            echo "   4. 🧲 Sensori: Hall, temperatura, cablaggio"
            echo "   5. 📡 Software: Caricare firmware"
            echo "   6. 🧪 Test: Calibrazione e test finale"
            read -p "Premi ENTER per continuare..."
            ;;
        3)
            read -p "Resettare tutto il progresso? (s/n): " reset
            if [ "$reset" = "s" ]; then
                for fase in "${!fasi[@]}"; do
                    sed -i "s/^$fase:.*/$fase:0/" "$PROGRESS_FILE"
                done
                echo "✅ Progresso resettato!"
            fi
            ;;
        0) 
            echo "👋 Arrivederci! 🌀"
            exit 0
            ;;
        *) echo "❌ Comando non valido!" ;;
    esac
done
