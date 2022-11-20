"""
修改文件名，适用于yangya建树流程

1. 修改文件名字，不能包含空格等其他特殊字符，可以包含_
2. 修改序列id,使得species@id
3. 检查新生成物种名，存档检查
hhy:20210420
"""

import re
import sys 
import os 
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def get_species_name(indir,ending,outdir,outending):
	species_name_list = list()

	for file in os.listdir(indir):
		rec_list = list()
		
		# 处理物种名
		if file.endswith(ending):
			species_name = re.sub(ending,"",file)
			species_name = re.sub(r"[^a-zA-Z0-9]","_",species_name)
			species_name_list.append(species_name.strip())

		# 合并新序列名
		for seq_record in SeqIO.parse(os.path.join(indir,file),"fasta"):
			new_seqid = "@".join([species_name.strip(),seq_record.id])
			new_seqid = re.sub(r"[^a-zA-Z0-9@]","_",new_seqid)
			assert re.match("^[a-zA-Z0-9_@]+$",new_seqid), "%s,id 格式错误"%(new_seqid)
			
			# 处理序列中的不统一的终止密码子
			new_seq = re.sub(r"\.","*",str(seq_record.seq))
			rec = SeqRecord(Seq(new_seq),id=new_seqid,description="")
			rec_list.append(rec)
		
		SeqIO.write(rec_list,os.path.join(outdir,species_name+outending),"fasta")

	with open("species_list.txt","w") as ouf:
		ouf.writelines("\n".join(species_name_list))

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print("python %s indir infile-ending outdir outfile-ending"%(sys.argv[0]))
		print("indir--初始文件夹")
		print("file-ending--文件后缀到物种名")
		print("outdir--输出文件夹")
		print("outfile-ending -- 输出文件后缀（区别处理cds和pep, _cds_fa/_protein_fa")
		sys.exit(0)
	get_species_name(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])



