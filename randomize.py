#! /usr/bin/env python3
"""
Randomize lines in input file and output to output file

Usage:
  randomize.py <input_file> <output_file>

"""
import sys, random

input_file = sys.argv[1]
output_file = sys.argv[2]

lines = []
with open(input_file) as i:
    lines = i.readlines()

random.shuffle(lines)

with open(output_file, 'w') as o:
    o.writelines(lines)


