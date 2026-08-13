#!/bin/bash

echo "🚀 Installazione Telekinesis RLbotics per Urban Lab"
echo "=================================================="
echo ""

# Verifica Python
python_version=$(python3 --version 2>&1 | grep -oP '(?<=Python )\d+\.\d+')
echo "🐍 Python version: $python_version"

# Installa requisiti base
echo ""
echo "📦 Installazione dipendenze base..."
pip install --upgrade pip
pip install gymnasium numpy pyyaml onnx onnxruntime

# Installa Telekinesis RLbotics
echo ""
echo "📦 Installazione Telekinesis RLbotics..."
pip install "telekinesis-rlbotics[gym]"

# Opzionale: GPU support
echo ""
read -p "🔧 Installare supporto GPU? (s/n): " gpu
if [ "$gpu" == "s" ]; then
    echo "📦 Installazione PyTorch con CUDA..."
    pip install torch --index-url https://download.pytorch.org/whl/cu128
    pip install "telekinesis-rlbotics[mjlab]"
fi

echo ""
echo "✅ Installazione completata!"
echo ""
echo "📋 Verifica:"
python3 -c "import telekinesis.rlbotics; print('✅ Telekinesis RLbotics installato!')"
python3 -c "import gymnasium; print('✅ Gymnasium installato!')"
