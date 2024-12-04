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
    grid = defaultdict(str)
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            grid[(x, y)] = char
    
    ans = 0
    for key, value in grid.items():
        if part == 1:
            if value == 'X':
                for dir in [(1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1)]:
                    word = 'X'
                    for i in range(1, 4):
                        coords = (key[0] + dir[0] * i, key[1] + dir[1] * i)
                        if coords in grid.keys():
                            word = word + grid[coords]
                    if word == 'XMAS':
                        ans += 1
        elif part == 2:
            if value == 'A':
                word = 'A'
                for dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    coords = (key[0] + dir[0], key[1] + dir[1])
                    if coords in grid.keys():
                        word = word + grid[coords]
                if word in ['AMMSS', 'ASSMM', 'AMSMS', 'ASMSM']:
                    ans += 1

    return ans  

print("Part 1:", solution(1))
print("Part 2:", solution(2))