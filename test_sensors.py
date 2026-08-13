#!/usr/bin/env python3
"""
🧪 Test Sensori Urban Lab - Versione Software
Simula e testa tutti i sensori del monopattino
"""

import time
import random
import json
from datetime import datetime
import threading

class SensorTester:
    def __init__(self):
        self.sensors = {
            'gps': {'status': 'OK', 'data': {'lat': 44.0576, 'lon': 12.5653, 'speed': 0}},
            'imu': {'status': 'OK', 'data': {'accel': [0, 0, 9.8], 'gyro': [0, 0, 0]}},
            'proximity': {'status': 'OK', 'data': {'distance': 150}},
            'nfc': {'status': 'OK', 'data': {'tag': 'None'}},
            'oled': {'status': 'OK', 'data': {'display': 'Urban Lab'}},
            'battery': {'status': 'OK', 'data': {'level': 100, 'voltage': 48.0}},
            'motor': {'status': 'OK', 'data': {'rpm': 0, 'temp': 25}},
        }
        self.running = True
        self.moving = False
        
    def run(self):
        print("🧪 URBAN LAB SENSOR TESTER")
        print("=" * 50)
        print("Test di tutti i sensori in corso...\n")
        
        # Avvia thread per aggiornamento dati
        def update_loop():
            while self.running:
                self.update_sensors()
                time.sleep(1)
        
        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()
        
        # Menu interattivo
        while self.running:
            print("\n📋 COMANDI:")
            print("  1 - Status completo")
            print("  2 - Test GPS")
            print("  3 - Test IMU")
            print("  4 - Test Prossimità")
            print("  5 - Test NFC")
            print("  6 - Test Motore")
            print("  7 - Simula movimento")
            print("  8 - Test AI Integration")
            print("  0 - Esci")
            
            try:
                choice = input("\n👉 Scegli: ").strip()
                self.execute_command(choice)
            except KeyboardInterrupt:
                print("\n👋 Test terminato")
                self.running = False
                break
    
    def update_sensors(self):
        """Aggiorna i dati dei sensori in tempo reale"""
        # GPS
        if self.moving:
            self.sensors['gps']['data']['speed'] = random.uniform(5, 20)
            self.sensors['gps']['data']['lat'] += random.uniform(-0.0001, 0.0001)
            self.sensors['gps']['data']['lon'] += random.uniform(-0.0001, 0.0001)
        else:
            self.sensors['gps']['data']['speed'] = 0
        
        # IMU (simula movimento)
        if self.moving:
            self.sensors['imu']['data']['accel'] = [
                random.uniform(-2, 2),
                random.uniform(-2, 2),
                random.uniform(8, 10)
            ]
            self.sensors['imu']['data']['gyro'] = [
                random.uniform(-5, 5),
                random.uniform(-5, 5),
                random.uniform(-5, 5)
            ]
        
        # Prossimità (simula ostacoli)
        if random.random() < 0.02:  # 2% di probabilità di un ostacolo
            self.sensors['proximity']['data']['distance'] = random.uniform(10, 50)
            self.sensors['proximity']['status'] = 'WARNING'
        else:
            self.sensors['proximity']['data']['distance'] = random.uniform(100, 200)
            self.sensors['proximity']['status'] = 'OK'
        
        # Batteria
        if self.moving:
            self.sensors['battery']['data']['level'] -= 0.05
            if self.sensors['battery']['data']['level'] < 0:
                self.sensors['battery']['data']['level'] = 0
        
        # Motore
        if self.moving:
            self.sensors['motor']['data']['rpm'] = random.uniform(100, 3000)
            self.sensors['motor']['data']['temp'] += random.uniform(0.1, 0.5)
        else:
            self.sensors['motor']['data']['rpm'] = 0
            if self.sensors['motor']['data']['temp'] > 25:
                self.sensors['motor']['data']['temp'] -= 0.1
    
    def execute_command(self, choice):
        """Esegue il comando selezionato"""
        if choice == '1':
            self.show_status()
        elif choice == '2':
            self.test_gps()
        elif choice == '3':
            self.test_imu()
        elif choice == '4':
            self.test_proximity()
        elif choice == '5':
            self.test_nfc()
        elif choice == '6':
            self.test_motor()
        elif choice == '7':
            self.toggle_movement()
        elif choice == '8':
            self.test_ai()
        elif choice == '0':
            self.running = False
            print("👋 Arrivederci!")
        else:
            print("❌ Comando non valido")
    
    def show_status(self):
        """Mostra lo stato completo"""
        print("\n📊 STATO COMPLETO:")
        print("=" * 50)
        for sensor, data in self.sensors.items():
            status = "✅" if data['status'] == 'OK' else "⚠️"
            print(f"{status} {sensor.upper()}: {data['status']}")
            if sensor == 'gps':
                print(f"   📍 Lat: {data['data']['lat']:.4f}")
                print(f"   📍 Lon: {data['data']['lon']:.4f}")
                print(f"   ⚡ Speed: {data['data']['speed']:.1f} km/h")
            elif sensor == 'imu':
                print(f"   📊 Accel: {data['data']['accel']}")
            elif sensor == 'proximity':
                print(f"   📏 Distanza: {data['data']['distance']:.1f} cm")
            elif sensor == 'battery':
                print(f"   🔋 Livello: {data['data']['level']:.1f}%")
                print(f"   ⚡ Voltaggio: {data['data']['voltage']:.1f}V")
            elif sensor == 'motor':
                print(f"   🌀 RPM: {data['data']['rpm']:.0f}")
                print(f"   🌡️ Temp: {data['data']['temp']:.1f}°C")
            print()
    
    def test_gps(self):
        """Test GPS"""
        print("\n📍 TEST GPS:")
        print("=" * 30)
        gps_data = self.sensors['gps']['data']
        print(f"Latitudine: {gps_data['lat']:.6f}")
        print(f"Longitudine: {gps_data['lon']:.6f}")
        print(f"Velocità: {gps_data['speed']:.1f} km/h")
        print(f"Stato: {self.sensors['gps']['status']}")
        
        # Verifica connessione GPS
        if gps_data['lat'] != 0 or gps_data['lon'] != 0:
            print("✅ GPS: Segnale acquisito")
        else:
            print("⚠️ GPS: In attesa di segnale...")
    
    def test_imu(self):
        """Test IMU"""
        print("\n📊 TEST IMU:")
        print("=" * 30)
        imu_data = self.sensors['imu']['data']
        print(f"Accelerometro: X={imu_data['accel'][0]:.2f}, Y={imu_data['accel'][1]:.2f}, Z={imu_data['accel'][2]:.2f} m/s²")
        print(f"Giroscopio: X={imu_data['gyro'][0]:.2f}, Y={imu_data['gyro'][1]:.2f}, Z={imu_data['gyro'][2]:.2f} °/s")
        print(f"Stato: {self.sensors['imu']['status']}")
    
    def test_proximity(self):
        """Test sensore prossimità"""
        print("\n📏 TEST PROSSIMITÀ:")
        print("=" * 30)
        prox_data = self.sensors['proximity']['data']
        print(f"Distanza: {prox_data['distance']:.1f} cm")
        print(f"Stato: {self.sensors['proximity']['status']}")
        
        if prox_data['distance'] < 50:
            print("⚠️ OSTACOLO RILEVATO!")
        elif prox_data['distance'] < 100:
            print("⚠️ Attenzione: ostacolo vicino")
        else:
            print("✅ Percorso libero")
    
    def test_nfc(self):
        """Test NFC"""
        print("\n🔑 TEST NFC:")
        print("=" * 30)
        nfc_data = self.sensors['nfc']['data']
        print(f"Tag: {nfc_data['tag']}")
        print(f"Stato: {self.sensors['nfc']['status']}")
        
        # Simula lettura tag
        if nfc_data['tag'] == 'None':
            nfc_data['tag'] = 'UID: ' + ''.join([str(random.randint(0,9)) for _ in range(8)])
            print("✅ Tag NFC letto con successo!")
    
    def test_motor(self):
        """Test motore"""
        print("\n🌀 TEST MOTORE:")
        print("=" * 30)
        motor_data = self.sensors['motor']['data']
        print(f"RPM: {motor_data['rpm']:.0f}")
        print(f"Temperatura: {motor_data['temp']:.1f}°C")
        print(f"Stato: {self.sensors['motor']['status']}")
        
        if motor_data['temp'] > 45:
            print("⚠️ ATTENZIONE: Temperatura elevata!")
        else:
            print("✅ Motore operativo")
    
    def toggle_movement(self):
        """Toggle movimento"""
        self.moving = not self.moving
        if self.moving:
            print("🚀 Simulazione movimento AVVIATA")
            self.sensors['motor']['status'] = 'OK'
        else:
            print("🛑 Simulazione movimento FERMATA")
    
    def test_ai(self):
        """Test AI Integration"""
        print("\n🧠 TEST AI INTEGRATION:")
        print("=" * 30)
        
        # Simula richiesta AI
        print("📤 Invio richiesta a Pytho AI...")
        time.sleep(1)
        
        # Simula risposta AI
        responses = [
            "✅ Sistema di diagnostica: Tutti i sensori OK",
            "🔋 Batteria: Carica sufficiente per 30km",
            "🌡️ Temperatura motore: Nella norma (35°C)",
            "📡 GPS: Segnale acquisito - Posizione valida",
            "🛣️ Condizioni: Percorso ottimale"
        ]
        
        print("📥 Risposta AI:")
        print(f"   🤖 {random.choice(responses)}")
        print("")
        print("✅ Test AI completato con successo!")

if __name__ == "__main__":
    tester = SensorTester()
    tester.run()
