import re
import sys 
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def process_seq(file,basefile):
	
	species = basefile.split(".")[0]

	my_record = list()
	for seq in SeqIO.parse(file,"fasta"):
		newid = "@".join([species,seq.id.replace(".","_")])
		rec = SeqRecord(seq.seq,id = newid,description="")
		my_record.append(rec)

	SeqIO.write(my_record,"%s/%s"%(sys.argv[2],os.path.basename(file)),"fasta")

for file in os.listdir(sys.argv[1]):
	process_seq(os.path.join(sys.argv[1],file),file)
