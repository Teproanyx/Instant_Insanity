from typing import List

from cleanup import cleanup
from cube import Cube
from graph import graph_solution


def main():
    cleanup()

    # Input
    color_set = list(input("Input Color Set: "))
    print("Input cube configuration:")
    cube_str = [input() for i in range(4)]

    # Invoke graphing
    solutions = graph_solution(four_cube_set(*cube_str), color_set)
    # Output solution(s)
    for i, solution in enumerate(solutions):
        print("Solution #", i + 1)
        for cube in solution:
            cube.print_cube()


def four_cube_set(cube1: str, cube2: str, cube3: str, cube4: str) -> List[Cube]:
    """Create a list of four Cube from strings"""
    return [Cube(list(cube1)), Cube(list(cube2)), Cube(list(cube3)), Cube(list(cube4))]


if __name__ == '__main__':
    main()
