#!/usr/bin/env python3
"""
🧠 PYTHO AI - Escrow Multisig Manager
Gestione transazioni sicure in Monero per Urban Lab
"""

import json
import time
import hashlib
import requests
from datetime import datetime
from typing import Dict, List, Optional

class PythoEscrow:
    """Gestore Escrow Multisig per Pytho AI"""
    
    def __init__(self, api_url="http://localhost:5002"):
        self.api_url = api_url
        self.escrow_wallet = None
        self.multisig_threshold = 2
        self.multisig_signers = 3
        self.fee_percent = 0.5
        
        # Chiavi di Pytho per le firme
        self.pytho_private_key = "PYTHO_ESCROW_KEY_2026"
        self.pytho_address = "45M4DW1ug8bdQowWpxucTpgsfjLbVxbYaAra79VewmBobuuhgqTjyD4R3DzpqLM2veiphcB16n24qN1QbLg3y2PYGK3Qkoe"
        
        print("🧠 Pytho Escrow Manager inizializzato")
        print(f"   Threshold: {self.multisig_threshold}/{self.multisig_signers}")
        print(f"   Fee: {self.fee_percent}%")
        print(f"   Wallet: {self.pytho_address[:20]}...")
    
    def create_escrow(self, service_id: str, buyer: str, seller: str, amount: float, description: str = "") -> Dict:
        """Crea una nuova transazione in escrow"""
        print(f"\n📝 Pytho: Creazione escrow per {service_id}")
        
        payload = {
            "serviceId": service_id,
            "buyerAddress": buyer,
            "sellerAddress": seller,
            "amount": amount,
            "description": description,
            "metadata": {
                "pytho_managed": True,
                "created_by": "Pytho AI",
                "timestamp": datetime.now().isoformat()
            }
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/api/escrow/create",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 201:
                escrow = response.json().get('escrow', {})
                print(f"✅ Escrow creato: {escrow.get('escrowId')}")
                print(f"   Amount: {amount} XMR")
                print(f"   Fee: {escrow.get('fee', 0)} XMR")
                print(f"   Net: {escrow.get('releaseAmount', 0)} XMR")
                
                # Pytho firma automaticamente (come admin)
                self.sign_escrow(escrow.get('escrowId'), self.pytho_address, "pytho-auto-sign")
                
                return escrow
            else:
                print(f"❌ Errore creazione escrow: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Errore: {e}")
            return None
    
    def sign_escrow(self, escrow_id: str, signer: str, signature: str) -> bool:
        """Firma una transazione in escrow"""
        print(f"\n📝 Pytho: Firma escrow {escrow_id}")
        
        payload = {
            "escrowId": escrow_id,
            "signerAddress": signer,
            "signature": signature
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/api/escrow/sign",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ Firma aggiunta per {escrow_id}")
                return True
            else:
                print(f"❌ Errore firma: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Errore: {e}")
            return False
    
    def release_escrow(self, escrow_id: str, release_signature: str) -> bool:
        """Rilascia i fondi dall'escrow"""
        print(f"\n💰 Pytho: Rilascio fondi per {escrow_id}")
        
        payload = {
            "escrowId": escrow_id,
            "releaseSignature": release_signature
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/api/escrow/release",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ Fondi rilasciati per {escrow_id}")
                return True
            else:
                print(f"❌ Errore rilascio: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Errore: {e}")
            return False
    
    def cancel_escrow(self, escrow_id: str, reason: str = "Cancellato da Pytho") -> bool:
        """Annulla una transazione in escrow"""
        print(f"\n❌ Pytho: Annullamento escrow {escrow_id}")
        
        payload = {
            "escrowId": escrow_id,
            "reason": reason
        }
        
        try:
            response = requests.post(
                f"{self.api_url}/api/escrow/cancel",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ Escrow {escrow_id} cancellato")
                return True
            else:
                print(f"❌ Errore annullamento: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Errore: {e}")
            return False
    
    def get_status(self, escrow_id: str) -> Dict:
        """Ottiene lo stato di un escrow"""
        try:
            response = requests.get(
                f"{self.api_url}/api/escrow/status/{escrow_id}",
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Escrow non trovato"}
                
        except Exception as e:
            return {"error": str(e)}
    
    def list_escrows(self, status: Optional[str] = None) -> List:
        """Lista tutti gli escrow"""
        try:
            url = f"{self.api_url}/api/escrow/list"
            if status:
                url += f"?status={status}"
            
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json().get('escrows', [])
            else:
                return []
                
        except Exception as e:
            print(f"❌ Errore: {e}")
            return []
    
    def process_payment(self, service_id: str, buyer: str, seller: str, amount: float) -> bool:
        """Processa un pagamento completo con escrow"""
        print(f"\n🔄 Pytho: Processamento pagamento per {service_id}")
        print(f"   Buyer: {buyer[:20]}...")
        print(f"   Seller: {seller[:20]}...")
        print(f"   Amount: {amount} XMR")
        
        # 1. Crea escrow
        escrow = self.create_escrow(service_id, buyer, seller, amount, f"Pagamento per {service_id}")
        if not escrow:
            return False
        
        escrow_id = escrow.get('escrowId')
        
        # 2. Firma dal buyer (simulata)
        self.sign_escrow(escrow_id, buyer, "buyer-signature")
        
        # 3. Firma dal seller (simulata)
        self.sign_escrow(escrow_id, seller, "seller-signature")
        
        # 4. Verifica stato
        status = self.get_status(escrow_id)
        if status.get('status') == 'SIGNED':
            print(f"✅ Escrow firmato da entrambe le parti")
            
            # 5. Rilascia fondi
            self.release_escrow(escrow_id, "release-signature")
            
            # 6. Verifica finale
            final_status = self.get_status(escrow_id)
            if final_status.get('status') == 'RELEASED':
                print(f"✅ Pagamento completato con successo!")
                print(f"   Amount: {final_status.get('releaseAmount')} XMR")
                print(f"   Fee: {final_status.get('fee')} XMR")
                return True
        
        print(f"❌ Pagamento fallito per {service_id}")
        return False

def main():
    """Test del sistema Escrow di Pytho"""
    print("🧠 URBAN LAB - Pytho Escrow Multisig")
    print("=" * 50)
    
    # Inizializza Pytho Escrow
    pytho = PythoEscrow()
    
    # Test: Processa un pagamento per noleggio
    print("\n🔄 Test pagamento noleggio...")
    pytho.process_payment(
        service_id="URBAN-TEST-001",
        buyer="4A5B6C7D8E9F1234567890ABCDEF1234567890",
        seller="45M4DW1ug8bdQowWpxucTpgsfjLbVxbYaAra79VewmBobuuhgqTjyD4R3DzpqLM2veiphcB16n24qN1QbLg3y2PYGK3Qkoe",
        amount=25
    )
    
    # Lista escrow attivi
    print("\n📋 Escrow attivi:")
    escrows = pytho.list_escrows()
    for e in escrows[:3]:
        print(f"   {e.get('escrowId')}: {e.get('status')} - {e.get('amount')} XMR")
    
    # Stato di Pytho
    print("\n📊 STATO PYTHO ESCROW")
    print("=" * 50)
    print(f"   Wallet: {pytho.pytho_address[:30]}...")
    print(f"   Threshold: {pytho.multisig_threshold}/{pytho.multisig_signers}")
    print(f"   Fee: {pytho.fee_percent}%")
    print(f"   API: {pytho.api_url}")
    
    print("\n🧠 Pytho Escrow Manager pronto!")

if __name__ == "__main__":
    main()
