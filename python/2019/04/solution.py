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


def test_password(input, part):
    req1 = True if len(input) == 6 else False
    req2 = any([input[i] == input[i + 1] for i in range(len(input) - 1)])
    req3 = True if set([input[i] <= input[i + 1] for i in range(len(input) - 1)]) == {True} else False
    faux = 'm' + input + 'm'
    req4 = any([faux[i] == faux[i + 1] and faux[i] != faux[i - 1] and faux[i] != faux[i + 2] for i in range(len(input))])

    if part == 1:
        answer = 1 if req1 and req2 and req3 else 0
    elif part == 2:
        answer = 1 if req1 and req2 and req3 and req4 else 0

    return answer

def solution(part):
    total = 0
    start, end = [int(x) for x in data[0].split("-")]

    for i in range(start, end + 1):
        total += test_password(str(i), part)

    return total

# 228 - too low

print("Part 1:", solution(1))
print("Part 2:", solution(2))