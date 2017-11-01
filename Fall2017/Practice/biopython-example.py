#! /usr/local/bin/python3

import sys
from Bio import SeqIO
import glob

def usage():
    print("Make individual .fa files for each cluster")
    print("Find genes of interest with input or HMMSearch")
    print("1. FASTA concatenated 2. MCL output 3. ./resultsDIR)

if len(sys.argv) != 4:
    usage()
    sys.exit(4)

# Dictionary match sequence ID in concatenated FASTA to one in mcl, create .fa files
def mcl_to_fasta(fasta_cat, mcl_out, outdir):
    clusterdic = {}  # key seqID, value is clusterID
    if outdir[-1] != "/": outdir += "/"
    with open(mcl_out, 'r') as mclin:
        for index, line in enumerate(mclin):
            spls = line.strip().split()
            clusterid = str(index + 1).zfill(4)
            for seqid in spls:
                clusterdic[seqid] = clusterid
    handle = open(fasta_cat, 'r')
    for record in SeqIO.parse(handle, "fasta"):
        seqid, seq = str(record.id), str(record.seq)
        try:
            clusterid = clusterdic[seqid]
            with open(outdir+"cluster"+clusterid+".fa", "a") as outfile:
                outfile.write(">"+seqid+'\n'+seq+'\n')
        except:
            pass
    handle.close()

mcl_to_fasta(fasta_cat=sys.argv[1], mcl_out=sys.argv[2], outdir=sys.argv[3])
