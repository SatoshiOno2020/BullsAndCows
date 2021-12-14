#!/usr/bin/env python

from Number import Number
from typing import List

class Player:
    def __init__(self):
        self.numbers = []

    def set_numbers(self, numbers:List) -> None:
        self.numbers = [Number(o, i) for o, i in zip(range(len(numbers)), numbers)]

    def __str__(self):
        return ",".join([str(_.number) for _ in self.numbers])


if __name__ == "__main__":
    player = Player()
    player.set_numbers([1,2,3])
    print(str(player)=="1,2,3")