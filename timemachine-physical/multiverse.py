#!/usr/bin/env python3
"""
🌀 URBAN LAB - Simulatore di Multiverso
Esplora le linee temporali alternative
"""

import time
import random

class Multiverse:
    def __init__(self):
        self.timelines = []
        self.choices = [
            "Hai scelto di viaggiare nel tempo",
            "Hai scelto di restare nel presente",
            "Hai scelto di cambiare il passato",
            "Hai scelto di esplorare il futuro",
            "Hai scelto di non viaggiare affatto"
        ]
        
    def create_timeline(self, choice):
        """Crea una linea temporale alternativa"""
        timeline = {
            'choice': choice,
            'consequences': [],
            'year': 2024 + random.randint(0, 100)
        }
        
        # Genera conseguenze
        consequences = [
            "Il mondo è cambiato radicalmente",
            "La tecnologia si è evoluta diversamente",
            "L'umanità ha fatto scoperte incredibili",
            "La società è collassata",
            "Viviamo in pace e armonia",
            "L'intelligenza artificiale domina il mondo",
            "Abbiamo contattato civiltà aliene",
            "La Terra è diventata un paradiso"
        ]
        
        num_consequences = random.randint(1, 3)
        timeline['consequences'] = random.sample(consequences, num_consequences)
        
        return timeline
    
    def show_multiverse(self):
        """Mostra le linee temporali alternative"""
        print("\n🌀 MULTIVERSO - LINEE TEMPORALI")
        print("=" * 60)
        
        for i, choice in enumerate(self.choices, 1):
            print(f"\n🌌 Linea Temporale {i}: {choice}")
            timeline = self.create_timeline(choice)
            print(f"   📅 Anno: {timeline['year']}")
            print(f"   🔮 Conseguenze:")
            for consequence in timeline['consequences']:
                print(f"      • {consequence}")
    
    def show_quantum_state(self):
        """Mostra lo stato quantistico del multiverso"""
        print("\n⚛️ STATO QUANTISTICO DEL MULTIVERSO")
        print("=" * 60)
        
        states = [
            "🟢 STABILE - Le linee temporali sono coerenti",
            "🟡 FLUTTUANTE - Alcune linee temporali divergono",
            "🔴 INSTABILE - Il multiverso è in crisi",
            "🌀 CAOTICO - Tutte le possibilità esistono"
        ]
        
        state = random.choice(states)
        print(f"   {state}")
        
        # Probabilità
        print("\n📊 PROBABILITÀ DELLE LINEE TEMPORALI:")
        for i in range(5):
            prob = random.randint(10, 80)
            bar = "█" * int(prob/5) + "░" * (20 - int(prob/5))
            print(f"   Linea {i+1}: [{bar}] {prob}%")
    
    def run(self):
        """Esegue il simulatore di multiverso"""
        print("🌀 URBAN LAB - SIMULATORE DI MULTIVERSO")
        print("=" * 60)
        print("")
        print("🌌 Esplora le infinite possibilità del tempo!")
        print("")
        
        self.show_multiverse()
        self.show_quantum_state()
        
        print("\n" + "=" * 60)
        print("🌀 In ogni universo, esisti in una forma diversa.")
        print("   Scegli con saggezza il tuo viaggio nel tempo!")

if __name__ == "__main__":
    multiverse = Multiverse()
    multiverse.run()
