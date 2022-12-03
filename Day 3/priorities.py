def priority(letter: str) -> int:
    """
    Get the priority of an item (represented by letters a, b, c..., A, B, C...
    Where a=1, b=2, ... A=27, ... Z=52.
    """
    if letter.isupper():
        return ord(letter) - 38 # ord(A) = 65, so 65-38 = 27, etc.
    elif letter.islower():
        return ord(letter) - 96


def part_i():
    priority_sum = 0
    with open("input.txt") as f:
        for line in f:
            rucksack = line.strip()

            halfway = len(rucksack)//2 
            assert (halfway) * 2 == len(rucksack) # Check rucksack has even number of items in it
            
            first_half = set(rucksack[:len(rucksack)//2])
            second_half = set(rucksack[halfway:])
            duplicate_item = first_half.intersection(second_half)
            value = priority(duplicate_item.pop())
            priority_sum += value

    print("Sum of priorities is", priority_sum)


def part_ii():
    # Thanks to unutbu from StackOverflow for this neat iteration method!
    # https://stackoverflow.com/questions/1657299/how-do-i-read-two-lines-from-a-file-at-a-time-using-python
    import itertools

    priority_sum = 0
    with open("input.txt") as f:
        for elf1, elf2, elf3 in itertools.zip_longest(*[f]*3):
            elf1, elf2, elf3 = set(elf1.strip()), set(elf2.strip()), set(elf3.strip())
            badge_token: set = elf1.intersection(elf2).intersection(elf3)
            value = priority(badge_token.pop())
            priority_sum += value

    print("Sum of priorities is", priority_sum)


if __name__ == "__main__":
    # part_i()
    part_ii()