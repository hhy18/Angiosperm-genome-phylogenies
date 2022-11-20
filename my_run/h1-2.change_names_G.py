"""
所有的geneid重新命名
"""

import re
import os 
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def main(cdsdir, pepdir, cdsout, pepout):
	for file in os.listdir(cdsdir):
		cdsfile = os.path.join(cdsdir,file)
		pepfile = os.path.join(pepdir,re.sub(r"cds","pep",file))

		species_num = re.search(r"(\d{4}_\d{3}_\w{3})",file).group(1)
		species_pre = re.search(r"\d{4}_\d{3}_(\w{3})",file).group(1)
		
		newid_dict = dict()
		flag = 1
		
		with open(os.path.join(cdsout,file),"w") as cds_ouf:
			for cds_seq in SeqIO.parse(cdsfile,"fasta"):
				newid = species_num + "@" + species_pre+"_G%d"%flag
				flag += 1
				newid_dict[cds_seq.id] = newid
				print(">"+newid+"\n"+str(cds_seq.seq),file=cds_ouf)

		with open(os.path.join(pepout,re.sub(r"cds","pep",file)),"w") as pep_ouf:
			for pep_seq in SeqIO.parse(pepfile,"fasta"):
				newid = newid_dict[pep_seq.id]
				print(">"+newid+"\n"+str(pep_seq.seq),file=pep_ouf)

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print("python %s cdsdir pepdir cdsout pepout"%sys.argv[0])
		sys.exit(0)

	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])




