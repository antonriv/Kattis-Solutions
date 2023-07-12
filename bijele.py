#! /usr/bin/python3

import sys

data = sys.stdin.read()[:-1].split(" ")
lst = list(map(int, data))

pieces = [1,1,2,2,2,8]

res = " ".join([str(pieces[i] - lst[i]) for i in range(6)])
print(res)