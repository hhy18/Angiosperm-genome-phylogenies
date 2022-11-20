"""
1. 编写去除长枝sh文件，s12.run_cut_long_internal_branches.py internal_branch_length_cutoff=0.6
"""

import re
import sys
import os

script = os.path.abspath("../scripts/cut_long_internal_branches.py")

def main(indir,minitaxa):
	indir = os.path.abspath(indir)
	# outdir = os.path.abspath(outdir)

	fullfile_list = list()
	for dirpath,dirname,files in os.walk(indir):
		for file in files:
			fullfile = os.path.join(dirpath,file)
			if fullfile.endswith("mm"):
				fullfile_list.append(fullfile)

	for i in fullfile_list:
		dirpath = os.path.dirname(i)
		basename = os.path.basename(i)
		# cluster = re.sub(r"\.fasttree_0\.05\.ts\.tt\.mm","",basename)
		# cluster = re.sub(r"\.fasttree\.tre\.tt\.mm","",basename)
#		script = "/data/01/user102/yangya_outgroup/scripts/cut_long_internal_branches.py"
#		subdir = "/data/01/user102/yangya_outgroup/output/4.tree_trim_0.1"
		print("cd {dirpath}; python2 {script} . mm 0.7 {minitaxa} .".format(minitaxa=minitaxa,dirpath=dirpath,script=script))

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python %s cluster_mm minitaxa outdir\ncluster_dir--cluster mm建树文件夹\nminitaxa--最小包含物种数量\n")
		sys.exit(0)
	main(sys.argv[1],sys.argv[2])
