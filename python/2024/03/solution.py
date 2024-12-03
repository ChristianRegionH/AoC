import sys
import re

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
    memory = ''
    for d in data:
        memory = memory + d
    instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", memory)
    do = True
    for i in instructions:
        if i.startswith("mul"):
            n1, n2 = i.split(",")
            n1 = int(n1[4:])
            n2 = int(n2[:-1])
            if part == 1:
                answer += n1 * n2
            else:
                answer += n1 * n2 * do
        elif i.startswith("don"):
            do = False
        else:
            do = True

    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))