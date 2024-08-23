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
    numbers = [int(x) for x in data]
    for i_a, number_a in enumerate(numbers):
        for i_b, number_b in enumerate(numbers[i_a + 1:]):
            if part == 1:
                if number_a + number_b == 2020:
                    return number_a * number_b
            elif part == 2:
                for i_c, number_c in enumerate(numbers[i_b + 1 + i_a + 1:]):
                    if number_a + number_b + number_c == 2020:
                        return number_a * number_b * number_c


print("Part 1:", solution(1))
print("Part 2:", solution(2))