#!/usr/bin/env python3
"""
🌀 URBAN LAB - Simulatore di Viaggio nel Tempo
Calcola i parametri per un viaggio temporale
"""

import math
import numpy as np
from dataclasses import dataclass

@dataclass
class ViaggioTemporale:
    """Parametri per un viaggio nel tempo"""
    anno_partenza: int
    anno_arrivo: int
    velocita_luce: float = 299792458  # m/s
    costante_gravitazionale: float = 6.674e-11
    
    def calcola_dilatazione(self, velocita: float) -> float:
        """Calcola la dilatazione temporale"""
        if velocita >= self.velocita_luce:
            return float('inf')
        gamma = 1 / math.sqrt(1 - (velocita**2 / self.velocita_luce**2))
        return gamma
    
    def calcola_energia(self, massa: float) -> float:
        """Calcola l'energia necessaria (E=mc²)"""
        return massa * self.velocita_luce**2
    
    def calcola_curvatura(self, massa: float, raggio: float) -> float:
        """Calcola la curvatura spazio-temporale"""
        return (2 * self.costante_gravitazionale * massa) / (raggio * self.velocita_luce**2)
    
    def simula_viaggio(self, velocita_frazione: float, massa: float) -> dict:
        """Simula un viaggio nel tempo"""
        velocita = velocita_frazione * self.velocita_luce
        dilatazione = self.calcola_dilatazione(velocita)
        energia = self.calcola_energia(massa)
        
        differenza_anni = abs(self.anno_arrivo - self.anno_partenza)
        tempo_proprio = differenza_anni * 365.25 * 24 * 3600
        tempo_esterno = tempo_proprio * dilatazione
        
        return {
            'velocita': velocita,
            'frazione_c': velocita_frazione,
            'dilatazione': dilatazione,
            'energia_necessaria': energia,
            'tempo_proprio': tempo_proprio / (365.25 * 24 * 3600),
            'tempo_esterno': tempo_esterno / (365.25 * 24 * 3600),
            'curvatura': self.calcola_curvatura(massa, 1000),
        }

def main():
    print("🌀 URBAN LAB - Simulatore di Viaggio nel Tempo")
    print("=" * 50)
    
    viaggio = ViaggioTemporale(anno_partenza=2024, anno_arrivo=2050)
    velocita_frazione = 0.99
    massa_veicolo = 1000
    
    print(f"📊 Viaggio da {viaggio.anno_partenza} a {viaggio.anno_arrivo}")
    print(f"⚡ Velocità: {velocita_frazione*100}% della luce")
    print("")
    
    risultati = viaggio.simula_viaggio(velocita_frazione, massa_veicolo)
    
    for key, value in risultati.items():
        if isinstance(value, float):
            print(f"   {key}: {value:.2e}")
        else:
            print(f"   {key}: {value}")

if __name__ == "__main__":
    main()
