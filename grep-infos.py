from Bio import SeqIO
for homo in SeqIO.parse("~/test.fastq", "fastq"):
    print(homo.id)