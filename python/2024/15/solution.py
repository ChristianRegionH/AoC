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

plan = []
moves = []
for line in data:
    if line == "":
        pass
    elif line[0] == "#":
        plan_line = ""
        for char in line:
            if char == "#":
                plan_line = plan_line + "##"
            elif char == ".":
                plan_line = plan_line + ".."
            elif char == "O":
                plan_line = plan_line + "[]"
            elif char == "@":
                plan_line = plan_line + "@."
        plan.append(plan_line)
    elif line[0] in ["^", "v", "<", ">"]:
        for char in line:
            moves.append(char)

for r, line in enumerate(plan):
    for c, value in enumerate(line):
        if value == "@":
            plan[r] = plan[r][:c] + "." + plan[r][c + 1:]
            R = r
            C = c
            break

def move_robot(plan, R, C, dir):
    outplan = plan

    dirs = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    possible_R = R + dirs[dir][0]
    possible_C = C + dirs[dir][1]

    # If robot can move freely, return new position
    if outplan[possible_R][possible_C] == ".":
        return outplan, possible_R, possible_C

    # If robot is pushing horizontically, return new position and plan
    if dir in ["<", ">"]:
        before = list(plan[R][:C])
        after = list(plan[R][C + 1:])
        new_row = ""
        if dir == ">":
            while after:
                next = after.pop(0)
                if next == "#":
                    return outplan, R, C
                elif next in ["[", "]"]:
                    new_row += next
                elif next == ".":
                    new_row = ".." + new_row + "".join(after)
                    outplan[R] = "".join(before) + new_row
                    return outplan, possible_R, possible_C
        elif dir == "<":
            while before:
                next = before.pop()
                if next == "#":
                    return outplan, R, C
                elif next in ["[", "]"]:
                    new_row = next + new_row
                elif next == ".":
                    new_row = "".join(before) + new_row + ".."
                    outplan[R] = new_row + "".join(after)
                    return outplan, possible_R, possible_C
    elif dir in ["^", "v"]:
        # Check row for row
        # CASES:
            # One case moved to two free spaces = "OK!"
            # Meeting a wall, no good!
            # Check cases above:
            # If ok, check next row above, until all cases are checked
            # Move all rows
            # Beware of case:
            # [][][]
            #   []
            # Only middle is pushed
        if dir == "^":
            to_check = [(R, C)]
            to_move = set()
            while to_check:
                check = to_check.pop(0)
                check_value = plan[check[0]][check[1]]
                checkR = check[0]
                checkC = check[1]
                # Check above
                above = (checkR - 1, checkC)
                above_value = plan[above[0]][above[1]]
                if above_value == "#":
                    return outplan, R, C
                elif above_value == check_value:
                    to_check.append(above)
                    to_move.add(check)
                elif above_value in ["[", "]"]:
                    to_move.add(check)
                    to_check.append(above)
                    if above_value == "[":
                        to_check.append((above[0], above[1] + 1))
                    elif above_value == "]":
                        to_check.append((above[0], above[1] - 1))
                elif above_value == ".":
                    to_move.add(check)
            if (R, C) in to_move:
                to_move.remove((R, C))
            sorted_moves = sorted(to_move)
            for sm in sorted_moves:
                outplan_above = list(outplan[sm[0] - 1])
                outplan_current = list(outplan[sm[0]])
                outplan_above[sm[1]] = outplan_current[sm[1]]
                outplan_current[sm[1]] = "."
                outplan[sm[0] - 1] = "".join(outplan_above)
                outplan[sm[0]] = "".join(outplan_current)
            return outplan, possible_R, possible_C
        
        if dir == "v":
            to_check = [(R, C)]
            to_move = set()
            while to_check:
                check = to_check.pop(0)
                check_value = plan[check[0]][check[1]]
                checkR = check[0]
                checkC = check[1]
                # Check below
                below = (checkR + 1, checkC)
                below_value = plan[below[0]][below[1]]
                if below_value == "#":
                    return outplan, R, C
                elif below_value == check_value:
                    to_check.append(below)
                    to_move.add(check)
                elif below_value in ["[", "]"]:
                    to_move.add(check)
                    to_check.append(below)
                    if below_value == "[":
                        to_check.append((below[0], below[1] + 1))
                    elif below_value == "]":
                        to_check.append((below[0], below[1] - 1))
                elif below_value == ".":
                    to_move.add(check)
            if (R, C) in to_move:
                to_move.remove((R, C))
            sorted_moves = sorted(to_move, reverse = True)
            for sm in sorted_moves:
                outplan_below = list(outplan[sm[0] + 1])
                outplan_current = list(outplan[sm[0]])
                outplan_below[sm[1]] = outplan_current[sm[1]]
                outplan_current[sm[1]] = "."
                outplan[sm[0] + 1] = "".join(outplan_below)
                outplan[sm[0]] = "".join(outplan_current)
            return outplan, possible_R, possible_C
           
for m in moves:
    plan, R, C = move_robot(plan, R, C, m)

gps_sum = 0
for r, line in enumerate(plan):
    print(line)
    for c, value in enumerate(line):
        if value == "[":
            gps_sum += 100 * r + c

print(gps_sum)