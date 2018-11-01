#! /usr/bin/env python3
'''
Calculates the mean inflammation of one file based on day and/or patient
'''
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--patient', action='store_true', help='calculates based on patients')
parser.add_argument('-d', '--day', action='store_true', help='calculates based on days')
parser.add_argument('-infile', nargs='*', type=argparse.FileType('r'), default=sys.stdin, help='filename to be processed')
parser.add_argument('-outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='file to write to; defaults to stdout')

args = parser.parse_args()

def process():
    if not (args.day or args.patient):
        for line in args.infile:
            line = [int(i) for i in line.split()]
            print(np.mean(line))
    else:
        for filename in args.infile:
            print(filename.name)
            if args.day:
                axis = 0
            else:
                axis = 1
            data = np.loadtxt(filename, delimiter=',')
            print(np.mean(data, axis=axis))
        
if __name__ == '__main__':
    process()
