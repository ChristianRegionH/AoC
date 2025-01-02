import copy
import sys
from collections import defaultdict

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

designs = []
for line in data:
    if "," in line:
        towels = line.split(", ")
    elif len(line) > 0:
        designs.append(line)

POSSIBLE = 0
COMBINATIONS = 0
for design in designs:
    print(design)
    pos = False
    candidates = ['']
    while True:
        candidate = candidates.pop()
        if candidate == design:
            pos = True
            COMBINATIONS += 1
            break
        for towel in towels:
            if design[len(candidate):].startswith(towel):
                candidates.append(candidate + towel)
        if not candidates:
            break
    if pos:
        POSSIBLE += 1

print(POSSIBLE)
print(COMBINATIONS)