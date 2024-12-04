import sys

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

def report_checker(report):
    safe = 1
    increasing = 0
    decreasing = 0
    for i in range(1, len(report)):
        if report[i] == report[i - 1]:
            safe = 0
            break
        if abs(report[i] - report[i - 1]) > 3:
            safe = 0
            break
        if report[i] > report[i - 1]:
            increasing += 1
        if report[i] < report[i - 1]:
            decreasing += 1
        if increasing > 0 and decreasing > 0:
            safe = 0
            break
    return safe

def solution(part):
    count = 0
    for line in data:
        report = [int(x) for x in line.split()]
        if part == 1:
            print(report)
            print(report_checker(report))
            print()
            count += report_checker(report)
        elif part == 2:
            subreports = []
            for i in range(len(report)):
                subreport = report[:i] + report[i + 1:]
                subreports.append(subreport)
                subreports.append(report)
            for sr in subreports:
                if report_checker(sr) == 1:
                    count += 1
                    break
    return count
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))