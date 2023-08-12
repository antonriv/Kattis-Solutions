#! /usr/bin/python3

import sys

position = 0
char = sys.stdin.read(1)

while char != '\n':
    
    if (char == ':') or (char == ';'):
        char = sys.stdin.read(1)
        position += 1
        if char == ')':
            print(position - 1)
            char = sys.stdin.read(1)
            position += 1
        elif char == '-':
            char = sys.stdin.read(1)
            position += 1
            if char == ')':
                print(position - 2)
                char = sys.stdin.read(1)
                position += 1 
    else:
        char = sys.stdin.read(1)
        position += 1 