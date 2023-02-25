from dice import Dice
from graph import graph_solution
from typing import List


def main():
    # dice_set_1 = four_dice_set("RRWRGB", "RWWRBG", "BGBGRW", "GWWBRG")
    dice_set_2 = four_dice_set("YWRYBW", "RRBYWB", "RBBWYY", "WWRBWY")
    # impossible_set = four_dice_set("BGYRBR", "BYYYGR", "GGBRYB", "BYGRGR")

    # graph_solution(dice_set_1, list("RGBW"))
    graph_solution(dice_set_2, list("BWYR"))
    # graph_solution(impossible_set, list("RGBY"))


def four_dice_set(dice1: str, dice2: str, dice3: str, dice4: str) -> List[Dice]:
    return [Dice(list(dice1)), Dice(list(dice2)), Dice(list(dice3)), Dice(list(dice4))]


if __name__ == '__main__':
    main()
