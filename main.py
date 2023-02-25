from typing import List

from cleanup import cleanup
from dice import Dice
from graph import graph_solution


def main():
    cleanup()

    # Input
    color_set = list(input("Input Color Set: "))
    print("Input dice configuration:")
    dice_str = [input() for i in range(4)]

    # Invoke graphing
    solutions = graph_solution(four_dice_set(*dice_str), color_set)
    # Output solution(s)
    for i, solution in enumerate(solutions):
        print("Solution #", i + 1)
        for die in solution:
            die.print_dice()


def four_dice_set(die1: str, die2: str, die3: str, die4: str) -> List[Dice]:
    """Create a list of four Dice from strings"""
    return [Dice(list(die1)), Dice(list(die2)), Dice(list(die3)), Dice(list(die4))]


if __name__ == '__main__':
    main()
