"""
1. 查看iqtree建树结果是否完整，不完整的需要重新尽心iqtree
"""

import re
import os 
import sys

iqtree = "/data/00/user/user102/anaconda3/envs/biosofeware/bin/iqtree"


def main(indir):
	indir = os.path.abspath(indir)

	for file in os.listdir(indir):
		if file.endswith("aln-cln"):
			full = os.path.join(indir,file)
			if not os.path.exists(full+".treefile"):
				print("{iqtree} -s {i} -m MFP -bb 1000 -bnni -nt AUTO -redo".format(iqtree=iqtree,i=full))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("python %s indir"%sys.argv[0])
		sys.exit()
	main(sys.argv[1])

