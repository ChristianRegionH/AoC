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

stones = defaultdict(int)
for stone in data[0].split():
    stones[int(stone)] = 1

blinks = 0
while True:
    if blinks in [25, 75]:
        print("After", blinks, "blinks:", sum([v for v in stones.values()]))
    if blinks == 75:
        break
    after_blink = defaultdict(int)
    for k, v in stones.items():
        kstr = str(k)
        len_kstr = len(kstr)
        if k == 0:
            after_blink[1] += v
        elif len_kstr % 2 == 0:
            after_blink[int(kstr[:len_kstr//2])] += v
            after_blink[int(kstr[len_kstr//2:])] += v
        else:
            after_blink[k * 2024] += v
    stones = after_blink
    blinks += 1