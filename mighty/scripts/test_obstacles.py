#!/usr/bin/env python3
"""
🧪 MIGHTY - Test con ostacoli dinamici
Utilizza il simulatore MIGHTY esistente
"""

import sys
import os

# Aggiungi il percorso per importare il simulatore
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Importa direttamente dal file esistente
exec(open(os.path.join(os.path.dirname(__file__), 'test_mighty_sim.py')).read())

def main():
    print("🏭 URBAN LAB - MIGHTY con ostacoli dinamici")
    print("=" * 50)
    
    # Crea il simulatore
    mighty = MightySimulator()
    
    # Aggiungi ostacoli
    print("\n⚠️ Aggiunta ostacoli...")
    obstacles = [
        (3.0, 2.0, 1.0),
        (5.0, 4.0, 0.8),
        (2.0, 6.0, 1.2),
        (7.0, 3.0, 0.5),  # Ostacolo aggiuntivo
        (8.5, 5.5, 0.7),  # Ostacolo aggiuntivo 2
    ]
    
    for x, y, r in obstacles:
        mighty.add_obstacle(x, y, r)
        print(f"   ⚠️ Ostacolo a ({x}, {y}) raggio {r}m")
    
    # Imposta obiettivo
    mighty.set_goal(10.0, 5.0)
    
    # Simula movimento
    print("\n🚀 Avvio simulazione con ostacoli...")
    print("-" * 50)
    
    for step in range(60):
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
        
        # Mostra se sta evitando ostacoli
        import numpy as np
        obstacles_near = 0
        for obs in obstacles:
            dist = np.linalg.norm(np.array(pos) - np.array([obs[0], obs[1]]))
            if dist < obs[2] + 1.0:
                obstacles_near += 1
        
        near = "⚠️" if obstacles_near > 0 else "✅"
        print(f"{near} Posizione: ({pos[0]:.2f}, {pos[1]:.2f})  ⚡ Velocità: {speed:.2f} m/s")
        
        # Controlla se arrivato
        if status['goal']:
            goal_dist = np.linalg.norm(np.array(pos) - np.array(status['goal']))
            if goal_dist < 0.5:
                print("\n✅ Obiettivo raggiunto!")
                break
        
        time.sleep(0.05)
    
    print("\n📊 Statistiche finali:")
    status = mighty.get_status()
    print(f"   📍 Posizione finale: ({status['position'][0]:.2f}, {status['position'][1]:.2f})")
    print(f"   ⚡ Velocità finale: {status['speed']:.2f} m/s")
    print(f"   🧠 Punti traiettoria: {status['trajectory_points']}")
    print(f"   🚧 Ostacoli evitati: {len(obstacles)}")

if __name__ == "__main__":
    main()
