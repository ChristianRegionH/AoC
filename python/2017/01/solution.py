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
    for line in data:
        total = 0
        if part == 1:
            for i in range(len(line)):
                if i == len(line) - 1:
                    if line[i] == line[0]:
                        total += int(line[i])
                else:
                    if line[i] == line[i + 1]:
                        total += int(line[i]) 
        elif part == 2:
            for i in range(len(line)):
                if i < len(line) / 2 - 1:
                    if line[i] == line[i + int(len(line) / 2)]:
                        total += int(line[i])
                else:
                    if line[i] == line[i - int(len(line) / 2)]:
                        total += int(line[i])

    return total
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))