/**
 * Configurazione Urban Lab Scooter
 * Pin mapping e costanti
 */

#ifndef CONFIG_H
#define CONFIG_H

// ============ PIN DEFINITIONS ============
// GPS
#define GPS_RX_PIN 4
#define GPS_TX_PIN 5
#define GPS_BAUD 9600

// IMU (I2C)
#define IMU_SDA 16
#define IMU_SCL 17

// OLED (I2C)
#define OLED_SDA 18
#define OLED_SCL 19
#define OLED_ADDR 0x3C
#define OLED_WIDTH 128
#define OLED_HEIGHT 64

// Prossimità
#define PROX_TRIG_PIN 22
#define PROX_ECHO_PIN 23

// NFC (SPI)
#define NFC_SS_PIN 26
#define NFC_RST_PIN 27
#define NFC_SCK_PIN 14
#define NFC_MOSI_PIN 13
#define NFC_MISO_PIN 12

// LED
#define LED_STATUS 2
#define LED_BATTERY 15

// Buzzer
#define BUZZER_PIN 25

// ============ PARAMETRI ============
#define MAX_SPEED 20.0  // km/h
#define MIN_BATTERY 20.0  // %
#define MAX_TEMP 45.0  // °C
#define PROX_DISTANCE 100  // cm

// ============ WiFi ============
#define WIFI_SSID "UrbanLab_Scooter"
#define WIFI_PASSWORD "scooter2024"

// ============ BLE ============
#define BLE_NAME "UrbanLab_Scooter"
#define BLE_SERVICE_UUID "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define BLE_CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

// ============ AI ============
#define AI_ENDPOINT "http://localhost:3005/api/pytho/chat"
#define AI_TIMEOUT 5000  // ms

#endif
