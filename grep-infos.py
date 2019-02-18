from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re
for homo in SeqIO.parse("test.fastq", "fasta"):
    pattern = re.compile(r"\|.+\|")
    idv = pattern.findall(homo.id)
    my_seq = Seq(str(homo.seq), IUPAC.protein)
    ids = re.sub(r"\[\'\||\|\'\]","",str(idv))
    for index, letter in enumerate(my_seq):
        AA = ['F','L','S','Y','C','W','P','H','Q','I','M','T','N','K','R','V','A','D','E','G']
        AA.remove(str(letter))
        for Var in AA:
            print ids, str(index+1), letter, Var