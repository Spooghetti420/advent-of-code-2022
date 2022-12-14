from typing import TextIO, Tuple

# I'm using a fixed-size sandbox and just sort of hoping that it works...
# I encountered some errors to do with missing horizontal space during the testing,
# so I just made it bigger. Problem solved! :P

def get_sandbox(f: TextIO, width: int = 1000) -> list[list[str]]:
    lines = [l.strip().split("->") for l in f.readlines()]
    sandbox = [["." for j in range(width)] for i in range(550)]
    for line in lines:
        for i in range(len(line)-1):
            draw_line(line[i], line[i+1], sandbox)
    return sandbox


def draw_line(start: str, end: str, sandbox: list) -> None:
    sx, sy = map(int, start.split(","))
    ex, ey = map(int, end.split(","))

    signum = lambda x: int(x/abs(x))
    if sx == ex:
        s = signum(ey-sy)
        for y in range(sy, ey+s, s):
            sandbox[y][sx] = "#"
    elif sy == ey:
        s = signum(ex-sx)
        for x in range(sx, ex+s, s):
            sandbox[sy][x] = "#"
    else:
        print("error")


def drop_grain(sandbox: list[list[str]]) -> Tuple[int, int]:
    settled = False
    sand_x, sand_y = 500, 0

    while not settled:
        if sandbox[sand_y+1][sand_x] == ".":
            sand_y += 1
        elif sandbox[sand_y+1][sand_x-1] == ".":
            sand_y += 1
            sand_x -= 1
        elif sandbox[sand_y+1][sand_x+1] == ".":
            sand_y += 1
            sand_x += 1
        else:
            sandbox[sand_y][sand_x] = "o"
            settled = True
    return (sand_x, sand_y)


def part_i(f: TextIO):
    sandbox = get_sandbox(f, 550)

    # Simulate sand
    count = 0
    abyss = False
    while not abyss:
        try:
            drop_grain(sandbox)
            count += 1
        except IndexError:
            # If there's an index error, the sand probably fell into the abyss
            abyss = True
    print(count)


def part_ii(f: TextIO):
    WIDTH = 1000
    lines = [l.strip().split("->") for l in f.readlines()]

    # Find the correct height of the floor (maximum y + 2)
    highest_y = 0
    for coord in lines:
        for pair in coord:
            _, y = pair.split(",")
            y = int(y)
            if y > highest_y:
                highest_y = y

    bottom = highest_y + 2

    # Create sandbox
    sandbox = [["." for j in range(WIDTH)] for i in range(550)]
    for line in lines:
        for i in range(len(line)-1):
            draw_line(line[i], line[i+1], sandbox)
    
    # Create floor
    for i in range(0, WIDTH):
        sandbox[bottom][i] = "#"

    # Simulate sand
    count = 0
    blocked = False
    while not blocked:
        x, y = drop_grain(sandbox)
        if (x, y) == (500, 0):
            blocked = True
        count += 1
    print(count)


def main():
    with open("input.txt") as f:
        # part_i(f)
        part_ii(f)


if __name__ == "__main__":
    main()