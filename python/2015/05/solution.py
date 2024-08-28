import hashlib
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
    answer = 0
    for string in data:
        req1 = True if sum([x in 'aeiou' for x in string]) >= 3 else False
        req2 = True if any(x[0] == x[1] for x in [string[i:i+2] for i in range(len(string) - 1)]) else False
        req3 = True if not any(x in ['ab', 'cd', 'pq', 'xy'] for x in [string[i:i+2] for i in range(len(string) - 1)]) else False
        pairs = [string[i:i+2] for i in range(len(string) - 1)]
        req4 = False
        for i, pair in enumerate(pairs):
            if pair in pairs[i+2:]:
                req4 = True
                break
        req5 = True if any(x[0] == x[2] for x in [string[i:i+3] for i in range(len(string) - 2)]) else False

        if part == 1:
            if req1 and req2 and req3:
                answer += 1
        if part == 2:
            if req4 and req5:
                answer += 1

    return answer

    
print("Part 1:", solution(1))
print("Part 2:", solution(2))