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
    flashes = 0

    for x in range(len(data[0])):
        for y in range(len(data)):
            grid[(x, y)] = int(data[x][y])

    step = 0
    while True:
        step += 1
        # Increase all octopi by 1
        for k in grid.keys():
            grid[k] = grid[k] + 1
        # Set intial flashing octopi
        flashed = set()
        for k, v in grid.items():
            if v >= 10:
                flashed.add(k)
        # Make a queue flashing octopi to affect nearby
        to_handle = []
        for f in flashed:
            to_handle.append(f)
        while to_handle:
            current = to_handle.pop()
            adjacents = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    coords = (current[0] + x, current[1] + y)
                    if coords in grid.keys():
                        adjacents.append(coords)
            for adjacent in adjacents:
                grid[adjacent] = grid[adjacent] + 1
            for k, v in grid.items():
                if v >= 10:
                    if k in flashed:
                        pass
                    else:
                        flashed.add(k)
                        to_handle.append(k)
        # Reset all flashed octopi
        for k, v in grid.items():
            if v >= 10:
                grid[k] = 0
                flashes += 1

        if part == 1:
            if step == 100:
                return flashes
        if part == 2:
            if set([v for v in grid.values()]) == {0}:
                return step

print("Part 1:", solution(1))
print("Part 2:", solution(2))