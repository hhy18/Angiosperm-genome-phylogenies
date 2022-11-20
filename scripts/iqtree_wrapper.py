"""
Input: a dir of cleaned alignments in fasta format and end with "-cln"
Output: trees estimated by raxml
"""

import os,sys
import subprocess
from seq import read_fasta_file

def iqtree_bs(DIR,cleaned,seqtype,num_cores=10,replicates=100):
	assert cleaned.endswith(".aln-cln"),\
		"raxml infile "+cleaned+" not ends with .aln-cln"
	assert seqtype == "aa" or seqtype == "dna","Input data type: dna or aa"
	assert len(read_fasta_file(DIR+cleaned)) >= 4,\
		"less than 4 sequences in "+DIR+cleaned
	clusterID = cleaned.split(".")[0]
	
	tree = DIR+clusterID+".iqtree_bs.tre"
	raw_tree = clusterID + ".treefile"
	# raw_tree = "RAxML_bipartitions."+cleaned
	if not os.path.exists(tree):
		infasta = cleaned if DIR == "./" else DIR+cleaned
		cmd = ["iqtree2", "-s", infasta, "-m", "MFP", "-B", "1000", "-bnni", "-redo", "--keep-ident", "-pre", clusterID, "-T", str(num_cores) ]
		print " ".join(cmd)
		
		p = subprocess.call(cmd,shell=False)
		assert p == 0,"Error iqtree"
		
		
		os.rename(raw_tree,tree)
		os.remove(clusterID+".bionj")
		os.remove(clusterID+".ckp.gz")
		os.remove(clusterID+".mldist")
		# os.remove(clusterID+".model.gz")
		os.remove(clusterID+".ufboot")
		os.remove(clusterID+".contree")
		os.remove(clusterID+".iqtree")
		os.remove(clusterID+".splits.nex")
			

	return tree

def main(DIR,num_cores,seqtype):
	if DIR[-1] != "/": DIR += "/"
	filecount = 0
	for i in os.listdir(DIR):
		if i.endswith(".aln-cln"):
			filecount += 1
			iqtree_bs(DIR,i,num_cores,seqtype)

	assert filecount > 0, "No file end with .aln-cln found in "+DIR
	
if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "python raxml_bs_wrapper.py DIR number_cores dna/aa"
		print "make sure that the executable is named 'iqtree' and is in the path"
		sys.exit(0)

	DIR,num_cores,seqtype = sys.argv[1:]
	main(DIR,num_cores,seqtype)

