from dice import Dice
from graph import graph_solution


def main():
    die = [Dice(list("RRWRGB")), Dice(list("RWWRBG")), Dice(list("BGBGRW")), Dice(list("GWWBRG"))]
    # die = [Dice(list("YWRYBW")), Dice(list("RRBYWB")), Dice(list("RBBWYY")), Dice(list("WWRBWY"))]

    graph_solution(die, list("RWGB"))


if __name__ == '__main__':
    main()
