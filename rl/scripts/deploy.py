#!/usr/bin/env python3
"""
🚀 Urban Lab - Deployment Script
Carica e testa la policy addestrata
"""

import numpy as np
import onnxruntime as ort
import argparse
import os

def load_policy(onnx_path):
    """Carica la policy ONNX"""
    if not os.path.exists(onnx_path):
        raise FileNotFoundError(f"Policy non trovata: {onnx_path}")
    
    session = ort.InferenceSession(onnx_path)
    return session

def get_action(session, observation):
    """Esegue la policy su un'osservazione"""
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    
    # Prepara input
    obs = np.array(observation, dtype=np.float32).reshape(1, -1)
    
    # Esegui inferenza
    action = session.run([output_name], {input_name: obs})[0]
    return action[0]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--policy', type=str, required=True, help='Path al file ONNX')
    parser.add_argument('--episodes', type=int, default=5, help='Numero episodi di test')
    args = parser.parse_args()
    
    print("🏭 Urban Lab - Deployment RL")
    print("=" * 50)
    print(f"📁 Policy: {args.policy}")
    print(f"🔄 Episodi: {args.episodes}")
    print("=" * 50)
    
    # Carica policy
    session = load_policy(args.policy)
    
    # Crea ambiente
    from environments.scooter_env import ScooterEnv
    env = ScooterEnv(render_mode='human')
    
    for episode in range(args.episodes):
        print(f"\n🔄 Episodio {episode + 1}")
        obs, _ = env.reset()
        total_reward = 0
        steps = 0
        
        while True:
            # Ottieni azione dalla policy
            action = get_action(session, obs)
            
            # Esegui azione
            obs, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward
            steps += 1
            env.render()
            
            if terminated or truncated:
                break
        
        print(f"📊 Reward totale: {total_reward:.2f}")
        print(f"📏 Step totali: {steps}")

if __name__ == "__main__":
    main()
