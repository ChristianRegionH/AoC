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
    left = []
    right = []
    for line in data:
        l, r = map(int, line.split('   '))
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()

    ans1 = 0
    ans2 = 0
    for i in range(len(left)):
        ans1 += abs(left[i] - right[i])
        n = left[i]
        ans2 += n * len([x for x in right if x == n])

    return ans1 if part == 1 else ans2

print("Part 1:", solution(1))
print("Part 2:", solution(2))