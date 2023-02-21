#! /usr/env/python3

import sys
import re
import argparse


parser = argparse.ArgumentParser('Input format validator')
parser.add_argument('--min-d', type=int, default=1)
parser.add_argument('--min-m', type=int, default=-5)
parser.add_argument('--max-d', type=int, default=20)
parser.add_argument('--max-m', type=int, default=10)
args = parser.parse_args()


line = sys.stdin.readline()

assert re.match(r"[1-9][0-9]* (0|-?[1-9][0-9]*)\n", line), line

d, m = map(int, line.split())

assert args.min_d <= d <= args.max_d
assert args.min_m <= m <= args.max_m

assert sys.stdin.readline() == ""

sys.exit(42)
