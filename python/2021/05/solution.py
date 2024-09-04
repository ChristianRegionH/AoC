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
        c1 = (int(c1.split(",")[0]), int(c1.split(",")[1]))
        c2 = (int(c2.split(",")[0]), int(c2.split(",")[1]))

        line_len = max(abs(c1[0] - c2[0]), abs(c1[1] - c2[1])) + 1

        for i in range(line_len):
            x_movement = (1 if c2[0] > c1[0] else -1) * (1 if c2[0] != c1[0] else 0)
            y_movement = (1 if c2[1] > c1[1] else -1) * (1 if c2[1] != c1[1] else 0)
            coords = (c1[0] + x_movement * i, c1[1] + y_movement * i)
            if c1[0] == c2[0] or c1[1] == c2[1]:
                grid[coords] = grid[coords] + 1
            else:
                if part == 2:
                    grid[coords] = grid[coords] + 1

    answer = len([k for k, v in grid.items() if v > 1])

    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))