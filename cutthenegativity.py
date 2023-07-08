#! /usr/bin/python3

import sys

res = ''
m = 0
for i, line in enumerate(sys.stdin.readlines()[1:]):
    for j, c in enumerate(line[:-1].split(" ")):
        if c != '-1':
            res += '{} {} {}\n'.format(i+1,j+1,c)
            m += 1
            
print('{}\n'.format(m) + res)