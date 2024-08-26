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
    dir_dict = {
        ('N', 'L'): ('W', (-1, 0)),
        ('N', 'R'): ('E', (1, 0)),
        ('E', 'L'): ('N', (0, 1)),
        ('E', 'R'): ('S', (0, -1)),
        ('S', 'L'): ('E', (1, 0)),
        ('S', 'R'): ('W', (-1, 0)),
        ('W', 'L'): ('S', (0, -1)),
        ('W', 'R'): ('N', (0, 1)),
    }

    visited = set()

    for line in data:
        print(line)
        current_pos = ('N', (0, 0))
        instructions = line.split(", ")
        for instruction in instructions:
            print(instruction)            
            c_dir = current_pos[0]
            c_pos = current_pos[1]
            dir = instruction[0:1]
            length = int(instruction[1:])
            new_dir = dir_dict[(c_dir, dir)][0]
            movement = dir_dict[(c_dir, dir)][1]
            for i in range(length):
                c_pos = [sum(x) for x in zip(c_pos, movement)]
                c_pos = tuple(c_pos)
                if part == 2:
                    print(c_pos)
                    if c_pos in visited:
                        break
                    else:
                        visited.add(c_pos)
                        print(f"{visited = }")
            current_pos = (new_dir, c_pos)
            answer = abs(current_pos[1][0]) + abs(current_pos[1][1])

            print()
        print()


    return answer
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))