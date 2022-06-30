import random
from Bio.Data import CodonTable

nucleotides = ['A', 'T', 'C', 'G']
seq = []
for a in range(0, 1000):
    i = random.randint(0, 3)
    seq.append(nucleotides[i])
sequence=(''.join(seq))

codons=[]
i=0
for codon in range (0, len(seq)//3):
    triplet=seq[i]+seq[i+1]+seq[i+2]
    codons.append(triplet)
    i+=3

standard_table = CodonTable.unambiguous_dna_by_id[1]
stopC=standard_table.stop_codons

sequence=[]
for i in codons:
    if i!=stopC[0] and i!=stopC[1] and i!=stopC[2]:
        sequence.append(i)

seq_=''
for i in sequence:
    seq_+=i
print(seq_)