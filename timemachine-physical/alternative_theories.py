#!/usr/bin/env python3
"""
🌀 URBAN LAB - Teorie Alternative sul Viaggio nel Tempo
Esplora diverse teorie fisiche
"""

import time

class TimeTheories:
    def __init__(self):
        self.theories = {
            "Relatività Generale": {
                "autore": "Albert Einstein",
                "anno": 1915,
                "descrizione": "Il tempo è una dimensione che può essere curvata",
                "viaggio_possibile": "Sì, nel futuro"
            },
            "Relatività Ristretta": {
                "autore": "Albert Einstein",
                "anno": 1905,
                "descrizione": "Il tempo rallenta con la velocità",
                "viaggio_possibile": "Sì, nel futuro"
            },
            "Meccanica Quantistica": {
                "autore": "Vari scienziati",
                "anno": 1920,
                "descrizione": "Il tempo potrebbe essere quantizzato",
                "viaggio_possibile": "Teorico"
            },
            "Teoria delle Stringhe": {
                "autore": "Vari scienziati",
                "anno": 1968,
                "descrizione": "Il tempo potrebbe essere una dimensione extra",
                "viaggio_possibile": "Teorico"
            },
            "Teoria di Kip Thorne": {
                "autore": "Kip Thorne",
                "anno": 1988,
                "descrizione": "Wormhole per viaggi nel tempo",
                "viaggio_possibile": "Teorico"
            },
            "Interpretazione di Copenhagen": {
                "autore": "Niels Bohr",
                "anno": 1927,
                "descrizione": "La realtà esiste solo quando osservata",
                "viaggio_possibile": "Filosofico"
            }
        }
    
    def show_theory(self, name):
        """Mostra una teoria"""
        theory = self.theories.get(name)
        if theory:
            print(f"\n📚 {name}")
            print("=" * 50)
            print(f"👨‍🔬 Autore: {theory['autore']}")
            print(f"📅 Anno: {theory['anno']}")
            print(f"📖 Descrizione: {theory['descrizione']}")
            print(f"🚀 Viaggio possibile: {theory['viaggio_possibile']}")
            print("")
            
            # Approfondimento
            if "Relatività Generale" in name:
                print("🔬 Approfondimento:")
                print("   • La gravità curva lo spazio-tempo")
                print("   • Wormhole potrebbero connettere tempi diversi")
                print("   • Necessario materiale esotico")
            elif "Relatività Ristretta" in name:
                print("🔬 Approfondimento:")
                print("   • Più veloce viaggi, più il tempo rallenta")
                print("   • Confermato da esperimenti con particelle")
                print("   • Il GPS usa correzioni relativistiche")
            elif "Teoria di Kip Thorne" in name:
                print("🔬 Approfondimento:")
                print("   • Wormhole stabili richiedono energia negativa")
                print("   • Effetto Casimir dimostra energia negativa")
                print("   • Ma non abbastanza per wormhole")
    
    def compare_theories(self):
        """Confronta le teorie"""
        print("\n📊 CONFRONTO TEORIE")
        print("=" * 50)
        print("")
        
        for name, theory in self.theories.items():
            status = "✅" if "Sì" in theory['viaggio_possibile'] else "🔬" if "Teorico" in theory['viaggio_possibile'] else "❌"
            print(f"{status} {name:30} → {theory['viaggio_possibile']:15}")
    
    def timeline_history(self):
        """Mostra la timeline storica"""
        print("\n⏳ TIMELINE STORICA")
        print("=" * 50)
        
        events = [
            (1905, "Einstein pubblica la Relatività Ristretta"),
            (1915, "Einstein pubblica la Relatività Generale"),
            (1927, "Nascita della Meccanica Quantistica"),
            (1968, "Prima teoria delle Stringhe"),
            (1988, "Kip Thorne propone wormhole per viaggi nel tempo"),
            (1990, "Prime simulazioni di viaggi nel tempo"),
            (2024, "Urban Lab inizia lo sviluppo della Macchina del Tempo")
        ]
        
        for year, event in events:
            time.sleep(0.3)
            print(f"   {year}: {event}")
    
    def run(self):
        """Esegue il simulatore di teorie"""
        print("🌀 URBAN LAB - TEORIE SUL VIAGGIO NEL TEMPO")
        print("=" * 50)
        print("")
        
        print("📋 Teorie disponibili:")
        for i, name in enumerate(self.theories.keys(), 1):
            print(f"   {i}. {name}")
        print(f"   {len(self.theories)+1}. Confronta tutte")
        print(f"   {len(self.theories)+2}. Timeline storica")
        print("")
        
        choice = int(input("Scegli una teoria (1-8): "))
        names = list(self.theories.keys())
        
        if choice <= len(names):
            self.show_theory(names[choice-1])
        elif choice == len(names) + 1:
            self.compare_theories()
        elif choice == len(names) + 2:
            self.timeline_history()
        else:
            print("Scelta non valida!")

if __name__ == "__main__":
    theories = TimeTheories()
    theories.run()
