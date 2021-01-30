#!/bin/bash

path=$1

#echo $1

function search {
	cd $@
	num_jpg=`ls |grep -i '.*jpg' | wc -l`
	num_png=`ls |grep -i '.*png' | wc -l`
	num_gif=`ls |grep -i '.*gif' | wc -l`
	num_pdf=`ls |grep -i '.*pdf' | wc -l`
	echo "$num_jpg jpg files"
	echo "$num_png png files"
	echo "$num_gif gif files"
	echo "$num_pdf pdf files"
}

search $path







