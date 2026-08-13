#!/usr/bin/env python3
"""
🏭 Urban Lab - Ambiente di Reinforcement Learning per Monopattino
Basato su Gymnasium e Telekinesis RLbotics
"""

import gymnasium as gym
from gymnasium import spaces
import numpy as np
import math
from typing import Optional, Dict, Any

class ScooterEnv(gym.Env):
    """
    Ambiente simulato per il monopattino Urban Lab.
    
    Stato (Observation):
    - Velocità (0-20 km/h)
    - Inclinazione (-15° a 15°)
    - Batteria (0-100%)
    - Distanza ostacolo (0-200cm)
    - RPM motore (0-3000)
    - Temperatura motore (0-60°C)
    
    Azioni (Action):
    - Accelerazione (-1 a 1)
    - Frenata (0 a 1)
    - Angolo sterzo (-30° a 30°)
    """
    
    def __init__(self, render_mode: Optional[str] = None):
        super(ScooterEnv, self).__init__()
        
        # Spazio delle osservazioni
        self.observation_space = spaces.Box(
            low=np.array([0, -15, 0, 0, 0, 0], dtype=np.float32),
            high=np.array([20, 15, 100, 200, 3000, 60], dtype=np.float32),
            dtype=np.float32
        )
        
        # Spazio delle azioni
        self.action_space = spaces.Box(
            low=np.array([-1, 0, -30], dtype=np.float32),
            high=np.array([1, 1, 30], dtype=np.float32),
            dtype=np.float32
        )
        
        self.render_mode = render_mode
        self.reset()
    
    def reset(self, seed: Optional[int] = None, options: Optional[Dict] = None):
        """Reset dell'ambiente"""
        super().reset(seed=seed)
        
        # Stato iniziale
        self.state = np.array([
            0.0,    # Velocità
            0.0,    # Inclinazione
            100.0,  # Batteria
            150.0,  # Distanza ostacolo
            0.0,    # RPM
            25.0    # Temperatura
        ], dtype=np.float32)
        
        self.steps = 0
        self.max_steps = 1000
        self.crashed = False
        
        return self.state, {}
    
    def step(self, action):
        """Esegue un passo nell'ambiente"""
        # Estrai azioni
        accel, brake, steer = action
        
        # Simula fisica
        self.state[0] += accel * 0.5  # Velocità
        self.state[0] = np.clip(self.state[0], 0, 20)
        
        # Inclinazione in base a accelerazione e sterzo
        self.state[1] += (accel * 0.5 + steer * 0.1)
        self.state[1] = np.clip(self.state[1], -15, 15)
        
        # Batteria
        self.state[2] -= (abs(accel) * 0.1 + brake * 0.05)
        self.state[2] = np.clip(self.state[2], 0, 100)
        
        # Distanza ostacolo (simula)
        self.state[3] -= (self.state[0] * 0.1)
        if self.state[3] < 0:
            self.crashed = True
            self.state[3] = 0
        
        # RPM motore
        self.state[4] = self.state[0] * 150
        self.state[4] = np.clip(self.state[4], 0, 3000)
        
        # Temperatura motore
        self.state[5] += (abs(accel) * 0.1 + self.state[0] * 0.01)
        self.state[5] = np.clip(self.state[5], 25, 60)
        
        # Calcola reward
        reward = self._calculate_reward(accel, brake, steer)
        
        # Step counter
        self.steps += 1
        
        # Termina episodio
        terminated = self.crashed or self.steps >= self.max_steps
        truncated = False
        
        return self.state, reward, terminated, truncated, {}
    
    def _calculate_reward(self, accel, brake, steer):
        """Calcola il reward per il passo corrente"""
        reward = 0.0
        
        # Reward per avanzamento
        reward += self.state[0] * 0.1
        
        # Penalità per frenata brusca
        if brake > 0.5:
            reward -= 0.5
        
        # Penalità per inclinazione eccessiva
        reward -= abs(self.state[1]) * 0.2
        
        # Reward per mantenere batteria
        reward += (self.state[2] / 100) * 0.1
        
        # Penalità per temperatura alta
        if self.state[5] > 45:
            reward -= 0.5
        
        # Penalità per crash
        if self.crashed:
            reward -= 10.0
        
        return reward
    
    def render(self):
        """Render dell'ambiente (opzionale)"""
        if self.render_mode == 'human':
            print(f"⚡ Velocità: {self.state[0]:.1f} km/h")
            print(f"📐 Inclinazione: {self.state[1]:.1f}°")
            print(f"🔋 Batteria: {self.state[2]:.1f}%")
            print(f"📏 Distanza ostacolo: {self.state[3]:.1f} cm")
            print(f"🌀 RPM: {self.state[4]:.0f}")
            print(f"🌡️ Temp: {self.state[5]:.1f}°C")
            print("-" * 30)

# Registrazione dell'ambiente
gym.register(
    id='ScooterEnv-v0',
    entry_point='rl.environments.scooter_env:ScooterEnv',
    max_episode_steps=1000
)

if __name__ == "__main__":
    # Test dell'ambiente
    env = ScooterEnv(render_mode='human')
    obs, _ = env.reset()
    
    for i in range(100):
        action = env.action_space.sample()  # Azione casuale
        obs, reward, terminated, truncated, _ = env.step(action)
        env.render()
        
        if terminated or truncated:
            print("🔄 Episodio terminato!")
            obs, _ = env.reset()
