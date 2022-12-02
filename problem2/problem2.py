from enum import IntEnum


class Shape(IntEnum):
    Rock, A, X = 1, 1, 1
    Paper, B, Y = 2, 2, 2
    Scissors, C, Z = 3, 3, 3


class Scores(IntEnum):
    Loss, X = 0, 0
    Draw, Y = 3, 3
    Win, Z = 6, 6


class Sets:
    Loss = {-1, 2}
    Win = {1, -2}
    Draw = {0}


def outcome1(opponent: str, you: str) -> int:
    diff = Shape[you] - Shape[opponent]
    if diff == 0:
        return Shape[you] + Scores.Draw
    elif diff in Sets.Win:
        return Shape[you] + Scores.Win
    else:
        return Shape[you]


def outcome2(opponent: str, you: str) -> int:
    if Scores[you] == Scores.Draw:
        return Shape[opponent] + Scores.Draw

    elif Scores[you] == Scores.Loss:
        if Shape[opponent] == Shape.Rock:
            return Shape.Scissors
        elif Shape[opponent] == Shape.Paper:
            return Shape.Rock
        else:
            return Shape.Paper

    elif Scores[you] == Scores.Win:
        score = Scores.Win
        if Shape[opponent] == Shape.Rock:
            return score + Shape.Paper
        elif Shape[opponent] == Shape.Paper:
            return score + Shape.Scissors
        else:
            return score + Shape.Rock


if __name__ == "__main__":
    # filename = "test_input.txt"
    filename = "puzzle_input.txt"

    with open(filename) as f:
        lines = f.readlines()

    score1, score2 = 0, 0
    for line in lines:
        if line:
            score1 += outcome1(opponent=line[0], you=line[2])
            score2 += outcome2(opponent=line[0], you=line[2])

    print(f"First score: {score1}, second score: {score2}")
