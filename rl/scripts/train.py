#!/usr/bin/env python3
"""
🚀 Urban Lab - Training Script per Scooter RL
Utilizza Telekinesis RLbotics
"""

import os
import sys
import yaml
import argparse
from datetime import datetime

# Aggiungi il path del progetto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gymnasium as gym
from telekinesis.rlbotics import PPO
from telekinesis.rlbotics.utils import set_seed, create_log_dir

# Importa l'ambiente personalizzato
from environments.scooter_env import ScooterEnv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='configs/scooter.yaml')
    parser.add_argument('--num-envs', type=int, default=8)
    parser.add_argument('--device', type=str, default='auto')
    parser.add_argument('--total-timesteps', type=int, default=1000000)
    args = parser.parse_args()
    
    # Carica configurazione
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Aggiorna con argomenti CLI
    config['env']['num_envs'] = args.num_envs
    config['training']['total_timesteps'] = args.total_timesteps
    config['device'] = args.device
    
    # Crea log directory
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_dir = f"logs/scooter_{timestamp}"
    create_log_dir(log_dir)
    
    print("🏭 Urban Lab - Training RL")
    print("=" * 50)
    print(f"📁 Log directory: {log_dir}")
    print(f"🔄 Numero ambienti: {config['env']['num_envs']}")
    print(f"📊 Total timesteps: {config['training']['total_timesteps']}")
    print(f"💻 Device: {config['device']}")
    print("=" * 50)
    
    # Setup seed
    set_seed(config.get('seed', 42))
    
    # Crea ambiente
    env = gym.make('ScooterEnv-v0')
    
    # Crea l'agente
    agent = PPO(
        env=env,
        learning_rate=config['algorithm']['learning_rate'],
        n_steps=config['algorithm']['n_steps'],
        batch_size=config['algorithm']['batch_size'],
        n_epochs=config['algorithm']['n_epochs'],
        gamma=config['algorithm']['gamma'],
        gae_lambda=config['algorithm']['gae_lambda'],
        clip_range=config['algorithm']['clip_range'],
        ent_coef=config['algorithm']['ent_coef'],
        vf_coef=config['algorithm']['vf_coef'],
        max_grad_norm=config['algorithm']['max_grad_norm'],
        device=config['device']
    )
    
    # Addestra
    print("🚀 Inizio training...")
    agent.learn(
        total_timesteps=config['training']['total_timesteps'],
        log_interval=config['training']['log_interval'],
        save_interval=config['training']['save_interval'],
        log_dir=log_dir
    )
    
    # Salva il modello finale
    model_path = f"{log_dir}/final_model"
    agent.save(model_path)
    print(f"✅ Modello salvato: {model_path}")
    
    # Esporta ONNX
    onnx_path = f"{log_dir}/policy.onnx"
    agent.export_onnx(onnx_path)
    print(f"✅ ONNX esportato: {onnx_path}")
    
    print("🎉 Training completato!")

if __name__ == "__main__":
    main()
