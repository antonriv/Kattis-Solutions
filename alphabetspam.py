#! /usr/bin/python3

import sys

underscore, lower, upper, symbol = [0,0,0,0]
c = sys.stdin.read(1)

while c != '\n':
    
    if c == '_':
        underscore += 1
    elif c in 'abcdefghijklmnopqrstuvwxyz':
        lower += 1
    elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        upper += 1
    else:
        symbol += 1
    
    c = sys.stdin.read(1)

tot = underscore + lower + upper + symbol

print(f'{underscore/tot}\n{lower/tot}\n{upper/tot}\n{symbol/tot}')