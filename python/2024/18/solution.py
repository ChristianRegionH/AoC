import copy
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

start = (0, 0)
#end = (6, 6)
end = (70, 70)

def find_shortest_path(number_of_bytes):
    grid = defaultdict(list)
    for x in range(start[0], end[0] + 1):
        for y in range(start[0], end[0] + 1):
            # Shortest path, accesible y/n
            if (x, y) == start:
                grid[(x, y)] = [0, 0]
            else:
                grid[(x, y)] = [float("inf"), 0]

    i = 1
    for line in data:
        x, y = list(map(int, line.split(",")))
        grid[(x, y)][1] = 1
        if i == number_of_bytes:
            last_byte = (x, y)
            break
        i += 1

    def find_adjacents(coords, grid):
        adjacents = []
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_coords = (coords[0] + dir[0], coords[1] + dir[1])
            if new_coords in grid.keys() and grid[new_coords][1] == 0:
                adjacents.append(new_coords)
        return adjacents

    queue = [start]
    while True:
        current = queue.pop(0)
        distance = grid[current][0]

        adjacents = find_adjacents(current, grid)
        for node in adjacents:
            if distance + 1 < grid[(node)][0]:
                grid[(node)][0] = distance + 1
                queue.append(node)
        if not queue:
            break
    
    return(grid[end][0], last_byte)

j = 1024
while True:
    f1, f2 = find_shortest_path(j)
    if j == 1024:
        print("Part 1:", f1)
    if f1 == float("inf"):
        print("Part 2:", str(f2[0]) + "," + str(f2[1]))
        break
    j += 1