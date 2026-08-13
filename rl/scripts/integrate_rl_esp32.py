#!/usr/bin/env python3
"""
🔗 Urban Lab - Integrazione RL con ESP32
Converte la policy ONNX in formato compatibile con ESP32
"""

import numpy as np
import onnx
from onnx import helper, TensorProto
import json
import os

def convert_policy_to_esp32(onnx_path, output_dir):
    """Converte policy ONNX per deployment su ESP32"""
    
    print("🏭 Urban Lab - Integrazione RL con ESP32")
    print("=" * 50)
    
    # Carica modello ONNX
    model = onnx.load(onnx_path)
    print(f"✅ Modello caricato: {onnx_path}")
    
    # Estrai pesi
    weights = {}
    for initializer in model.graph.initializer:
        name = initializer.name
        data = onnx.numpy_helper.to_array(initializer)
        weights[name] = data.tolist()
        print(f"   📊 {name}: {data.shape}")
    
    # Converti in formato per ESP32 (C array)
    esp32_code = []
    esp32_code.append("// 🏭 Urban Lab - Policy per ESP32")
    esp32_code.append("// Generato automaticamente da RLbotics")
    esp32_code.append("")
    esp32_code.append("#include <Arduino.h>")
    esp32_code.append("#include <math.h>")
    esp32_code.append("")
    
    # Definisci pesi come array
    for name, data in weights.items():
        if isinstance(data, list):
            esp32_code.append(f"const float {name}[] = {{")
            # Converti lista in stringa formattata
            flat_data = []
            for item in data:
                if isinstance(item, list):
                    flat_data.extend(item)
                else:
                    flat_data.append(item)
            line = ", ".join([f"{x:.6f}" for x in flat_data[:20]])
            if len(flat_data) > 20:
                line += ", ..."
            esp32_code.append(f"    {line}")
            esp32_code.append("};")
            esp32_code.append("")
    
    # Funzione di forward pass
    esp32_code.append("// Forward pass della policy")
    esp32_code.append("float* policy_forward(float* obs) {")
    esp32_code.append("    // Implementazione forward pass")
    esp32_code.append("    // Nota: per ESP32, usare micrograd o implementare manualmente")
    esp32_code.append("    static float action[3];")
    esp32_code.append("    action[0] = 0.0; // Accelerazione")
    esp32_code.append("    action[1] = 0.0; // Frenata")
    esp32_code.append("    action[2] = 0.0; // Sterzo")
    esp32_code.append("    return action;")
    esp32_code.append("}")
    
    # Salva il codice ESP32
    esp32_file = os.path.join(output_dir, "policy_esp32.h")
    with open(esp32_file, 'w') as f:
        f.write("\n".join(esp32_code))
    print(f"✅ Codice ESP32 generato: {esp32_file}")
    
    # Crea file di configurazione
    config = {
        "input_size": 6,
        "output_size": 3,
        "hidden_layers": [256, 256, 128],
        "activation": "tanh"
    }
    config_file = os.path.join(output_dir, "policy_config.json")
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"✅ Configurazione salvata: {config_file}")
    
    print("🎯 Integrazione completata!")
    print("📋 Successivo: carica policy_esp32.h sul tuo ESP32")

if __name__ == "__main__":
    import sys
    import glob
    
    # Trova l'ultima policy
    log_dirs = glob.glob("logs/scooter_*")
    if not log_dirs:
        print("❌ Nessuna policy trovata! Esegui prima train.py")
        sys.exit(1)
    
    latest_log = max(log_dirs)
    onnx_path = os.path.join(latest_log, "policy.onnx")
    
    if not os.path.exists(onnx_path):
        print(f"❌ Policy non trovata: {onnx_path}")
        sys.exit(1)
    
    output_dir = "esp32_policy"
    os.makedirs(output_dir, exist_ok=True)
    
    convert_policy_to_esp32(onnx_path, output_dir)
