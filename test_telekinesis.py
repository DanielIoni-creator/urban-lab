#!/usr/bin/env python3
"""
🏭 Urban Lab - Test Telekinesis Wrapper
"""

import sys
sys.path.append('.')

from telekinesis.rlbotics import PPO, Policy, set_seed, create_log_dir
import numpy as np

print("🏭 Test Telekinesis Wrapper")
print("=" * 50)

# Test set_seed
set_seed(42)

# Test create_log_dir
log_dir = create_log_dir("logs/test")

# Test PPO
ppo = PPO(
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10
)

# Test learn
ppo.learn(total_timesteps=10000, log_dir="logs/test")

# Test save
ppo.save("logs/test/model.pth")

# Test export ONNX
ppo.export_onnx("logs/test/policy.onnx")

# Test Policy
policy = Policy("logs/test/policy.onnx")
obs = np.array([0, 0, 100, 150, 0, 25])
action = policy.get_action(obs)
print(f"📊 Azione: {action}")

print("")
print("✅ Tutti i test superati!")
print("🏭 Urban Lab - Telekinesis Wrapper funzionante!")
