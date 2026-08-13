#!/usr/bin/env python3
"""
🌀 URBAN LAB - Simulatore del Paradosso Temporale
Esplora i paradossi del viaggio nel tempo
"""

import time
import random

class TemporalParadox:
    def __init__(self):
        self.timeline = []
        self.paradoxes = [
            "Il Paradosso del Nonno",
            "Il Paradosso dell'Uomo Che Ha Ucciso Il Proprio Nonno",
            "Il Paradosso del Viaggiatore che Incontra Se Stesso",
            "Il Paradosso dell'Orologio",
            "Il Paradosso di Bootstrap",
            "Il Paradosso del Presente Alterato"
        ]
        
    def explain_paradox(self, paradox):
        """Spiega un paradosso temporale"""
        explanations = {
            "Il Paradosso del Nonno": """
            ⚠️ PARADOSSO DEL NONNO
            Se viaggi nel passato e uccidi tuo nonno prima che 
            tuo padre nasca, non esisterai mai per viaggiare nel tempo.
            """,
            "Il Paradosso dell'Uomo Che Ha Ucciso Il Proprio Nonno": """
            ⚠️ PARADOSSO DELL'UOMO CHE HA UCCISO IL PROPRIO NONNO
            Vai nel passato e uccidi tuo nonno. Se non esisti, 
            non puoi andare nel passato per ucciderlo.
            """,
            "Il Paradosso del Viaggiatore che Incontra Se Stesso": """
            ⚠️ PARADOSSO DEL VIAGGIATORE CHE INCONTRA SE STESSO
            Se incontri te stesso nel passato, quale delle due 
            versioni è quella originale?
            """,
            "Il Paradosso dell'Orologio": """
            ⚠️ PARADOSSO DELL'OROLOGIO
            Viaggi nel passato e dai un orologio a te stesso, 
            che usi per viaggiare nel tempo. Da dove viene l'orologio?
            """,
            "Il Paradosso di Bootstrap": """
            ⚠️ PARADOSSO DI BOOTSTRAP
            Un oggetto viene mandato nel passato, dove viene usato 
            per creare l'oggetto stesso. Da dove viene l'oggetto?
            """,
            "Il Paradosso del Presente Alterato": """
            ⚠️ PARADOSSO DEL PRESENTE ALTERATO
            Se cambi il passato, il presente cambia. Ma se il presente 
            cambia, le tue motivazioni per viaggiare cambiano.
            """
        }
        return explanations.get(paradox, "Paradosso sconosciuto")
    
    def simulate_paradox(self, paradox):
        """Simula un paradosso temporale"""
        print(f"\n🌀 SIMULAZIONE: {paradox}")
        print("=" * 50)
        
        explanation = self.explain_paradox(paradox)
        print(explanation)
        
        # Simula la linea temporale
        print("\n📊 Simulazione della linea temporale:")
        timeline = [
            "2024: Inizio della ricerca",
            "2040: Scoperta del viaggio nel tempo",
            "2050: Primo viaggio nel passato",
            f"2050: {paradox} si verifica!",
            "????: La linea temporale viene alterata"
        ]
        
        for event in timeline:
            time.sleep(0.5)
            print(f"   → {event}")
        
        print("\n🤯 Risultato della simulazione:")
        outcomes = [
            "La linea temporale si corregge da sola",
            "La linea temporale si divide (multiverso)",
            "Il paradosso crea un loop infinito",
            "Il viaggiatore scompare dalla realtà",
            "Il tempo si ripara automaticamente"
        ]
        outcome = random.choice(outcomes)
        print(f"   {outcome}")
        print("")
        
        # Possibili soluzioni
        print("🔬 Possibili soluzioni:")
        solutions = [
            "Principio di Autoconsistenza di Novikov",
            "Interpretazione dei Mondi Multipli",
            "La Linea Temporale si auto-corregge",
            "La Causa e l'Effetto sono in loop"
        ]
        for solution in solutions:
            print(f"   • {solution}")
    
    def run(self):
        """Esegue il simulatore di paradossi"""
        print("🌀 URBAN LAB - SIMULATORE DI PARADOSSI TEMPORALI")
        print("=" * 50)
        print("⚠️ ATTENZIONE: I paradossi sono teorici!")
        print("   La fisica attuale non ha ancora risolto questi problemi")
        print("")
        
        print("📋 Paradossi disponibili:")
        for i, paradox in enumerate(self.paradoxes, 1):
            print(f"   {i}. {paradox}")
        
        print("")
        choice = int(input("Scegli un paradosso da simulare (1-6): "))
        paradox = self.paradoxes[choice - 1]
        
        self.simulate_paradox(paradox)
        
        print("")
        print("📚 Curiosità:")
        print("   • Il Paradosso del Nonno è il più famoso")
        print("   • Esistono almeno 6 soluzioni teoriche")
        print("   • Il viaggio nel futuro è dimostrato, il passato no")

if __name__ == "__main__":
    paradox = TemporalParadox()
    paradox.run()
