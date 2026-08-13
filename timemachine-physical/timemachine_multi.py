#!/usr/bin/env python3
"""
🌀 URBAN LAB - Viaggi Multipli nel Tempo
Pianifica e confronta diversi viaggi
"""

from simulator import ViaggioTemporale
import numpy as np

class TimeTravelPlanner:
    def __init__(self):
        self.travels = []
        
    def add_travel(self, start, end, velocity):
        """Aggiungi un viaggio alla lista"""
        v = ViaggioTemporale(start, end)
        r = v.simula_viaggio(velocity, 1000)
        self.travels.append({
            'start': start,
            'end': end,
            'velocity': velocity,
            'results': r
        })
        
    def compare_travels(self):
        """Confronta tutti i viaggi pianificati"""
        print("\n📊 CONFRONTO VIAGGI NEL TEMPO")
        print("=" * 60)
        
        for i, travel in enumerate(self.travels, 1):
            r = travel['results']
            print(f"\n🚀 Viaggio {i}: {travel['start']} → {travel['end']}")
            print(f"   ⚡ Velocità: {travel['velocity']*100:.1f}% luce")
            print(f"   ⏳ Dilatazione: {r['dilatazione']:.2f}x")
            print(f"   🕐 Tempo proprio: {r['tempo_proprio']:.1f} anni")
            print(f"   🌍 Tempo esterno: {r['tempo_esterno']:.1f} anni")
            print(f"   📅 Arrivo sulla Terra: {int(travel['start'] + r['tempo_esterno'])}")
    
    def find_best_travel(self, max_time, destination):
        """Trova il viaggio migliore entro un limite di tempo"""
        print(f"\n🔍 CERCA VIAGGIO VERSO {destination}")
        print(f"⏳ Tempo massimo: {max_time} anni")
        print("=" * 60)
        
        best_travel = None
        best_ratio = 0
        
        for velocity in np.linspace(0.5, 0.999, 20):
            v = ViaggioTemporale(2024, destination)
            r = v.simula_viaggio(velocity, 1000)
            
            if r['tempo_proprio'] <= max_time:
                ratio = r['tempo_esterno'] / r['tempo_proprio']
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_travel = (velocity, r)
        
        if best_travel:
            vel, r = best_travel
            print(f"\n✅ Viaggio ottimale trovato!")
            print(f"   ⚡ Velocità: {vel*100:.1f}% della luce")
            print(f"   ⏳ Dilatazione: {r['dilatazione']:.2f}x")
            print(f"   🕐 Tempo proprio: {r['tempo_proprio']:.1f} anni")
            print(f"   🌍 Tempo esterno: {r['tempo_esterno']:.1f} anni")
        else:
            print("\n❌ Nessun viaggio trovato entro il limite di tempo!")

# Esegui il pianificatore
if __name__ == "__main__":
    planner = TimeTravelPlanner()
    
    print("🌀 URBAN LAB - PIANIFICATORE DI VIAGGI NEL TEMPO")
    print("=" * 50)
    
    # Aggiungi viaggi
    planner.add_travel(2024, 2050, 0.9)
    planner.add_travel(2024, 2100, 0.99)
    planner.add_travel(2024, 3000, 0.99)
    planner.add_travel(2024, 3000, 0.999)
    
    # Confronta
    planner.compare_travels()
    
    # Trova il miglior viaggio
    planner.find_best_travel(50, 3000)
