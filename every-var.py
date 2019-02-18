from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re

for homo in SeqIO.parse("homo_cds.fq", "fasta"):
    coding_dna = Seq(str(homo.seq), IUPAC.unambiguous_dna)
    protein_ori = coding_dna.translate()
    protein_ori = str(protein_ori)[:-1]
    nc = 0
    for dna in coding_dna._data:
        coding_dna_var = coding_dna[:nc] + "A" + coding_dna[(nc+1):]
        protein = coding_dna_var.translate()
        protein = str(protein)[:-1]
        if str(protein_ori) != str(protein):
            if len(str(protein_ori)) == len(str(protein)):
                ac = 0
                for aa in protein:
                    if aa == protein_ori[ac]:
                        ac = ac + 1
                    else:
                        if aa != '*':
                            print str(nc+1),' ',coding_dna[nc],'A',' ',str(ac+1),' ',protein_ori[ac],' ',aa
                            break
                        else:
                            break
        coding_dna_var = coding_dna[:nc] + "T" + coding_dna[(nc+1):]
        protein = coding_dna_var.translate()
        protein = str(protein)[:-1]
        if str(protein_ori) != str(protein):
            if len(str(protein_ori)) == len(str(protein)):
                ac = 0
                for aa in protein:
                    if aa == protein_ori[ac]:
                        ac = ac + 1
                    else:
                        if aa != '*':
                            print str(nc+1),' ',coding_dna[nc],'T',' ',str(ac+1),' ',protein_ori[ac],' ',aa
                            break
                        else:
                            break
        coding_dna_var = coding_dna[:nc] + "C" + coding_dna[(nc+1):]
        protein = coding_dna_var.translate()
        protein = str(protein)[:-1]
        if str(protein_ori) != str(protein):
            if len(str(protein_ori)) == len(str(protein)):
                ac = 0
                for aa in protein:
                    if aa == protein_ori[ac]:
                        ac = ac + 1
                    else:
                        if aa != '*':
                            print str(nc+1),' ',coding_dna[nc],'C',' ',str(ac+1),' ',protein_ori[ac],' ',aa
                            break
                        else:
                            break
        coding_dna_var = coding_dna[:nc] + "G" + coding_dna[(nc+1):]
        protein = coding_dna_var.translate()
        protein = str(protein)[:-1]
        if str(protein_ori) != str(protein):
            if len(str(protein_ori)) == len(str(protein)):
                ac = 0
                for aa in protein:
                    if aa == protein_ori[ac]:
                        ac = ac + 1
                    else:
                        if aa != '*':
                            print str(nc+1),' ',coding_dna[nc],'G',' ',str(ac+1),' ',protein_ori[ac],' ',aa
                            break
                        else:
                            break
        nc = nc + 1