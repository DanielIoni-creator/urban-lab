#!/bin/bash
# 🏭 Urban Lab - Attiva ambiente
cd ~/urban-lab-scooter
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "✅ Ambiente Urban Lab attivato!"
echo "📌 Telekinesis Wrapper (stub) - Python 3.13"
echo "📌 Versione Python: $(python --version)"
