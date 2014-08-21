#!/bin/bash
#
# ./timeit.sh script.sh
starttime=$(date +"%s")
$1 # run script
endtime=$(date +"%s")
exectime=$(($endtime-$starttime))
echo "$(($exectime / 60))m $(($exectime % 60))s elapsed"
