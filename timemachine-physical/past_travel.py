#!/usr/bin/env python3
"""
🌀 URBAN LAB - Viaggio nel Passato (Teorico)
Simulazione di viaggio nel passato con wormhole
"""

import time
import random

class PastTravel:
    def __init__(self):
        self.historical_events = {
            "Antica Roma": -753,
            "Nascita di Cristo": -4,
            "Caduta dell'Impero Romano": 476,
            "Scoperta dell'America": 1492,
            "Rivoluzione Francese": 1789,
            "Prima Guerra Mondiale": 1914,
            "Seconda Guerra Mondiale": 1939,
            "Sbarco sulla Luna": 1969
        }
        
    def show_events(self):
        print("📜 EVENTI STORICI DISPONIBILI")
        print("=" * 50)
        for i, (event, year) in enumerate(self.historical_events.items(), 1):
            print(f"{i:2}. {event:25} → {year}")
        print("")
    
    def travel_to_past(self, event, year):
        """Simula il viaggio nel passato"""
        print(f"\n🌀 VIAGGIO VERSO: {event} ({year})")
        print("=" * 50)
        
        print("⚠️ ATTENZIONE: Il viaggio nel passato è TEORICO!")
        print("   Richiede wormhole e energia negativa.")
        print("   La fisica attuale non lo ha ancora dimostrato.")
        print("")
        
        print("🔄 Apertura wormhole...")
        time.sleep(1)
        print("🌌 Distorsione spazio-temporale...")
        time.sleep(1)
        print("⚡ Energia negativa accumulata...")
        time.sleep(1)
        print("🌟 Wormhole stabile!")
        time.sleep(0.5)
        
        print(f"\n📍 Sei arrivato al {year}!")
        print(f"📅 Evento: {event}")
        print("")
        
        # Simula l'evento storico
        print("🔍 Cosa vedi:")
        descriptions = {
            "Antica Roma": "Vedi il Colosseo, i legionari romani e il Foro Romano.",
            "Nascita di Cristo": "Vedi Betlemme, la stella cometa e la grotta della natività.",
            "Caduta dell'Impero Romano": "Vedi i barbari che entrano a Roma.",
            "Scoperta dell'America": "Vedi Colombo che sbarca nel Nuovo Mondo.",
            "Rivoluzione Francese": "Vedi la presa della Bastiglia.",
            "Prima Guerra Mondiale": "Vedi le trincee e i soldati.",
            "Seconda Guerra Mondiale": "Vedi lo sbarco in Normandia.",
            "Sbarco sulla Luna": "Vedi Neil Armstrong che cammina sulla Luna."
        }
        print(f"   {descriptions.get(event, 'Evento storico in corso...')}")
        
        print("")
        print("⚠️ ATTENZIONE AL PARADOSSO!")
        print("   Se modifichi il passato, il presente potrebbe cambiare.")
        print("   Il Paradosso del Nonno è un rischio reale!")
    
    def run(self):
        """Esegue il viaggio nel passato"""
        print("🌀 URBAN LAB - VIAGGIO NEL PASSATO (TEORICO)")
        print("=" * 50)
        print("")
        
        self.show_events()
        
        choice = int(input("Scegli un evento storico (numero): "))
        events = list(self.historical_events.items())
        event, year = events[choice - 1]
        
        self.travel_to_past(event, year)

if __name__ == "__main__":
    travel = PastTravel()
    travel.run()
