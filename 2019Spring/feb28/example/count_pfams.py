#!/usr/bin/env python3
"""
Program that counts the unique number of single-copy marker genes in a cluster
and writes the single-copy marker gene counts to a tab-delimited file.
Input: clusterName clusterColumn autometaClusteringOutput.tsv outputName.tsv [expectedNumberMarkers]
Returns: outputName.tsv, prints(observed/expected)
"""

__author__ = 'Evan R. Rees'

import sys
import os

import pandas as pd

######:Handling Input:#######
usage = 'count_pfams.py <cluster_name> <cluster_column> </path/to/recursive_dbscan_output.tab> </path/to/outfile> [<expected_num>]'
if not len(sys.argv) >= 4:
    exit(usage)

cluster_name = sys.argv[1]
cluster_col = sys.argv[2]
assert type(cluster_name) == str, 'cluster_name must be a string'
infpath = os.path.abspath(sys.argv[3])
############################
# Reading table into pandas dataframe
df = pd.read_csv(infpath, index_col=cluster_col, sep='\t')
df = df[df.index == cluster_name]
# Use python debugger to see what the dataframe looks like...
# Uncomment the line below and rerun the program. You may type df to see the obj
# You can exit the debugger by typing q.
# You may step through the program in the debugger with n and s if you want to
# Follow each method or function. (I recommend using 'n' here...)
# import pdb; pdb.set_trace()

# Returns True/False for contigs that do/dont contain single-copy marker genes
ctgs_with_pfams = df.single_copy_PFAMs.notnull()
# Retrieve the contigs using the boolean array from above
df = df[ctgs_with_pfams]
# Retrieve a list of each contigs string of single-copy marker genes
pfams_nested = df.single_copy_PFAMs.tolist()
# Split the csv string into a list of single-copy marker genes and append to a
# list for each contig with a string of single-copy marker genes
pfams = [pfam for p in pfams_nested for pfam in p.split(',')]


##### Output file handling ######
outfpath = os.path.abspath(sys.argv[4])
outfile = open(outfpath, 'w')
header = 'pfam\tnum_copies\n'
outfile.write(header)
#################################

#Iterate through the list as a set to retrieve the unique single-copy markers
for pfam in set(pfams):
    # By employing count on pfams below.. This is accessing the list...
    # so we will find redundancy if any occur as multiple copies.
    num_copies = str(pfams.count(pfam))
    # Place this information in a line that is tab-delimited
    line = '\t'.join([pfam,num_copies])
    # print(line)
    # Write the line to the output file.
    outfile.write(line+'\n')
# Tell user full path where file was written.
print('Written: {}'.format(outfpath))

# Exception handling for last optional input argument.
try:
    expected=int(sys.argv[5])
except IndexError as e:
    print('Assuming expected_num as 139')
    expected=139
except ValueError as e:
    print('Must provide an integer for expected number of marker genes')
    exit(usage)

# Information on what is expected. Notice we can determine the n unique markers
# with set() and len() of the list of single-copy markers in the cluster.
print('({obs}/{exp})\t(Observed/Expected)'.format(obs=len(set(pfams)),exp=expected))
# QED
