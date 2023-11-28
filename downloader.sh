#!/bin/bash
# [usage] downloader.sh [list.csv]

# make directory
mkdir -p ./_site

# download file
while read LINE || [ -n "${LINE}" ]
do
	# Exclude Empty line & Commentout
	[ -z "${LINE}" ] && continue
	[ "${LINE:0:1}" == "#" ] && continue

	FILENAME=$(echo ${LINE} | cut -d , -f 1 | sed -e 's/"//g')
	URL=$(echo ${LINE} | cut -d , -f 2 | sed -e 's/"//g')

	wget ${URL} -O ./_site/${FILENAME}
done < ${1}
