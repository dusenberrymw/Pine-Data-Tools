#!/bin/bash
# use 'lib/timeit.sh pipeline.sh' to measure execution time
set -v  # echo the commands

lib/preprocess.py data/data.csv data/data_preprocessed.csv 1

lib/csv2pine.py data/data_preprocessed.csv data/data_pinedata.txt 1 25

lib/split.py data/data_pinedata.txt data/data_pineTrain.txt data/data_pineTest.txt 0.9 80377

# lib/automate_passes_pine.py data/data_pineTrain.txt data/data_pineTest.txt 25,30,1 50 1

pine data/data_pineTrain.txt 25,30,1 -f results/model -p 5 -np 1 -l 0.01

pine data/data_pineTest.txt _ -t -i results/model -pf results/p_raw.txt

lib/classify.py results/p_raw.txt results/p_class.txt

lib/stats.py data/data_pineTest.txt results/p_class.txt > results/stats.txt

# diff -y -W 25 data/data_pineTest.txt results/p_raw.txt
