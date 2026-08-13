#!/usr/bin/env python3
"""
🌀 URBAN LAB - Server del Portale del Tempo Fisico
Avvia un server locale per visualizzare il portale
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Messaggi di log più puliti
        print(f"🌀 {format % args}")

def main():
    print("")
    print("🌀 URBAN LAB - Portale del Tempo Fisico")
    print("=" * 50)
    print(f"📁 Directory: {DIRECTORY}")
    print(f"🌐 Server avviato su: http://localhost:{PORT}")
    print("")
    print("📋 Comandi disponibili:")
    print("   http://localhost:8080/        → Portale principale")
    print("   http://localhost:8080/test.html → Pagina di test")
    print("")
    print("🔄 Apertura del browser...")
    print("")
    
    # Apri il browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Avvia il server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Server in esecuzione su http://localhost:{PORT}")
        print("📌 Premi CTRL+C per fermare il server")
        print("")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("")
            print("👋 Server fermato. Arrivederci!")
            httpd.shutdown()

if __name__ == "__main__":
    main()
