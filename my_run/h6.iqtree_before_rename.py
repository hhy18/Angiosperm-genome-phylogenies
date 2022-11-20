"""
1. iqtree 不能出现@, IQTREE 运行前修改id
"""

import re
import os 
import sys
from Bio import SeqIO

def sub(content):
	# new_content = re.sub("_","@",content.group())
	# new_content = re.sub("_____","_",content.group())
	# new_content = re.sub("_","_____",content.group())
	new_content = re.sub("@","___",content.group())

	return new_content

def main(indir,outdir):
	indir = os.path.abspath(indir)

	for file in os.listdir(indir):
		if file.endswith("fa"):
			full = os.path.join(indir,file)
			with open(os.path.join(outdir,file),"w") as ouf:
				for seq in SeqIO.parse(full,"fasta"):
					# newid = re.sub(r"_G\d+",sub,seq.id)
					newid = re.sub(r"@",sub,seq.id)
					print(">"+newid+"\n"+seq.seq,file=ouf)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python %s indir outdir"%sys.argv[0])
		sys.exit(0)
	main(sys.argv[1],sys.argv[2])