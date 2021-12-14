#!/usr/bin/env python

######################################################
#
# BullsAndCows - or Mastermind, Numer0n, Code Braker(megatenI,II)
# written by Satoshi Ono (s.ono@aixtal.com)
# 2021.12.3
#
######################################################

from Computer import Computer
from Player import Player

PIECES = 3

def main():
    print(" ****************************************************************\n",
          "*                    Bulls                                     *\n",
          "*                             And                              *\n",
          "*                                     Cows                     *\n",
          "****************************************************************" )
    computer = Computer()
    computer.generate_numbers(PIECES)
    player = Player()
    print("\n終了したいときは「exit」と入力してください。\n")

    while True:
        input_numbers = input('３つの数字を入れてください。（例：1,2,3）： ')
        if input_numbers == 'exit':
            print('終了します。')
            break
        p_numbers_str = input_numbers.split(sep=',')
        p_numbers_int = [int(_) for _ in p_numbers_str]
        player.set_numbers(p_numbers_int)

        answer = [p == c for p in player.numbers for c in computer.numbers]
        cow = answer.count("cow")
        bull = answer.count("bull")
        if bull==PIECES:
            print("正解！")
            break

        print("Cow: %d , Bull: %d" % (cow, bull))


if __name__ == "__main__":
    main()