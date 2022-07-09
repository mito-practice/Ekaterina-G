import numpy as np
import pandas as pd
from Bio import SeqIO

position=[]
amino_acid=[]
percent_conservativeness=[]
location=[]


list_of_aminoacids=[]
for seq_record in SeqIO.parse("/home/ekaterina/Desktop/Homeworks/HW1/data/alignment.fasta", "fasta"):
    list_of_aminoacids.append(list(seq_record.seq))


table_of_strings = np.array(list_of_aminoacids)

table_of_columns = np.transpose(table_of_strings)

conservativeness=[]
aminocid=[]
location=[]
percent_conservativeness=[]
for i in table_of_columns:
    i= str(i)
    for j in range(0,len(i)):
        if i[j].isalpha()==True:
            conservativeness.append(i.count(i[j]))
            aminocid.append(i[j])
            i=i.replace(i[j], ' ')

for l in conservativeness:
    percent_conservativeness.append(l*100/len(table_of_columns[0]))

d = {'aminoasid': aminocid, 'conservativeness': conservativeness, 'percent_conservativeness': percent_conservativeness}
data = pd.DataFrame(data=d)
print(data)

from pathlib import Path
filepath = Path('/home/ekaterina/Desktop/Homeworks/HW1/data/percent_conservativeness.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
data.to_csv(filepath, sep='\t')

