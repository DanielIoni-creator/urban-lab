#!/usr/bin/env python3
"""
🌀 Macchina del Tempo - Controller Raspberry Pi 5
Gestione interfaccia e comunicazione con Arduino
"""

import serial
import time
import json
import threading
from datetime import datetime

class TimeMachineController:
    def __init__(self):
        self.serial_port = None
        self.connected = False
        self.sensor_data = {
            'campo_magnetico': 0,
            'wormhole_aperto': False,
            'sistema_attivo': False,
            'tempo_viaggio': 0
        }
        
        # Connetti ad Arduino
        try:
            self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            time.sleep(2)
            self.connected = True
            print("✅ Connesso ad Arduino!")
        except:
            print("⚠️ Arduino non trovato! Avvio in modalità simulazione")
            self.connected = False
        
        # Avvia thread per lettura seriale
        self.running = True
        self.thread = threading.Thread(target=self.read_serial)
        self.thread.daemon = True
        self.thread.start()
    
    def read_serial(self):
        """Legge i dati da Arduino"""
        while self.running:
            if self.connected and self.serial_port:
                try:
                    data = self.serial_port.readline().decode().strip()
                    if data.startswith("DATA:"):
                        parts = data[5:].split(',')
                        if len(parts) >= 4:
                            self.sensor_data['campo_magnetico'] = int(parts[0])
                            self.sensor_data['sistema_attivo'] = bool(int(parts[1]))
                            self.sensor_data['wormhole_aperto'] = bool(int(parts[2]))
                            self.sensor_data['tempo_viaggio'] = int(parts[3]) / 1000
                except:
                    pass
            time.sleep(0.1)
    
    def avvia_viaggio(self):
        """Avvia il viaggio nel tempo"""
        print("🌀 Avvio viaggio nel tempo...")
        if self.connected and self.serial_port:
            self.serial_port.write(b"START\n")
            return True
        else:
            print("🔧 Modalità simulazione: viaggio iniziato!")
            self.sensor_data['sistema_attivo'] = True
            return True
    
    def ferma_viaggio(self):
        """Ferma il viaggio nel tempo"""
        print("🔄 Fermo viaggio nel tempo...")
        if self.connected and self.serial_port:
            self.serial_port.write(b"STOP\n")
            return True
        else:
            print("🔧 Modalità simulazione: viaggio fermato!")
            self.sensor_data['sistema_attivo'] = False
            return True
    
    def get_status(self):
        """Restituisce lo stato attuale"""
        return {
            'connected': self.connected,
            'sensor_data': self.sensor_data,
            'timestamp': datetime.now().isoformat()
        }
    
    def run_interactive(self):
        """Modalità interattiva"""
        print("🌀 MACCHINA DEL TEMPO - CONTROLLER")
        print("=" * 50)
        print("Comandi:")
        print("  start - Avvia viaggio")
        print("  stop  - Ferma viaggio")
        print("  status - Mostra stato")
        print("  exit  - Esci")
        print("")
        
        while self.running:
            cmd = input("> ").strip().lower()
            
            if cmd == 'start':
                self.avvia_viaggio()
            elif cmd == 'stop':
                self.ferma_viaggio()
            elif cmd == 'status':
                status = self.get_status()
                print(json.dumps(status, indent=2))
            elif cmd == 'exit':
                self.running = False
                print("Arrivederci! 🌀")
            else:
                print("Comando non riconosciuto!")

if __name__ == "__main__":
    controller = TimeMachineController()
    controller.run_interactive()
