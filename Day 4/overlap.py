from __future__ import annotations
from typing import Collection


class Elf:
    starting_sector: int
    ending_sector: int

    def __init__(self, range_str: str) -> None:
        self.starting_sector, self.ending_sector = (int(i) for i in range_str.split("-"))
    
    @classmethod
    def from_pair(cls, pairing: str) -> Collection[Elf]:
        first_elf, second_elf = pairing.strip().split(",")
        first_elf, second_elf = cls(first_elf), cls(second_elf)
        return first_elf, second_elf

    @staticmethod
    def find_total_overlap(first: Elf, second: Elf) -> bool:
        """ 
        Overlapping in these two cases:
            # № 1
            # ...456...
            # ...45....
            # № 2
            # ...45....
            # ...456...
        """
        if first.starting_sector <= second.starting_sector and first.ending_sector >= second.ending_sector:
            return True
        if second.starting_sector <= first.starting_sector and second.ending_sector >= first.ending_sector:
            return True
        return False

    @staticmethod
    def find_overlap(first: Elf, second: Elf) -> bool:
        """
        Now the criteria are a little different...
            # e.g. the following ranges overlap:
            # .234567..
            # 12345....
            # So if the first starts before the second and ends after the starting point of the second... then we have an overlap.
            # Vice versa also applies, so we just have to test both ways.
        """
        if first.starting_sector <= second.starting_sector and first.ending_sector >= second.starting_sector:
            return True
        if second.starting_sector <= first.starting_sector and second.ending_sector >= first.starting_sector:
            return True
        return False


def part_i():
    overlaps = 0
    with open("input.txt") as f:
        for pairing in f:
            first_elf, second_elf = Elf.from_pair(pairing)
            if Elf.find_total_overlap(first_elf, second_elf):
                overlaps += 1

    print("Number of overlaps is", overlaps)

def part_ii():
    overlaps = 0
    with open("input.txt") as f:
        for pairing in f:
            first_elf, second_elf = Elf.from_pair(pairing)
            if Elf.find_overlap(first_elf, second_elf):
                overlaps += 1

    print("Number of overlaps is", overlaps)


if __name__ == "__main__":
    # part_i()
    part_ii()