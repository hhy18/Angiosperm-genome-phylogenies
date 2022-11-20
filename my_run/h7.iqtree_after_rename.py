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
	# new_content = re.sub("_","_____",content.group())
	content_list = re.split("_",content.group())
	content1 = "_".join(content_list[0:3]) + "@" + "_".join(content_list[3:5])
	# content2 = content.group()
	# new_content = "@".join([content1,content2])

	return content1

def main(indir,outdir):
	indir = os.path.abspath(indir)
	outdir = os.path.abspath(outdir)

	for dirpath, dirnames, files in os.walk(indir):
		for file in files:
			if file.endswith("bs.tre"):
				full = os.path.join(dirpath,file)
				out_dir = os.path.join(outdir,os.path.basename(os.path.dirname(full)))
				if not os.path.exists(out_dir):
					os.mkdir(out_dir)
				with open(os.path.join(out_dir,file),"w") as ouf:
					with open(full) as inf:
						lines = inf.read()
						# new_lines = re.sub(r"\d{4}_\d{3}_\w{3}_\w{3}_\w+",sub,lines)
						# new_lines = re.sub(r"_G\d+","",lines)
						new_lines = re.sub("___","@",lines)
						# new_lines = re.sub("@","_",lines)
						print(new_lines,file=ouf)
					

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("python %s indir outdir"%sys.argv[0])
		sys.exit(0)
	main(sys.argv[1],sys.argv[2]) 

