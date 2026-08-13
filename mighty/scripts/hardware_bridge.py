#!/usr/bin/env python3
"""
🔌 MIGHTY - Bridge per Hardware Reale
Collega MIGHTY con ESP32 e sensori fisici
"""

import time
import json
import serial
import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class SensorData:
    """Dati dai sensori del monopattino"""
    speed: float = 0.0
    battery: float = 100.0
    temperature: float = 25.0
    imu_accel: tuple = (0.0, 0.0, 0.0)
    imu_gyro: tuple = (0.0, 0.0, 0.0)
    gps_lat: float = 44.0576
    gps_lon: float = 12.5653
    obstacle_distance: float = 10.0  # metri

class MightyHardwareBridge:
    """Bridge tra MIGHTY e hardware reale"""
    
    def __init__(self, serial_port: Optional[str] = None):
        self.serial_port = serial_port
        self.serial_conn = None
        
        # Stato del monopattino
        self.sensor_data = SensorData()
        self.command = {'linear': 0.0, 'angular': 0.0}
        
        # Collega al seriale se specificato
        if serial_port:
            try:
                self.serial_conn = serial.Serial(serial_port, 115200, timeout=0.1)
                print(f"✅ Connesso a {serial_port}")
            except Exception as e:
                print(f"❌ Errore connessione: {e}")
    
    def read_sensors(self):
        """Legge i dati dai sensori del monopattino"""
        # Se abbiamo connessione seriale, leggi i dati reali
        if self.serial_conn and self.serial_conn.in_waiting:
            try:
                data = self.serial_conn.readline().decode().strip()
                if data:
                    sensor_json = json.loads(data)
                    self.sensor_data = SensorData(
                        speed=sensor_json.get('speed', 0.0),
                        battery=sensor_json.get('battery', 100.0),
                        temperature=sensor_json.get('temperature', 25.0),
                        imu_accel=tuple(sensor_json.get('imu_accel', [0,0,0])),
                        imu_gyro=tuple(sensor_json.get('imu_gyro', [0,0,0])),
                        gps_lat=sensor_json.get('gps_lat', 44.0576),
                        gps_lon=sensor_json.get('gps_lon', 12.5653),
                        obstacle_distance=sensor_json.get('obstacle_distance', 10.0)
                    )
            except:
                pass
        
        # Se non abbiamo dati reali, simula
        else:
            self._simulate_sensors()
        
        return self.sensor_data
    
    def _simulate_sensors(self):
        """Simula dati sensori (fallback)"""
        self.sensor_data.speed = np.random.uniform(0, 5)
        self.sensor_data.battery = max(0, self.sensor_data.battery - 0.01)
        self.sensor_data.obstacle_distance = max(0.5, 
            10.0 + np.random.randn() * 2)
    
    def send_command(self, linear: float, angular: float):
        """Invia comandi al monopattino"""
        self.command = {'linear': linear, 'angular': angular}
        
        # Invia via seriale se connesso
        if self.serial_conn:
            try:
                cmd_json = json.dumps(self.command)
                self.serial_conn.write((cmd_json + '\n').encode())
            except:
                pass
        
        print(f"📤 Comando: linear={linear:.2f}, angular={angular:.2f}")
    
    def run(self, goal_x: float = 10.0, goal_y: float = 5.0):
        """Loop principale per hardware"""
        print(f"🏭 MIGHTY Hardware Bridge - Obiettivo: ({goal_x}, {goal_y})")
        print("=" * 50)
        
        # Posizione corrente (da GPS)
        position = np.array([0.0, 0.0])
        
        while True:
            # Leggi sensori
            sensors = self.read_sensors()
            
            # Calcola traiettoria (semplificata)
            direction = np.array([goal_x, goal_y]) - position
            distance = np.linalg.norm(direction)
            
            if distance < 0.5:
                print("✅ Obiettivo raggiunto!")
                break
            
            # Evita ostacoli (basato su distanza sensori)
            if sensors.obstacle_distance < 2.0:
                # Sterza per evitare
                angular = 0.5 * (1.0 - sensors.obstacle_distance / 2.0)
                linear = 0.0
                print(f"⚠️ Ostacolo a {sensors.obstacle_distance:.2f}m - Sterzata!")
            else:
                # Avanza normalmente
                linear = min(5.0, distance * 0.5)
                angular = 0.0
            
            # Invia comando
            self.send_command(linear, angular)
            
            # Aggiorna posizione simulata
            if linear > 0:
                position += np.array([0.1, 0.0])
            
            # Mostra stato
            print(f"📍 Pos: ({position[0]:.2f}, {position[1]:.2f})  "
                  f"⚡ Vel: {sensors.speed:.2f} m/s  "
                  f"🚧 Dist: {sensors.obstacle_distance:.2f}m")
            
            time.sleep(0.1)

if __name__ == "__main__":
    # Test con simulazione
    print("🧪 Test Hardware Bridge (simulato)")
    bridge = MightyHardwareBridge()  # Nessuna porta seriale
    bridge.run(goal_x=5.0, goal_y=3.0)
