from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Directory:
    path: Path
    parent: Directory = field(default=None)
    contents: list[Directory | File] = field(default_factory=list)

    def __str__(self) -> str:
        return self.path.stem

    def size_of(self) -> int:
        s = 0
        for c in self.contents:
            if isinstance(c, Directory):
                s += c.size_of()
            else:
                s += c.size
        return s


@dataclass
class File:
    size: int
    name: str

    def __str__(self) -> str:
        return f"{self.size} {self.name}"


def process_commands(text: list[str]):
    root = Path("/")

    base = Directory(root)
    current = base

    for line in text:
        line = line.strip()
        if line.startswith("$"):
            line = line[2:]
            # Process command
            args = line.split(" ")
            command = args[0]
            if len(args) == 2:
                arg = args[1]
            else:
                arg = None

            if command == "cd":
                if arg == "/":
                    current = base
                elif arg == "..":
                    current = current.parent
                else:
                    new_path = current.path / arg
                    for c in current.contents:
                        if isinstance(c, Directory) and c.path == new_path:
                            current = c
                            break
                    else:
                        print("problem")

            elif command == "ls":
                pass
        else:
            if line.startswith("dir"):
                _, name = line.split(" ")
                new_path = current.path / name
                current.contents.append(Directory(new_path, parent=current))
            else:
                size, filename = line.split(" ")
                current.contents.append(File(int(size), filename))

    return base


def print_tree(directory: Directory, indent: int = 0) -> None:
    print(" "*indent + directory.path.stem)
    for content in directory.contents:
        if isinstance(content, File):
            print(" "*(indent+2) + str(content)) 
        elif isinstance(content, Directory):
            # print(" "*(indent+2) + content.path.stem)
            print_tree(content, indent+2)


def sum_tree_lesser_100000(root: Directory):
    r = 0
    for content in root.contents:
        if isinstance(content, Directory):
            dir_size = content.size_of()
            if dir_size < 100000:
                r += dir_size
            r += sum_tree_lesser_100000(content)
    
    return r


def all_sizes(root: Directory):
    for content in root.contents:
        if isinstance(content, Directory):
            dir_size = content.size_of()
            yield dir_size
            for s in all_sizes(content):
                yield s


def part_i(commands: list[str]):
    base = process_commands(commands)
    file_size = sum_tree_lesser_100000(base)
    print(file_size)


def part_ii(commands: list[str]):
    base = process_commands(commands)
    root_size = base.size_of()
    total_space = 70000000
    remaining = total_space - root_size
    requisite = 30000000 - remaining

    sizes = [s for s in all_sizes(base)]
    sizes = [s for s in sizes if s >= requisite] + [root_size]

    print(sizes)


def main():
    with open("input.txt") as f:
        commands = f.readlines()

    # part_i(commands)
    part_ii(commands)

if __name__ == "__main__":
    main()