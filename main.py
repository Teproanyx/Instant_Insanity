from dice import Dice
import instant_insanity
from graph import graph_solution


def main():
    die = [Dice(list("RRWRGB")), Dice(list("RWWRBG")), Dice(list("BGBGRW")), Dice(list("GWWBRG"))]
    # die = [Dice(list("YWRYBW")), Dice(list("RRBYWB")), Dice(list("RBBWYY")), Dice(list("WWRBWY"))]

    graph_solution(die, list("RWGB"))

    # for dices in instant_insanity.brute_force(die):
    #     print(dices)
    # print(edge_solution(die))


if __name__ == '__main__':
    main()
