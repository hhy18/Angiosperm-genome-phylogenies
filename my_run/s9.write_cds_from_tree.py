"""
1. 从去除旁系同源的树中提取cds fasta序列
"""

import re
import os 
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def main(trefile):
	fasta_name = re.sub("tre","fa",os.path.basename(trefile))
	tre_seq = list()
	
	with open(trefile) as inf:
		content = inf.readline()
		seqid = re.findall(r"(\w+@\w+):",content)
		print(len(seqid))
		for i in seqid:
			newid = i.strip().split("@")[0]
			rec = SeqRecord(seq_dict[i],id=newid,description="")
			tre_seq.append(rec)
	
	SeqIO.write(tre_seq,os.path.join(sys.argv[3],fasta_name),"fasta")



if __name__ == "__main__":
	
	if len(sys.argv) != 4:
		print("python %s ortholog_dir all_cds cds_fasta\northolog_dir--MO直系同源树文件夹\nall_cds--all.cds.fa文件路径\ncds_fasta--树中写出cds序列文件夹"%sys.argv[0])
		sys.exit(0)
	
	seq_dict = dict()
	for seq in SeqIO.parse(sys.argv[2],"fasta"):
		seq_dict[seq.id] = seq.seq
	
	for file in os.listdir(sys.argv[1]):
		full = os.path.join(sys.argv[1],file)
		if full.endswith("tre"):
			main(full)