#! /usr/bin/python3

import sys

merged_str = ''.join([s.rstrip() for s in sys.stdin.readlines()])
res = ''.join(sorted(merged_str))

print(res)