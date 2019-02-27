#!/usr/bin/env python3


__author__ = 'Evan R. Rees'

import sys
import os

import pandas as pd

usage = 'count_pfams.py <cluster_name> <cluster_column> </path/to/recursive_dbscan_output.tab> </path/to/outfile> [<expected_num>]'
if not len(sys.argv) >= 4:
    exit(usage)

cluster_name = sys.argv[1]
cluster_col = sys.argv[2]
assert type(cluster_name) == str, 'cluster_name must be a string'
infpath = os.path.abspath(sys.argv[3])
df = pd.read_csv(infpath, index_col=cluster_col, sep='\t')
df = df[df.index == cluster_name]
ctgs_with_pfams = df.single_copy_PFAMs.notnull()
df = df[ctgs_with_pfams]
pfams_nested = df.single_copy_PFAMs.tolist()
pfams = [pfam for p in pfams_nested for pfam in p.split(',')]

outfpath = os.path.abspath(sys.argv[4])
outfile = open(outfpath, 'w')
header = 'pfam\tnum_copies\n'
outfile.write(header)

for pfam in set(pfams):
    num_copies = str(pfams.count(pfam))
    line = '\t'.join([pfam,num_copies])
    # print(line)
    outfile.write(line+'\n')

print('Written: {}'.format(outfpath))

try:
    expected=sys.argv[5]
    assert type(expected) == int, 'expected_num must be an int'
except IndexError as e:
    print('Assuming expected_num as 139')
    expected=139

print('({obs}/{exp})\t(Observed/Expected)'.format(obs=len(set(pfams)),exp=expected))
