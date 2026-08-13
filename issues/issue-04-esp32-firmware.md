---
title: "[URBAN-004] Caricamento e Test Firmware ESP32"
labels: ["priority: high", "area: firmware", "type: feature", "status: todo", "complexity: hard"]
assignees: DanielIoni-creator
---

## 📋 Descrizione
Caricare e testare il firmware ESP32 sul hardware.

## 🎯 Obiettivi
- [ ] Installare PlatformIO
- [ ] Caricare firmware su ESP32
- [ ] Testare sensori (GPS, IMU, NFC, OLED)
- [ ] Testare connessione WiFi
- [ ] Testare connessione BLE
- [ ] Testare comandi seriali

## 📊 Specifiche
**Sensori:**
- GPS NEO-6M (GPIO 4,5)
- IMU MPU6050 (GPIO 16,17)
- OLED 1.3" (GPIO 18,19)
- NFC RC522 (GPIO 26,27)
- Prossimità HC-SR04 (GPIO 22,23)

**Comunicazione:**
- WiFi: UrbanLab_Scooter
- BLE: UrbanLab_Scooter

## 📎 Risorse
- Firmware: firmware/esp32/src/main.cpp
- Config: firmware/esp32/include/config.h
- PlatformIO: firmware/esp32/platformio.ini

## 🔗 Link
- [Firmware ESP32](https://github.com/DanielIoni-creator/urban-lab/tree/feature/ai-integration/firmware/esp32)
