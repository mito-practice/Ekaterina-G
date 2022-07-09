from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

my_file = open('/home/ekaterina/Desktop/Homeworks/HW1/data/translations.fasta', 'w')

#трансляция для того, чтоб потом загнать это в маскл и выровнять, чтобы было все четко ввиде красивой фасты
for seq_r in SeqIO.parse("/home/ekaterina/Desktop/Homeworks/HW1/data/seqdump5.fasta", "fasta"):
    my_file.write('>' + str(seq_r.id) + '\n')
    p = seq_r.translate(table=11, stop_symbol="") #11 для бактерий
    my_file.write(str(p.seq) + '\n')
my_file.close()

#после выравнивания в маскл, поптка посчитать длины гэпов
file=open('/home/ekaterina/Desktop/Homeworks/HW1/data/alignment.fasta', 'r')
lines=file.readlines()

counts_gaps=[]
len_this_gap=0
for line in lines:
    if '>' in line:
        continue
    for i in range(0, len(line)-1):
        if line[i+1]==line[i] and line[i]=='-':
            len_this_gap+=1
        if line[i]!=line[i+1]:
            if len_this_gap!=0:
                counts_gaps.append(len_this_gap)
                len_this_gap=0
file.close
ser = pd.Series(counts_gaps, copy=False)
fig = plt.figure()
plt.hist(ser)
plt.title('gap length')
plt.grid(True)

plt.show()