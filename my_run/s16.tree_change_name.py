"""
将建好的树文件中的label名称修改为 number_speciesc_order
"""

import re
import sys
import os
def sub_defind(i):
	i = i.group()
	ii = re.search(r"(\d{4}_\d{3})",i).group(1)
	if ii in change_dict:
		return change_dict[ii]


def main(change_file,treefile):
	
	global change_dict;
	change_dict = dict()
	with open(change_file) as inf:
		for index,lines in enumerate(inf.readlines()):
			if index > 0:
				line = lines.strip().split(",")
				newname = re.sub(r"[^0-9_a-zA-Z]","_",lines.strip())
				change_dict[line[0]] = newname

	with open(treefile) as inf:
		content = inf.read()
		new_content = re.sub(r"\d{4}_\d{3}_\w{3}",sub_defind,content)
		print(new_content)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("python %s ref_file treefile"%sys.argv[0])
		sys.exit(0)
	main(sys.argv[1],sys.argv[2])
