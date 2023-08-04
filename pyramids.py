#! /usr/bin/python3

import sys

N = int(sys.stdin.read()[:-1])

upper_bound = pow(3*N/4, 1/3)

m = int(upper_bound + 1)
while m*(2*m+1)*(2*m-1)/3 > N:
    m -= 1

print(m)