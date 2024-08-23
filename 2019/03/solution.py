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
    gamma = ""
    epsilon = ""

    for i in range(len(data[0])):
        total = 0
        for line in data:
            if line[i] == "0":
                total -= 1
            else:
                total += 1
        gamma = gamma + ("1" if total > 0 else "0")

    for x in gamma:
        epsilon = epsilon + ("1" if x == "0" else "0")

    answer = int(gamma, 2) *  int(epsilon, 2)

    return answer
    

print("Part 1:", solution(1))
#print("Part 2:", solution(2))