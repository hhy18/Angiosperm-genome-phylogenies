"""
1. 运行此步骤之前，需要在目录2.diamond执行 cat *.cdhit > all.fa; diamond makedb --in all.fa -d diamond 
2. 创建diamond sh 文件
3. 此处需要修改-d 参数建库文件位置
4. 目标序列最大匹配数量设置为 3000
"""

import re
import sys
import os 
import subprocess

def sh_diamond(indir,ending,outdir,db):
	indir = os.path.abspath(indir)
	outdir = os.path.abspath(outdir)
	db = os.path.abspath(db)
	db = re.sub(".dmnd","", db)

	for file in os.listdir(indir):
		if file.endswith(ending):
			fullfile = os.path.abspath(os.path.join(indir,file))
			outfile = os.path.abspath(os.path.join(outdir,file))

			print("blastn -db {all_fa} -query {fullfile} -evalue 10 -num_threads 5  -out {outfile}.rawblast -max_target_seqs 1000 \
-outfmt '6 qseqid qlen sseqid slen frames pident nident length mismatch gapopen qstart qend sstart send evalue bitscore'".format(all_fa=db,fullfile=fullfile,outfile=outfile))

if __name__ == "__main__":
	if len(sys.argv) != 5:
		print("需要提前cat *.cdhit > all.fa; diamond makedb 数据库")
		print("python %s indir ending outdir makedb\nindir--蛋白cdhit去冗余文件夹 \nending--一般为cdhit \noutdir--diamond输出文件夹"%(sys.argv[0]))
		print("makedb--建立索引文件位置")
		sys.exit(0)

	indir,ending,outdir,db = sys.argv[1:]
	sh_diamond(indir,ending,outdir,db)
