#!/usr/bin/env python3
"""
🧠 AI Controller per Monopattino del Futuro
Integrazione con Pytho AI e ChatGPT
"""

import requests
import json
import time

class AIScooterController:
    def __init__(self):
        self.pytho_url = "http://localhost:3005/api/pytho/chat"
        self.chatgpt_url = "https://api.openai.com/v1/chat/completions"
        self.api_key = None  # Da configurare

    def ask_pytho(self, message):
        """Chiede aiuto a Pytho AI"""
        try:
            response = requests.post(
                self.pytho_url,
                json={"message": message},
                timeout=5
            )
            if response.status_code == 200:
                return response.json().get("data", {}).get("reply", "Nessuna risposta")
        except:
            return "⚠️ Pytho AI non disponibile"

    def ask_chatgpt(self, message):
        """Chiede aiuto a ChatGPT"""
        if not self.api_key:
            return "⚠️ API key non configurata"

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "gpt-4-turbo-preview",
                "messages": [
                    {"role": "system", "content": "Sei un esperto di monopattini elettrici"},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.7,
                "max_tokens": 300
            }
            response = requests.post(
                self.chatgpt_url,
                headers=headers,
                json=data,
                timeout=10
            )
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except:
            return "⚠️ ChatGPT non disponibile"

    def diagnostica(self, stato):
        """Esegue diagnostica in tempo reale"""
        messaggio = f"""
        Il monopattino ha questi valori:
        - Batteria: {stato.get('battery', 0)}%
        - Velocità: {stato.get('speed', 0)} km/h
        - Temperatura: {stato.get('temperature', 25)}°C
        - GPS: {stato.get('gps', {}).get('lat', 0)}, {stato.get('gps', {}).get('lon', 0)}
        
        Cosa consigli?
        """
        return self.ask_pytho(messaggio)

if __name__ == "__main__":
    print("🧠 AI Controller - Monopattino del Futuro")
    ai = AIScooterController()

    # Test
    stato_test = {"battery": 45, "speed": 18, "temperature": 32}
    print("\n🔍 Diagnostica:")
    print(ai.diagnostica(stato_test))
