import random
from Bio.Data import CodonTable

nucleotides = ['A', 'T', 'C', 'G']
seq = []
for a in range(0, 1000):
    i = random.randint(0, 3)
    seq.append(nucleotides[i])
sequence=(''.join(seq))


standard_table = CodonTable.unambiguous_dna_by_id[1]
stopC=standard_table.stop_codons

codons=[]
i=0
for codon in range (0, len(seq)//3):
    triplet=seq[i]+seq[i+1]+seq[i+2]
    i += 3
    if triplet in stopC:
        continue
    else:
        codons.append(triplet)

random_sequence=''
for i in range(0,len(codons)):
    random_sequence+=codons[i]

generated_seq_file=open('/home/ekaterina/Desktop/Homeworks/HW1/data/random_generated_seq.txt','w')
generated_seq_file.write(random_sequence)
generated_seq_file.close
