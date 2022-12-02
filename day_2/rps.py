


points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

opponent_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

self_moves = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}


def calc(guide):
    total = 0
    for round in guide:
        moves = round.split(" ")
        points = points_for(self_moves[moves[1]], opponent_moves[moves[0]])
        total += points
        print(total)

    return total


def calc_again(guide):
    total = 0
    for round in guide:
        moves = round.split(" ")
        if moves[1] == "Y":
            total += (3 + points[opponent_moves[moves[0]]])
        elif moves[1] == "Z":
            total += (6 + get_winner(opponent_moves[moves[0]]))
        else:
            total += (get_loser(opponent_moves[moves[0]]))
    
    return total

def get_winner(option):
    if option == "rock":
        return points["paper"]

    if option == "paper":
        return points["scissors"]

    return points["rock"]


def get_loser(option):
    if option == "rock":
        return points["scissors"]

    if option == "paper":
        return points["rock"]

    return points["paper"]

def points_for(self_move, opponent_move):
    if self_move == opponent_move:
        return 3 + points[self_move]

    if self_move == "rock" and opponent_move == "scissors":
        return 6 + points[self_move]

    if self_move == "paper" and opponent_move == "rock":
        return 6 + points[self_move]

    if self_move == "scissors" and opponent_move == "paper":
        return 6 + points[self_move]

    return points[self_move]


with open('./input.txt') as f:
    data = f.read().strip()
    lines = data.split("\n")
    total = calc(lines)
    print('Part 1: ', total)
    
    total_again = calc_again(lines)
    print('Part 2:', total_again)
