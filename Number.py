#!/usr/bin/env python

class Number:
    def __init__(self, order:int, number:int):
        self.order = order

        if number < 0 or number > 9:
            raise OverflowError("numberは0~9の値でなければなりません。")
        self.number = number

    def __eq__(self, other:"Number") -> str:
        if self.number == other.number:
            if self.order == other.order:
                return "bull"
            return "cow"
        return "none"

    def __str__(self):
        return "[ %d, %d ]" % (self.order, self.number)

if __name__ == "__main__":
    a = Number(0, 1)
    b = Number(1, 1)
    c = Number(1, 2)
    print((a==a)=="bull")
    print((a==b)=="cow")
    print((a==c)=="none")