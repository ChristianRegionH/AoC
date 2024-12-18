import sys
from collections import defaultdict
import re

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

machines = []
machine = defaultdict(tuple)
for line in data:
    if line.startswith("Button A"):
        output = re.findall(r": X\+(\d+), Y\+(\d+)", line)
        machine["A"] = tuple(map(int, output[0]))
    elif line.startswith("Button B"):
        output = re.findall(r": X\+(\d+), Y\+(\d+)", line)
        machine["B"] = tuple(map(int, output[0]))
    elif line.startswith("Prize"):
        output = re.findall(r": X\=(\d+), Y\=(\d+)", line)
        machine["Prize"] = tuple(map(int, output[0]))
        machines.append(machine)
    else:
        machine = defaultdict(tuple)

# A = 3 tokens
# B = 1 tokens
ans1 = 0
for machine in machines:
    target = machine["Prize"]
    combinations = []
    while True:
        for ai in range(100):
            if ai * machine['A'][0] > target[0]:
                break
            for bi in range(100):
                if bi * machine['B'][0] > target[0]:
                    break
                test = (ai * machine['A'][0] + bi * machine['B'][0], ai * machine['A'][1] + bi * machine['B'][1])
                if test == target:
                    combinations.append((ai, bi))
        break 
    
    ans = 0
    for c in combinations:
        if ans == 0:
            ans = c[0] * 3 + c[1] * 1
        else:
            if c[0] * 3 + c[1] * 1 < ans:
                ans = c[0] * 3 + c[1] * 1

    ans1 += ans

print(ans1)