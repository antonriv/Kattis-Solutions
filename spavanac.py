#! /usr/bin/python3

import sys

data = sys.stdin.read()[:-1].split(" ")

h, m = int(data[0]), int(data[1])

if m < 45:
    
    if h == 0:
        h = 23
    else:
        h -= 1
    m = 60 - (45 - m)
    
else:
    m = m - 45

print(f'{h} {m}')