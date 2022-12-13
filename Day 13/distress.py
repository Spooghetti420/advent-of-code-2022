from typing import TextIO


def in_order(left, right) -> bool:
    if isinstance(left, list) and isinstance(right, list):
        for i, j in zip(left, right):
            if (order := in_order(i, j)) == -1:
                continue
            else:
                return order
        if len(right) == len(left):
            return -1
        return len(right) > len(left)
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return -1
        return left < right
    if isinstance(left, int) and isinstance(right, list):
        return in_order([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return in_order(left, [right])


def part_i(f: TextIO):
    pairs = [pair.split("\n") for pair in f.read().strip().split("\n\n")]
    for i in range(len(pairs)):
        pairs[i][0] = eval(pairs[i][0])
        pairs[i][1] = eval(pairs[i][1])
    
    count = 0
    for i, pair in enumerate(pairs):
        if in_order(*pair):
            count += i+1
    print(count)


def part_ii(f: TextIO):
    packets = [eval(line) for line in f.read().replace("\n\n", "\n").split("\n")]
    # Bubble sort because why not
    for i in range(len(packets)-1):
        for j in range(0, len(packets)-i-1):
            if not in_order(packets[j], packets[j+1]):
                packets[j], packets[j+1] = packets[j+1], packets[j]


    div1 = packets.index([[2]])+1
    div2 = packets.index([[6]])+1

    print(div1 * div2)

def main():
    with open("input.txt") as f:
        # part_i(f)
        part_ii(f)


if __name__ == "__main__":
    main()