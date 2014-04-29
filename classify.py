#! /usr/bin/env python3
"""
Round predictions for classifications purposes

Usage:
    classify.py <input_file.txt> <output_file.txt>

"""
import sys, csv

input_file = sys.argv[1]
output_file = sys.argv[2]

lines = []
with open(input_file) as i:
    lines = i.readlines()

newlines = [str(round(float(line))) for line in lines]

with open(output_file, 'w') as o:
    writer = csv.writer(o)
    for line in newlines:
        writer.writerow(line)
