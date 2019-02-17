from Bio import SeqIO
for homo in SeqIO.parse("test.fastq", "fasta"):
    print(homo.id + "\n")