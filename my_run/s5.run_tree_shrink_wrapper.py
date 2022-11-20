"""
1. 写出sh文件，用于修剪树文件 tree_shrink_wrapper
"""

import re
import sys 
import os 

script = "/data/01/user102/yangya_outgroup/scripts/tree_shrink_wrapper.py"

def main(indir,outdir,q,ending):
	indir = os.path.abspath(indir)
	
	fullfile_list = list()
	for dirpath,dirname,files in os.walk(indir):
		for file in files:
			fullfile = os.path.join(dirpath,file)
			if fullfile.endswith(ending):
				fullfile_list.append(fullfile)

	for i in fullfile_list:
		dirs = os.path.dirname(i)
		subdir = re.sub("."+ending,"",os.path.basename(i))
		print("cd {outdir}; mkdir {subdir}; cd {subdir}; cp {i} ./; python2 {script} . {ending} {q} .".format(ending=ending,subdir=subdir,i=i,script=script,outdir=outdir,q=q))

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print("!!! iqtree 结果修改@")
		print("python %s cluster_treedir treeshrink_outdir q_threshold ending"%sys.argv[0])
		print("cluster_treedir--cluster建树目录")
		print("treeshrink_outdir--treeshrink输出目录")
		print("q_threshold--错误率阈值—默认0.05")
		print("ending--树文件结尾字符")
		sys.exit(0)

	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])


