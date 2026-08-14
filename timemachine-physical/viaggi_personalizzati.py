#!/usr/bin/env python3
"""
🌀 URBAN LAB - Viaggi Personalizzati nel Tempo
Calcola il viaggio perfetto per te
"""

from simulator import ViaggioTemporale

print("🌀 URBAN LAB - VIAGGI PERSONALIZZATI")
print("=" * 50)
print()

# Input utente
anno_partenza = int(input("📅 Anno di partenza: "))
anno_arrivo = int(input("📅 Anno di arrivo: "))
velocita = float(input("⚡ Velocità (% della luce, 0-99.99): ")) / 100
massa = float(input("⚖️ Massa del veicolo (kg, default 1000): ") or "1000")

# Calcola
v = ViaggioTemporale(anno_partenza, anno_arrivo)
r = v.simula_viaggio(velocita, massa)

print()
print("=" * 50)
print("📊 RISULTATI DEL VIAGGIO")
print("=" * 50)
print(f"🌀 Da {anno_partenza} a {anno_arrivo}")
print(f"⚡ Velocità: {velocita*100}% della luce")
print(f"⏳ Dilatazione: {r['dilatazione']:.2f}x")
print(f"🕐 Tempo proprio: {r['tempo_proprio']:.1f} anni")
print(f"🌍 Tempo esterno: {r['tempo_esterno']:.1f} anni")
print(f"📅 Sulla Terra sarà il: {int(anno_partenza + r['tempo_esterno'])}")
print()
print("🔬 Energia necessaria:")
print(f"   {r['energia_necessaria']:.2e} J")
print(f"   Equivalente a {r['energia_necessaria']/3.6e15:.2f} megatoni di TNT")
print()

# Consigli
if r['tempo_proprio'] > 100:
    print("⚠️ Il viaggio dura più di una vita umana!")
elif r['tempo_proprio'] > 50:
    print("⚠️ Il viaggio dura gran parte della tua vita!")
else:
    print("✅ Viaggio fattibile in una vita umana!")

if r['tempo_esterno'] > 1000:
    print("🌍 Sulla Terra passeranno millenni!")
elif r['tempo_esterno'] > 100:
    print("🌍 Sulla Terra passeranno secoli!")
else:
    print("🌍 Sulla Terra passeranno pochi decenni!")
