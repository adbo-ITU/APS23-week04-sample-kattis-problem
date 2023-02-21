#! /usr/env/python3

import sys
import re

line = sys.stdin.readline()

assert re.match(r"[1-9][0-9]* (0|-?[1-9][0-9]*)\n", line), line

d, m = map(int, line.split())

assert 1 <= d <= 20
assert -5 <= m <= 10

assert sys.stdin.readline() == ""

sys.exit(42)
