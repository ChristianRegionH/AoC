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
    rules = defaultdict(list)
    updates = []
    for line in data:
        if "|" in line:
            after, before = map(int, line.split("|"))
            rules[after].append(before)
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])

    ans1 = 0
    ans2 = 0
    for update in updates:
        count_before = []
        for n in update:
            count_before.append(len([x for x in rules[n] if x in update]))
        _, correct_order = map(list, zip(*sorted(zip(count_before, update), reverse = True)))
        middle = correct_order[len(correct_order) // 2]
        if correct_order == update:
            ans1 += middle
        else:
            ans2 += middle

    return ans1 if part == 1 else ans2

print("Part 1:", solution(1))
print("Part 2:", solution(2))