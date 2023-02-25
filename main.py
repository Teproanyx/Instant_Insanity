from dice import Dice
from graph import graph_solution
from typing import List


def main():
    dice_set_1 = four_dice_set("RRWRGB", "RWWRBG", "BGBGRW", "GWWBRG")
    # dice_set_2 = four_dice_set("YWRYBW", "RRBYWB", "RBBWYY", "WWRBWY")
    # impossible_set = four_dice_set("BGYRBR", "BYYYGR", "GGBRYB", "BYGRGR")

    graph_solution(dice_set_1, get_color_dice_set(dice_set_1[0]))
    # graph_solution(dice_set_2, get_color_dice_set(dice_set_2[0]))
    # graph_solution(impossible_set, get_color_dice_set(impossible_set[0]))


def four_dice_set(dice1: str, dice2: str, dice3: str, dice4: str) -> List[Dice]:
    return [Dice(list(dice1)), Dice(list(dice2)), Dice(list(dice3)), Dice(list(dice4))]


def get_color_dice_set(dice: Dice) -> List[str]:
    return list(dict.fromkeys(dice.__str__()))


if __name__ == '__main__':
    main()
