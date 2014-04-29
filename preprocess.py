#! /usr/bin/env python3
"""
Preprocess data, line by line

Usage:
    proprocess.py <input_file.csv> <output_file.csv> [<headers_present = 0>]

"""
import sys, csv, re

def process(line):
    processed_line = []
    for item in line:
        item = re.sub('^(y|yes|positive|abnormal|male|m|t)$', '1', item.strip(), flags=re.IGNORECASE)
        item = re.sub('^(n|no|negative|normal|none|female|f)$', '0', item.strip(), flags=re.IGNORECASE)
        processed_line.append(item)
    return processed_line

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
    headers_present = sys.argv[3]
except IndexError:
    headers_present = 0

i = open(input_file)
o = open(output_file, 'w')

reader = csv.reader(i)
writer = csv.writer(o)

if headers_present:
    headers = next(reader)
    new_headers = []
    for item in headers:
        item = item.strip()
        item = item.replace(" ", "_")
        item = item.replace("|", "_")
        item = item.replace(":", "_")
        new_headers.append(item)
    writer.writerow(new_headers)

for line in reader:
    processed_line = process(line)
    writer.writerow(processed_line)
