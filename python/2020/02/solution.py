import re
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
    valid = 0
    for line in data:
        policy, password = line.split(": ")
        min, maxletter = policy.split("-")
        max, letter = maxletter.split(" ")
        if part == 1:
            if int(min) <= len(password) - len(password.replace(letter, "")) <= int(max):
                valid += 1
        elif part == 2:
            if password[int(min) - 1] == letter and password[int(max) - 1] == letter:
                valid += 1
                print(f"{password=}")
                print(f"{valid=}")
    return valid

#print("Part 1:", solution(1))
print("Part 2:", solution(2)) # DOESN'T WORK!
