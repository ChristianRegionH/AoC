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
    pos = (0, 0, 0)

    for line in data:
        direction, x = line.split(" ")
        x = int(x)
        if part == 1:
            if direction == "forward":
                pos = (pos[0] + x, pos[1], pos[2])
            elif direction == "down":
                pos = (pos[0], pos[1] + x, pos[2])
            elif direction == "up":
                pos = (pos[0], pos[1] - x, pos[2])

        elif part == 2:
            if direction == "down":
                pos = (pos[0], pos[1], pos[2] + x)
            elif direction == "up":
                pos = (pos[0], pos[1], pos[2] - x)
            elif direction == "forward":
                pos = (pos[0] + x, pos[1] + (pos[2] * x), pos[2])

    answer = pos[0] * pos[1]
    
    return answer
    

print("Part 1:", solution(1))
print("Part 2:", solution(2))