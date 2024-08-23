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
    secret_key = data[0]
    for i in range(100000000):
        new_secret_key = secret_key + str(i)
        m = hashlib.md5(new_secret_key.encode()).hexdigest()[0:5 if part == 1 else 6]
        if part == 1:
            if m == "00000":
                return i
        elif part == 2:
            if m == "000000":
                return i
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))