import subprocess
from Bio import SeqIO

def alinear(clustalomega_path,input_path):

    output_path = r".\aligned_sequences_version3.fasta"

    command = [
    clustalomega_path,
    "--in", input_path,
    "--out", output_path,
    "--seqtype=DNA",
    "--threads=12",  
    "-v",
    "--force" ]

    try:
        subprocess.run(command, check=True)
        print("Alineamiento completado exitosamente.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Clustal Omega: {e}")


def comprobar_alineamiento(output_path):
    secuencias = list(SeqIO.parse(output_path, "fasta"))
    if not secuencias:
        print("No se encontraron secuencias alineadas.")
        return
    
    secuencia_base = secuencias[0].seq
    print(f"Comparando con la primera secuencia: {secuencias[0].id}")
    
    for seq in secuencias[1:]:  # Comenzar desde la segunda secuencia
        cambios = sum(1 for base1, base2 in zip(secuencia_base, seq.seq) if base1 != base2 and base1 != '-' and base2 != '-')
        print(f"ID: {seq.id}, Cambios: {cambios}")

