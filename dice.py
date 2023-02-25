from typing import List


class Dice:
    def __init__(self, face: List[str]):
        self.up = face[0]
        self.left = face[1]
        self.front = face[2]
        self.right = face[3]
        self.down = face[4]
        self.back = face[5]

    def turn_left(self) -> None:
        self.left, self.back, self.front, self.right = self.front, self.left, self.right, self.back

    def turn_right(self) -> None:
        self.right, self.front, self.back, self.left = self.front, self.left, self.right, self.back

    def turn_up(self) -> None:
        self.up, self.back, self.down, self.front = self.front, self.up, self.back, self.down

    def turn_down(self) -> None:
        self.down, self.front, self.up, self.back = self.front, self.up, self.back, self.down

    def __str__(self) -> str:
        return self.up + self.left + self.front + self.right + self.down + self.back

    def __eq__(self, other) -> bool:
        return self.front == other.front and self.back == other.back and self.left == other.left and \
            self.right == other.right and self.up == other.up and self.down == other.down

    def print_dice(self):
        print(f"\t{self.up}\n{self.left}\t{self.front}\t{self.right}\n\t{self.down}\n\t{self.back}")

    def to_edge(self):
        return [(self.up, self.down), (self.front, self.back), (self.left, self.right)]
