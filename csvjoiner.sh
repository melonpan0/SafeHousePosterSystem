#!/bin/bash

# Usage: csvjoiner.sh [inputpath] [output]

# get Index
indexfile=`find ./_site/ -name "*.csv" | sort | head -n 1`
cat ${indexfile} | head -n 1 > $2

# joiner
for file in `find ./_site/ -name "*.csv" | sort`; do
	# anything
	cat ${file} | sed "1d" >> $2
	echo "" >> $2
done
