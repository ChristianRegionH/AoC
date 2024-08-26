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
    for row in data:
        values = [int(x) for x in row.split()]
        if part == 1:
            difference = abs(min(values) - max(values))
            answer += difference
        if part == 2:
            for number in values:
                other_values = values.copy()
                other_values.remove(number)
                for other_number in other_values:
                    divident = number / other_number
                    if divident == int(divident):
                        answer += int(divident)
    
    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))