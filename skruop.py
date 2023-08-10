#! /usr/bin/python3

import sys

n = int(sys.stdin.readline()[:-1])
volume = 7

for _ in range(n):
    indicator = sys.stdin.readline()[-3:-2]
    
    if (indicator == 'd') and (volume != 0):
        volume -= 1
    if (indicator == 'p') and (volume != 10):
        volume += 1

print(volume)