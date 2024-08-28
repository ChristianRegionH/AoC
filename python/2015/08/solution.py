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
    answer = 0

    if part == 1:
        for string in data:
            string_literal = string[1:-1]
            value = ""
            while string_literal != "":
                if string_literal[0] != "\\":
                    value = value + string_literal[0]
                    string_literal = string_literal[1:]
                elif string_literal[0:2] == "\\\\":
                    value = value + "\\"
                    string_literal = string_literal[2:]
                elif string_literal[0:2] == "\\\"":
                    value = value + "\""
                    string_literal = string_literal[2:]
                elif string_literal[0:2] == "\\x":
                    value = value + "@"
                    string_literal = string_literal[4:]

            len_literal = len(string)
            len_value = len(value)
            answer = answer + len_literal - len_value

    elif part == 2:
        for string in data:
            string_literal = string
            value = ""
            while string_literal != "":
                if string_literal[0] != "\"":
                    value = value + ""
                    value = value + string_literal[0]
                    string_literal = string_literal[1:]
                elif string_literal[0:2] == "\\\\":
                    value = value + "\\"
                    string_literal = string_literal[2:]
                elif string_literal[0:2] == "\\\"":
                    value = value + "\""
                    string_literal = string_literal[2:]
                elif string_literal[0:2] == "\\x":
                    value = value + "@"
                    string_literal = string_literal[4:]

            len_literal = len(string)
            len_value = len(value)
            answer = answer + len_literal - len_value

    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))