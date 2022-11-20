"""
1. 写出sh文件，标记单系枝
"""

import re
import sys 
import os 

script = os.path.abspath("../scripts/mask_tips_by_taxonID_genomes.py")

def main(indir):
	indir = os.path.abspath(indir)
	fullfile_list = list()
	for dirpath,dirname,files in os.walk(indir):
		for file in files:
			fullfile = os.path.join(dirpath,file)
			if fullfile.endswith("tt"):
				fullfile_list.append(fullfile)

	for i in fullfile_list:
	#	script = "/data/01/user102/yangya_outgroup/scripts/mask_tips_by_taxonID_genomes.py"
		dirpath = os.path.dirname(i)
		print("cd {dirpath}; python2 {script} . ".format(dirpath=dirpath,script=script))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("python %s cluster_dir \ncluster_tt--cluster tt 建树文件夹"%sys.argv[0])
		sys.exit(0)
	
	main(sys.argv[1])


