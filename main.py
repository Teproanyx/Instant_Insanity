from dice import Dice
from graph import graph_solution
from typing import List


def main():
    die = [Dice(list("RRWRGB")), Dice(list("RWWRBG")), Dice(list("BGBGRW")), Dice(list("GWWBRG"))]
    # die = [Dice(list("YWRYBW")), Dice(list("RRBYWB")), Dice(list("RBBWYY")), Dice(list("WWRBWY"))]


def get_color_dice_set(dice: Dice) -> List[str]:
    return list(dict.fromkeys(dice.__str__()))


if __name__ == '__main__':
    main()
