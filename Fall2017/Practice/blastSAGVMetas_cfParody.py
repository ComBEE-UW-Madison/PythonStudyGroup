#!/usr/bin/python

import sys, os, glob, subprocess
#from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor

def usage():
	print "Usage: blastSAGVMetas.py 'path2SAGsfasta(glob)' 'metagenomes(glob)' threads(int)"
	print "Makes db and runs blastn with the following settings"

if len(sys.argv) != 4:
	usage()
	exit()

path2SAGs=sys.argv[1]
path2Metas=sys.argv[2]
threads=int(sys.argv[3])

def call_blast(params):
	SAGname, metaname = params
	SAGdb=SAGname+".db"
	outSAG=os.path.basename(os.path.splitext(SAGname)[0])
	outmeta=os.path.basename(os.path.splitext(metaname)[0])
	outname=outmeta+'-vs-'+outSAG+'.blast'
	cmd=['blastn', '-task blastn', '-db '+SAGdb, '-query '+metaname,'-out '+outname, '-outfmt 6'] # add alt blast settings here
	print ' '.join(cmd), os.getpid() #testing line, left in for log file
	os.system(' '.join(cmd)) #replace with subprocess when you figure it out
	subprocess.call(cmd)

if __name__ == '__main__':
	#p=Pool(threads)
    p = ProcessPoolExecutor(max_workers = threads)
    #with ThreadPoolExecutor(max_workers=threads) as p:

	#print path2SAGs
	SAGfiles=glob.glob(path2SAGs)
	metafiles=glob.glob(path2Metas)
	#print SAGfiles
	#all possible combos of SAGs vs Metagenomes
	inlist=[]
	for SAG in SAGfiles:
		os.system('makeblastdb -in '+SAG+' -out '+SAG+'.db'+' -dbtype nucl')
		for meta in metafiles:
			inlist.append([SAG, meta])
	#print inlist
	p.map(call_blast,inlist)
	p.close()

'''
The (approximate) size of these chunks can be specified by setting chunksize to
# a positive integer. For very long iterables, using a large value for chunksize
can significantly improve performance compared to the default size of 1. With
ThreadPoolExecutor, chunksize has no effect.
'''
# Larger than memory issue
from concurrent.futures import ProcessPoolExecutor

def sum_row(line):
    return sum([int(x) for x in line.split()])

with ProcessPoolExecutor(max_workers=4) as executor:
    with open('numbers.txt') as fh:
        for result in executor.map(sum_row,fh,chunksize = 2):
            print(result)

# Catch results
def coverage_parser(fileName):
    try:
        temp = pd.read_csv(cov_dir + '/' + fileName,
                   sep='\t',header=None,usecols=[0,1], names=['contig','position'])
        dic = {}
        for contig in temp.contig.unique():
            dic[contig] = temp[temp['contig'] == contig]['position'].tolist()
        return(dic)
    except EmptyDataError:
        print(fileName + ' is empty')

with ProcessPoolExecutor(max_workers=40) as executor:
    for fileName, dic in zip(cov_list, executor.map(coverage_parser,cov_list,
													chunksize = 1)):
        if dic:
            fly_sample = fileName.split('_')[1]
            for contig in dic:
                dic_cov[contig][fly_sample] = dic[contig]
