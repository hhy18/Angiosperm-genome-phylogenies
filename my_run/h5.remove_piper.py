"""
1. 删除cluster中19_39胡椒目物种
"""

import re
import os 
import sys
from Bio import SeqIO

def main(indir,outdir):
	indir = os.path.abspath(indir)

	for file in os.listdir(indir):
		if file.endswith(".fa"):
			full = os.path.join(indir,file)
			with open(os.path.join(outdir,file),"w") as ouf:
				for seq in SeqIO.parse(full,"fasta"):
					if not re.search(r"19_39",seq.id):
						print(">"+seq.id+"\n"+seq.seq,file=ouf)


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python %s indir outdir"%sys.argv[0])
		sys.exit(0)

	main(sys.argv[1],sys.argv[2])
