import sys
import math

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

def solution(part):
    crabs = [int(x) for x in data[0].split(",")]

    min_crab = min(crabs)
    max_crab = max(crabs)

    lowest = math.inf
    # Possible positions to align
    for i in range(min_crab, max_crab + 1):
        total = 0
        for crab in crabs:
            if part == 1:
                total = total + abs(crab - i)
            elif part == 2:
                for j in range(1, abs(crab - i) + 1):
                    total = total + j
        if total < lowest:
            lowest = total

    return lowest

print("Part 1:", solution(1))
print("Part 2:", solution(2))