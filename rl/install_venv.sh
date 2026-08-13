#!/bin/bash
# 🏭 Urban Lab - Installazione in Virtual Environment

echo "🚀 Urban Lab - Installazione in Virtual Environment"
echo "=================================================="
echo ""

cd ~/urban-lab-scooter

# Attiva il venv se non è attivo
if [ -z "$VIRTUAL_ENV" ]; then
    echo "🔧 Attivazione virtual environment..."
    source venv/bin/activate
fi

# Installa dipendenze
echo "📦 Installazione dipendenze..."
pip install gymnasium numpy pyyaml onnx onnxruntime matplotlib
pip install "telekinesis-rlbotics[gym]"
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo ""
echo "✅ Installazione completata!"
echo "📌 Per attivare il venv: source ~/urban-lab-scooter/activate_venv.sh"
