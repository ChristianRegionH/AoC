import sys
import copy
from collections import defaultdict

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

# Get starting grid, starting position and starting direction
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = defaultdict(int)
for r, row in enumerate(data):
        for c, value in enumerate(row):
            if value in ["^", "v", "<", ">"]:
                if value == "^":
                    dir = 0
                elif dir == ">":
                    dir = 1
                elif value == "v":
                    dir = 2
                elif value == "<":
                    dir = 3            
                pos = (r, c)
                grid[(r, c)] = '.'
            else:
                grid[(r, c)] = value

def insert_obstacle(grid, obstacle_position):
    new_grid = copy.deepcopy(grid)
    new_grid[obstacle_position] = "#"
    return new_grid

# Returns visited number of visited if it goes out of bounds or 1 if it ends in a loop
def traverse_grid(grid, pos, dir):
    visited = set()
    visited.add((pos, dir))
        
    while True:
        next_pos = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        if next_pos not in grid.keys():
            return visited
        elif grid[next_pos] == ".":
            if (next_pos, dir) in visited:
                return 1
            else:
                visited.add((next_pos, dir))
                pos = next_pos
        else:
            dir = 0 if dir == 3 else dir + 1
            continue

path = set()
for x in traverse_grid(grid, pos, dir):
     path.add(x[0])

ans1 = len(path)
ans2 = 0
for coords in path:
    new_grid = insert_obstacle(grid, coords)
    if traverse_grid(new_grid, pos, dir) == 1:
        ans2 += 1

print(ans1)
print(ans2)