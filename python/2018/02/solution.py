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
    if part == 1:
        twos = 0
        threes = 0
        for box in data:
            letters = defaultdict(int)
            for letter in box:
                letters[letter] += 1
            twos += 1 if any([k for k, v in letters.items() if v == 2]) else 0
            threes += 1 if any([k for k, v in letters.items() if v == 3]) else 0
        checksum = twos * threes
        return checksum
    
    elif part == 2:
        hit_length = len(data[0]) - 1
        pairs = []
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                pairs.append((data[i], data[j]))
        for pair in pairs:
            answer = ""
            for i in range(len(pair[0])):
                if pair[0][i] == pair[1][i]:
                    answer = answer + pair[0][i]
            if len(answer) == hit_length:
                return answer
            
print("Part 1:", solution(1))
print("Part 2:", solution(2))