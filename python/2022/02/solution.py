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
    total_score = 0
    
    opponent_plays = {
        "A": (0, "rock"), 
        "B": (0, "paper"), 
        "C": (0, "scissors")
        }
    my_plays = {
        "X": (1, "rock"), 
        "Y": (2, "paper"), 
        "Z": (3, "scissors")
        }
    rigged_games = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    outcomes = {
        ("rock", "rock"): 3,
        ("rock", "paper"): 6,
        ("rock", "scissors"): 0,
        ("paper", "rock"): 0,
        ("paper", "paper"): 3,
        ("paper", "scissors"): 6,
        ("scissors", "rock"): 6,
        ("scissors", "paper"): 0,
        ("scissors", "scissors"): 3
        }
    
    for line in data:
        opponent, me = line.split(" ")
        if part == 1:
            matchup = (opponent_plays[opponent][1], my_plays[me][1])
            score = my_plays[me][0] + outcomes[matchup]
        elif part == 2:
            for k, v in outcomes.items():
                if k[0] == opponent_plays[opponent][1]:
                    if v == rigged_games[me]:
                        my_play = k[1]
            matchup = (opponent_plays[opponent][1], my_play)
            score = sum([int(v[0]) for k, v in my_plays.items() if v[1] == my_play]) + outcomes[matchup]
        total_score += score    

    return total_score

print("Part 1:", solution(1))
print("Part 2:", solution(2))