#!/usr/bin/env python3
"""
🔄 URBAN LAB - Test Continuo Macchina del Tempo
Monitoraggio in tempo reale dei componenti
"""

import time
import random
import sys
from datetime import datetime

class ContinuousTest:
    def __init__(self):
        self.components = {
            'Raspberry Pi 5': {'status': 'OK', 'temp': 45},
            'Arduino Mega': {'status': 'OK', 'temp': 35},
            'Bobina Tesla': {'status': 'STANDBY', 'temp': 25},
            'Sensori Hall': {'status': 'OK', 'reading': 512},
            'Batteria': {'status': 'OK', 'level': 95}
        }
        self.running = True
        
    def run(self):
        print("🔄 URBAN LAB - TEST CONTINUO")
        print("=" * 50)
        print("Premi CTRL+C per fermare\n")
        
        while self.running:
            self.update()
            self.display()
            time.sleep(2)
    
    def update(self):
        # Simula variazioni
        for comp in self.components:
            if comp == 'Bobina Tesla':
                self.components[comp]['temp'] += random.uniform(-0.5, 0.5)
            elif comp == 'Sensori Hall':
                self.components[comp]['reading'] = random.randint(200, 800)
            elif comp == 'Batteria':
                self.components[comp]['level'] -= 0.1
                if self.components[comp]['level'] < 0:
                    self.components[comp]['level'] = 0
    
    def display(self):
        print(f"\r⏰ {datetime.now().strftime('%H:%M:%S')} ", end="")
        for comp, data in self.components.items():
            status = data.get('status', 'OK')
            if status == 'OK':
                icon = '✅'
            elif status == 'STANDBY':
                icon = '⏳'
            else:
                icon = '❌'
            print(f"{icon}{comp} ", end="")
        sys.stdout.flush()

if __name__ == "__main__":
    test = ContinuousTest()
    try:
        test.run()
    except KeyboardInterrupt:
        print("\n\n✅ Test fermato!")
