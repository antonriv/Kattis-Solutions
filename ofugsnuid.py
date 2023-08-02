#! /usr/bin/python3

import sys

N = int(sys.stdin.readline()[:-1])
lst = [sys.stdin.readline()[:-1] for _ in range(N)]

for i in range(1,N+1):
    print(lst[-i])