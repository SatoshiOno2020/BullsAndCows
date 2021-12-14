#!/usr/bin/env python

from Number import Number
import random

class Computer:
    def __init__(self):
        self.numbers = []

    def generate_numbers(self, pcs: int) -> None:
        i = 0
        while i < pcs:
            temp_Number = Number(i, random.randint(0, 9))
            if not "cow" in [_ == temp_Number for _ in self.numbers]:
                self.numbers.append(temp_Number)
                i+=1

    def __str__(self):
        return ",".join([str(_.number) for _ in self.numbers])


if __name__ == "__main__":
    computer = Computer()
    computer.generate_numbers(3)
    print(computer)