# 🧠 Urban Lab - Reinforcement Learning con Telekinesis RLbotics

## 📋 Cos'è Telekinesis RLbotics?
Telekinesis RLbotics è una libreria leggera e accelerata su GPU per Reinforcement Learning, 
progettata per robotica e sistemi embedded.

## 🎯 Applicazioni per Urban Lab

### 1. Stabilità e Controllo
- Il monopattino impara a bilanciarsi automaticamente
- Ottimizzazione della frenata in base al terreno
- Adattamento alla guida in tempo reale

### 2. Ottimizzazione Energetica
- Massimizzazione dell'autonomia
- Recupero energetico ottimale in frenata
- Profili di guida eco-friendly

### 3. Guida Autonoma
- Navigazione su percorsi semplici
- Rilevamento e evitamento ostacoli
- Parcheggio automatico

## 🔧 Stack Tecnologico
┌─────────────────────────────────────────────┐
│ URBAN LAB SCOOTER │
├─────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────────────┐ │
│ │ Sensori │ │ Telekinesis RL │ │
│ │ (IMU, GPS) │ │ (Policy Training) │ │
│ └─────────────┘ └─────────────────────┘ │
│ │ │ │
│ ┌──────▼────────────────────▼──────┐ │
│ │ Policy Inference │ │
│ │ (ESP32 / Edge Device) │ │
│ └──────────────────────────────────┘ │
│ │ │
│ ┌──────▼──────┐ │
│ │ Motore │ │
│ │ Freni │ │
│ └─────────────┘ │
└─────────────────────────────────────────────┘
text


## 📦 Requisiti
- Python 3.10-3.12
- PyTorch (CUDA opzionale)
- Telekinesis RLbotics

## 🚀 Installazione
```bash
# Installazione base (CPU)
pip install "telekinesis-rlbotics[gym]"

# Installazione con supporto GPU
pip install torch --index-url https://download.pytorch.org/whl/cu128
pip install "telekinesis-rlbotics[mjlab]"

📁 Struttura del Progetto
text

rl/
├── environments/          # Ambienti personalizzati
│   └── scooter_env.py    # Ambiente del monopattino
├── configs/              # Configurazioni training
│   └── scooter.yaml      # Config per lo scooter
├── models/               # Modelli addestrati
│   └── policy.onnx      # Policy esportata
└── scripts/              # Utilità
    ├── train.py         # Training script
    └── deploy.py        # Deployment script


