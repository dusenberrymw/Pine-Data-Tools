#!/bin/bash
# use './timeit.sh pipeline.sh' to measure execution time
set -v  # echo the commands

preprocess.py Data.csv Data_preprocessed.csv 1

csv2pine.py Data_preprocessed.csv Data_pineData.txt 1 25

split.py Data_pineData.txt Data_pineTrain.txt Data_pineTest.txt 0.9

# automate_passes_pine.py Data_pineTrain.txt Data_pineTest.txt 25,30,1 50 1

pine Data_pineTrain.txt 25,30,1 -f model -p 5 -np 1 -l 0.01

pine Data_pineTest.txt _ -t -i model -pf p_raw.txt

classify.py p_raw.txt p_class.txt

stats.py Data_pineTest.txt p_class.txt #> stats.txt

# diff -y -W 25 Data_pineTest.txt p_raw.txt
