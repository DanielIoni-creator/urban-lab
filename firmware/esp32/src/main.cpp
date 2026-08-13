/**
 * 🛴 Urban Lab Scooter - Firmware ESP32
 * Monopattino del Futuro - AI Integration
 * 
 * Sensori: GPS, IMU, Prossimità, NFC, OLED
 * Controllo: Motore Brushless 800W
 * Comunicazione: WiFi, BLE, UART
 */

#include <Arduino.h>
#include <WiFi.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <Wire.h>
#include <SPI.h>

// Librerie sensori
#include <TinyGPS++.h>
#include <MPU6050.h>
#include <Adafruit_SSD1306.h>
#include <MFRC522.h>

// ============ CONFIGURAZIONE ============
#define OLED_WIDTH 128
#define OLED_HEIGHT 64
#define OLED_ADDR 0x3C

#define GPS_BAUD 9600
#define GPS_RX_PIN 4
#define GPS_TX_PIN 5

#define NFC_SS_PIN 26
#define NFC_RST_PIN 27

#define PROX_TRIG_PIN 22
#define PROX_ECHO_PIN 23

// ============ OGGETTI GLOBALI ============
// GPS
TinyGPSPlus gps;
HardwareSerial gpsSerial(1);

// IMU
MPU6050 imu;

// OLED
Adafruit_SSD1306 display(OLED_WIDTH, OLED_HEIGHT, &Wire, -1);

// NFC
MFRC522 nfc(NFC_SS_PIN, NFC_RST_PIN);

// BLE
BLEServer *pServer = NULL;
BLECharacteristic *pCharacteristic = NULL;
bool deviceConnected = false;

// Stato veicolo
struct ScooterState {
  float speed = 0;
  float battery = 100;
  float temperature = 25;
  float motorTemp = 30;
  float gpsLat = 44.0576;
  float gpsLon = 12.5653;
  int errors = 0;
  bool isMoving = false;
  bool isLocked = false;
} scooterState;

// ============ PROTOTIPI FUNZIONI ============
void setupWiFi();
void setupBLE();
void setupSensors();
void readSensors();
void displayStatus();
void updateBLE();
void checkErrors();

// ============ SETUP ============
void setup() {
  Serial.begin(115200);
  Serial.println("🛴 Urban Lab Scooter - Firmware v1.0.0");
  Serial.println("🏭 Inizializzazione...");
  
  // Setup sensori
  setupSensors();
  
  // Setup comunicazione
  setupWiFi();
  setupBLE();
  
  Serial.println("✅ Sistema pronto!");
  Serial.println("📡 Monitoraggio attivo...");
}

// ============ SETUP SENSORI ============
void setupSensors() {
  // GPS
  gpsSerial.begin(GPS_BAUD, SERIAL_8N1, GPS_RX_PIN, GPS_TX_PIN);
  Serial.println("📡 GPS: Inizializzato");
  
  // IMU
  Wire.begin();
  imu.initialize();
  if (imu.testConnection()) {
    Serial.println("📡 IMU: Connesso");
  } else {
    Serial.println("❌ IMU: Errore connessione");
  }
  
  // OLED
  if (display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR)) {
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(0, 0);
    display.println("Urban Lab");
    display.println("Scooter v1.0");
    display.display();
    Serial.println("📡 OLED: Inizializzato");
  } else {
    Serial.println("❌ OLED: Errore connessione");
  }
  
  // NFC
  SPI.begin();
  nfc.PCD_Init();
  Serial.println("📡 NFC: Inizializzato");
}

// ============ SETUP WiFi ============
void setupWiFi() {
  const char* ssid = "UrbanLab_Scooter";
  const char* password = "scooter2024";
  
  WiFi.begin(ssid, password);
  Serial.print("📡 WiFi: Connessione");
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println(" ✅ Connesso!");
    Serial.print("📡 IP: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println(" ❌ Connessione fallita");
  }
}

// ============ SETUP BLE ============
void setupBLE() {
  BLEDevice::init("UrbanLab_Scooter");
  pServer = BLEDevice::createServer();
  BLEService *pService = pServer->createService("4fafc201-1fb5-459e-8fcc-c5c9c331914b");
  pCharacteristic = pService->createCharacteristic(
                      "beb5483e-36e1-4688-b7f5-ea07361b26a8",
                      BLECharacteristic::PROPERTY_READ |
                      BLECharacteristic::PROPERTY_WRITE |
                      BLECharacteristic::PROPERTY_NOTIFY
                    );
  pService->start();
  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();
  Serial.println("📡 BLE: Avviato - UrbanLab_Scooter");
}

// ============ LOOP PRINCIPALE ============
void loop() {
  // Leggi sensori
  readSensors();
  
  // Aggiorna display
  displayStatus();
  
  // Aggiorna BLE
  updateBLE();
  
  // Controlla errori
  checkErrors();
  
  delay(100);
}

// ============ LETTURA SENSORI ============
void readSensors() {
  // GPS
  while (gpsSerial.available() > 0) {
    if (gps.encode(gpsSerial.read())) {
      if (gps.location.isValid()) {
        scooterState.gpsLat = gps.location.lat();
        scooterState.gpsLon = gps.location.lng();
        scooterState.speed = gps.speed.kmph();
      }
    }
  }
  
  // IMU (accelerometro + giroscopio)
  int16_t ax, ay, az, gx, gy, gz;
  imu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  // Prossimità
  digitalWrite(PROX_TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(PROX_TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(PROX_TRIG_PIN, LOW);
  long duration = pulseIn(PROX_ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;
  
  // Simula batteria in discesa
  if (scooterState.battery > 0) {
    scooterState.battery -= 0.01;
  }
}

// ============ DISPLAY OLED ============
void displayStatus() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  
  display.print("🌡️ ");
  display.print(scooterState.temperature);
  display.println(" C");
  
  display.print("🔋 ");
  display.print(scooterState.battery);
  display.println("%");
  
  display.print("📡 ");
  display.print(scooterState.gpsLat, 4);
  display.print(" ");
  display.println(scooterState.gpsLon, 4);
  
  display.print("⚡ ");
  display.print(scooterState.speed);
  display.println(" km/h");
  
  display.display();
}

// ============ UPDATE BLE ============
void updateBLE() {
  if (deviceConnected) {
    char buffer[100];
    sprintf(buffer, "%.2f,%.2f,%.2f,%.2f,%.2f",
            scooterState.speed,
            scooterState.battery,
            scooterState.temperature,
            scooterState.gpsLat,
            scooterState.gpsLon);
    pCharacteristic->setValue(buffer);
    pCharacteristic->notify();
  }
}

// ============ CONTROLLO ERRORI ============
void checkErrors() {
  int errorCount = 0;
  
  if (scooterState.battery < 20) {
    Serial.println("⚠️ Batteria bassa: <20%");
    errorCount++;
  }
  
  if (scooterState.temperature > 45) {
    Serial.println("⚠️ Temperatura alta: >45°C");
    errorCount++;
  }
  
  scooterState.errors = errorCount;
}

// ============ COMANDI SERIALI ============
// Puoi inviare comandi via Serial Monitor:
// status - Mostra stato
// unlock - Sblocca monopattino
// lock - Blocca monopattino
void serialEvent() {
  while (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "status") {
      Serial.println("=== STATO MONOPATTINO ===");
      Serial.printf("Velocità: %.2f km/h\n", scooterState.speed);
      Serial.printf("Batteria: %.1f%%\n", scooterState.battery);
      Serial.printf("Temperatura: %.1f°C\n", scooterState.temperature);
      Serial.printf("GPS: %.4f, %.4f\n", scooterState.gpsLat, scooterState.gpsLon);
      Serial.printf("Errori: %d\n", scooterState.errors);
    }
    else if (command == "unlock") {
      scooterState.isLocked = false;
      Serial.println("🔓 Scooter sbloccato!");
    }
    else if (command == "lock") {
      scooterState.isLocked = true;
      Serial.println("🔒 Scooter bloccato!");
    }
  }
}
