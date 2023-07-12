#! /usr/bin/python3

import sys

lst = []
for index in range(1,6):
    string = sys.stdin.readline()
    if 'FBI' in string:
        lst += [str(index)]

if lst == []:
    print("HE GOT AWAY!")
else:
    res = " ".join(lst)
    print(res)