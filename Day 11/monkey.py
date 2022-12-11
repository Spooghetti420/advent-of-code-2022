import math
import re
from typing import TextIO

DESC_PATTERN = r"Monkey (\d+):\n  Starting items: (\d+(?:, \d+)*)\n  Operation: new = old ([\*\+]) ((?:\d+)|(?:old))\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"

class Monkey:
    def __init__(self, description: str) -> None:
        m = re.match(DESC_PATTERN, description)
        self.number, self.items, self.operator, self.operand, self.modulus, self.if_true, self.if_false = m.groups()
        self.number = int(self.number)
        self.items = [int(i) for i in self.items.split(", ")]
        try:
            self.operand = int(self.operand)
        except ValueError:
            # Operand must be "old" here
            pass
        self.modulus = int(self.modulus)
        self.if_true: int = int(self.if_true)
        self.if_false: int = int(self.if_false)
        self.inspection_count: int = 0

    def __repr__(self) -> str:
        return f"Monkey {self.number}({self.items},new=old{self.operator}{self.operand},divisible by {self.modulus},if true pass to {self.if_true}, else {self.if_false})"


def part_i(f: TextIO):
    monkey_passages = f.read().split("\n\n")
    monkeys = [Monkey(desc) for desc in monkey_passages]
    for _ in range(20):
        for m in monkeys:
            print(m.items)
            recipients: list[Monkey] = []
            for j, old in enumerate(m.items):
                # Make inspection
                m.inspection_count += 1

                # Update worry level
                if m.operator == "+":
                    if m.operand == "old": m.items[j] = old + old
                    if isinstance(m.operand, int): m.items[j] = old + int(m.operand)
                elif m.operator == "*":
                    if m.operand == "old": m.items[j] = old * old
                    if isinstance(m.operand, int): m.items[j] = old * int(m.operand)
                m.items[j] //= 3

                # Decide who gets the item now
                if m.items[j] % m.modulus == 0:
                    recipient = monkeys[m.if_true]
                    print("Threw to monkey", m.if_true)
                else:
                    recipient = monkeys[m.if_false]
                    print("Threw to monkey", m.if_false)
                
                recipients.append(recipient)
            for r in recipients:
                r.items.append(m.items.pop(0))
            print()
        for m in monkeys:
            print(m.items)


    monkeys.sort(key=lambda m: m.inspection_count, reverse=True)
    monkey_business = monkeys[0].inspection_count * monkeys[1].inspection_count
    for m in monkeys:
        print(m.inspection_count)
    print(monkey_business)
    

def part_ii(f: TextIO):
    monkey_passages = f.read().split("\n\n")
    monkeys = [Monkey(desc) for desc in monkey_passages]
    lcm = math.lcm(*(m.modulus for m in monkeys)) # Repeatedly shunt down the numbers by
    # taking the remainder modulo (the lowest common multiple of all the monkeys' moduli)...
    for _ in range(10000):
        for m in monkeys:
            recipients: list[Monkey] = []
            for j, old in enumerate(m.items):
                # Make inspection
                m.inspection_count += 1

                # Update worry level
                if m.operator == "+":
                    if m.operand == "old": m.items[j] = old + old
                    if isinstance(m.operand, int): m.items[j] = old + int(m.operand)
                elif m.operator == "*":
                    if m.operand == "old": m.items[j] = old * old
                    if isinstance(m.operand, int): m.items[j] = old * int(m.operand)
                m.items[j] %= lcm

                # Decide who gets the item now
                if m.items[j] % m.modulus == 0:
                    recipient = monkeys[m.if_true]
                else:
                    recipient = monkeys[m.if_false]

                recipients.append(recipient)
            
            for r in recipients:
                r.items.append(m.items.pop(0))


    monkeys.sort(key=lambda m: m.inspection_count, reverse=True)
    monkey_business = monkeys[0].inspection_count * monkeys[1].inspection_count
    for m in monkeys:
        print(m.inspection_count)
    print(monkey_business)


def main():
    with open("input.txt") as f:
        # part_i(f)
        part_ii(f)


if __name__ == "__main__":
    main()