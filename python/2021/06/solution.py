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
    datax = [int(x) for x in data[0].split(",")]
    fish = defaultdict(int)
    
    for f in datax:
        fish[f] = fish[f] + 1

    for i in range(80 if part == 1 else 256):
        new_fish = defaultdict(int)
        for k, v in fish.items():
            if k == 0:
                new_fish[6] = new_fish[6] + v
                new_fish[8] = new_fish[8] + v
            else:
                new_fish[k - 1] = new_fish[k - 1] + v
        fish = new_fish

    answer = sum([v for v in fish.values()])

    return answer

print("Part 1:", solution(1))
print("Part 2:", solution(2))