import glob
import os
from typing import List

from dice import Dice
from graph import graph_solution


def main():
    for f in glob.glob("*.svg"):
        os.remove(f)

    dice_set_1 = four_dice_set("RRWRGB", "RWWRBG", "BGBGRW", "GWWBRG")
    dice_set_2 = four_dice_set("YWRYBW", "RRBYWB", "RBBWYY", "WWRBWY")
    impossible_set = four_dice_set("BGYRBR", "BYYYGR", "GGBRYB", "BYGRGR")

    # graph_solution(dice_set_1, list("RGBW"))
    solutions = graph_solution(dice_set_2, list("BWYR"))
    # graph_solution(impossible_set, list("RGBY"))

    for i, solution in enumerate(solutions):
        print("Solution #", i + 1)
        for each_dice in solution:
            each_dice.print_dice()


def four_dice_set(dice1: str, dice2: str, dice3: str, dice4: str) -> List[Dice]:
    return [Dice(list(dice1)), Dice(list(dice2)), Dice(list(dice3)), Dice(list(dice4))]


if __name__ == '__main__':
    main()
