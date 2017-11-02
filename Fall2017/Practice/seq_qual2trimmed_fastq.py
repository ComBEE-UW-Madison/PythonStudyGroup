#!/usr/bin/env python
import sys, os
from Bio import SeqIO
from Bio.SeqIO.QualityIO import PairedFastaQualIterator
import numpy as np
from optparse import OptionParser

# Takes a folder containing corresponding seq and qual files,
# and makes a single FASTQ file. Trim the two ends, and make sure
# it is not longer than 1000bp so it is acceptable for Mothur
# Author: huan.fan@wisc.edu

Usage = "seq_qual2trimmed_fastq.py seq_qual_directory -q 10, -w 6"
version = '%prog 20171010.1'
parser = OptionParser(usage = Usage, version = version)
parser.add_option("-q", dest = "q_cutoff", default = 10,
		  help = "quality score cut off, default = 10")
parser.add_option("-w", dest = "window", default = 6,
		  help = "consecutive window, default = 6")

(options, args) = parser.parse_args()

def combine(fastq_dir, basename):
    """
    Combine the seq and qual file into fastq
    """
    try:
    	fastafile = open(fastq_dir + '/' + basename + ".seq")
    	qualfile = open(fastq_dir + '/' + basename + ".qual")
    except IOError:
    	print("Either the file cannot be opened or there is no corresponding")
    	print("seq or quality file for " + basename)
    	sys.exit()
    rec_iter = PairedFastaQualIterator(fastafile,qualfile)
    SeqIO.write(rec_iter, open(fastq_dir + '/' + basename + ".fastq", "w"), "fastq")


def trim_fastq_biopython(in_file, out_file, q_cutoff=10, consec=6, id=None):
    """
    Trim a FASTQ file and write out the trimmed sequences as a FASTQ file.

    Only processes the sequence with identifer string rec.  If id
    is None, takes first sequence.
    """
    # Load in sequences using Bio.SeqIO.  We'll keep the result as a dict.
    sample = os.path.basename(in_file[:len(in_file)-len('_F.ab1.fastq')])
    with open(in_file) as f:
        seqs = SeqIO.to_dict(SeqIO.parse(f, 'fastq'))

    # Pull out the id we want
    if id is None:
        key, seq = seqs.popitem()
    else:
        try:
            seq = seqs[id]
        except KeyError:
                raise KeyError('id not found in input file')

    # Get Boolean array for good quality
    q_good = np.array(seq.letter_annotations['phred_quality']) >= q_cutoff

    # Find first set of consec good bases
    i = 0
    while i < len(q_good) - consec and not q_good[i:i+consec].all():
        i += 1

    # Find last set of consec good bases
    j = len(q_good)
    while j >= consec and not q_good[j-consec:j].all():
        j -= 1
    if j > 1000:
        j = 1000
    # Write out trimmed sequence

    with open(out_file, 'w') as f:
        seq.id = sample
        seq.description = ''
        SeqIO.write(seq[i:j], f, 'fastq')

def main(fastq_dir, q_cutoff = 10, consec = 6):
    with open(fastq_dir + '.namefile','w') as nameFile:
        for fileName in os.listdir(fastq_dir):
            if fileName[-len('.seq'):] == '.seq':
                basename = '.'.join(fileName.split(".")[:-1])
                combine(fastq_dir, basename)
                in_file = fastq_dir + '/' + basename + '.fastq'
                out_file = fastq_dir + '/trimmed_' + basename + '.fastq'
                if '_F.ab1.' in out_file:
                    nameFile.write(out_file + '\t')
                    nameFile.write(out_file.replace('_F.ab1.', '_R.ab1.') + '\n')
                trim_fastq_biopython(in_file, out_file, q_cutoff=int(q_cutoff), consec=int(consec), id=None)
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please specify the directory where the seq and qual files are.")
        sys.exit()
    elif len(sys.argv) == 2:
        sys.exit(main(sys.argv[1]))
    elif len(sys.argv) > 2:
        sys.exit(main(sys.argv[1],options.q_cutoff,options.window))
