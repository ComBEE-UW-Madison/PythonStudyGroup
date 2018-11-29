#! /usr/bin/env python3
'''
Calculates the mean inflammation of one file based on day and/or patient
'''
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--day', type='store_true', help='calculates based on days')
parser.add_argument('-p', '--patient', type='store_true', help='calculates based on patients')
parser.add_argument('-f', '--file', type=file, nargs='*', default=sys.stdin, help='filename to be processed')
args = parser.parse_args()

#print(args)
assert args.day or args.patient, 'you must have either patient or day option enabled'

if args.day:
    axis=0
else:
    axis=1

def process():
    if args.file:
        with open(args.file, 'r') as f:
            data = np.loadtxt(filename, delimiter=',')
            for m in np.mean(data, axis=axis):
                print(m)
    else:
        data = sys.stdin.split()
        print(data)


if __name__ == '__main__':
    process()
