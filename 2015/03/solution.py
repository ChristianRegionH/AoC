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
    pos = (0, 0)
    houses = defaultdict(int)

    houses[pos] += 1

    for dir in data[0]:
        if dir == "^":
            pos = (pos[0], pos[1] + 1)
        elif dir == "v":
            pos = (pos[0], pos[1] - 1)
        elif dir == ">":
            pos = (pos[0] + 1, pos[1])
        elif dir == "<":
            pos = (pos[0] - 1, pos[1])
        houses[pos] += 1

    answer = len(houses)

    return answer
    

print("Part 1:", solution(1))
#print("Part 2:", solution(2))