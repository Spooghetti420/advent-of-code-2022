def visible_interior_trees(row: int, lines: list[str]):

    line = lines[row].strip()[1:-1]
    total = 0
    for col in range(len(line)):
        col += 1  # Normalise i to start at 1 (as 1 is the index of the second char of each line)
        if is_visible(row, col, lines):
            total += 1
        
    return total

def is_visible(row: int, col: int, grid: list[str]):
    width = len(grid[0])
    height = len(grid)
    current = grid[row][col]

    def visible_left():
        for i in range(col-1, -1, -1):
            element = grid[row][i]
            if element >= current:
                return False
        return True
    def visible_right():
        for i in range(col+1, width):
            element = grid[row][i]
            if element >= current:
                return False
        return True
    def visible_up():
        for i in range(row-1, -1, -1):
            element = grid[i][col]
            if element >= current:
                return False
        return True
    def visible_down():
        for i in range(row+1, height):
            element = grid[i][col]
            if element >= current:
                return False
        return True
    return visible_left() or visible_right() or visible_down() or visible_up()

def scenic_score(row: int, col: int, grid: list[str]):
    width = len(grid[0])
    height = len(grid)
    current = grid[row][col]

    def visible_left() -> int:
        count = 0
        for i in range(col-1, -1, -1):
            count += 1
            element = grid[row][i]
            if element >= current:
                break
        return count
    def visible_right():
        count = 0
        for i in range(col+1, width):
            count += 1
            element = grid[row][i]
            if element >= current:
                break
        return count
    def visible_up():
        count = 0
        for i in range(row-1, -1, -1):
            count += 1
            element = grid[i][col]
            if element >= current:
                break
        return count
    def visible_down():
        count = 0
        for i in range(row+1, height):
            count += 1
            element = grid[i][col]
            if element >= current:
                break
        return count

    l = visible_left()
    r = visible_right()
    d = visible_down()
    u = visible_up()
    
    return l * r * d * u


def part_i(lines: list[str]):
    visible_trees = 0


    for i, line in enumerate(lines):
        line = line.strip()

        if i == 0 or i == len(lines)-1: visible_trees += len(line); continue

        visible_trees += 2 # The exterior trees

        visible_trees += visible_interior_trees(i, lines)

    print(visible_trees)


def part_ii(lines: list[str]):
    current = 0
    for i, line in enumerate(lines):
        line = line.strip()

        if i == 0 or i == len(lines)-1: continue

        for j, col in enumerate(line[1:-1]):
            current = max(current, scenic_score(i, j+1, lines))
    
    print(current)


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        part_i(lines)
        part_ii(lines)

if __name__ == "__main__":
    main()