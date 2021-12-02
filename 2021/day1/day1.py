#!/usr/bin/env python
import sys

# --- part 1
def part_one(input_fn, depths):
    print('Part 1: ', end='')

    count = 0
    prev = 10000000000000    # haha, old C64-style thinking! :-)

    for d in depths:
        if d > prev:
            count += 1
        prev = d
    print(f'Result = {count}')


# --- part 2
def part_two(input_fn, depths):
    print('Part 2: ', end='')

    def split_into_windows(elems, wsize=3):
        for i in range(len(elems)):
            if len(elems[i:i+wsize]) == wsize:
                yield elems[i:i+wsize]

    a = list(split_into_windows(depths))
    b = list(split_into_windows(depths[1:]))

    count = 0
    for x, y in zip(a, b):
        if sum(y) > sum(x):
            count += 1
    print(f'Result = {count}')


# -- main
input_fn = sys.argv[1]
depths = []

for line in open(input_fn):
    depths.append(int(line.strip()))

part_one(input_fn, depths)
part_two(input_fn, depths)

