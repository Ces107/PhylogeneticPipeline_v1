import os
import sys

from src.procesamiento_secuencias import procesar_secuencias
from src.alineamiento import alinear, comprobar_alineamiento

def main():
    
    directorio_data = r"..\Proyecto\data"
    directorio_tools = r"..\Proyecto\tools"
    archivo_secuencias = os.path.join(directorio_data, "sequences.fasta")
    archivo_secuencias_filtradas = os.path.join(directorio_data, "filtradas_sequences.fasta")
    archivo_secuencias_alineadas = os.path.join(directorio_data, "aligned_sequences.fasta")
    clustalomega_path = os.path.join(directorio_tools, "clustal-omega-1.2.2-win64", "clustalo.exe")

    # Asegúrate de que Clustal Omega esté en la ubicación esperada
    if not os.path.exists(clustalomega_path):
        raise FileNotFoundError(f"No se encontró Clustal Omega en {clustalomega_path}")

    procesar_secuencias(archivo_secuencias, 26000, 32000)

    alinear(clustalomega_path, archivo_secuencias_filtradas)

    comprobar_alineamiento(archivo_secuencias_alineadas)

    print("Pipeline completado.")






if __name__ == "__main__":
    main()
