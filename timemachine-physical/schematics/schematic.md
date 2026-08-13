# 📐 SCHEMA ELETTRICO - MACCHINA DEL TEMPO

## 🔌 CONNESSIONI PRINCIPALI
┌─────────────────────────────────────────────────────────────┐
│ MACCHINA DEL TEMPO │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐ │
│ │ Batteria │──│ Inverter │──│ Bobine di Tesla │ │
│ │ 48V 100Ah │ │ 48V→220V │ │ 100kV 50kHz │ │
│ └─────────────┘ └─────────────┘ └─────────────────────┘ │
│ │ │ │ │
│ ┌──────▼────────────────▼───────────────────▼──────┐ │
│ │ Raspberry Pi 5 + Arduino Mega │ │
│ │ (Controllo centralizzato e sensori) │ │
│ └───────────────────────────────────────────────────┘ │
│ │ │ │ │
│ ┌──────▼────────────────▼───────────────────▼──────┐ │
│ │ Sensori e Periferiche │ │
│ │ • Sensori Hall • Display OLED • LED Status │ │
│ └───────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
text


## 📋 LISTA COMPONENTI ELETTRONICI

| ID | Componente | Specifica | Qty |
|----|------------|-----------|-----|
| P1 | Batteria | LiFePO4 48V 100Ah | 1 |
| P2 | Inverter | 48V DC → 220V AC | 1 |
| P3 | Bobina Tesla | 100kV 50kHz | 1 |
| P4 | Condensatori | 1000µF 450V | 10 |
| P5 | Raspberry Pi 5 | 8GB RAM | 1 |
| P6 | Arduino Mega | 2560 | 1 |
| P7 | Schermo OLED | 7" HDMI | 1 |
| P8 | Sensore Hall | A1324 | 4 |
| P9 | Sensore Temp | DS18B20 | 4 |
| P10 | LED Status | RGB | 4 |

## 🔧 COLLEGAMENTI ARDUINO

ARDUINO MEGA → PERIFERICHE
───────────────────────────
Pin 13 → LED Status (Blu)
Pin 12 → Sensore Hall 1
Pin 11 → Sensore Hall 2
Pin 10 → Sensore Hall 3
Pin 9 → Sensore Hall 4
Pin 8 → Relè Bobina
Pin 7 → Relè Inverter
Pin 6 → Buzzer Allarme
Pin 5 → LED Rosso (Allarme)
Pin 4 → LED Verde (OK)
Pin 3 → Pulsante Avvio
Pin 2 → Pulsante Stop
text


## 🔌 COLLEGAMENTI RASPBERRY PI

RASPBERRY PI 5 → ARDUINO + DISPLAY
───────────────────────────────────
GPIO 2 (SDA) → Arduino I2C
GPIO 3 (SCL) → Arduino I2C
GPIO 14 (TX) → Arduino RX
GPIO 15 (RX) → Arduino TX
HDMI → Display OLED 7"
USB → Keyboard/Mouse
text

Salva: Ctrl+O → Enter → Ctrl+X
📄 FILE 3: FIRMWARE ARDUINO
bash

nano timemachine-physical/electronics/arduino_firmware.ino

Copia e incolla:
cpp

/*
 * 🌀 Macchina del Tempo - Firmware Arduino Mega
 * Controllo periferiche e sensori
 */

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Definizioni PIN
#define LED_STATUS 13
#define LED_ROSSO 5
#define LED_VERDE 4
#define RELAY_BOBINA 8
#define RELAY_INVERTER 7
#define BUZZER 6
#define BUTTON_START 3
#define BUTTON_STOP 2

// Sensori Hall
#define HALL_SENSOR_1 A0
#define HALL_SENSOR_2 A1
#define HALL_SENSOR_3 A2
#define HALL_SENSOR_4 A3

// Display LCD (I2C)
LiquidCrystal_I2C lcd(0x27, 20, 4);

// Variabili di stato
bool sistema_attivo = false;
bool wormhole_aperto = false;
int campo_magnetico = 0;
unsigned long tempo_avvio = 0;

void setup() {
  Serial.begin(115200);
  
  // Inizializza pin
  pinMode(LED_STATUS, OUTPUT);
  pinMode(LED_ROSSO, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(RELAY_BOBINA, OUTPUT);
  pinMode(RELAY_INVERTER, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(BUTTON_START, INPUT_PULLUP);
  pinMode(BUTTON_STOP, INPUT_PULLUP);
  
  // Inizializza display
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("MACCHINA TEMPO");
  lcd.setCursor(0, 1);
  lcd.print("INIZIALIZZAZIONE...");
  
  // LED Status
  digitalWrite(LED_STATUS, HIGH);
  
  Serial.println("🌀 Macchina del Tempo - Avviata!");
  Serial.println("📡 Sensori in attesa...");
  
  delay(2000);
  lcd.clear();
  lcd.print("PRONTO!");
}

void loop() {
  // Leggi sensori Hall
  int hall1 = analogRead(HALL_SENSOR_1);
  int hall2 = analogRead(HALL_SENSOR_2);
  int hall3 = analogRead(HALL_SENSOR_3);
  int hall4 = analogRead(HALL_SENSOR_4);
  
  int campo_medio = (hall1 + hall2 + hall3 + hall4) / 4;
  
  // Aggiorna display
  lcd.setCursor(0, 0);
  lcd.print("CAMPO: ");
  lcd.print(campo_medio);
  lcd.print("   ");
  
  lcd.setCursor(0, 1);
  if (sistema_attivo) {
    lcd.print("WORMHOLE: APERTO");
  } else {
    lcd.print("WORMHOLE: CHIUSO");
  }
  
  // Controllo pulsanti
  if (digitalRead(BUTTON_START) == LOW) {
    avvia_sistema();
  }
  
  if (digitalRead(BUTTON_STOP) == LOW) {
    ferma_sistema();
  }
  
  // Monitoraggio wormhole
  if (sistema_attivo) {
    monitora_wormhole(campo_medio);
  }
  
  // Invia dati a Raspberry Pi
  invia_dati(campo_medio);
  
  delay(100);
}

void avvia_sistema() {
  Serial.println("🌀 Avvio sistema...");
  
  // Sequenza di avvio
  digitalWrite(LED_VERDE, HIGH);
  digitalWrite(RELAY_INVERTER, HIGH);
  
  for (int i = 0; i < 3; i++) {
    digitalWrite(BUZZER, HIGH);
    delay(200);
    digitalWrite(BUZZER, LOW);
    delay(200);
  }
  
  digitalWrite(RELAY_BOBINA, HIGH);
  sistema_attivo = true;
  tempo_avvio = millis();
  
  lcd.clear();
  lcd.print("WORMHOLE APERTO!");
  lcd.setCursor(0, 1);
  lcd.print("VIAGGIO IN CORSO");
  
  Serial.println("✅ Wormhole aperto!");
}

void ferma_sistema() {
  Serial.println("🔄 Chiusura wormhole...");
  
  digitalWrite(RELAY_BOBINA, LOW);
  digitalWrite(RELAY_INVERTER, LOW);
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_ROSSO, HIGH);
  
  digitalWrite(BUZZER, HIGH);
  delay(1000);
  digitalWrite(BUZZER, LOW);
  
  sistema_attivo = false;
  wormhole_aperto = false;
  
  lcd.clear();
  lcd.print("WORMHOLE CHIUSO");
  lcd.setCursor(0, 1);
  lcd.print("RITORNO AL PRESENTE");
  
  Serial.println("✅ Wormhole chiuso!");
}

void monitora_wormhole(int campo) {
  // Simula la stabilità del wormhole
  if (campo > 800) {
    wormhole_aperto = true;
    digitalWrite(LED_VERDE, HIGH);
    digitalWrite(LED_ROSSO, LOW);
  } else if (campo < 400) {
    wormhole_aperto = false;
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_ROSSO, HIGH);
  }
  
  // Calcola tempo di viaggio
  unsigned long durata = (millis() - tempo_avvio) / 1000;
  if (sistema_attivo && durata % 10 == 0) {
    Serial.print("⏳ Viaggio in corso: ");
    Serial.print(durata);
    Serial.println(" secondi");
  }
}

void invia_dati(int campo) {
  // Invia dati via seriale a Raspberry Pi
  Serial.print("DATA:");
  Serial.print(campo);
  Serial.print(",");
  Serial.print(sistema_attivo ? 1 : 0);
  Serial.print(",");
  Serial.print(wormhole_aperto ? 1 : 0);
  Serial.print(",");
  Serial.println(millis());
}
