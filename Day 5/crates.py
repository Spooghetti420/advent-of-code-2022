import re
from dataclasses import dataclass as struct

@struct
class Move:
    number_to_move: int
    start_from: int
    end_at: int

    def __repr__(self) -> str:
        return f"(#{self.number_to_move} : {self.start_from} -> {self.end_at})"


MOVE_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")

def split_row(row: str, n: int = 4):
    """Splits a row, like [Z] [M] [P], into each of its elements."""
    for i in range(0, len(row), n):
        yield row[i:i+4].strip().replace("[", "").replace("]", "")

def load_crates():
    crates_len = None  # We don't know how many crates there are in a row yet...
    crates = []
    instructions = []
    with open("input.txt") as f:
        first_crate_stack = f.readline()
        crates_len = len(first_crate_stack)//4
        crates: list[list[str]] = [[] for _ in range(crates_len)]
        f.seek(0)

        while (line := f.readline()).strip().startswith("["):
            crates_on_the_row = split_row(line)
            for i, crate in enumerate(crates_on_the_row):
                # print(i, crate)
                crates[i].append(crate)  # The "top" of each stack is its last element

        f.readline() # Ignore the empty row
        for line in f:  # Read the remaining lines
            m = re.match(MOVE_PATTERN, line.strip())
            instructions.append(Move(*(int(m.group(i)) for i in range(1, 4))))

    # The list was generated in really the wrong order; I want to be able to "append" to each sublist
    # to add new stuff to the TOP, but right now the conceptual "top" of each sublist is in fact the start
    # of the list. So, I reverse all the elements of each sublist (pile), and then remove all the empty elements.
    for l in crates:
        l.reverse()
        while len(l) > 0 and (cell := l[-1]) == "":
            l.pop()

    return crates, instructions

def read_message(crates) -> str:
    message = ""
    for pile in crates:
        message += pile[-1]
    return message


def move_crate_9000(crates: list[list[str]], move: Move) -> None:
    """Moves a crate according to a move instruction, in-place."""
    for _ in range(move.number_to_move):
        crates[move.end_at-1].append(crates[move.start_from-1].pop())


def move_crate_9001(crates: list[list[str]], move: Move) -> None:
    """
    Move crates according to instructions, but multiple at a time.
    I.e., we move an entire sublist at a time from one pile to another.
    """
    intermediate = []
    for _ in range(move.number_to_move):
        intermediate.append(crates[move.start_from-1].pop())

    for _ in range(move.number_to_move):
        crates[move.end_at-1].append(intermediate.pop())


def part_i():
    crates, instructions = load_crates()
    for instruction in instructions:
        move_crate_9000(crates, instruction)

    print(read_message(crates))


def part_ii():
    crates, instructions = load_crates()
    for instruction in instructions:
        move_crate_9001(crates, instruction)

    print(read_message(crates))


if __name__ == "__main__":
    part_ii()