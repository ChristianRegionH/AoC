import re
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
    answer = 0

    lights = defaultdict(int)
    for x in range(1000):
        for y in range(1000):
            lights[(x, y)] = 0

    for line in data:
        instructions = re.findall(r"(\w+) (\d+),(\d+)", line)
        action = instructions[0][0]
        coords1 = [int(x) for x in [instructions[0][1], instructions[0][2]]]
        coords2 = [int(x) for x in [instructions[1][1], instructions[1][2]]]
        for x in range(coords1[0], coords2[0] + 1):
            for y in range(coords1[1], coords2[1] + 1):
                if action == "on":
                    lights[(x, y)] = 1 if part == 1 else lights[(x, y)] + 1
                elif action == "off":
                    lights[(x, y)] = 0 if part == 1 else max(lights[(x, y)] - 1, 0)
                elif action == "toggle":
                    lights[(x, y)] = 1 - lights[(x, y)] if part == 1 else lights[(x, y)] + 2
    
    for brightness in lights.values():
        answer += brightness

    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))