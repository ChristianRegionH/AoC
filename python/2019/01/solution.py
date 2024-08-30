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
    total = 0

    if part == 1:
        for number in data:
            total += int(number)//3 - 2
    elif part == 2:
        for number in data:
            fuel = int(number)
            while fuel > 0:
                fuel = max(int(fuel)//3 - 2, 0)
                total += fuel
    return total
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))