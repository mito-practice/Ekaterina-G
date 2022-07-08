from Bio import SeqIO

k = 5
kmer_5 = open('/home/ekaterina/Desktop/Homeworks/HW2/data/5kmer.txt','w')
for sequence in SeqIO.parse("/home/ekaterina/Desktop/Homeworks/HW2/data/Homo_sapiens.GRCh37.dna.alt.fa", "fasta"):
    print(sequence.id)
    for i in range(0, len(sequence), 1):
        if sequence.seq[i: i + k]!='NNNNN':
            cur_kmer = sequence.seq[i: i + k]
            kmer_5.write(str(cur_kmer)+'\n')
            print(str(cur_kmer))
kmer_5.close()

