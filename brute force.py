import copy
from dice import Dice


def brute_force(die) -> list:
    for d1 in generate_all_permutation(die[0]):
        # if d1 == Dice(list("RRWGRB")):
        #     print('d1 good')
        for d2 in generate_all_permutation(die[1]):
            # if d2 == Dice(list("WBGRRW")) or d2 == Dice(list("RBGRWW")):
            #     print('d2 good')
            for d3 in generate_all_permutation(die[2]):
                # if d3 == Dice(list("GWBBGR")):
                #     print('d3 good')
                for d4 in generate_all_permutation(die[3]):
                    # if d4 == Dice(list("WGRWBG")) or d4 == Dice(list("BGRWWG")):
                    #     print('d4 good')
                    if is_solution(new_die := [d1, d2, d3, d4]):
                        return new_die

    return []


def is_solution(die: list) -> bool:
    front = [d.front for d in die]
    left = [d.left for d in die]
    right = [d.right for d in die]
    back = [d.back for d in die]

    return is_unique(front) and is_unique(left) and is_unique(right) and is_unique(back)


def is_unique(face: list) -> bool:
    return len(face) == len(set(face))


def generate_all_permutation(d: Dice) -> list:
    perm = []
    for i in range(4):
        perm.extend(generate_sides_permutation(d))
        d.turn_up()

    d.turn_left()
    d.turn_up()

    for i in range(2):
        # yield from d.generate_sides_permutation()
        perm.extend(generate_sides_permutation(d))
        d.turn_up()
        d.turn_up()

    d.turn_down()
    d.turn_right()

    return perm


def generate_sides_permutation(d: Dice) -> list:
    sides = []
    for i in range(4):
        # yield self
        sides.append(copy.deepcopy(d))
        d.turn_left()

    return sides
