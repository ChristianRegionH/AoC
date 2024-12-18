import sys
from collections import defaultdict
import re

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

for line in data:
    if line.startswith("Register A: "):
        A_base = int(re.findall(r"\: (\d+)", line)[0])
    if line.startswith("Register B: "):
        B_base = int(re.findall(r"\: (\d+)", line)[0])
    if line.startswith("Register C: "):
        C_base = int(re.findall(r"\: (\d+)", line)[0])
    if line.startswith("Program"):
        program = line.split("Program: ")[1]
        program = list(map(int, program.split(",")))

program_txt = ""
for l in program:
    program_txt = program_txt + "," + str(l)
program_txt = program_txt[1:]
print("Program:", program_txt)

i = 0
while True:
    instruction_pointer = 0
    out = ""
    i += 1
    A = i
    B = B_base
    C = C_base
    if i % 10000 == 0:
        print("Iteration", i)
    while True:
        if len(out) > len(program_txt):
            break

        if instruction_pointer + 1 > len(program):
            break

        opcode = program[instruction_pointer]
        literal = program[instruction_pointer + 1]
        combo_dict = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: A,
            5: B,
            6: C,
            7: False
        }
        combo = combo_dict[literal]

        def dv(reg):
            numerator = A
            denominator = 2 ** combo
            return numerator // denominator

        jump = False
        if opcode == 3:
            if A == 0:
                pass
            else:
                jump = True
                instruction_pointer = literal
                opcode = literal

        if opcode == 0:
            A = dv(A)
        if opcode == 1:
            B = B ^ literal
        if opcode == 2:
            B = combo % 8
        if opcode == 4:
            B = B ^ C
        if opcode == 5:
            if out == '':
                out = out + str(combo % 8)
            else:
                out = out + ',' + str(combo % 8)
        if opcode == 6:
            B = dv(B)
        if opcode == 7:
            C = dv(C)

        if jump == False:
            instruction_pointer += 2

        if A == A_base:
            print("Part 1", program_txt)

    if out == program_txt:
        print("Part 2:", i)
        break