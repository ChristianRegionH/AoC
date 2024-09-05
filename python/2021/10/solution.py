import sys
import math

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

def solution(part):
    part1 = 0
    part2 = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    points = {
        ')': [3, 1],
        ']': [57, 2],
        '}': [1197, 3],
        '>': [25137, 4]
    }

    for line in data:
        expected = []
        line_corrupted = False
        for char in line:
            if char in pairs.keys():
                expected.append(pairs[char])
            elif char == expected[-1]:
                expected.pop()
            else:
                part1 += points[char][0]
                line_corrupted = True
                break

        if line_corrupted == False:
            part2_score = 0
            for char in expected[::-1]:
                part2_score *= 5
                part2_score += points[char][1]
            part2.append(part2_score)
        part2.sort()

    if part == 1:
        return part1
    elif part == 2:
        return part2[len(part2) // 2]

print("Part 1:", solution(1))
print("Part 2:", solution(2))