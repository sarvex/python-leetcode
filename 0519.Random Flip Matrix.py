import random


class Solution:
    """Fisher-Yates shuffle approach for random matrix cell flipping.

    Intuition:
        Treat the matrix as a 1D array. Use a virtual shuffle where we swap
        the selected index with the last available index, shrinking the pool.

    Approach:
        Maintain a mapping for swapped indices. On each flip, pick a random
        index from the remaining pool, map it to its actual value, and swap
        with the last element. Reset clears the mapping.

    Complexity:
        Time: O(1) per flip, O(1) per reset
        Space: O(k) where k is number of flips since last reset
    """

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.total = rows * cols
        self.index_map: dict[int, int] = {}

    def flip(self) -> list[int]:
        self.total -= 1
        random_index = random.randint(0, self.total)
        actual_index = self.index_map.get(random_index, random_index)
        self.index_map[random_index] = self.index_map.get(self.total, self.total)
        return [actual_index // self.cols, actual_index % self.cols]

    def reset(self) -> None:
        self.total = self.rows * self.cols
        self.index_map.clear()
