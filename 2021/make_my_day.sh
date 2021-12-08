#!/usr/bin/env bash

source .AOC_SESSION

if [ "$1" == "" ] ; then 
    day=$(find . -type d | grep day | sed -e 's/..day//' | sort -rn | head -n 1)
    day=$(expr $day + 1)
else 
    day=$1
fi

echo "Generating day $day ..."
daynum=$day
day=day$day

mkdir $day
cat day1/.nvimrc | sed -e "s/day1/$day/g" > $day/.nvimrc
touch $day/$day.py
curl --cookie "session=$SESSION_ID" -o $day/$day.input https://adventofcode.com/2021/day/$daynum/input
touch $day/$day.test

