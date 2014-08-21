#! /usr/bin/env python3
"""
Compute RMSE from Pine validation/test and predictions files

Usage:
  rmse.py <test_file_with_correct_outputs.txt> <predictions_file.txt>

"""
import sys, csv, math

test_file = sys.argv[1]
predictions_file = sys.argv[2]

test_reader = csv.reader(open(test_file), delimiter = "|" )
p_reader = csv.reader(open(predictions_file), delimiter = "," )

squared_diffs = []
n = 0

for p_line in p_reader:
    test_line = next(test_reader)
    test_line = test_line[0].strip().split(",")

    for y, p in zip(test_line, p_line):
        diff = float(y) - float(p)
        squared_diff = diff * diff
        squared_diffs.append(squared_diff)
        n += 1
squared_diffs = sum(squared_diffs)
MSE = squared_diffs/n
RMSE = math.sqrt(MSE)

print("RMSE: {0}\n".format(RMSE))
