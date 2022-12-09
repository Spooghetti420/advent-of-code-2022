from typing import TextIO


DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def perform_row_instruction(instruction: str, knots: list[tuple], visited: set):
    direction, steps = instruction.split(" ")
    way = DIRS[direction]
    for _ in range(int(steps)):
        head = knots[0]
        knots[0] = (head[0]+way[0], head[1]+way[1])
        for i in range(len(knots)-1):
            head = knots[i]
            tail = knots[i+1]
            knots[i+1] = update_tail(head, tail)
        visited.add(knots[-1])

    return knots


"""I leave this here to show my old appraoch :)"""
# def perform_row_instruction(instruction: str, head, tail, visited: set):
#     direction, steps = instruction.split(" ")
#     way = DIRS[direction]
#     for _ in range(int(steps)):
#         head = (head[0]+way[0], head[1]+way[1])
#         tail = update_tail(head, tail)
#         visited.add(tail)

#     return head, tail


def update_tail(head, tail):
    dx = head[0]-tail[0]
    dy = head[1]-tail[1]
    if (dx**2 + dy**2)**0.5 >= 2:
        # Move diagonally by one tile in either or both directions
        if dx>1: dx = 1
        if dx<-1: dx = -1
        if dy>1: dy = 1
        if dy<-1: dy = -1
    else:
        # If the distance is too short, don't move at all
        dx = dy = 0
    
    tail = (tail[0]+dx, tail[1]+dy)
    return tail


def part_i(f: TextIO):
    head = (0, 0)
    tail = (0, 0)
    visited = set()
    for line in f:
        line = line.strip()
        head, tail = perform_row_instruction(line, [head, tail], visited)
    print(len(visited))


def part_ii(f: TextIO):
    knots = [(0, 0) for _ in range(10)]
    visited = set()
    for line in f:
        line = line.strip()
        knots = perform_row_instruction(line, knots, visited)
    print(len(visited))


def main():
    with open("input.txt") as f:
        part_i(f)
        f.seek(0)
        part_ii(f)


if __name__ == "__main__":
    main()