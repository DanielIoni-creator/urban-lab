#!/usr/bin/env python3
"""
🧪 MIGHTY - Test con ostacoli in movimento
Simula ostacoli che si muovono
"""

import numpy as np
import time
import sys
import os

# Importa il simulatore
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from mighty_sim import MightySimulator, Obstacle

def main():
    print("🏭 URBAN LAB - MIGHTY con ostacoli in movimento")
    print("=" * 50)
    
    # Crea il simulatore
    mighty = MightySimulator()
    
    # Aggiungi ostacoli statici
    obstacles_static = [
        (3.0, 2.0, 1.0),
        (7.0, 3.0, 0.5),
    ]
    
    # Aggiungi ostacoli dinamici (in movimento)
    obstacles_dynamic = {
        'pos': np.array([5.0, 4.0]),
        'vel': np.array([0.3, 0.2]),
        'radius': 0.8
    }
    
    for x, y, r in obstacles_static:
        mighty.add_obstacle(x, y, r)
    
    print(f"⚠️ Ostacolo dinamico a (5.0, 4.0) raggio 0.8m in movimento")
    
    # Imposta obiettivo
    mighty.set_goal(10.0, 5.0)
    
    # Simula movimento
    print("\n🚀 Avvio simulazione con ostacoli in movimento...")
    print("-" * 50)
    
    for step in range(80):
        # Aggiorna posizione ostacolo dinamico
        obstacles_dynamic['pos'] += obstacles_dynamic['vel'] * 0.1
        
        # Aggiungi ostacolo dinamico alla lista
        dyn_obs = Obstacle(
            obstacles_dynamic['pos'][0],
            obstacles_dynamic['pos'][1],
            obstacles_dynamic['radius']
        )
        
        # Sostituisci gli ostacoli con quelli aggiornati
        mighty.obstacles = []
        for x, y, r in obstacles_static:
            mighty.add_obstacle(x, y, r)
        mighty.add_obstacle(dyn_obs.x, dyn_obs.y, dyn_obs.radius)
        
        # Calcola traiettoria
        mighty.compute_trajectory()
        
        # Evita ostacoli
        mighty.avoid_obstacles()
        
        # Muovi
        mighty.move(dt=0.1)
        
        # Mostra stato
        status = mighty.get_status()
        pos = status['position']
        speed = status['speed']
        dyn_pos = obstacles_dynamic['pos']
        
        print(f"📍 Pos: ({pos[0]:.2f}, {pos[1]:.2f})  ⚡ Vel: {speed:.2f} m/s  🚧 Ost: ({dyn_pos[0]:.2f}, {dyn_pos[1]:.2f})")
        
        # Controlla se arrivato
        if status['goal']:
            goal_dist = np.linalg.norm(np.array(pos) - np.array(status['goal']))
            if goal_dist < 0.5:
                print("\n✅ Obiettivo raggiunto con ostacoli dinamici!")
                break
        
        time.sleep(0.05)
    
    print("\n📊 Statistiche finali:")
    status = mighty.get_status()
    print(f"   📍 Posizione finale: ({status['position'][0]:.2f}, {status['position'][1]:.2f})")
    print(f"   ⚡ Velocità finale: {status['speed']:.2f} m/s")
    print(f"   🚧 Ostacoli evitati: {len(mighty.obstacles)}")

if __name__ == "__main__":
    main()
