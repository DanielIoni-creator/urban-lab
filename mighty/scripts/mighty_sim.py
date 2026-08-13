#!/usr/bin/env python3
"""
🧠 MIGHTY Simulator Module
Versione importabile del simulatore MIGHTY
"""

import numpy as np
import time
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class Obstacle:
    x: float
    y: float
    radius: float

class MightySimulator:
    """Simulatore MIGHTY per Urban Lab"""
    
    def __init__(self):
        self.position = np.array([0.0, 0.0])
        self.velocity = np.array([0.0, 0.0])
        self.max_speed = 6.7  # m/s
        self.max_accel = 2.0
        self.obstacles = []
        self.trajectory = []
        self.goal = None
        
    def add_obstacle(self, x: float, y: float, radius: float):
        """Aggiunge un ostacolo alla mappa"""
        self.obstacles.append(Obstacle(x, y, radius))
        print(f"⚠️ Ostacolo aggiunto: ({x}, {y}) raggio {radius}m")
    
    def set_goal(self, x: float, y: float):
        """Imposta l'obiettivo"""
        self.goal = np.array([x, y])
        print(f"🎯 Obiettivo impostato: ({x}, {y})")
    
    def compute_trajectory(self):
        """Calcola la traiettoria usando l'ottimizzazione MIGHTY"""
        if self.goal is None:
            return
        
        # Calcola distanza e direzione
        direction = self.goal - self.position
        distance = np.linalg.norm(direction)
        
        if distance < 0.1:
            print("✅ Obiettivo raggiunto!")
            return
        
        # Genera traiettoria (semplificata)
        num_points = 20
        trajectory_points = []
        
        for i in range(num_points):
            t = i / num_points
            # Movimento con accelerazione costante
            pos = self.position + direction * t * 0.5
            trajectory_points.append(pos.copy())
        
        self.trajectory = trajectory_points
        return trajectory_points
    
    def avoid_obstacles(self):
        """Evita ostacoli usando il metodo di MIGHTY"""
        if not self.obstacles or len(self.trajectory) < 2:
            return
        
        # Controlla ogni punto della traiettoria
        for i, point in enumerate(self.trajectory):
            for obs in self.obstacles:
                dist = np.linalg.norm(point - np.array([obs.x, obs.y]))
                if dist < obs.radius:
                    # Devia dalla traiettoria
                    deviation = np.array([obs.x, obs.y]) - point
                    deviation_norm = np.linalg.norm(deviation)
                    if deviation_norm > 0:
                        deviation = deviation / deviation_norm * (obs.radius - dist + 0.5)
                        self.trajectory[i] = point + deviation
                        print(f"🔄 Deviazione ostacolo a punto {i}")
    
    def move(self, dt: float = 0.1):
        """Muove il robot lungo la traiettoria"""
        if not self.trajectory:
            return
        
        # Trova il punto più vicino sulla traiettoria
        min_dist = float('inf')
        target_idx = 0
        
        for i, point in enumerate(self.trajectory):
            dist = np.linalg.norm(point - self.position)
            if dist < min_dist:
                min_dist = dist
                target_idx = i
        
        if target_idx < len(self.trajectory) - 1:
            target = self.trajectory[target_idx + 1]
            direction = target - self.position
            distance = np.linalg.norm(direction)
            
            if distance > 0.1:
                # Calcola velocità
                speed = min(self.max_speed, distance / dt)
                direction = direction / distance
                
                # Applica accelerazione
                accel = (speed - np.linalg.norm(self.velocity)) / dt
                accel = min(accel, self.max_accel)
                
                # Aggiorna posizione
                self.velocity = direction * speed
                self.position += self.velocity * dt
            else:
                self.velocity = np.array([0.0, 0.0])
    
    def get_status(self):
        """Restituisce lo stato attuale"""
        return {
            'position': self.position.tolist(),
            'velocity': self.velocity.tolist(),
            'speed': np.linalg.norm(self.velocity),
            'goal': self.goal.tolist() if self.goal is not None else None,
            'obstacles': len(self.obstacles),
            'trajectory_points': len(self.trajectory)
        }

# Funzione di test rapido
if __name__ == "__main__":
    print("🧠 MIGHTY Simulator - Test Rapido")
    sim = MightySimulator()
    sim.add_obstacle(3.0, 2.0, 1.0)
    sim.set_goal(10.0, 5.0)
    
    for _ in range(10):
        sim.compute_trajectory()
        sim.avoid_obstacles()
        sim.move(0.1)
        status = sim.get_status()
        print(f"Pos: {status['position']}, Speed: {status['speed']:.2f}")
