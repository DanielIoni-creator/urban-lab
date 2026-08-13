#!/usr/bin/env python3
"""
🌀 URBAN LAB - Macchina del Tempo 3D
Visualizzazione interattiva del viaggio nel tempo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from simulator import ViaggioTemporale

class TimeMachine3D:
    def __init__(self):
        self.fig = plt.figure(figsize=(14, 10))
        self.fig.patch.set_facecolor('black')
        self.fig.suptitle('🌀 MACCHINA DEL TEMPO - VIAGGIO 3D', 
                         color='#00ffcc', fontsize=20, fontweight='bold')
        
        # Setup 3D
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor('black')
        self.ax.grid(False)
        self.ax.set_xlabel('X (anni luce)', color='#66ffcc')
        self.ax.set_ylabel('Y (anni luce)', color='#66ffcc')
        self.ax.set_zlabel('Tempo', color='#66ffcc')
        
        # Parametri di viaggio
        self.anno_partenza = 2024
        self.anno_arrivo = 3000
        self.velocita = 0.99
        self.trajectory = []
        self.points = 100
        
        # Calcola traiettoria
        self.calculate_trajectory()
        
        # Setup animazione
        self.anim = FuncAnimation(self.fig, self.update, 
                                 frames=range(self.points), 
                                 interval=50, blit=False)
        
        plt.show()
    
    def calculate_trajectory(self):
        """Calcola la traiettoria 3D del viaggio"""
        v = ViaggioTemporale(self.anno_partenza, self.anno_arrivo)
        r = v.simula_viaggio(self.velocita, 1000)
        
        # Genera punti della traiettoria
        t = np.linspace(0, 1, self.points)
        
        # X: posizione spaziale (spirale)
        x = 10 * t * np.cos(2 * np.pi * t * 3)
        y = 10 * t * np.sin(2 * np.pi * t * 3)
        
        # Z: tempo (dilatazione)
        z = self.anno_partenza + t * (self.anno_arrivo - self.anno_partenza)
        z = z / 100  # Scala per visualizzazione
        
        # Dilatazione temporale (effetto wormhole)
        dilatazione = 1 + (r['dilatazione'] - 1) * t
        self.trajectory = np.column_stack((x, y, z, dilatazione))
    
    def update(self, frame):
        """Aggiorna la visualizzazione"""
        self.ax.clear()
        self.ax.set_facecolor('black')
        
        # Traiettoria completa
        self.ax.plot(self.trajectory[:frame, 0], 
                    self.trajectory[:frame, 1], 
                    self.trajectory[:frame, 2], 
                    color='#00ffcc', linewidth=2, alpha=0.7)
        
        # Posizione attuale
        if frame > 0:
            pos = self.trajectory[frame-1]
            self.ax.scatter(pos[0], pos[1], pos[2], 
                          color='#00ffcc', s=100, alpha=1)
            
            # Effetto wormhole
            self.ax.scatter(pos[0], pos[1], pos[2], 
                          color='#7b2ffc', s=200, alpha=0.3)
        
        # Disegna il tunnel temporale
        theta = np.linspace(0, 2*np.pi, 20)
        for i in range(0, frame, 5):
            if i < len(self.trajectory):
                pos = self.trajectory[i]
                r = 0.5 + 0.5 * (i / self.points)
                x_circle = pos[0] + r * np.cos(theta)
                y_circle = pos[1] + r * np.sin(theta)
                z_circle = np.full_like(theta, pos[2])
                self.ax.plot(x_circle, y_circle, z_circle, 
                           color='#7b2ffc', alpha=0.1)
        
        # Labels
        self.ax.set_xlabel('X (anni luce)', color='#66ffcc', fontsize=10)
        self.ax.set_ylabel('Y (anni luce)', color='#66ffcc', fontsize=10)
        self.ax.set_zlabel('Tempo', color='#66ffcc', fontsize=10)
        
        # Info
        if frame > 0:
            pos = self.trajectory[frame-1]
            info_text = f'🌀 Anno: {self.anno_partenza + frame * (self.anno_arrivo - self.anno_partenza) / self.points:.0f}'
            info_text += f'\n⚡ Velocità: {self.velocita*100:.1f}% c'
            info_text += f'\n⏳ Dilatazione: {pos[3]:.2f}x'
            self.ax.text2D(0.02, 0.98, info_text, 
                          transform=self.ax.transAxes,
                          color='#00ffcc', fontsize=12,
                          bbox=dict(boxstyle='round', facecolor='black', alpha=0.8))
        
        # Limiti
        self.ax.set_xlim([-12, 12])
        self.ax.set_ylim([-12, 12])
        self.ax.set_zlim([0, 35])
        
        # Angolo di visuale
        self.ax.view_init(elev=25, azim=45 + frame * 0.5)

if __name__ == "__main__":
    print("🌀 URBAN LAB - Macchina del Tempo 3D")
    print("=" * 50)
    print("🔄 Visualizzazione del viaggio nel tempo...")
    print("📌 Chiudi la finestra per fermare l'animazione")
    print("")
    print("⚡ Velocità: 99% della luce")
    print("📅 Da 2024 a 3000")
    print("=" * 50)
    
    tm = TimeMachine3D()
