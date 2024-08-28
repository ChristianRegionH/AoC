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
    string = data[0]
    
    new_string = ""
    for j in range(50):
        for i in range(len(string)):
            if i == 0:
                run = 1
            elif string[i] == string[i - 1]:
                run += 1
            elif string[i] != string[i - 1]:
                new_string = new_string + str(run) + string[i - 1]
                run = 1
            if i == len(string) - 1:
                new_string = new_string + str(run) + string[i]
        string = new_string
        new_string = ""
    
    return len(string)
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))