#!/usr/bin/env python3
"""
🛴 Urban Lab Scooter Simulator
Simula i dati dei sensori per test senza hardware
"""

import time
import random
import json
import threading
from datetime import datetime

class ScooterSimulator:
    def __init__(self):
        self.state = {
            'speed': 0,
            'battery': 100,
            'temperature': 25,
            'motor_temp': 30,
            'gps': {'lat': 44.0576, 'lon': 12.5653},
            'is_moving': False,
            'is_locked': False,
            'errors': 0
        }
        self.running = True
        
    def run(self):
        print("🛴 Urban Lab Scooter Simulator")
        print("=" * 50)
        print("Simulazione sensori attiva...")
        print("Comandi: status, move, stop, lock, unlock, exit")
        print("")
        
        # Thread per aggiornamento automatico
        def update_loop():
            while self.running:
                self.update_state()
                time.sleep(1)
        
        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()
        
        # Interfaccia comandi
        while self.running:
            try:
                cmd = input("> ").strip().lower()
                self.execute_command(cmd)
            except KeyboardInterrupt:
                print("\n👋 Simulazione terminata")
                self.running = False
                break
    
    def update_state(self):
        """Aggiorna lo stato simulato"""
        if self.state['is_moving']:
            self.state['speed'] = random.uniform(5, 20)
            self.state['battery'] -= 0.05
        else:
            self.state['speed'] = 0
            
        # Simula riscaldamento
        if self.state['speed'] > 0:
            self.state['temperature'] += 0.01
            self.state['motor_temp'] += 0.02
        
        # Simula GPS drift
        self.state['gps']['lat'] += random.uniform(-0.0001, 0.0001)
        self.state['gps']['lon'] += random.uniform(-0.0001, 0.0001)
        
        # Controlla errori
        self.state['errors'] = 0
        if self.state['battery'] < 20:
            self.state['errors'] += 1
        if self.state['temperature'] > 45:
            self.state['errors'] += 1
    
    def execute_command(self, cmd):
        """Esegue i comandi"""
        if cmd == 'status':
            print(json.dumps(self.state, indent=2))
        elif cmd == 'move':
            self.state['is_moving'] = True
            print("🚀 In movimento...")
        elif cmd == 'stop':
            self.state['is_moving'] = False
            self.state['speed'] = 0
            print("🛑 Fermo")
        elif cmd == 'lock':
            self.state['is_locked'] = True
            print("🔒 Bloccato")
        elif cmd == 'unlock':
            self.state['is_locked'] = False
            print("🔓 Sbloccato")
        elif cmd == 'exit':
            self.running = False
        else:
            print("Comandi: status, move, stop, lock, unlock, exit")

if __name__ == "__main__":
    simulator = ScooterSimulator()
    simulator.run()
