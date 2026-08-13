#!/usr/bin/env python3
"""
🔧 Calibrazione Sensori per Urban Lab
Calibra IMU, GPS e LiDAR per il monopattino
"""

import time
import json
import numpy as np
from dataclasses import dataclass, asdict

@dataclass
class CalibrationData:
    imu_offset: tuple = (0.0, 0.0, 0.0)
    imu_scale: tuple = (1.0, 1.0, 1.0)
    gps_offset: tuple = (0.0, 0.0)
    lidar_offset: float = 0.0
    timestamp: float = 0.0

class SensorCalibrator:
    """Calibratore sensori per Urban Lab"""
    
    def __init__(self):
        self.calibration = CalibrationData()
        self.samples = []
        self.calibrating = False
        
    def collect_samples(self, sensor_type, data, duration=5.0):
        """Raccoglie campioni per calibrazione"""
        print(f"📊 Calibrazione {sensor_type}...")
        print(f"   Raccogliendo campioni per {duration}s")
        
        start_time = time.time()
        samples = []
        
        while time.time() - start_time < duration:
            if sensor_type == 'imu':
                samples.append(data)
            elif sensor_type == 'gps':
                samples.append(data)
            time.sleep(0.1)
        
        return np.array(samples)
    
    def calibrate_imu(self, samples):
        """Calibra IMU (accelerometro/giroscopio)"""
        print("🔧 Calibrazione IMU...")
        
        # Calcola offset (media)
        offset = np.mean(samples, axis=0)
        
        # Calcola scale (deviazione standard)
        scale = np.std(samples, axis=0)
        
        self.calibration.imu_offset = tuple(offset)
        self.calibration.imu_scale = tuple(np.clip(scale, 0.1, 10.0))
        
        print(f"   Offset: {offset}")
        print(f"   Scale: {scale}")
        
    def calibrate_gps(self, samples):
        """Calibra GPS"""
        print("🔧 Calibrazione GPS...")
        
        # Calcola offset
        offset = np.mean(samples, axis=0)
        
        self.calibration.gps_offset = tuple(offset)
        
        print(f"   Offset GPS: {offset}")
    
    def save_calibration(self, filename='calibration.json'):
        """Salva i dati di calibrazione"""
        data = asdict(self.calibration)
        data['timestamp'] = time.time()
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Calibrazione salvata in {filename}")
    
    def load_calibration(self, filename='calibration.json'):
        """Carica i dati di calibrazione"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.calibration = CalibrationData(**data)
            print(f"✅ Calibrazione caricata da {filename}")
            return True
        except:
            print("❌ Nessun file di calibrazione trovato")
            return False

def main():
    print("🔧 URBAN LAB - Calibrazione Sensori")
    print("=" * 50)
    
    calibrator = SensorCalibrator()
    
    # Simula dati sensori
    imu_samples = np.random.randn(50, 3) * 0.1
    gps_samples = np.random.randn(50, 2) * 0.01
    
    # Calibra
    calibrator.calibrate_imu(imu_samples)
    calibrator.calibrate_gps(gps_samples)
    
    # Salva
    calibrator.save_calibration()
    
    print("\n📋 Calibrazione completata!")
    print("📌 Usa calibration.json per configurare il monopattino")

if __name__ == "__main__":
    main()
