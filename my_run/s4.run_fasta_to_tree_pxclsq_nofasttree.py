
"""
1. 批量运行cluster建树，需要将所有的fasta进行分割
2. 每个运行新建目录
3. 根据总数量，自定义分割文件
"""

import re
import sys 
import os 

script = os.path.abspath("../scripts/fasta_to_tree_pxclsq_hhy.py")

def split_file(cluster_dir,tree_outdir):
	cluster_dir = os.path.abspath(cluster_dir)
	tree_outdir = os.path.abspath(tree_outdir)
	start, end = 1, len(os.listdir(cluster_dir))
	for i in range(start,end+1):
		dirs = tree_outdir
		file = cluster_dir
		python2 = "/data/00/user/user102/anaconda3/envs/python27/bin/python2.7"
		print("mkdir {dirs}/cluster{i}; chmod 777 {dirs}/cluster{i}; cp {file}/cluster{i}.fa {dirs}/cluster{i}/cluster{i}.fa; cd {dirs}/cluster{i}; \
{python2} {script} ./ 5 dna y > cluster{i}.log 2>&1;".format(python2 = python2,dirs=dirs,i=i,file=file,script=script))

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python %s cluster_dir tree_outdir"%sys.argv[0])
		sys.exit(0)

	split_file(sys.argv[1],sys.argv[2])
