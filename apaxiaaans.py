#! /usr/bin/python3

import sys 

word = sys.stdin.read(1)

next_char = sys.stdin.read(1)
while next_char != '\n':
    if next_char == word[-1]:
        next_char = sys.stdin.read(1)
    else:
        word += next_char
        next_char = sys.stdin.read(1)

print(word)