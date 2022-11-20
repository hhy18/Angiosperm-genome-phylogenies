"""
执行后面连续几步
1. python blast_to_mcl.py all.rawblast <hit_fraction_cutoff>
2. mcl all.rawblast.hit-frac0.5.minusLogEvalue --abc -te 5 -tf 'gq(5)' -I 2 -o hit-frac0.5_I2_e5
3. mkdir <outDIR>
4.python write_fasta_files_from_mcl.py <fasta files with or without ends cut> <mcl_outfile> <minimal_taxa> <outDIR>
"""

import re
import sys
import os 

script1 = "/data/01/user102/yangya_outgroup/scripts/blast_to_mcl.py"
script2 = "/data/01/user102/yangya_outgroup/scripts/write_fasta_files_from_mcl.py"
python = "/data/00/user/user102/anaconda3/envs/python27/bin/python2.7"

def main(diamond_outdir):
	diamond_outdir = os.path.abspath(diamond_outdir)
	print("cd %s \ncat ./*rawblastp > ./all.rawblast"%diamond_outdir)
	print("{python} {script1} ./all.rawblast 0.5".format(python=python,script1=script1))
	hit_frac = os.path.join(diamond_outdir,"all.rawblast.hit-frac0.5.minusLogEvalue.interspecific")
	hit_frac_output = os.path.join(diamond_outdir,"hit-frac0.5_I1.4_e5")
	print("mcl {hit_frac} --abc -te 5 -tf 'gq(5)' -I 1.4 -o {hit_frac_output}".format(hit_frac=hit_frac,hit_frac_output=hit_frac_output))
	print("mkdir hit-frac0.5_I1.4_e5_cluster")
	print("{python} {script2} ./all.fa {hit_frac_output} 14 ./hit-frac0.5_I1.4_e5_cluster".format(python=python,script2=script2,hit_frac_output=hit_frac_output))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("注意！！！\n不能并行运行，只能sh单独运行！！！")
		print("python %s diamond_outdir \ndiamond_outdir--diamond输出文件夹"%(sys.argv[0]))
		sys.exit(0)

	main(sys.argv[1])
