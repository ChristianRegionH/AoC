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

def solution(part):
    floor = 0
    
    for i, p in enumerate(data[0]):
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1

        if part == 2:
            if floor == -1:
                return i + 1

    return floor
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))