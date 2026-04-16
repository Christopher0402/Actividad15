import json
import os
from datetime import datetime

def process_data(input_file, version):
    log_file = "backup.log"
    output_file = "filtered_data.json"
    
    # a. Leer información
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # b. Procesar (Filtro de ejemplo)
    filtered = [item for item in data if item.get("active") == True]
    count = len(filtered)
    
    # c. Generar archivo de resultados
    with open(output_file, 'w') as f:
        json.dump(filtered, f)
    
    # d. Registrar actividad en backup.log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] File: {input_file} | Result: {count} records filtered | Version: {version}\n"
    
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    print(f"Se filtró {count} datos")

if __name__ == "__main__":
    # La versión se puede pasar como variable de entorno o entrada manual
    ver = os.getenv("APP_VERSION", "1.0.0")
    process_data('data.json', ver)