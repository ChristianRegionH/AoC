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
    grid = defaultdict(int)

    for line in data:
        c1, c2 = line.split(" -> ")
        x1, y1 = c1.split(",")
        x2, y2 = c2.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[(x, y)] = grid[(x, y)] + 1
        else:
            if part == 2:
                
            

    answer = len([k for k, v in grid.items() if v > 1])

    return answer

    
print("Part 1:", solution(1))
print("Part 2:", solution(2))