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
        for line in data:
            compartment1, compartment2 = line[0:int(len(line)/2)], line[int(len(line)/2):]
            for letter in compartment1:
                if letter in compartment2:
                    score = ord(letter) - 96 if ord(letter) >= 97 else ord(letter) - 38
                    total += score
                    break
    
    elif part == 2:
        groups = []
        group = []
        for i, rucksack in enumerate(data):
            group.append(rucksack)
            if (i + 1) % 3 == 0:
                groups.append(group)
                group = []
        for group in groups:
            dict = defaultdict(list)
            for rucksack in group:
                for letter in rucksack:
                    if rucksack in dict[letter]:
                        pass
                    else:
                        dict[letter].append(rucksack)
            for k, v in dict.items():
                if len(v) == 3:

                    score = ord(k) - 96 if ord(k) >= 97 else ord(k) - 38
                    total += score

    return total
    

print("Part 1:", solution(1))
print("Part 2:", solution(2))