import Bio
from Bio import SeqIO, SeqRecord
from Bio.Seq import Seq
from Bio.Seq import MutableSeq
import pandas as pd
import matplotlib.pyplot as plt

my_file = open('/home/ekaterina/Desktop/Homeworks/HW1/data/translations.fasta', 'w')

for seq_r in SeqIO.parse("/home/ekaterina/Desktop/Homeworks/HW1/data/seqdump5.fasta", "fasta"):
    my_file.write('>' + str(seq_r.id) + '\n')
    p = seq_r.translate(table=11, stop_symbol="")
    my_file.write(str(p.seq) + '\n')
my_file.close()

file=open('/home/ekaterina/Desktop/Homework/HW1/data/alignment.fasta', 'r')
lines=file.readlines()
counts_gaps=[]
for line in lines:
    if '>' in line:
        continue
    if '-' in line:
        counts_gaps.append(line.count('-'))

data = pd.DataFrame(counts_gaps)


fig = plt.figure()
plt.hist(data)
plt.title('gap length')
plt.grid(True)

plt.show()
