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
    signals = defaultdict(int)

    data2 = []
    for line in data:
        if line.split(" -> ")[0].isdigit():
            data2.append(line)
    for line in data:
        if "AND" in line.split(" -> ")[0]:
            data2.append(line)
    for line in data:
        if "OR" in line.split(" -> ")[0]:
            data2.append(line)
    for line in data:
        if "LSHIFT" in line.split(" -> ")[0]:
            data2.append(line)
    for line in data:
        if "RSHIFT" in line.split(" -> ")[0]:
            data2.append(line)
    for line in data:
        if "NOT" in line.split(" -> ")[0]:
            data2.append(line)

    for line in data2:
        instruction, recipient = line.split(" -> ")
        if instruction.isdigit():
            signals[recipient] = int(instruction)
        elif "AND" in instruction or "OR" in instruction:
            operator = instruction.split(" ")[1]
            s1 = signals[instruction.split(" ")[0]]
            s2 = signals[instruction.split(" ")[2]]
            if operator == "AND":
                signals[recipient] = s1 & s2
            else:
                signals[recipient] = s1 | s2
        elif "LSHIFT" in instruction or "RSHIFT" in instruction:
            operator = instruction.split(" ")[1]
            s1 = signals[instruction.split(" ")[0]]
            s2 = int(instruction.split(" ")[2])
            if operator == "LSHIFT":
                signals[recipient] = s1 << s2
            else:
                signals[recipient] = s1 >> s2
        elif "NOT" in instruction:
            s1 = signals[instruction.split(" ")[1]]
            signals[recipient] = 65536 + ~s1

    return signals
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))
