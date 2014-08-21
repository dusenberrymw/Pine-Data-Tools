#! /usr/bin/env python3
"""
Compute accuracy from validation/test and predictions files:

    accuracy = (number correct predictions)/(total number cases)

Usage:
  stats.py <test_file_with_correct_outputs.txt> <predictions_file.txt>

"""
import sys, csv, math

test_file = sys.argv[1]
predictions_file = sys.argv[2]

test_reader = csv.reader(open(test_file), delimiter = " " )
p_reader = csv.reader(open(predictions_file), delimiter = "\n" )

correct = 0
n = 0
pos = 0
neg = 0
tp = 0
fp = 0
tn = 0
fn = 0

for p_line in p_reader:
    test_line = next(test_reader)
    n += 1
    y = float(test_line[0]) # correct answer
    p = float(p_line[0]) # predicted answer

    if y == 1: # pos test case
        pos += 1
        if p == y:
            correct += 1
            tp += 1
        else: # p == -1
            fn += 1
    elif y == 0 or y == -1: # neg test case
        neg += 1
        if p == y:
            correct += 1
            tn += 1
        else: # p == 1
            fp += 1

accuracy = correct/n
try:
    sensitivity = tp/(tp+fn)
except ZeroDivisionError:
    sensitivity = "NaN"
try:
    specificity = tn/(tn+fp)
except ZeroDivisionError:
    specificity = "NaN"
try:
    ppv = tp/(tp+fp)
except ZeroDivisionError:
    ppv = "NaN"
try:
    npv = tn/(tn+fn)
except ZeroDivisionError:
    npv = "NaN"

print("Total cases: {0}".format(n))
print("--Total positive cases: {0}".format(pos))
print("--Total negative cases: {0}".format(neg))
print("Correct predictions: {0}".format(correct))
print("---")
print("Accuracy: {0}".format(accuracy))
print("Sensitivity: {0}".format(sensitivity))
print("Specificity: {0}".format(specificity))
print("PPV: {0}".format(ppv))
print("NPV: {0}".format(npv))
print()
