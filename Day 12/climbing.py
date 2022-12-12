from __future__ import annotations
from dataclasses import dataclass, field
from typing import TextIO


def height(letter: str) -> int:
    if letter == "S": letter = "a"
    if letter == "E": letter = "z"
    return ord(letter)-96


@dataclass
class Node:
    x: int
    y: int
    h: int
    neighbours: list[Node] = field(default_factory=list, repr=False)
    local_goal: float = field(default=float("inf"))
    global_goal: float = field(default=float("inf"))
    visited: bool = field(default=False)
    parent: Node = field(default=None)

    def dist(self, other: Node):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

    def add_neigbour(self, other: Node):
        if other.h - self.h <= 1:
            self.neighbours.append(other)


def setup_grid(f: TextIO) -> tuple[list[list[Node]], Node, Node]:
    line_length = len(first := f.readline())
    lines = [first] + f.readlines()
    map_height = len(lines)

    start: Node = None
    end: Node = None
    terrain: list[list[Node]] = [[(i,j) for i in range(line_length)] for j in range(map_height)]
    for j, l in enumerate(lines):
        for i, square in enumerate(l):
            terrain[j][i] = Node(i, j, height(square))
            if square == "S":
                start = terrain[j][i]
            elif square == "E":
                end = terrain[j][i]

    # Now generate neighbours
    for j, l in enumerate(terrain):
        for i, node in enumerate(l):
            if j > 0:
                node.add_neigbour(terrain[j-1][i])
            if j < len(terrain)-1:
                node.add_neigbour(terrain[j+1][i])
            if i > 0:
                node.add_neigbour(terrain[j][i-1])
            if i < len(terrain[0])-1:
                node.add_neigbour(terrain[j][i+1])

    return terrain, start, end


def astar(start: Node, end: Node) -> int:
    start.local_goal = 0
    start.global_goal = start.dist(end)

    untested_nodes: list[Node] = [start]
    while untested_nodes:
        untested_nodes.sort(key=lambda n: n.global_goal)

        while len(untested_nodes) > 0 and untested_nodes[0].visited:
            untested_nodes.pop(0)

        if not untested_nodes:
            break
        
        current = untested_nodes[0]
        current.visited = True
        for neighbour in current.neighbours:
            if not neighbour.visited:
                untested_nodes.append(neighbour)
                neighbour_goal = current.local_goal + current.dist(neighbour)
                if neighbour_goal < neighbour.local_goal:
                    neighbour.parent = current
                    neighbour.local_goal = neighbour_goal
                    neighbour.global_goal = neighbour.local_goal + neighbour.dist(end)

    # Calculate the length of the path
    p = end
    count = 0
    while p.parent != start:
        count += 1
        p = p.parent

    return count+1


def part_i(f: TextIO):
    _, start, end = setup_grid(f)

    print(astar(start, end))


def part_ii(f: TextIO):
    """This takes a good bit to run... some 15 seconds, maybe!"""
    grid, _, end = setup_grid(f)
    grid: list[list[Node]]


    # The grid needs to be reset every time, because my A* algorithm affects the nodes directly.
    # We go through every node in the grid and manually fix any alterations.
    def reset_grid(grid: list[list[Node]]):
        for i, line in enumerate(grid):
            for j, square in enumerate(line):
                grid[i][j].local_goal = float("inf")
                grid[i][j].global_goal = float("inf")
                grid[i][j].parent = None
                grid[i][j].visited = False

    count = 0
    lowest = float("inf")
    for line in grid:
        for square in line:
            if square.h == 1:
                count += 1
                print(f"Solving distance {count}...")
                try:
                    d = astar(square, end)
                except AttributeError:
                    # Oh my God, please just don't ask! It WORKED, somehow!!?!?!?
                    print("\tSkipping...")
                if d < lowest:
                    lowest = d
                reset_grid(grid)

    print(lowest)


def main():
    with open("input.txt") as f:
        # part_i(f)
        part_ii(f)


if __name__ == "__main__":
    main()