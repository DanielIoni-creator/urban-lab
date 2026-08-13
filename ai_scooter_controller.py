#!/usr/bin/env python3
"""
🛴 AI SCOOTER CONTROLLER - Monopattino del Futuro
Urban Lab Rimini - MyZubster Integration
"""

import time
import json
import threading
from datetime import datetime
import requests

class AIScooterController:
    def __init__(self):
        print("🛴 AI Scooter Controller - Avvio...")
        print("🏭 Urban Lab Rimini - Monopattino del Futuro")
        print("=" * 50)
        
        self.ai_config = {
            'pytho_url': 'http://localhost:3005/api/pytho/chat'
        }
        
        self.scooter_state = {
            'speed': 0,
            'battery': 100,
            'temperature': 25,
            'motor_temp': 30,
            'gps': {'lat': 44.0576, 'lon': 12.5653},
            'status': 'idle',
            'errors': [],
            'urban_lab': {
                'location': 'Via Bonsi, Rimini',
                'project': 'Monopattino del Futuro',
                'version': '1.0.0'
            }
        }
        
        self.start_monitoring()

    def start_monitoring(self):
        def monitor():
            while True:
                self.update_state()
                self.check_errors()
                time.sleep(5)
        thread = threading.Thread(target=monitor, daemon=True)
        thread.start()
        print("📡 Monitoraggio attivo")

    def update_state(self):
        self.scooter_state['battery'] = max(0, self.scooter_state['battery'] - 0.5)
        self.scooter_state['temperature'] = 25 + (self.scooter_state['speed'] * 0.1)

    def check_errors(self):
        errors = []
        if self.scooter_state['battery'] < 20:
            errors.append("Batteria bassa (<20%)")
        if self.scooter_state['temperature'] > 45:
            errors.append("Temperatura eccessiva")
        if errors:
            self.scooter_state['errors'] = errors
            self.ask_ai_for_help(errors)

    def ask_ai_for_help(self, errors):
        try:
            prompt = f"Monopattino Urban Lab ha problemi: {', '.join(errors)}"
            response = requests.post(
                self.ai_config['pytho_url'],
                json={'message': prompt},
                timeout=5
            )
            if response.status_code == 200:
                advice = response.json()['data']['reply']
                print(f"🤖 Pytho consiglia: {advice}")
        except requests.exceptions.RequestException:
            print("⚠️ Pytho AI non disponibile - Modalità offline")
        except:
            pass

    def get_status(self):
        return {
            'scooter_state': self.scooter_state,
            'timestamp': datetime.now().isoformat(),
            'urban_lab': self.scooter_state['urban_lab']
        }

if __name__ == "__main__":
    controller = AIScooterController()
    print("")
    print("📋 COMANDI DISPONIBILI:")
    print("   status  - Mostra stato monopattino")
    print("   ai:     - Chiedi aiuto a Pytho AI")
    print("   exit    - Esci")
    print("")
    
    while True:
        try:
            cmd = input("> ").strip()
            if cmd == 'exit':
                print("👋 Arrivederci da Urban Lab!")
                break
            elif cmd == 'status':
                print(json.dumps(controller.get_status(), indent=2))
            elif cmd.startswith('ai:'):
                msg = cmd[3:].strip()
                controller.ask_ai_for_help([msg])
            else:
                print("Comandi: status, ai: <messaggio>, exit")
        except KeyboardInterrupt:
            print("\n👋 Arrivederci da Urban Lab!")
            break
