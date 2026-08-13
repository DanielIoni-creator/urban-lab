---
title: "[URBAN-002] Configurazione Ambiente Gymnasium per Scooter"
labels: ["priority: critical", "area: rl", "type: feature", "status: done", "complexity: medium"]
assignees: DanielIoni-creator
---

## 📋 Descrizione
Creare e configurare l'ambiente Gymnasium personalizzato per il monopattino Urban Lab.

## 🎯 Obiettivi
- [x] Creare ScooterEnv
- [x] Definire observation space (6 parametri)
- [x] Definire action space (3 azioni)
- [x] Implementare reward function
- [x] Registrare ambiente
- [ ] Testare con training semplice

## 📊 Specifiche
**Observation Space:**
- Velocità (0-20 km/h)
- Inclinazione (-15° a 15°)
- Batteria (0-100%)
- Distanza ostacolo (0-200cm)
- RPM motore (0-3000)
- Temperatura motore (0-60°C)

**Action Space:**
- Accelerazione (-1 a 1)
- Frenata (0 a 1)
- Sterzo (-30° a 30°)

## 🔗 Link
- [Ambiente Gymnasium](https://github.com/DanielIoni-creator/urban-lab/blob/feature/ai-integration/rl/environments/scooter_env.py)
