#!/usr/bin/env python3
"""
🔌 Test Connessione ESP32
Verifica se l'ESP32 è connesso e risponde
"""

import serial
import time
import sys

def test_esp32_connection(port='/dev/ttyUSB0', baudrate=115200):
    """Testa la connessione con ESP32"""
    try:
        print(f"🔌 Test connessione ESP32 su {port}...")
        ser = serial.Serial(port, baudrate, timeout=2)
        time.sleep(2)  # Attendi che l'ESP32 si avvii
        
        # Invia comando di test
        ser.write(b"TEST\n")
        time.sleep(0.5)
        
        # Leggi risposta
        response = ser.read(ser.in_waiting or 100)
        if response:
            print(f"✅ ESP32 risponde: {response[:50]}")
            return True
        else:
            print("⚠️ ESP32 connesso ma non risponde")
            return False
            
    except serial.SerialException as e:
        print(f"❌ Errore connessione: {e}")
        return False
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False

if __name__ == "__main__":
    # Testa su porte comuni
    ports = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0']
    
    for port in ports:
        print(f"\n📌 Test su {port}")
        if test_esp32_connection(port):
            print(f"✅ ESP32 trovato su {port}")
            sys.exit(0)
    
    print("\n❌ Nessun ESP32 trovato!")
    print("💡 Verifica:")
    print("   1. ESP32 collegato via USB")
    print("   2. Driver installati")
    print("   3. Permessi: sudo chmod 666 /dev/ttyUSB*")
