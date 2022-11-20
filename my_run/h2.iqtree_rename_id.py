"""
1. iqtree 不能识别@符号，经常出现@符号后会丢失后面的geneid，所有使用iqtree运行的时候，需要修改id
2. 修改iqtree建树结果中geneid，后面的分析需要@为分割符号
"""

import re
import sys
import os 

def sub(content):
	# new_content = re.sub("_","@",content.group())
	# new_content = re.sub("_____","_",content.group())
	new_content = re.sub("_","_____",content.group())

	return new_content

def main(indir,outdir):
	indir = os.path.abspath(indir)
	outdir = os.path.abspath(outdir)

	for file in os.listdir(indir):
		if file.endswith("treefile"):
			full = os.path.join(indir,file)
			with open(os.path.join(outdir,file),"w") as ouf:
				with open(full) as inf:
					lines = inf.read()
					new_lines = re.sub(r"_G\d+","",lines)
					print(new_lines,file=ouf)
					

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python %s indir outdir"%sys.argv[0])
		sys.exit(0)
	main(sys.argv[1],sys.argv[2]) 

