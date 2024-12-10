import sys

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

grid = dict()
for r, line in enumerate(data):
    for c, value in enumerate(line):
        grid[(r, c)] = int(value)

ans1 = 0
ans2 = 0

trails = []
trailcoords = set()
for k, v in grid.items():
    if v == 0:
        trails.append([k])

while trails:
    trail = trails.pop()
    next_step = len(trail)
    if next_step == 10:
        ans2 += 1
        if (trail[0], trail[9]) not in trailcoords:
            ans1 += 1
            trailcoords.add((trail[0], trail[9]))
        continue
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:       
        pos = (trail[0][0] + dir[0], trail[0][1] + dir[1])
        if pos in grid and grid[pos] == next_step:
            trails.append([pos] + trail)

print(ans1)
print(ans2)