#! /usr/bin/python3

import sys

n, k = [int(i) for i in sys.stdin.readline()[:-1].split(" ")]

tot = 0
for _ in range(k):
    tot += int(sys.stdin.readline()[:-1])

lowest = (-3*(n-k) + tot) / n
highest = (3*(n-k) + tot) / n

print(f'{lowest} {highest}')