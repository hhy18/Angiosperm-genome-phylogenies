"""
1. 通过blast结果取回hit score分数最好的基因
"""

import re
import sys
import os 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def main(indir,ending,corefa,outdir,old_dir):
	indir = os.path.abspath(indir)
	outdir = os.path.abspath(outdir)

	# 读取core fa 序列
	seq_dict = dict()
	for seq in SeqIO.parse(corefa,"fasta"):
		seq_dict[seq.id]=seq.seq

	# 遍历blast结果文件
	for file in os.listdir(indir):
		if file.endswith(ending):
			ortho_gene = dict()
			full = os.path.join(indir,file)
			
			# 读取原始序列
			rec_old = list()
			old_ortho_file = os.path.join(old_dir,re.sub(r"\.rawblastp","",file))
			for seq in SeqIO.parse(old_ortho_file,"fasta"):
				recs = SeqRecord(seq.seq,id=seq.id,description="")
				rec_old.append(recs)

			# 判断文件中最好的匹配
			with open(full) as inf:
				for lines in inf.readlines():
					line = lines.strip().split()
					species = line[2].split("@")[0]
					
					if species not in ortho_gene:
						ortho_gene[species] = {}
					
					if line[2] not in ortho_gene[species].keys():
						ortho_gene[species][line[2]] = [line[-1]]
					
					ortho_gene[species][line[2]].append(line[0])

			# 寻找每个新加物种的最优比对
			species_ortho = list()
			for k1,v1 in ortho_gene.items():
				score = 0
				for k2,v2 in v1.items():
					if len(v2) == 18 and float(v2[0]) > score:
						score = float(v2[0])
						species_ortho.append(k2)
			
			# 加入物种的单拷贝加入原始序列
			i = 0
			for id_name in species_ortho:
				ids = id_name.strip().split("@")[0]
				rec = SeqRecord(Seq(str(seq_dict[id_name])),id=ids,description="")
				rec_old.append(rec)


			# 写出新序列到新文件夹
			print("现在总序列数量：",len(rec_old))
			if len(rec_old) > 21:
				print(file)
			SeqIO.write(rec_old,os.path.join(outdir,re.sub(r"\.rawblastp","",file)),"fasta")

if __name__ == "__main__":
	if len(sys.argv) != 6:
		print("python %s indir ending corefa outdir old_ortho_dir"%sys.argv[0])
		print("indir--取回同源blast的文件夹")
		print("ending--blast结果文件后缀")
		print("corefa--makebd的需加入的物种蛋白集合")
		print("outdir--新输出的目录,不能是相同目录")
		print("old_ortho_dir--新加物种前获得的直系同源蛋白序列文件夹")
		sys.exit(0)
	
	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])