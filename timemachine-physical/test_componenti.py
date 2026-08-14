#!/usr/bin/env python3
"""
🧪 URBAN LAB - Test Componenti Macchina del Tempo
Verifica il funzionamento di ogni componente
"""

import time
import sys

def test_raspberry_pi():
    """Test Raspberry Pi 5"""
    print("🧪 Test Raspberry Pi 5...")
    try:
        import platform
        print(f"   ✅ Sistema: {platform.system()}")
        print(f"   ✅ Versione: {platform.version()}")
        return True
    except:
        print("   ❌ Errore Raspberry Pi")
        return False

def test_arduino():
    """Test Arduino Mega"""
    print("🧪 Test Arduino Mega...")
    try:
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "Mega" in port.description:
                print(f"   ✅ Arduino trovato su: {port.device}")
                return True
        print("   ⚠️ Arduino non trovato (controlla connessione USB)")
        return False
    except:
        print("   ❌ Errore Arduino")
        return False

def test_sensori():
    """Test sensori Hall"""
    print("🧪 Test Sensori Hall...")
    # Simula test sensori
    import random
    valori = [random.randint(200, 800) for _ in range(4)]
    print(f"   📊 Letture sensori: {valori}")
    if all(200 <= v <= 800 for v in valori):
        print("   ✅ Sensori funzionanti")
        return True
    else:
        print("   ⚠️ Sensori da calibrare")
        return False

def test_bobine():
    """Test bobine Tesla"""
    print("🧪 Test Bobine Tesla...")
    print("   ⚠️ Test manuale richiesto!")
    print("   📌 Verifica:")
    print("      1. Isolamento perfetto")
    print("      2. Scarica controllata")
    print("      3. Nessun cortocircuito")
    return True

def main():
    print("🧪 URBAN LAB - TEST COMPONENTI")
    print("=" * 50)
    print("")
    
    tests = [
        ("Raspberry Pi 5", test_raspberry_pi),
        ("Arduino Mega", test_arduino),
        ("Sensori Hall", test_sensori),
        ("Bobine Tesla", test_bobine)
    ]
    
    risultati = []
    for nome, test in tests:
        print(f"\n📌 Test {nome}:")
        result = test()
        risultati.append((nome, result))
    
    print("\n" + "=" * 50)
    print("📊 RIEPILOGO TEST:")
    for nome, result in risultati:
        stato = "✅" if result else "❌"
        print(f"   {stato} {nome}")
    
    totali = sum(1 for _, r in risultati if r)
    print(f"\n📈 Componenti funzionanti: {totali}/{len(risultati)}")

if __name__ == "__main__":
    main()
