#! /usr/bin/env python3
"""
Convert CSV file to pine format.

Usage:
  csv2pine.py <input_file> <output_file> [<headers_present = 0>]
               [<label_index = 0>]

If headers are present, set argv[3] == 1
If no labels in file, set argv[4] == -1

"""
import sys
import csv

def construct_line(label, line):
    """Build a data line using generic numbers for features"""
    # Can scale the label (target) here, and convert multiclass datasets
    #   to have label vectors.
    #   Ex: if label==4 and there are 5 possible classes,
    #       target vector = 0,0,0,1,0 (start class index at 1)

    # now build the line
    new_line = []
    new_line.append("{0} | ".format(label))
    for i, item in enumerate(line):
        if not item:  # if item == ''
            return False  # this line is missing a data point, so skip it
            #item = 0  # or just set to 0
        # Can edit specific features ('items') here

        # now convert to pine style and add to line
        new_item = "{0},".format(item)
        new_line.append(new_item)
    new_line = "".join(new_line).rstrip(",")
    new_line += "\n"
    return new_line

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    headers_present = int(sys.argv[3])
except IndexError:
    headers_present = 0
try:
    label_index = int(sys.argv[4])
except IndexError:
    label_index = 0

i = open(input_file)
o = open(output_file, 'w')

reader = csv.reader(i)

if headers_present:
    headers = next(reader)

for line in reader:
    if label_index == -1: # if no label is present
        label = ''
    else:
        label = line.pop(label_index)
    new_line = construct_line(label, line)
    if new_line:  # we may skip certain lines
        o.write(new_line)

i.close()
o.close()
