#! /usr/bin/python3

import sys

L = int(sys.stdin.readline()[:-1])
D = int(sys.stdin.readline()[:-1])
X = int(sys.stdin.readline()[:-1])

l = L % 9
d = D % 9
x = X % 9

# Min candidate for N
if x < l:
    N = L + (x - l + 9)
elif x >= l:
    N = L + (x - l)

# Max candidate for M
if x <= d:
    M = D - (d - x)
elif x > d:
    M = D - (d - x + 9)

# Function to calculate the sum of digits of a non-negative integer
def sum_digits(k):
    s = 0
    while k != 0:
        s += k % 10
        k = int(k/10)

    return s

# Find N
while sum_digits(N) != X:
    N += 9

# Find M
while sum_digits(M) != X:
    M -= 9
    
print(N)
print(M)