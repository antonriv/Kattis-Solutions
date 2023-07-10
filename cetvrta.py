#! /usr/bin/python3

import sys

x, y = [], []
for _ in range(3):
    coord = sys.stdin.readline()[:-1].split(" ")
    x += [coord[0]]
    y += [coord[1]]
    
def find_unique(lst):
    if lst[0] == lst[1]:
        return lst[2]
    elif lst[0] == lst[2]:
        return lst[1]
    else:
        return lst[0]

print(find_unique(x), find_unique(y))