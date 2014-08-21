#! /usr/bin/env python3
"""
Run Pine on training data to learn, then test on test data, and
    finally compute error

Usage:
    run_pine.py [-h] [-p PASSES] [-m MODEL_FILE]
                [-pred PREDICTIONS_FILE] [-other OTHER]
                train_file test_file network_layout

"""
import sys, os, argparse

parser = argparse.ArgumentParser(description='Run VW training & testing')
parser.add_argument('train_file', type=argparse.FileType('r'), help='a Pine training file')
parser.add_argument('test_file', type=argparse.FileType('r'), help='a Pine testing file')
parser.add_argument('network_layout')
parser.add_argument('-p', '--passes', type=int, default=1)
parser.add_argument('-m', '--model_file', default='model')
parser.add_argument('-pred', '--predictions_file', default='p.txt')
parser.add_argument('-other', default="", nargs='+', help='Other VW arguments')

args = parser.parse_args() # get args from command line

try:
    args.other = args.other[0].split(",")
    for i, item in enumerate(args.other):
        args.other[i] = args.other[i]+" "
except IndexError:
    args.other = [""]

cmd = ['pine ', args.train_file.name+" ", args.network_layout+" ",
       "-f "+str(args.model_file)+" ", "-p "+str(args.passes)+" "] + args.other
cmd = "".join(cmd)
print(cmd)
os.system(cmd)

print()

cmd = ['pine ', '-t ', args.test_file.name+" ", args.network_layout+" ",
       "-i "+str(args.model_file)+" ",
       "-pf "+str(args.predictions_file)+" "] + args.other
cmd = "".join(cmd)
print(cmd)
os.system(cmd)

print()

cmd = ("./rmse.py {0} {1}".format(args.test_file.name, args.predictions_file))
# cmd = ("./rmse.py {0} {1}; diff -y -W 25 {0} {1}".
#     format(args.test_file.name, args.predictions_file))
print(cmd)
os.system(cmd)
print()
