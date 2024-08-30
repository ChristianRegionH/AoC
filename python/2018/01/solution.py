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

data = [int(x) for x in data]

def solution(part):

    total = 0
    visited = set()
    visited.add(total)
    
    while True:
        for number in data:
            total += number
            if part == 2:
                if total in visited:
                    return total
            visited.add(total)
            
        if part == 1:
            return total
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))