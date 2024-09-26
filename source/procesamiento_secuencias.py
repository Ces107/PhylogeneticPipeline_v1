from Bio import SeqIO

def procesar_secuencias(archivo_fasta, longitud_min, longitud_max):

    secuencias_validas = {}

    for seq_record in SeqIO.parse(archivo_fasta, "fasta"):

        
        print(f"Leyendo secuencia: {seq_record.id}, longitud {len(seq_record.seq)}")


        secuencia = str(seq_record.seq).upper()
       
        if len(secuencia) >= longitud_min and len(secuencia) <= longitud_max:
            print("Secuencia completa")


            if secuencia not in secuencias_validas:
                secuencias_validas[secuencia] = seq_record.id
            else:
                secuencias_validas[secuencia] += "_" + seq_record.id
           
           
    
        else:
            print(f"Secuencia incorrecta, id: {seq_record.id}")


    with open("..\\Proyecto\\data\\filtradas_sequences.fasta", "w+") as output_file:

        for sequence in secuencias_validas:
            output_file.write(">" + secuencias_validas[sequence] + "\n" + sequence + "\n")

    print("CLEAN!!!\nPlease check filtradas_" + archivo_fasta)