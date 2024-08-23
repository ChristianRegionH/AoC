import sys

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

def solution(part):
    elves = []
    current = 0
    for line in data:
        if line == "":
            elves.append(current)
            current = 0
        else:
            current += int(line)
    elves.sort(reverse = True)
    return sum(elves[0:1 if part == 1 else 3])
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))