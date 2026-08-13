#!/usr/bin/env python3
"""
🌀 URBAN LAB - Macchina del Tempo GUI
Interfaccia grafica per il viaggio nel tempo
"""

import tkinter as tk
from tkinter import ttk, messagebox
from simulator import ViaggioTemporale

class TimeMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🌀 Urban Lab - Macchina del Tempo")
        self.root.geometry("600x700")
        self.root.configure(bg='#0a0a0f')
        
        # Stile
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#0a0a0f', foreground='#00ffcc', font=('Orbitron', 10))
        style.configure('TEntry', fieldbackground='#1a1a2a', foreground='#00ffcc')
        
        # Header
        header = tk.Label(root, text="🌀 MACCHINA DEL TEMPO", 
                         font=('Orbitron', 20, 'bold'),
                         fg='#00ffcc', bg='#0a0a0f')
        header.pack(pady=20)
        
        # Frame input
        frame = tk.Frame(root, bg='#0a0a0f')
        frame.pack(pady=20, padx=40, fill='x')
        
        # Anno partenza
        tk.Label(frame, text="📅 Anno di partenza:", 
                fg='#66ffcc', bg='#0a0a0f', font=('Orbitron', 10)).pack(anchor='w')
        self.anno_partenza = tk.Entry(frame, bg='#1a1a2a', fg='#00ffcc', 
                                     insertbackground='#00ffcc')
        self.anno_partenza.insert(0, "2024")
        self.anno_partenza.pack(fill='x', pady=5)
        
        # Anno arrivo
        tk.Label(frame, text="📅 Anno di arrivo:", 
                fg='#66ffcc', bg='#0a0a0f', font=('Orbitron', 10)).pack(anchor='w')
        self.anno_arrivo = tk.Entry(frame, bg='#1a1a2a', fg='#00ffcc',
                                   insertbackground='#00ffcc')
        self.anno_arrivo.insert(0, "3000")
        self.anno_arrivo.pack(fill='x', pady=5)
        
        # Velocità
        tk.Label(frame, text="⚡ Velocità (% della luce):", 
                fg='#66ffcc', bg='#0a0a0f', font=('Orbitron', 10)).pack(anchor='w')
        self.velocita = tk.Scale(frame, from_=0, to=99.99, resolution=0.01,
                                orient='horizontal', bg='#0a0a0f', fg='#00ffcc',
                                troughcolor='#1a1a2a', highlightthickness=0)
        self.velocita.set(99)
        self.velocita.pack(fill='x', pady=5)
        
        # Pulsante viaggio
        btn_viaggio = tk.Button(root, text="🌀 AVVIA VIAGGIO", 
                               command=self.avvia_viaggio,
                               bg='#00ffcc', fg='#0a0a0f',
                               font=('Orbitron', 12, 'bold'),
                               padx=20, pady=10,
                               relief='flat', cursor='hand2')
        btn_viaggio.pack(pady=20)
        
        # Risultati
        self.text_risultati = tk.Text(root, height=15, 
                                     bg='#0a0a0f', fg='#00ffcc',
                                     font=('Share Tech Mono', 10),
                                     relief='flat')
        self.text_risultati.pack(padx=40, pady=10, fill='both', expand=True)
        
        # Status bar
        self.status = tk.Label(root, text="⏳ In attesa di viaggio...",
                              fg='#66ffcc', bg='#0a0a0f', font=('Orbitron', 8))
        self.status.pack(pady=10)
    
    def avvia_viaggio(self):
        try:
            # Leggi input
            anno_partenza = int(self.anno_partenza.get())
            anno_arrivo = int(self.anno_arrivo.get())
            velocita = self.velocita.get() / 100
            
            # Calcola viaggio
            v = ViaggioTemporale(anno_partenza, anno_arrivo)
            r = v.simula_viaggio(velocita, 1000)
            
            # Mostra risultati
            self.text_risultati.delete(1.0, tk.END)
            self.text_risultati.insert(tk.END, "="*50 + "\n")
            self.text_risultati.insert(tk.END, "🌀 RISULTATI DEL VIAGGIO\n")
            self.text_risultati.insert(tk.END, "="*50 + "\n\n")
            self.text_risultati.insert(tk.END, f"📅 Da {anno_partenza} a {anno_arrivo}\n")
            self.text_risultati.insert(tk.END, f"⚡ Velocità: {velocita*100:.1f}% della luce\n")
            self.text_risultati.insert(tk.END, f"⏳ Dilatazione: {r['dilatazione']:.2f}x\n\n")
            self.text_risultati.insert(tk.END, f"🕐 Tempo proprio: {r['tempo_proprio']:.1f} anni\n")
            self.text_risultati.insert(tk.END, f"🌍 Tempo esterno: {r['tempo_esterno']:.1f} anni\n")
            self.text_risultati.insert(tk.END, f"📅 Sulla Terra: {int(anno_partenza + r['tempo_esterno'])}\n\n")
            self.text_risultati.insert(tk.END, f"⚡ Energia: {r['energia_necessaria']:.2e} J\n")
            
            # Messaggio
            if r['tempo_proprio'] > 80:
                self.text_risultati.insert(tk.END, "\n⚠️ Viaggio più lungo della vita umana!")
            elif r['tempo_proprio'] > 50:
                self.text_risultati.insert(tk.END, "\n⚠️ Viaggio durerà gran parte della tua vita!")
            else:
                self.text_risultati.insert(tk.END, "\n✅ Viaggio fattibile in una vita umana!")
            
            self.status.config(text="✅ Viaggio completato con successo!")
            
        except Exception as e:
            messagebox.showerror("Errore", f"Errore: {e}")
            self.status.config(text="❌ Errore nel calcolo del viaggio")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeMachineGUI(root)
    root.mainloop()
