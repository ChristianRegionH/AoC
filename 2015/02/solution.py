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
    answer = 0

    for line in data:
        l, w, h = line.split("x")
        s1, s2, s3 = int(l) * int(w), int(w) * int(h), int(h) * int(l)
        paper = 2 * s1 + 2 * s2 + 2 * s3 + min(s1, s2, s3)
        sides = [int(l), int(w), int(h)]
        sides.sort()
        ribbon = sides[0] * 2 + sides[1] * 2 + sides[0] * sides[1] * sides[2]
        if part == 1:
            answer += paper
        elif part == 2:
            answer += ribbon

    return answer
    

print("Part 1:", solution(1))
print("Part 2:", solution(2))   