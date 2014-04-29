#! /usr/bin/env python3
"""
Automate the number of passes for pine.
Used to determine an ideal number of passes

Usage:
  automate_passes_pine.py <train_file> <test_file> <network_layout>
                          <max_passes> [<verbose=0>] [<other_args>]

"""
import sys, subprocess, re

train_file = sys.argv[1]
test_file = sys.argv[2]
network_layout = sys.argv[3]
max_passes = int(sys.argv[4])
try:
    verbose = int(sys.argv[5])
except IndexError:
    verbose = 0
other = ""
if len(sys.argv) > 6:
    for i in range(6, len(sys.argv)):
        other += sys.argv[i] + " "
other = other.strip().split()

p = re.compile("RMSE: (\d+[.]\d+)")

best_passes = -1
best_rmse = float("inf")

model_file = "model"
model_string = "-f="+model_file

for i in range(max_passes):
    cmd = ['pine', train_file, network_layout, model_string,
           "-p 1"] + other
    ret = subprocess.check_output(cmd, universal_newlines=True)
    cmd = ['pine', '-t', test_file, network_layout, "-i="+model_file,
          "-pf=p.txt"] + other
    ret = subprocess.check_output(cmd, universal_newlines=True)

    cmd = ['./rmse.py', test_file, 'p.txt']
    ret = subprocess.check_output(cmd, universal_newlines=True)
    if verbose:
        print("Pass: {0} -> RMSE: {1}".format(i+1,
              p.search(ret).group(1)))
    rmse = float(p.search(ret).group(1))  # get the RMSE as a float
    if rmse < best_rmse:
        best_rmse = rmse
        best_passes = i+1
    # for the next iterations, just train once more over the saved model
    model_string = "-i="+model_file

print("Optimal passes: {0}".format(best_passes))
print("RMSE: {0}".format(best_rmse))
