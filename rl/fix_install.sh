#!/bin/bash
# 🏭 Urban Lab - Fix Installazione per Kali

echo "🔧 Fix Installazione Urban Lab RL"
echo "=================================="
echo ""

cd ~/urban-lab-scooter

# Attiva venv
if [ -z "$VIRTUAL_ENV" ]; then
    source venv/bin/activate
fi

# Disinstalla vecchie versioni
echo "🧹 Pulizia installazioni precedenti..."
pip uninstall telekinesis-rlbotics gymnasium -y 2>/dev/null

# Installa dipendenze di sistema
echo "📦 Installazione dipendenze di sistema..."
sudo apt install python3-gymnasium python3-numpy python3-yaml -y

# Installa nel venv
echo "📦 Installazione pacchetti Python..."
pip install --upgrade pip
pip install numpy pyyaml onnx onnxruntime matplotlib
pip install gymnasium
pip install "telekinesis-rlbotics[gym]" --no-cache-dir

# Verifica
echo ""
echo "✅ Verifica installazione:"
python -c "import gymnasium; print('✅ Gymnasium OK')"
python -c "from telekinesis.rlbotics import PPO; print('✅ Telekinesis OK')"

echo ""
echo "🎉 Installazione completata!"
