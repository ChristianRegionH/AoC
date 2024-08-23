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
    total = 0
    for pairs in data:
        p1, p2 = pairs.split(",")
        p1 = [int(x) for x in p1.split("-")]
        p2 = [int(x) for x in p2.split("-")]

        if part == 1:
            if (p1[0] >= p2[0] and p1[1] <= p2[1]) or (p2[0] >= p1[0] and p2[1] <= p1[1]):
                total += 1
        elif part == 2:
            if (p2[0] <= p1[0] <= p2[1] or p2[0] <= p1[1] <= p2[1]) or (p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]):
                total += 1
                
    return total

print("Part 1:", solution(1))
print("Part 2:", solution(2))