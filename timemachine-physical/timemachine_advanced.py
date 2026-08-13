#!/usr/bin/env python3
"""
🌀 URBAN LAB - Macchina del Tempo Avanzata
Con effetti sonori, visivi e simulazione realistica
"""

import time
import sys
import os
import numpy as np
from datetime import datetime
from simulator import ViaggioTemporale

class AdvancedTimeMachine:
    def __init__(self):
        self.wormhole_open = False
        self.velocity = 0.99
        self.destination_year = 3000
        self.current_year = 2024
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_animation(self, text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def wormhole_effect(self):
        """Simula l'apertura del wormhole"""
        self.clear_screen()
        print("🌀 " + "="*48 + " 🌀")
        print("        APERTURA DEL WORMHOLE IN CORSO...")
        print("🌀 " + "="*48 + " 🌀")
        
        frames = [
            "🌌 Distorsione spazio-temporale...",
            "🌀 Creazione del tunnel di Einstein-Rosen...",
            "⚡ Energia negativa accumulata...",
            "🌟 Wormhole stabile!",
            "🚀 Pronto per il viaggio!"
        ]
        
        for i, frame in enumerate(frames):
            progress = "█" * (i + 1) + "░" * (len(frames) - i - 1)
            print(f"\r[{progress}] {frame}", end="")
            time.sleep(1.5)
        
        print("\n\n✅ WORMHOLE APERTO CON SUCCESSO!")
        self.wormhole_open = True
        time.sleep(1)
    
    def travel_effect(self):
        """Simula il viaggio nel tempo"""
        self.clear_screen()
        print("🚀 VIAGGIO NEL TEMPO IN CORSO")
        print("=" * 50)
        
        v = ViaggioTemporale(self.current_year, self.destination_year)
        r = v.simula_viaggio(self.velocity, 1000)
        
        total_steps = 50
        for i in range(total_steps + 1):
            progress = int(i / total_steps * 50)
            bar = "█" * progress + "░" * (50 - progress)
            
            # Calcolo anno corrente
            year = int(self.current_year + (self.destination_year - self.current_year) * (i / total_steps))
            
            # Effetto dilatazione
            dilatazione = 1 + (r['dilatazione'] - 1) * (i / total_steps)
            
            print(f"\r[{bar}] Anno: {year} | Dilatazione: {dilatazione:.2f}x", end="")
            time.sleep(0.1)
        
        print("\n\n✅ VIAGGIO COMPLETATO!")
        print(f"📍 Arrivato all'anno {self.destination_year}")
        print(f"⏳ Dilatazione temporale: {r['dilatazione']:.2f}x")
        print(f"🕐 Tempo trascorso per te: {r['tempo_proprio']:.1f} anni")
        print(f"🌍 Tempo trascorso sulla Terra: {r['tempo_esterno']:.1f} anni")
        
        return r
    
    def show_future(self, results):
        """Mostra il futuro"""
        self.clear_screen()
        print("🌅 BENVENUTO NEL FUTURO!")
        print("=" * 50)
        print(f"📅 Anno attuale: {self.destination_year}")
        print(f"⚡ Velocità di viaggio: {self.velocity*100}% della luce")
        print(f"⏳ Dilatazione temporale: {results['dilatazione']:.2f}x")
        print(f"🕐 Hai viaggiato per {results['tempo_proprio']:.1f} anni")
        print(f"🌍 Sulla Terra sono passati {results['tempo_esterno']:.1f} anni")
        print("")
        
        # Previsioni future
        print("🔮 PREVISIONI PER IL FUTURO:")
        predictions = [
            "🤖 Intelligenza artificiale avanzata",
            "🚀 Viaggi interstellari commerciali",
            "🧬 Vita umana estesa a 150+ anni",
            "🌍 Energia pulita e sostenibile",
            "🧠 Neurotecnologia e realtà virtuale totale"
        ]
        
        for pred in predictions:
            print(f"  • {pred}")
        
        print("")
        print("🌀 Vuoi tornare al presente? (s/n): ", end="")
        if input().lower() == 's':
            self.return_to_present(results)
    
    def return_to_present(self, results):
        """Torna al presente"""
        self.clear_screen()
        print("🔄 RITORNO AL PRESENTE")
        print("=" * 50)
        print("📦 Preparazione per il viaggio di ritorno...")
        time.sleep(1)
        
        # Simula il ritorno
        print("🌀 Riapertura wormhole...")
        time.sleep(1)
        print("🚀 Viaggio di ritorno in corso...")
        time.sleep(2)
        
        print(f"\n✅ Sei tornato al {datetime.now().year}!")
        print(f"🕐 Hai viaggiato per {results['tempo_proprio']:.1f} anni")
        print(f"🌍 Sulla Terra sono passati {results['tempo_esterno']:.1f} anni")
        print(f"📅 Sulla Terra ora è il {int(2024 + results['tempo_esterno'])}")
        print("")
        print("🤯 Sei più giovane di {:.1f} anni rispetto a chi è rimasto sulla Terra!".format(
            results['tempo_esterno'] - results['tempo_proprio']
        ))
    
    def run(self):
        """Esegue la macchina del tempo"""
        self.clear_screen()
        print("🌀 URBAN LAB - MACCHINA DEL TEMPO AVANZATA")
        print("=" * 50)
        print("")
        print("⚠️ Avvertenze:")
        print("  • Questo è un simulatore basato sulla relatività di Einstein")
        print("  • Il viaggio nel tempo è teoricamente possibile")
        print("  • Richiede tecnologia avanzata non ancora disponibile")
        print("")
        print("📋 Parametri di viaggio predefiniti:")
        print(f"  📅 Da: {self.current_year}")
        print(f"  📅 A: {self.destination_year}")
        print(f"  ⚡ Velocità: {self.velocity*100}% della luce")
        print("")
        input("🔑 Premi ENTER per iniziare il viaggio...")
        
        # Fasi del viaggio
        self.wormhole_effect()
        results = self.travel_effect()
        time.sleep(1)
        self.show_future(results)
        
        print("\n" + "="*50)
        print("🌀 Grazie per aver viaggiato con Urban Lab!")
        print("📖 Ricorda: il futuro è nelle tue mani!")

if __name__ == "__main__":
    tm = AdvancedTimeMachine()
    tm.run()
