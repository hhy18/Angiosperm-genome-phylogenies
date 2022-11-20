"""
获得iqtree的log文件中的模型
"""

import re 
import os 
import sys

def main(indir,indir2):
	file_model = dict()
	for file in os.listdir(indir):
		if file.endswith("log"):
			fullfile = os.path.join(indir,file)
			with open(fullfile) as inf:
				content = inf.read()
				model = re.search(r"Best-fit.*:(.*)chosen",content).group(1)
				file_model[file.rstrip(".log")]=model

	for file in os.listdir(indir2):
		if file.endswith("aln-cln"):
			fullfile = os.path.join(indir2,file)
			print("iqtree -s %s -m %s -B 1000 -bnni -T AUTO -redo"%(fullfile, file_model[file]))

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("python %s iqtree_log_dir trimal_dir"%sys.argv[0])
		sys.exit(0)
	main(sys.argv[1],sys.argv[2])
