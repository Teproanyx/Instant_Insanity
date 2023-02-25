from typing import List

from cleanup import cleanup
from dice import Dice
from graph import graph_solution


def main():
    cleanup()

    # Input
    color_set = list(input("Input Color Set: "))
    print("Input die configuration:")
    die_str = [input() for i in range(4)]

    # Invoke graphing
    solutions = graph_solution(four_dice_set(*dice_str), color_set)
    # Output solution(s)
    for i, solution in enumerate(solutions):
        print("Solution #", i + 1)
        for each_dice in solution:
            each_dice.print_dice()


def four_dice_set(dice1: str, dice2: str, dice3: str, dice4: str) -> List[Dice]:
    """Create a list of four Dice from strings"""
    return [Dice(list(dice1)), Dice(list(dice2)), Dice(list(dice3)), Dice(list(dice4))]


if __name__ == '__main__':
    main()
