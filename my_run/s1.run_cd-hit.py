"""
0. cd-hit -i taxonID.fa -o taxonID.fa.cdhit -c 0.995 -n 5 -T <num_cores>
1. 创建cd-hit运行文件
"""
import re
import sys 
import os 

def sh_cdhit(indir,outdir):
    indir = os.path.abspath(indir)
    outdir = os.path.abspath(outdir)


    for file in os.listdir(indir):
        fullfile = os.path.join(indir,file)
        print("cd-hit-est -i %s -o %s/%s.cdhit -c 0.99 -n 10 -r 0 -T %d"%(fullfile,outdir,file,10))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python %s indir outdir\nindir -- 包含cds序列文件的文件夹\noutdir -- cd-hit输出文件夹"%(sys.argv[0]))
        sys.exit(0)
    sh_cdhit(sys.argv[1],sys.argv[2])
