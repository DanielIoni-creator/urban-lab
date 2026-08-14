#!/bin/bash
# 🌀 URBAN LAB - Avvia il Portale del Tempo Fisico

cd ~/urban-lab-scooter/portal

# Ferma eventuali server precedenti
pkill -f "python3 -m http.server" 2>/dev/null
pkill -f "server.py" 2>/dev/null
sleep 1

# Avvia il server
echo "🌀 Avvio Portale del Tempo Fisico..."
python3 -m http.server 8080 &
sleep 2

echo ""
echo "🌐 Server avviato su: http://localhost:8080"
echo ""
echo "📌 Apri il browser e vai a: http://localhost:8080"
echo "📌 Oppure usa: firefox http://localhost:8080"
echo ""
echo "📌 Per fermare il server: pkill -f 'http.server'"
