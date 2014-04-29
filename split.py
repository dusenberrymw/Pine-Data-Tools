#! /usr/bin/env python3
"""
Split file lines randomly into two output files.

Usage:
  split.py <input_file> <output_file_1> <output_file_2>
            [<probability_of_writing_to_the_first_file = 0.9>]
            [random_seed = random.randint()]
            [<headers_present = 0>] [<copy_headers = 0>]

Note: use -1 for the random seed to assign a random value for the seed. This
    is useful if there are headers present, but the seed has not been chosen

"""
import csv
import sys
import random

input_file = sys.argv[1]
output_file1 = sys.argv[2]
output_file2 = sys.argv[3]
try:
    P = float(sys.argv[4])
except IndexError:
    P = 0.9
try:
    seed = float(sys.argv[5])
    if seed == -1: # skip seed
        seed = random.randint(1, 100000)
except IndexError:
    seed = random.randint(1, 100000)
try:
    headers_present = int(sys.argv[6])
except IndexError:
    headers_present = 0
try:
    copy_headers = int(sys.argv[7])
except IndexError:
    copy_headers = 0

print("P = {0}".format(P))
print("Random seed = {0}".format(seed))

i = open(input_file)
o1 = open(output_file1, 'w')
o2 = open(output_file2, 'w')

reader = csv.reader(i)
writer1 = csv.writer(o1)
writer2 = csv.writer(o2)

if headers_present:
    headers = next(reader)
if copy_headers:
    writer1.writerow(headers)
    writer2.writerow(headers)

random.seed(seed)
for line in reader:
    r = random.random()
    if r > P:
        writer2.writerow(line)
    else:
        writer1.writerow(line)

i.close()
o1.close()
o2.close()
