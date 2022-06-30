import pandas as pd
from Bio import SeqIO
position=[]
amino_acid=[]
percent_conservativeness=[]
import matplotlib.pyplot as plt

for r in range (0,249):
    l = []
    for seq_r in SeqIO.parse("/home/ekaterina/Desktop/Homeworks/HW1/data/alignment.fasta", "fasta"):
        l.append(seq_r.seq[r])
        num = 0
    for x in range(0,len(l)-1):
        if l[0]==l[x+1]:
            num+=1

    if num >= 20:
        if l[0]!='-':
            #print(f'amino acid {l[0]}')
            #print('count=', num)
            #print('percent conservativeness=', (num / 249) * 100)
            #print(f"Position = {r + 1}")
            position.append(r+1)
            amino_acid.append(l[0])
            percent_conservativeness.append((num/249)*100)

d = {'position': position, 'amino_acid': amino_acid, 'percent_conservativeness': percent_conservativeness}
data = pd.DataFrame(data=d)
print(data)

from pathlib import Path
filepath = Path('/home/ekaterina/Desktop/Homeworks/HW1/table/percent_conservativeness.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
data.to_csv(filepath, sep='\t')

