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

def test_password(input):
    chars = [ord(x) for x in input]
    req1 = any([(chars[i] + 1 == chars[i + 1] and chars[i + 1] + 1 == chars[i + 2]) for i in range(len(chars) - 2)])
    req2 = not any([x in 'iol' for x in input])
    req3 = True if len(set([x for x in [input[i:i+2] for i in range(len(input) - 1)] if x[0] == x[1]])) >= 2 else False

    return req1 and req2 and req3

def next_password(input, n):
    if input[n] == "z":
        new_input = input[0:n] + "a" + input[n + 1:]
        return next_password(new_input, n - 1)
    else:
        new_input = input[0:n] + chr(ord(input[n]) + 1) + input[n + 1:]
        return new_input

next_passwords = []
password = data[0]
while len(next_passwords) != 2:
    password = next_password(password, 7)
    if test_password(password):
        next_passwords.append(password)

print("Part 1:", next_passwords[0])
print("Part 2:", next_passwords[1])
