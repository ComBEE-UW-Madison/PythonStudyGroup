from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator

 def getTopUndetReads(self, ct):
     '''
         Retrieves most frequent undetermined reads
     '''
     indxCnt = {}
     for f_in in self.getUndetFilesFromCt(ct):
         with gzip.open(f_in) as f:
             for rec in FastqGeneralIterator(f):
                 # 1st line in rec:
                 # @J00168:.... 2:N:0:indx
                 indx = rec[0].split(':')[-1]
                 try:
                     indxCnt[indx] += 1
                 except KeyError:
                     indxCnt[indx] = 1
     counts = sorted(indxCnt.items(), key=lambda x: x[1], reverse=True)
     stop_criteria_met = False
     i = 0
     while not stop_criteria_met:
         stop_criteria_met = True
         indx = counts[i][0]
         for el in indx:
             if el != indx[0]:
                 stop_criteria_met = False
         i = i + 1
     return counts[:i + 1]
