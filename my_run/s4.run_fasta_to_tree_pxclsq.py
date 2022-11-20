"""
1. 批量运行cluster建树，需要将所有的fasta进行分割
2. 每个运行新建目录
3. 根据总数量，自定义分割文件
"""

import re
import sys 
import os 

script = "/data/01/user102/maketree/23.maketree_some_yangya_only_cds_nofilter/scripts/fasta_to_tree_pxclsq_hhy.py"

def split_file(start,end,cluster_dir,tree_outdir):
	cluster_dir = os.path.abspath(cluster_dir)
	tree_outdir = os.path.abspath(tree_outdir)
	total = len(os.listdir(cluster_dir))
	if int(end) <= total:
		for i in range(start,end+1):
			dirs = tree_outdir
			file = cluster_dir
			python2 = "/data/00/user/user102/anaconda3/envs/python27/bin/python2.7"
			print("mkdir {dirs}/cluster{i}; chmod 777 {dirs}/cluster{i}; cp {file}/cluster{i}.fa {dirs}/cluster{i}/cluster{i}.fa; cd {dirs}/cluster{i}; \
{python2} {script} ./ 2 aa y > cluster{i}.log 2>&1;".format(python2 = python2,dirs=dirs,i=i,file=file,script=script))
	else:
		print("not so much cluster")
		sys.exit(0)

def remove_file(start,end,total=6835):
	if int(end) <= total:
		for i in range(start,end):
			dirs = "/data/01/user102/yangya_outgroup/output/3.cluster"
			script = "/data/01/user102/yangya_outgroup/scripts/fasta_to_tree_pxclsq_hhy.py"
			file = "/data/01/user102/yangya_outgroup/output/2.diamond/hit-frac0.5_I2_e5_cluster"
			python2 = "/data/00/user/user102/anaconda3/envs/python27/bin/python2.7"
			print("rm -rf {dirs}/cluster{i}".format(dirs=dirs,i=i))
	else:
		print("not so much cluster")
		sys.exit(0)

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print("python %s start_num end_num cluster_dir tree_outdir total_cluster"%sys.argv[0])
		print("start_num--开始数字\nend_num--终止数字\ncluster_dir--clustr文件夹\ntree_outdir--建树生成文件夹\n")
		sys.exit(0)

	split_file(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4])
