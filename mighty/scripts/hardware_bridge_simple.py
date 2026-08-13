#!/usr/bin/env python3
"""
🔌 MIGHTY - Bridge Semplificato per Hardware
Versione senza dipendenze seriali per test
"""

import time
import json
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

class MightyHardwareBridgeSimple:
    """Bridge semplificato tra MIGHTY e hardware"""
    
    def __init__(self):
        self.sensor_data = SensorData()
        self.command = {'linear': 0.0, 'angular': 0.0}
        self.position = np.array([0.0, 0.0])
        self.goal = np.array([10.0, 5.0])
        self.step = 0
        
        print("🏭 MIGHTY Hardware Bridge (Semplificato)")
        print("=" * 50)
        print("📌 Simula sensori e invia comandi")
        print("")
    
    def read_sensors(self):
        """Legge i dati dai sensori (simulati)"""
        # Simula movimento
        self.sensor_data.speed = np.random.uniform(0, 5)
        self.sensor_data.battery = max(0, self.sensor_data.battery - 0.01)
        self.sensor_data.temperature = 25 + np.random.randn() * 2
        self.sensor_data.obstacle_distance = max(0.5, 
            10.0 + np.random.randn() * 3)
        
        return self.sensor_data
    
    def send_command(self, linear: float, angular: float):
        """Invia comandi al monopattino"""
        self.command = {'linear': linear, 'angular': angular}
        
        # Stampa comando (simula invio)
        status = "🚀" if linear > 1 else "⏸️"
        print(f"{status} Comando: linear={linear:.2f}, angular={angular:.2f}")
    
    def compute_trajectory(self):
        """Calcola traiettoria verso l'obiettivo"""
        direction = self.goal - self.position
        distance = np.linalg.norm(direction)
        
        if distance < 0.5:
            print("✅ Obiettivo raggiunto!")
            return None
        
        # Calcola velocità lineare e angolare
        linear = min(5.0, distance * 0.5)
        
        # Sterza per evitare ostacoli
        if self.sensor_data.obstacle_distance < 2.0:
            angular = 0.5 * (1.0 - self.sensor_data.obstacle_distance / 2.0)
            linear = 0.0
            print(f"⚠️ Ostacolo a {self.sensor_data.obstacle_distance:.2f}m")
        else:
            angular = 0.0
        
        return {'linear': linear, 'angular': angular}
    
    def run(self, goal_x: float = 10.0, goal_y: float = 5.0):
        """Loop principale"""
        self.goal = np.array([goal_x, goal_y])
        print(f"🎯 Obiettivo: ({goal_x}, {goal_y})")
        print("-" * 50)
        
        while True:
            # Leggi sensori
            sensors = self.read_sensors()
            
            # Calcola traiettoria
            cmd = self.compute_trajectory()
            if cmd is None:
                break
            
            # Invia comando
            self.send_command(cmd['linear'], cmd['angular'])
            
            # Aggiorna posizione simulata
            if cmd['linear'] > 0:
                self.position += np.array([0.05, 0.0])
            
            # Mostra stato
            print(f"📍 Pos: ({self.position[0]:.2f}, {self.position[1]:.2f})  "
                  f"⚡ Vel: {sensors.speed:.2f} m/s  "
                  f"🚧 Dist: {sensors.obstacle_distance:.2f}m")
            
            self.step += 1
            time.sleep(0.1)

if __name__ == "__main__":
    # Test con simulazione
    print("🧪 Test Hardware Bridge (semplificato)")
    bridge = MightyHardwareBridgeSimple()
    bridge.run(goal_x=5.0, goal_y=3.0)
