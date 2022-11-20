"""
1. 编写运行prune_paralogs_MO.py的sh文件,
"""

import re
import os 
import sys

script = os.path.abspath("../scripts/prune_paralogs_MO.py")

def main(indir,outdir,minitaxa):
	indir = os.path.abspath(indir)
	outdir = os.path.abspath(outdir)

	subtree_list = list()
	for dirpath,dianame,files in os.walk(indir):
		for file in files:
			fullfile = os.path.join(dirpath,file)
			if fullfile.endswith("subtree"):
				subtree_list.append(fullfile)

	# print("number of subtree %s"%(len(subtree_list)))
	for i in subtree_list:
		subdir = os.path.dirname(i)
		# script = "/data/01/user102/maketree/22.maketree_some_yangya_only_cds/scripts/prune_paralogs_MO.py"
		# taxon_id = "/data/01/user102/project_2021/1.phylogeny/phylogenomic_dataset_construction/taxon.id"
		print("cd {subdir}; python2 {script} . subtree  {minitaxa} {outdir}".format(minitaxa=minitaxa,subdir=subdir,script=script,outdir=outdir))

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("注意！！！\n先修改/data/01/user102/yangya_outgroup/scripts/prune_paralogs_MO.py中ingroup和outgroup列表")
		print("python %s subtree_dir ortho_outdir minitaxa \nsubtree_dir--cut_long_branch的产生subtree文件夹\northo_outdir--产生直系同源树的输出文件夹\nminitaxa--树中包含最小物种数量"%sys.argv[0])
		sys.exit(0)
	main(sys.argv[1],sys.argv[2],sys.argv[3]) 
