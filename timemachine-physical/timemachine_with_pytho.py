#!/usr/bin/env python3
"""
🌀 URBAN LAB - Macchina del Tempo con Pytho AI
Integrazione completa tra la Macchina del Tempo e l'AI
"""

import sys
import time
from pytho_timemachine import PythoTimeMachine
from simulator import ViaggioTemporale

class TimeMachineWithPytho:
    def __init__(self):
        self.pytho = PythoTimeMachine()
        self.travel_history = []
        
    def display_menu(self):
        print("\n" + "=" * 50)
        print("🌀 URBAN LAB - MACCHINA DEL TEMPO + PYTHO AI")
        print("=" * 50)
        print("")
        print("1. 🚀 Avvia la Macchina del Tempo")
        print("2. 🧠 Parla con Pytho AI")
        print("3. 📊 Analizza un viaggio")
        print("4. 🌌 Viaggio Interstellare")
        print("5. 📝 Cronologia viaggi")
        print("6. ℹ️ Info e teoria")
        print("0. ❌ Esci")
        print("")
    
    def start_time_machine(self):
        """Avvia la Macchina del Tempo"""
        print("\n🌀 Avvio Macchina del Tempo...")
        print("📅 Inserisci i parametri del viaggio:")
        
        try:
            start = int(input("   Anno di partenza (es. 2024): "))
            end = int(input("   Anno di arrivo (es. 3000): "))
            velocity = float(input("   Velocità (% della luce, es. 99): ")) / 100
            
            # Analisi con Pytho
            print("\n🧠 Pytho sta analizzando il viaggio...")
            time.sleep(1)
            
            analysis = self.pytho.analyze_travel(start, end, velocity)
            
            print("\n📊 RISULTATI:")
            print("=" * 40)
            for key, value in analysis.items():
                if key != 'consiglio':
                    print(f"   {key}: {value}")
            print("\n💡 Consiglio di Pytho:")
            print(f"   {analysis.get('consiglio', 'Viaggio interessante!')}")
            
            # Previsioni sul futuro
            print("\n🔮 Previsioni di Pytho per il futuro:")
            predictions = self.pytho.predict_future(end)
            for pred in predictions:
                print(f"   • {pred}")
            
            # Salva nella cronologia
            self.travel_history.append({
                'start': start,
                'end': end,
                'velocity': velocity,
                'analysis': analysis
            })
            
        except Exception as e:
            print(f"❌ Errore: {e}")
    
    def chat_with_pytho(self):
        """Chat interattiva con Pytho"""
        print("\n🧠 Avvio chat con Pytho AI...")
        print("📌 Digita 'exit' per tornare al menu")
        print("")
        
        while True:
            try:
                user_input = input("🌀 Tu: ")
                if user_input.lower() in ['exit', 'esci', 'back']:
                    break
                responses = self.pytho.chat(user_input)
                for response in responses:
                    print(f"🧠 Pytho: {response}")
                    time.sleep(0.5)
                print("")
            except KeyboardInterrupt:
                break
    
    def analyze_travel(self):
        """Analizza un viaggio specifico"""
        print("\n📊 Analisi viaggio personalizzata")
        print("")
        
        start = int(input("📅 Anno di partenza: "))
        end = int(input("📅 Anno di arrivo: "))
        velocity = float(input("⚡ Velocità (% della luce): ")) / 100
        
        v = ViaggioTemporale(start, end)
        r = v.simula_viaggio(velocity, 1000)
        
        print("\n📊 ANALISI COMPLETA:")
        print("=" * 40)
        print(f"   🌀 Viaggio: {start} → {end}")
        print(f"   ⚡ Velocità: {velocity*100}% luce")
        print(f"   ⏳ Dilatazione: {r['dilatazione']:.2f}x")
        print(f"   🕐 Tempo proprio: {r['tempo_proprio']:.1f} anni")
        print(f"   🌍 Tempo esterno: {r['tempo_esterno']:.1f} anni")
        print(f"   ⚡ Energia: {r['energia_necessaria']:.2e} J")
        print(f"   📅 Sulla Terra: {int(start + r['tempo_esterno'])}")
    
    def interstellar_travel(self):
        """Avvia il viaggio interstellare"""
        print("\n🌌 Avvio Viaggio Interstellare...")
        try:
            exec(open('interstellar_travel.py').read())
        except:
            print("❌ Errore nell'avvio del viaggio interstellare")
    
    def show_history(self):
        """Mostra la cronologia dei viaggi"""
        if not self.travel_history:
            print("\n📝 Nessun viaggio registrato ancora!")
            return
        
        print("\n📝 CRONOLOGIA VIAGGI:")
        print("=" * 40)
        for i, travel in enumerate(self.travel_history, 1):
            print(f"\n🚀 Viaggio {i}:")
            print(f"   📅 {travel['start']} → {travel['end']}")
            print(f"   ⚡ {travel['velocity']*100}% luce")
            analysis = travel['analysis']
            print(f"   ⏳ Dilatazione: {analysis.get('dilatazione', 'N/A')}")
            print(f"   🕐 Tempo proprio: {analysis.get('tempo_proprio', 'N/A')}")
    
    def show_info(self):
        """Mostra informazioni sulla teoria"""
        print("\n📚 TEORIA DEL VIAGGIO NEL TEMPO")
        print("=" * 50)
        print("""
🌀 PRINCIPI FONDAMENTALI:

1. RELATIVITÀ RISTRETTA (Einstein, 1905)
   - Il tempo rallenta con la velocità
   - Δt = t₀ / √(1 - v²/c²)

2. RELATIVITÀ GENERALE (Einstein, 1915)
   - La gravità curva lo spazio-tempo
   - I wormhole potrebbero permettere viaggi nel passato

3. MECCANICA QUANTISTICA
   - Il tempo potrebbe essere quantizzato
   - L'entanglement potrebbe collegare passato e futuro

4. TEORIA DELLE STRINGHE
   - Dimensioni extra dello spazio-tempo
   - Possibili viaggi attraverso dimensioni nascoste

💡 CURIOSITÀ:
- Il GPS usa correzioni relativistiche ogni giorno!
- I muoni viaggiano nel futuro a causa della dilatazione
- Il CERN accelera particelle al 99.9999% di c
""")
    
    def run(self):
        """Esegue il programma principale"""
        print("🌀 URBAN LAB - MACCHINA DEL TEMPO CON PYTHO AI")
        print("=" * 50)
        print(self.pytho.greet())
        print("")
        
        while True:
            self.display_menu()
            choice = input("📋 Scegli un'opzione: ")
            
            if choice == '0':
                print("\n👋 Arrivederci! Viaggia sicuro nel tempo! 🌀")
                break
            elif choice == '1':
                self.start_time_machine()
            elif choice == '2':
                self.chat_with_pytho()
            elif choice == '3':
                self.analyze_travel()
            elif choice == '4':
                self.interstellar_travel()
            elif choice == '5':
                self.show_history()
            elif choice == '6':
                self.show_info()
            else:
                print("❌ Opzione non valida!")
            
            print("\n" + "=" * 50)
            input("Premi ENTER per continuare...")

if __name__ == "__main__":
    tm = TimeMachineWithPytho()
    tm.run()
