#!/usr/bin/env python3
"""
🚀 Urban Lab - Training Semplificato (test)
Versione ridotta per verificare il funzionamento
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gymnasium as gym
from environments.scooter_env import ScooterEnv
import numpy as np
from datetime import datetime

def main():
    print("🏭 Urban Lab - Training Semplificato (TEST)")
    print("=" * 50)
    
    # Crea ambiente
    env = gym.make('ScooterEnv-v0')
    
    # Training semplice (random agent)
    episodes = 10
    rewards_history = []
    
    for episode in range(episodes):
        obs, _ = env.reset()
        total_reward = 0
        steps = 0
        
        while True:
            # Azione casuale (placeholder)
            action = env.action_space.sample()
            obs, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward
            steps += 1
            
            if terminated or truncated:
                break
        
        rewards_history.append(total_reward)
        print(f"📊 Episodio {episode+1}: Reward = {total_reward:.2f}, Steps = {steps}")
    
    print(f"\n📈 Reward media: {np.mean(rewards_history):.2f}")
    print(f"📊 Reward max: {np.max(rewards_history):.2f}")
    print(f"📉 Reward min: {np.min(rewards_history):.2f}")
    print("\n✅ Test completato! Il sistema funziona.")
    print("📌 Prossimo passo: addestrare con Telekinesis RL")

if __name__ == "__main__":
    main()
