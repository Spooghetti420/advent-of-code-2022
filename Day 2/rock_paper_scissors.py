from typing import Literal

SHAPE_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

LOSS = 0
DRAW = 3
WIN = 6

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
MATCHUPS = {
    ("A", "X"): DRAW,
    ("A", "Y"): WIN,
    ("A", "Z"): LOSS,

    ("B", "X"): LOSS,
    ("B", "Y"): DRAW,
    ("B", "Z"): WIN,
    
    ("C", "X"): WIN,
    ("C", "Y"): LOSS,
    ("C", "Z"): DRAW
}


# Converts the elf's instructions for part 2:
# X = need to lose, Y = need to draw, Z = need to lose
DECRYPT = {
    ("A", "X"): "Z",
    ("A", "Y"): "X",
    ("A", "Z"): "Y",

    ("B", "X"): "X",
    ("B", "Y"): "Y",
    ("B", "Z"): "Z",

    ("C", "X"): "Y",
    ("C", "Y"): "Z",
    ("C", "Z"): "X"
}

def play_trick(opponent_choice: Literal["A", "B", "C"], my_choice: Literal["X", "Y", "Z"]) -> int:
    """Play a round of rock-paper-scissors and return how much score I got from the round."""
    score = SHAPE_SCORES[my_choice] + MATCHUPS[(opponent_choice, my_choice)]
    return score

def part_i():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            opponent, me = line.split(" ")
            total += play_trick(opponent, me)

    print("Total score is", total)

def part_ii():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            opponent, code = line.split(" ")

            # Coded response requires a lookup to discern what I actually need to play
            me = DECRYPT[(opponent, code)]
            total += play_trick(opponent, me)

    print("Total score is", total)

if __name__ == "__main__":
    # part_i()
    part_ii()