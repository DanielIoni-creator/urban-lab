#!/usr/bin/env python3
"""
🌀 URBAN LAB - Grafici della Macchina del Tempo
Visualizzazione scientifica dei viaggi
"""

import matplotlib.pyplot as plt
import numpy as np
from simulator import ViaggioTemporale

class TimeTravelGraphs:
    def __init__(self):
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        self.fig.patch.set_facecolor('#0a0a0f')
        self.fig.suptitle('🌀 MACCHINA DEL TEMPO - ANALISI SCIENTIFICA', 
                         color='#00ffcc', fontsize=16, fontweight='bold')
        
    def plot_dilatation(self):
        """Grafico della dilatazione temporale"""
        velocities = np.linspace(0, 0.999, 100)
        dilatation = 1 / np.sqrt(1 - velocities**2)
        
        self.ax1.plot(velocities, dilatation, color='#00ffcc', linewidth=2)
        self.ax1.fill_between(velocities, 1, dilatation, alpha=0.3, color='#00ffcc')
        self.ax1.set_xlabel('Velocità (frazione di c)', color='#66ffcc')
        self.ax1.set_ylabel('Dilatazione temporale', color='#66ffcc')
        self.ax1.set_title('Dilatazione del Tempo', color='#00ffcc')
        self.ax1.grid(True, alpha=0.2)
        self.ax1.set_facecolor('#0a0a0f')
        self.ax1.tick_params(colors='#66ffcc')
        
    def plot_energy(self):
        """Grafico dell'energia necessaria"""
        masses = np.linspace(1, 100, 50)
        energies = masses * (3e8)**2
        
        self.ax2.plot(masses, energies, color='#7b2ffc', linewidth=2)
        self.ax2.fill_between(masses, 0, energies, alpha=0.3, color='#7b2ffc')
        self.ax2.set_xlabel('Massa (kg)', color='#66ffcc')
        self.ax2.set_ylabel('Energia (J)', color='#66ffcc')
        self.ax2.set_title('Energia Necessaria (E=mc²)', color='#00ffcc')
        self.ax2.grid(True, alpha=0.2)
        self.ax2.set_facecolor('#0a0a0f')
        self.ax2.tick_params(colors='#66ffcc')
        
    def plot_time_travel(self):
        """Grafico del viaggio nel tempo"""
        years = np.arange(2024, 3000, 10)
        proper_times = []
        external_times = []
        
        for year in years:
            v = ViaggioTemporale(2024, year)
            r = v.simula_viaggio(0.99, 1000)
            proper_times.append(r['tempo_proprio'])
            external_times.append(r['tempo_esterno'])
        
        self.ax3.plot(years, proper_times, color='#00ffcc', linewidth=2, label='Tempo proprio')
        self.ax3.plot(years, external_times, color='#ff6b35', linewidth=2, label='Tempo esterno')
        self.ax3.set_xlabel('Anno di arrivo', color='#66ffcc')
        self.ax3.set_ylabel('Tempo (anni)', color='#66ffcc')
        self.ax3.set_title('Tempo Proprio vs Tempo Esterno', color='#00ffcc')
        self.ax3.grid(True, alpha=0.2)
        self.ax3.legend(facecolor='#0a0a0f', labelcolor='#66ffcc')
        self.ax3.set_facecolor('#0a0a0f')
        self.ax3.tick_params(colors='#66ffcc')
        
    def plot_comparison(self):
        """Confronto velocità-tempo"""
        speeds = np.linspace(0.5, 0.999, 20)
        time_ratios = []
        
        for speed in speeds:
            v = ViaggioTemporale(2024, 3000)
            r = v.simula_viaggio(speed, 1000)
            time_ratios.append(r['tempo_esterno'] / r['tempo_proprio'])
        
        self.ax4.bar(speeds, time_ratios, color='#7b2ffc', alpha=0.7)
        self.ax4.set_xlabel('Velocità (frazione di c)', color='#66ffcc')
        self.ax4.set_ylabel('Rapporto tempi (esterno/proprio)', color='#66ffcc')
        self.ax4.set_title('Efficienza del Viaggio', color='#00ffcc')
        self.ax4.set_facecolor('#0a0a0f')
        self.ax4.tick_params(colors='#66ffcc')
        
    def show(self):
        """Mostra tutti i grafici"""
        self.plot_dilatation()
        self.plot_energy()
        self.plot_time_travel()
        self.plot_comparison()
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print("🌀 URBAN LAB - Generazione grafici scientifici...")
    graphs = TimeTravelGraphs()
    graphs.show()
