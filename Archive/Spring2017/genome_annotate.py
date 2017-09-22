#! usr/bin/python

import math
import sys

# >python genomeannotate.py <Annotation_file 3-4 col_FFF.txt> <File_you_want_to_annotate_3> 

#class dictreadin():
	
a = sys.argv[1]
b = sys.argv[2]


def readict(arg):
	
	if arg == a :	    # well that was long and painful but first successful OO python I've written it must be == a not "a" , a is fileobject "a" is str
		with open(a, 'rb') as fin:
			rows = (line.split('\t') for line in fin)
			dictA = {row[0].strip():row[1:] for row in rows}   
			return dictA
	elif arg == b :
		with open(b, 'rb') as fin:
			rows = (line.split('\t') for line in fin)
			dictB = {row[0].strip():row[1:] for row in rows}
			return dictB

class annotate(): 
	#def __init__(self):
	#	self.tangerine = 5
	
	def iterating(self,dictA,dictB):
		for key in dictB:
			if key in dictA:
				Val1 = dictB[key][0] # referring to a value in a multi mapped dictionary i.e {key:[valu1, valu2]} allows for multivalue storage from data
				AnnotateF = dictA[key][0]
				Annotate2 = dictA[key][1]
				Annotate3 = dictA[key][2]				
				print key,"\t",Val1.strip(),"\t",AnnotateF.strip(),"\t",Annotate2.strip(),"\t",Annotate3.strip()

			elif key not in dictA:					
				print key,"\t",dictB[key].strip(),"\t","not in Annotate list"


if __name__ == "__main__":
	c = annotate()				# I'm making object c to be of the class annotate
	c.iterating(readict(a),readict(b))	# this line takes c which is now of the annotation class and runs the function iterating on the two dictionaries from args

	

	#print c.tangerine,"eq c.tangerine"	# example of class attribute
	#print readict(a)			# this should output the contents of sys.argv[1]













