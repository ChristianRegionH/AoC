import sys
from collections import defaultdict
import copy

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

grid = defaultdict(str)
for r, line in enumerate(data):
    for c, value in enumerate(line):
        grid[(r, c)] = value



# Output adjacent coords horizontally and vertically
def find_adjacent(coords):
    adjacent_coords = []
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        adjacent_coords.append((coords[0] + dir[0], coords[1] + dir[1]))
    return adjacent_coords

plants = defaultdict(list)
for k, v in grid.items():
    adjacents = find_adjacent(k)
    for a in adjacents:
        if a in grid.keys():
            if grid[a] == v:
                plants[k].append(a)
    if k not in plants.keys():
        plants[k] = []

plantsdict = copy.deepcopy(plants)
plots = []
plot = []
while plants:
    if not plot:
        next_key = list(plants.keys())[0]
        plot.append(next_key)
        plants.pop(next_key)
    done = True
    for k, v in plants.items():
        if len(set(v).intersection(set(plot))) > 0:
            plot.append(k)
            plants.pop(k)
            if plants:
                done = False
            break
    if done:
        plots.append(plot)
        plot = []

ans1 = 0
ans2 = 0
for plot in plots:
    print(plot)
    area = len(plot)
    perimeter = 0
    for plant in plot:
        perimeter += 4 - len(plantsdict[plant])

    sides = 0
    corner = plot[0]
    for plant in plot:
        if plant[0] <= corner[0] and plant[1] <= corner[1]:
            corner = plant
    current = corner
    checked_plants = set(current)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir = 0
    while True:
        if len(checked_plants) == len(plot):
            sides += 1
            break
        check = (dirs[dir][0] + current[0], dirs[dir][1] + current[1])

        if check in plot:
            current = check
            checked_plants.add(current)
            print("Moved to current:", current)
        else:
            if check not in checked_plants:
                sides += 1
        
        else:
            if check in checked_plants:
                dir = 0 if dir == 3 else dir + 1
            break
            print("Added side")
            sides += 1
            dir = 0 if dir == 3 else dir + 1
    print(area)
    print(sides)
    print()

    ans1 += area * perimeter
    ans2 += area * sides

print(ans1)
print(ans2)