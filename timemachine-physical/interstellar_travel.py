#!/usr/bin/env python3
"""
🌌 URBAN LAB - Viaggi Interstellari
Simulazione di viaggi verso altre stelle
"""

import math
import time
from simulator import ViaggioTemporale

class InterstellarTravel:
    def __init__(self):
        self.destinations = {
            'Proxima Centauri': 4.24,
            'Alpha Centauri': 4.37,
            'Barnard\'s Star': 5.96,
            'Wolf 359': 7.78,
            'Sirius': 8.60,
            'Epsilon Eridani': 10.5,
            'Tau Ceti': 11.9,
            'Gliese 581': 20.3,
            'Kepler-442': 1200,
            'Andromeda Galaxy': 2540000
        }
        
    def show_destinations(self):
        print("🌌 DESTINAZIONI DISPONIBILI")
        print("=" * 50)
        for i, (name, dist) in enumerate(self.destinations.items(), 1):
            print(f"{i:2}. {name:20} → {dist:8.2f} anni luce")
        print("")
        
    def calculate_travel(self, destination, velocity):
        """Calcola il viaggio verso una destinazione"""
        dist = self.destinations[destination]
        
        # Tempo sulla Terra
        time_earth = dist / velocity
        
        # Dilatazione temporale
        v = ViaggioTemporale(2024, 3000)
        r = v.simula_viaggio(velocity, 1000)
        dilatazione = r['dilatazione']
        
        # Tempo per il viaggiatore
        time_ship = time_earth / dilatazione
        
        return {
            'destination': destination,
            'distance': dist,
            'velocity': velocity,
            'time_earth': time_earth,
            'time_ship': time_ship,
            'dilatation': dilatazione,
            'arrival_earth': 2024 + time_earth
        }
    
    def show_travel(self, result):
        """Mostra i risultati del viaggio"""
        print("\n🚀 RISULTATI DEL VIAGGIO")
        print("=" * 50)
        print(f"📍 Destinazione: {result['destination']}")
        print(f"📏 Distanza: {result['distance']:.2f} anni luce")
        print(f"⚡ Velocità: {result['velocity']*100:.1f}% della luce")
        print(f"⏳ Dilatazione: {result['dilatation']:.2f}x")
        print(f"🕐 Tempo sulla nave: {result['time_ship']:.2f} anni")
        print(f"🌍 Tempo sulla Terra: {result['time_earth']:.2f} anni")
        print(f"📅 Arrivo sulla Terra: {int(result['arrival_earth'])}")
        print("")
        
        # Effetto paradosso
        if result['time_ship'] > 80:
            print("⚠️ Il viaggio dura più di una vita umana!")
        elif result['time_ship'] > 50:
            print("⚠️ Il viaggio durerà gran parte della tua vita!")
        else:
            print("✅ Viaggio fattibile in una vita umana!")
        
        print("")
        print("🔮 Effetto del viaggio:")
        diff = result['time_earth'] - result['time_ship']
        print(f"   Sarai più giovane di {diff:.2f} anni")
        print(f"   Rispetto a chi è rimasto sulla Terra!")
    
    def run(self):
        """Esegue il simulatore interstellare"""
        print("🌌 URBAN LAB - VIAGGI INTERSTELLARI")
        print("=" * 50)
        print("")
        
        self.show_destinations()
        
        # Scegli destinazione
        choice = int(input("Scegli una destinazione (numero): "))
        dest_names = list(self.destinations.keys())
        destination = dest_names[choice - 1]
        
        # Scegli velocità
        print("")
        print("⚡ Scegli la velocità:")
        print("1. 50% della luce (lento)")
        print("2. 90% della luce (veloce)")
        print("3. 99% della luce (molto veloce)")
        print("4. 99.9% della luce (estremo)")
        speed_choice = int(input("Scelta (1-4): "))
        
        speeds = [0.5, 0.9, 0.99, 0.999]
        velocity = speeds[speed_choice - 1]
        
        # Calcola e mostra
        result = self.calculate_travel(destination, velocity)
        self.show_travel(result)

if __name__ == "__main__":
    travel = InterstellarTravel()
    travel.run()
