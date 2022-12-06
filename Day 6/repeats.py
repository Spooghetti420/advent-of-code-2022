def search_unique(text: str, length: int) -> int:
    i = 0
    while i < len(text):
        sub = text[i:i+length]
        if len(set(sub)) == length:  # The set is all the unique characters, so if it's got 14 elements, the chars are all unique!
            return i+length
        i += 1

    return -1  # Really gotta honour that return type :P


def part_i(text):
    print(search_unique(text, 4))


def part_ii(text):
    print(search_unique(text, 14))


def main():
    with open("input.txt") as f:
        text = f.read().strip()

    # part_i(text)
    part_ii(text)

if __name__ == "__main__":
    main()