from collections import deque


class SnakeGame:
    """Simulates the classic Snake game on a grid.

    Intuition:
        Track the snake body as an ordered sequence and use a set for O(1)
        collision detection. The head moves in the given direction, and the
        tail is removed unless food is eaten.

    Approach:
        Use a deque for the snake body (head at front, tail at back) and a
        set for occupied positions. On each move, compute the new head
        position. If out of bounds, return -1. If food is at the new
        position, increment score and keep the tail. Otherwise remove the
        tail from both the deque and the set. If the new head collides with
        the body, return -1. Otherwise add the new head and return the score.

    Complexity:
        Time: O(1) per move
        Space: O(n + m) where n is the snake length and m is the food count
    """

    def __init__(self, width: int, height: int, food: list[list[int]]) -> None:
        """Initialize the game board, snake position, and food list."""
        self.rows = height
        self.cols = width
        self.food = food
        self.score = 0
        self.food_index = 0
        self.body: deque[tuple[int, int]] = deque([(0, 0)])
        self.occupied: set[tuple[int, int]] = {(0, 0)}

    def move(self, direction: str) -> int:
        """Move the snake in the given direction and return the score or -1 if game over."""
        head_row, head_col = self.body[0]
        new_row, new_col = head_row, head_col
        match direction:
            case "U":
                new_row -= 1
            case "D":
                new_row += 1
            case "L":
                new_col -= 1
            case "R":
                new_col += 1
        if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
            return -1
        if (
            self.food_index < len(self.food)
            and new_row == self.food[self.food_index][0]
            and new_col == self.food[self.food_index][1]
        ):
            self.score += 1
            self.food_index += 1
        else:
            self.occupied.remove(self.body.pop())
        if (new_row, new_col) in self.occupied:
            return -1
        self.body.appendleft((new_row, new_col))
        self.occupied.add((new_row, new_col))
        return self.score
