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
for c, line in enumerate(data):
    for r, value in enumerate(line):
        grid[(c, r)] = int(value)

trails = []
complete_trails = []
for k, v in grid.items():
    if v == 0:
        trails.append([k])

while trails:
    trail = trails.pop()
    next_step = len(trail)
    if next_step == 10:
        complete_trails.append(trail)
        continue
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:       
        pos = (trail[0][0] + dir[0], trail[0][1] + dir[1])
        if pos in grid and grid[pos] == next_step:
            trails.append([pos] + trail)

ans1 = 0
ans2 = 0
start_ends = set()
for trail in complete_trails:
    start = trail.pop()
    end = trail.pop(0)
    if (start, end) not in start_ends:
        ans1 += 1
    start_ends.add((start, end))
    ans2 += 1

print(ans1)
print(ans2)