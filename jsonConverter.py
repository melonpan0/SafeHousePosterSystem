#!/usr/bin/env python3
import json
import re
import argparse

# parser設定
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="PATH of Input CSV File", type=str)
parser.add_argument("-o", help="PATH of Output JSON File", type=str)

args = parser.parse_args()
csvfile = args.i
jsonfile = args.o


with open(csvfile, mode="r", encoding="utf-8") as f:
	fp = open(csvfile)

fp = open(csvfile)
lines = fp.readlines()

# 前処理
photolist = []
for line in lines:
	photolist.append(re.sub("[# \n]", "", line).split(","))


photodict = {}

for list in photolist[1:(1 + len(photolist))]:
	if len(list) < 3:
			continue
	tmp = {list[0]:{photolist[0][1]:int(list[1]), photolist[0][2]:list[2], photolist[0][3]:list[3]}}
	photodict.update(tmp)

with open(jsonfile, mode="w", encoding="utf-8") as f:
	json.dump(photodict, f, ensure_ascii=False, indent="\t")

