#!/usr/bin/env python3

d, m = map(int, input().split())

if d == 1:
    print("crit fail!")
elif d == 20:
    print("nat 20")
else:
    print(d + m)
