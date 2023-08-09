#! /usr/bin/python3

import sys

probability = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':5, '9':4, '10':3, '11':2, '12': 1}

n = int(sys.stdin.readline()[:-1])
hotels = sys.stdin.readline()[:-1].split(" ")

p = 0
for h in hotels:
    p += probability[h]

print(p/36)