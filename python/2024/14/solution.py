import sys
from collections import defaultdict
import re
import os

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

WIDE = 101
TALL = 103

robots = defaultdict(tuple)
for r in data:
    pos, velocity = r.split(" ")
    x, y = list(map(int, pos[2:].split(",")))
    vx, vy = list(map(int, velocity[2:].split(",")))
    robots[((x, y), (vx, vy))] = (x, y)    

i = 1
while True:
    for k, v in robots.items():
        new_x = v[0] + k[1][0]
        new_y = v[1] + k[1][1]
        if new_x < 0:
            new_x = WIDE + new_x
        elif new_x >= WIDE:
            new_x = new_x - WIDE
        if new_y < 0:
            new_y = TALL + new_y
        elif new_y >= TALL:
            new_y = new_y - TALL
        robots[k] = (new_x, new_y)

    if i == 100:
        Q1, Q2, Q3, Q4 = 0, 0, 0, 0
        for k, v in robots.items():
            if v[0] < WIDE // 2 and v[1] < TALL // 2:
                Q1 += 1
            elif v[0] < WIDE // 2 and v[1] > TALL // 2:
                Q3 += 1
            elif v[0] > WIDE // 2 and v[1] < TALL // 2:
                Q2 += 1
            elif v[0] > WIDE // 2 and v[1] > TALL // 2:
                Q4 += 1
        print(Q1, Q2, Q3, Q4)
        print(Q1 * Q2 * Q3 * Q4)

    ndict = defaultdict(int)

    for v in robots.values():
        ndict[v] += 1

    if len(ndict) == len([n for n in ndict.values() if n == 3]):
        print("ONLY 3s")
        print(i)
        print()
        break

    if i % 10000 == 0:
        print("i", i)

    i += 1