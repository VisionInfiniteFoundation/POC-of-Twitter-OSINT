#!/bin/sh
python3.4 1.twtsearch.py
sleep 15
while true
do
	python3.4 2twttalks.py
	sleep 15
	python3.4 3.twtFollowers.py
	sleep 15
done
