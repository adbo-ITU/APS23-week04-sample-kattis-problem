import random
import argparse


parser = argparse.ArgumentParser('Random input generator')
# By convention, the last argv argument is a random seed. So we just have a positional argument for this.
parser.add_argument('seed', type=int)
parser.add_argument('--min-d', type=int, default=1)
parser.add_argument('--min-m', type=int, default=-5)
parser.add_argument('--max-d', type=int, default=20)
parser.add_argument('--max-m', type=int, default=10)
parser.add_argument('--exact-d', type=int)
parser.add_argument('--exact-m', type=int)
args = parser.parse_args()

random.seed(args.seed)

d = random.randint(args.min_d, args.max_d) if args.exact_d is None else args.exact_d
m = random.randint(args.min_m, args.max_m) if args.exact_m is None else args.exact_m

print(d, m)
