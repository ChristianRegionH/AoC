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
    pos = ((0, 0), (0, 0))
    houses = defaultdict(int)

    if part == 1:
        houses[pos[0]] += 1
    elif part == 2:
        for p in pos:
            houses[p] += 1

    dirs = {
        (0, "^"): ((0, 1),  (0, 0)),
        (0, "v"): ((0, -1), (0, 0)),
        (0, ">"): ((1, 0),  (0, 0)),
        (0, "<"): ((-1, 0), (0, 0)),
        (1, "^"): ((0, 0),  (0, 1)),
        (1, "v"): ((0, 0), (0, -1)),
        (1, ">"): ((0, 0),  (1, 0)),
        (1, "<"): ((0, 0), (-1, 0)),
    }

    for i, dir in enumerate(data[0]):
        which_santa = 0 if part == 1 else i % 2
        direction = dirs[(which_santa, dir)]
        pos = ((pos[0][0] + direction[0][0], pos[0][1] + direction[0][1]), (pos[1][0] + direction[1][0], pos[1][1] + direction[1][1]))
        
        if part == 1:
            houses[pos[0]] += 1
        elif part == 2:
            for p in pos:
                houses[p] += 1

    answer = len(houses)

    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))