from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re
for homo in SeqIO.parse("uniprot-organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22.fasta", "fasta"):
    pattern = re.compile(r"\|.+\|")
    idv = pattern.findall(homo.id)
    my_seq = Seq(str(homo.seq), IUPAC.protein)
    ids = re.sub(r"\[\'\||\|\'\]","",str(idv))
    for index, letter in enumerate(my_seq):
        AA = ['F','L','S','Y','C','W','P','H','Q','I','M','T','N','K','R','V','A','D','E','G','U','O']
        for aa in AA:
            if letter == aa:
                AA.remove(str(letter))
                break
        for Var in AA:
            print ids, str(index+1), letter, Var