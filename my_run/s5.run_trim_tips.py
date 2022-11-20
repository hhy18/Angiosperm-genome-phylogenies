"""
1. 写出sh文件，用于修剪树文件 tree_shrink_wrapper, 产生tt
"""

import re
import sys 
import os 

script = os.path.abspath("../scripts/trim_tips.py")

def main(indir):
	indir = os.path.abspath(indir)
	fullfile_list = list()
	for dirpath,dirname,files in os.walk(indir):
		for file in files:
			fullfile = os.path.join(dirpath,file)
			if fullfile.endswith("tre"):
				fullfile_list.append(fullfile)

	for i in fullfile_list:
		dirs = os.path.dirname(i)
		# subdir = re.sub(r"\.fasttree\.tre","",os.path.basename(i))
		# outdir = "/data/01/user102/yangya_outgroup/output/3.tt_mm"
		print("cd {dirs}; python2 {script} . tre 0.5 2".format(dirs=dirs,script=script))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("python %s indir \nindir--cluster建树文件夹"%sys.argv[0])
		sys.exit(0)
	
	main(sys.argv[1])


