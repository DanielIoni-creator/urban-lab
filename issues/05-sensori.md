# 📡 Sensori e Scheda Elettronica

**Priorità**: Alta
**Stima**: 2 settimane
**Assegnato a**: Team Elettronica

## 📋 Descrizione
Implementare il sistema di sensori e la scheda di controllo basata su ESP32.

## 🎯 Obiettivi
- [ ] Progettare PCB per ESP32
- [ ] Integrare sensori (GPS, IMU, NFC, Prossimità)
- [ ] Implementare display OLED
- [ ] Sviluppare firmware base

## 📡 Sensori
| Sensore | Modello | Funzione |
|---------|---------|----------|
| GPS | NEO-6M | Navigazione |
| IMU | MPU6050 | Stabilità |
| Prossimità | HC-SR04 | Sicurezza |
| NFC | RC522 | Autenticazione |
| OLED | 1.3" | Display |

## 🔌 Connessioni
- GPIO 4-5: GPS
- GPIO 16-17: IMU
- GPIO 22-23: Prossimità
- GPIO 26-27: NFC

## ✅ Checklist
- [ ] Schemi elettrici completati
- [ ] PCB progettato
- [ ] Sensori testati individualmente
- [ ] Firmware ESP32 funzionante
- [ ] Integrazione completata

## 📎 Documenti
- Sensori specifiche (docs/sensors-specs.md)
- Schema collegamenti (docs/sensors-specs.md)
