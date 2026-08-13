#!/usr/bin/env python3
"""
📊 Urban Lab - Dashboard Training RL
Visualizza il progresso del training in tempo reale
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import json
import os
import sys
from datetime import datetime

class RLDashboard:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.episodes = []
        self.rewards = []
        self.losses = []
        
        # Setup plot
        plt.style.use('dark_background')
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(12, 8))
        self.fig.suptitle('🏭 Urban Lab - RL Training Dashboard', fontsize=16)
        
        self.ax1.set_title('Episode Rewards')
        self.ax1.set_xlabel('Episode')
        self.ax1.set_ylabel('Total Reward')
        self.ax1.grid(True, alpha=0.3)
        
        self.ax2.set_title('Training Loss')
        self.ax2.set_xlabel('Step')
        self.ax2.set_ylabel('Loss')
        self.ax2.grid(True, alpha=0.3)
        
    def update(self, frame):
        """Aggiorna il grafico con nuovi dati"""
        # Leggi il log più recente
        log_file = os.path.join(self.log_dir, 'progress.json')
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r') as f:
                    data = json.load(f)
                    
                # Aggiorna dati
                if 'episodes' in data:
                    self.episodes = data['episodes']
                    self.rewards = data['rewards']
                if 'losses' in data:
                    self.losses = data['losses']
            except:
                pass
        
        # Aggiorna grafici
        if self.episodes:
            self.ax1.clear()
            self.ax1.plot(self.episodes, self.rewards, 'g-', alpha=0.7)
            self.ax1.set_title('Episode Rewards')
            self.ax1.set_xlabel('Episode')
            self.ax1.set_ylabel('Total Reward')
            self.ax1.grid(True, alpha=0.3)
            
        if self.losses:
            self.ax2.clear()
            self.ax2.plot(self.losses, 'r-', alpha=0.7)
            self.ax2.set_title('Training Loss')
            self.ax2.set_xlabel('Step')
            self.ax2.set_ylabel('Loss')
            self.ax2.grid(True, alpha=0.3)
        
        return self.ax1, self.ax2
    
    def run(self):
        """Avvia la dashboard"""
        anim = FuncAnimation(self.fig, self.update, interval=1000)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    import glob
    
    # Trova l'ultimo log
    log_dirs = glob.glob("logs/scooter_*")
    if not log_dirs:
        print("❌ Nessun log trovato! Esegui prima train.py")
        sys.exit(1)
    
    latest_log = max(log_dirs)
    print(f"📊 Dashboard per: {latest_log}")
    
    dashboard = RLDashboard(latest_log)
    dashboard.run()
