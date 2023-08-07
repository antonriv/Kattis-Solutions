#! /usr/bin/python3

import sys

N = int(sys.stdin.readline()[:-1])
M = int(sys.stdin.readline()[:-1])

k = M // N
r = M % N

for _ in range(r):
    print('*'*(k+1))
for _ in range(N-r):
    print('*'*k)