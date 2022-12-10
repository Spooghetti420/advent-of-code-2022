from typing import TextIO


# Maybe this isn't necessary, since (all of these) % 40 == 20, but just in case
IMPORTANT_SIGNALS = {
    20, 60, 100, 140, 180, 220
}

def part_i(f: TextIO):
    x = 1
    cycle = 0
    strength = 0

    def get_signal():
        nonlocal strength
        if cycle in IMPORTANT_SIGNALS:
            strength += cycle * x

    for line in f:
        line = line.strip()
        if line == "": break

        args = line.split()
        if args[0] == "noop":
            cycle += 1
            get_signal()
        elif args[0] == "addx":
            cycle += 1
            get_signal()
            cycle += 1
            get_signal()
            x += int(args[1])
    print(strength)


def part_ii(f: TextIO):
    x = 1
    screen = ["."*40 for _ in range(6)]
    scanx = 0
    scany = 0

    def draw_screen():
        nonlocal screen, scanx, scany
        if scanx-1 <= x <= scanx+1:
            # Ah, how I wish characters could just be assigned to...
            screen[scany] = screen[scany][:scanx] + "#" + screen[scany][scanx+1:]
        # Advance scan line
        scanx += 1
        if scanx >= 40:
            scanx = 0
            scany += 1

    for line in f:
        line = line.strip()
        if line == "": break

        # I've kept the references to "cycle" because it shows at what kind of times the screen gets drawn to.
        args = line.split()
        if args[0] == "noop":
            # cycle += 1
            draw_screen()
        elif args[0] == "addx":
            # cycle += 1
            draw_screen()
            # cycle += 1
            draw_screen()
            x += int(args[1])
    for line in screen:
        # Just print this way for easier reading :)
        for char in line:
            print(char, end=" ")
        print()


def main():
    with open("input.txt") as f:
        # part_i(f)
        part_ii(f)


if __name__ == "__main__":
    main()