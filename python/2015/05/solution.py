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
    if part == 1:
        nice = 0
        
        for string in data:
            if len(string) - len(string.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")) < 3:
                continue

            ok = 0
            for i in range(len(string)):
                if i != 0:
                    if string[i - 1] == string[i]:
                        ok += 1

            if len(string) - len(string.replace("ab", "").replace("cd", "").replace("pq", "").replace("xy", "")) != 0:
                continue

            if ok > 0:
                nice += 1

    elif part == 2:
        nice = 0

        for string in data:
            print(string)
            ok = 0
            for i in range(len(string)):
                try:
                    if string[i:i+2] in string[i+2:]:
                        ok += 1
                        print("Passed first test: ", string[i:i+2])
                        break
                except:
                    pass
            for i in range(len(string)):
                try:
                    if string[i] == string[i+2] and string[i] != string[i+1]:
                        ok += 1
                        print("Passed second test: ", string[i:i+3])
                        break
                except:
                    pass

            if ok >= 2:
                nice += 1
            print(f"{nice = }")
            print()

    return nice

    
print("Part 1:", solution(1))
print("Part 2:", solution(2))