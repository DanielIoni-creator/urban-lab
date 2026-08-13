# 🚀 MIGHTY - Trajectory Planning per Urban Lab

## 📋 Cos'è MIGHTY?
MIGHTY è un sistema open-source di pianificazione traiettorie che permette a robot e droni di evitare ostacoli in millisecondi mantenendo voli fluidi ed efficienti.

Sviluppato da **MIT e University of Pennsylvania**, MIGHTY utilizza:
- **Hermite splines** per traiettorie fluide
- **Ottimizzazione congiunta** di percorso e tempo
- **Mappe LiDAR** per la navigazione in tempo reale

## 🎯 Applicazioni per Urban Lab
| Area | Applicazione |
|------|-------------|
| **Monopattino** | Navigazione autonoma in ambienti urbani |
| **Evitamento ostacoli** | Rilevamento e schivata in millisecondi |
| **Ottimizzazione percorso** | Percorsi più veloci e sicuri |
| **Mappatura 3D** | Ricostruzione dell'ambiente in tempo reale |

## 📊 Performance
- **Velocità**: fino a 6.7 m/s in test reali
- **Efficienza**: 15% più veloce di altri metodi
- **Tempo computazionale**: 90% di altri sistemi
- **Successo**: 100% di evitamento ostacoli

## 📁 Strutturamighty/
├── src/ # Repository MIGHTY originale
├── configs/ # Configurazioni per Urban Lab
├── scripts/ # Script di integrazione
└── docs/ # Documentazione
text


## 🚀 Installazione
```bash
# Usando Docker (consigliato)
cd mighty/src
make build

# O installazione nativa
./setup.sh

🔗 Link

    Repository originale: https://github.com/mit-acl/mighty

    Paper: https://arxiv.org/abs/2511.10822

text


Salva: Ctrl+O → Enter → Ctrl+X

## 📄 FILE 2: CONFIGURAZIONE URBAN LAB
```bash
nano mighty/configs/urban_lab_config.yaml

Copia e incolla:
yaml

# 🏭 Urban Lab - Configurazione MIGHTY
# Adattata per il monopattino elettrico

# Parametri del veicolo
vehicle:
  type: ground_robot
  max_speed: 6.7  # m/s (24 km/h)
  max_acceleration: 2.0
  max_deceleration: 3.0
  wheelbase: 1.2  # metri

# Pianificazione traiettoria
trajectory:
  planner: mighty
  spline_type: hermite
  degree: 5
  segments: 10
  optimization_iterations: 50

# Sensori
sensors:
  lidar:
    enabled: true
    range: 30  # metri
    resolution: 0.1
  camera:
    enabled: true
    vio: true  # Visual Inertial Odometry

# Mappatura
mapping:
  type: occupancy_grid
  resolution: 0.1
  size: 100  # metri
  update_rate: 10  # Hz

# Controllo
control:
  type: mpc
  horizon: 20
  dt: 0.05
  weight_tracking: 1.0
  weight_smoothness: 0.1

# Simulazione
simulation:
  world: urban_environment
  num_agents: 1
  dynamic_obstacles: true

