def get_elf_totals():
    with open("input.txt", mode="r", encoding="utf-8") as data:
        elves = [sum([int(e) for e in d.split("\n") if e]) for d in data.read().split("\n\n")]
    return sorted(elves, reverse=True)

def part_i():
    totals = get_elf_totals()
    print(totals[0])

def part_ii(max_scores: int = 3):
    totals = get_elf_totals()
    print(sum(totals[:max_scores]))


if __name__ == "__main__":
    # part_i()
    part_ii(3)