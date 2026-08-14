#!/usr/bin/env python3
"""
🧠 URBAN LAB - Pytho AI + Macchina del Tempo
Assistente AI per i viaggi nel tempo
"""

import json
import time
import random
from datetime import datetime
from simulator import ViaggioTemporale

class PythoTimeMachine:
    """Assistente AI per la Macchina del Tempo"""
    
    def __init__(self):
        self.name = "Pytho"
        self.personality = "scienziato entusiasta"
        self.knowledge = {
            "relatività": "La relatività di Einstein è la base del viaggio nel tempo",
            "wormhole": "I wormhole potrebbero permettere viaggi nel passato",
            "energia": "Serve energia pari a quella di una stella",
            "paradossi": "Il paradosso del nonno è il problema principale"
        }
        self.conversation_history = []
        
    def greet(self):
        """Saluto iniziale"""
        greetings = [
            "🌀 Ciao! Sono Pytho, il tuo assistente per i viaggi nel tempo!",
            "⏳ Pronto per esplorare lo spazio-tempo? Sono Pytho!",
            "🌌 Benvenuto nella Macchina del Tempo! Sono il tuo AI Pytho."
        ]
        return random.choice(greetings)
    
    def analyze_travel(self, start_year, end_year, velocity):
        """Analizza un viaggio nel tempo"""
        v = ViaggioTemporale(start_year, end_year)
        results = v.simula_viaggio(velocity, 1000)
        
        analysis = {
            "viaggio": f"Da {start_year} a {end_year}",
            "velocita": f"{velocity*100}% della luce",
            "dilatazione": f"{results['dilatazione']:.2f}x",
            "tempo_proprio": f"{results['tempo_proprio']:.1f} anni",
            "tempo_esterno": f"{results['tempo_esterno']:.1f} anni",
            "energia": f"{results['energia_necessaria']:.2e} J"
        }
        
        # Consigli
        if results['tempo_proprio'] > 100:
            analysis["consiglio"] = "⚠️ Il viaggio dura più di una vita umana!"
        elif results['tempo_proprio'] > 50:
            analysis["consiglio"] = "⚠️ Il viaggio durerà gran parte della tua vita!"
        else:
            analysis["consiglio"] = "✅ Viaggio fattibile in una vita umana!"
        
        return analysis
    
    def predict_future(self, year):
        """Previsioni sul futuro"""
        predictions = {
            2050: ["🤖 IA avanzata", "🚀 Viaggi spaziali commerciali", "🧬 Vita estesa a 120 anni"],
            2100: ["🌍 Energia pulita", "🧠 Neurotecnologia", "🌌 Colonie spaziali"],
            3000: ["🌟 Civiltà interstellare", "🧬 Immortalità", "🌍 Terra paradiso"],
            5000: ["🚀 Viaggi intergalattici", "🧠 Coscienza collettiva", "🌌 Universo esplorato"]
        }
        
        # Trova la previsione più vicina
        closest_year = min(predictions.keys(), key=lambda x: abs(x - year))
        return predictions.get(closest_year, ["🔮 Il futuro è oltre la nostra immaginazione!"])
    
    def explain_concept(self, concept):
        """Spiega un concetto fisico"""
        explanations = {
            "dilatazione": "Il tempo rallenta per chi si muove velocemente. Più vai veloce, più il tempo scorre lentamente per te!",
            "wormhole": "Un wormhole è un tunnel nello spazio-tempo che collega due punti distanti. Potrebbe permettere viaggi nel passato!",
            "energia": "Per viaggiare nel tempo serve energia enorme. E=mc² significa che anche piccole masse contengono energia immensa!",
            "paradossi": "Il paradosso del nonno: se torni indietro e uccidi tuo nonno, non saresti mai nato per farlo!",
            "multiverso": "Ogni scelta crea un universo parallelo. Esistono infinite versioni di te stesso!"
        }
        return explanations.get(concept.lower(), "🔬 Concetto interessante! Studiando la fisica possiamo capirlo meglio.")
    
    def chat(self, user_input):
        """Gestisce la conversazione con l'utente"""
        self.conversation_history.append(f"Utente: {user_input}")
        
        # Analizza l'input
        user_input = user_input.lower()
        
        responses = []
        
        if "viaggio" in user_input or "tempo" in user_input:
            responses.append("🔮 Posso aiutarti a pianificare un viaggio nel tempo!")
            responses.append("📅 Dimmi: da che anno vuoi partire e dove vuoi andare?")
            
        elif "futuro" in user_input:
            responses.append("🔮 Il futuro è affascinante! Ecco alcune previsioni:")
            responses.append("   • IA superintelligente")
            responses.append("   • Viaggi interstellari")
            responses.append("   • Vita eterna")
            
        elif "energia" in user_input:
            responses.append("⚡ L'energia è il cuore del viaggio nel tempo!")
            responses.append("   • E = mc² è la chiave")
            responses.append("   • Servono quantità astronomiche")
            
        elif "paradossi" in user_input:
            responses.append("🌀 I paradossi sono il mistero più affascinante!")
            responses.append("   • Il paradosso del nonno")
            responses.append("   • Il paradosso di Bootstrap")
            responses.append("   • Esistono soluzioni teoriche!")
            
        elif "ciao" in user_input or "salve" in user_input:
            responses.append(self.greet())
            
        elif "grazie" in user_input:
            responses.append("🌀 Prego! Sono qui per aiutarti a esplorare lo spazio-tempo!")
            
        elif "aiuto" in user_input or "help" in user_input:
            responses.append("📋 Comandi disponibili:")
            responses.append("   • 'viaggio' - Pianifica un viaggio")
            responses.append("   • 'futuro' - Previsioni sul futuro")
            responses.append("   • 'energia' - Spiega l'energia")
            responses.append("   • 'paradossi' - Spiega i paradossi")
            responses.append("   • 'aiuto' - Mostra questo messaggio")
            
        else:
            responses.append("🧠 Interessante! Sto elaborando...")
            responses.append(f"💡 {self.explain_concept(user_input)}")
            responses.append("🌀 Vuoi sapere altro? Chiedimi di: viaggio, futuro, energia, paradossi")
        
        self.conversation_history.append(f"Pytho: {responses[0]}")
        return responses

    def run(self):
        """Avvia l'assistente Pytho"""
        print("🧠 URBAN LAB - PYTHO AI ASSISTANT")
        print("=" * 50)
        print(self.greet())
        print("📌 Sono qui per aiutarti con i viaggi nel tempo!")
        print("💡 Chiedimi qualsiasi cosa sulla relatività, energia o paradossi.")
        print("📋 Digita 'aiuto' per i comandi disponibili.")
        print("=" * 50)
        print("")

        while True:
            try:
                user_input = input("🌀 Tu: ")
                
                if user_input.lower() in ['exit', 'esci', 'quit', 'q']:
                    print("👋 Arrivederci! Ricorda: il futuro è nelle tue mani!")
                    break
                    
                responses = self.chat(user_input)
                for response in responses:
                    print(f"🧠 Pytho: {response}")
                    time.sleep(0.5)
                print("")
                
            except KeyboardInterrupt:
                print("\n👋 Arrivederci! 🌀")
                break

if __name__ == "__main__":
    pytho = PythoTimeMachine()
    pytho.run()
