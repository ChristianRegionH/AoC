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
    rows = defaultdict(list)
    instructions = []
    for line in data:
        if len(line) != len(line.replace("[", "")):
            for i, crate in enumerate(range(2,len(line), 4)):
                if line[crate - 1] == " ":
                    pass
                else:
                    rows[i + 1].append(line[crate - 1])
    print(rows)        

print("Part 1:", solution(1))
print("Part 2:", solution(2))