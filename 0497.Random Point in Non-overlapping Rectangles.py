from bisect import bisect_left
from random import randint


class Solution:
    """Weighted random sampling using prefix sums and binary search.

    Intuition:
        Each rectangle has a number of integer points proportional to its area.
        We can weight sampling by area using prefix sums and binary search.

    Approach:
        Build a prefix sum array of rectangle areas. To pick a random point,
        generate a random number in [1, total_points], binary search for the
        rectangle, then uniformly sample a point within that rectangle.

    Complexity:
        Time: O(n) for init, O(log n) for pick
        Space: O(n)
    """

    def __init__(self, rects: list[list[int]]) -> None:
        self.rects = rects
        self.prefix_sums = [0] * len(rects)
        for i, (x1, y1, x2, y2) in enumerate(rects):
            self.prefix_sums[i] = self.prefix_sums[i - 1] + (x2 - x1 + 1) * (
                y2 - y1 + 1
            )

    def pick(self) -> list[int]:
        value = randint(1, self.prefix_sums[-1])
        idx = bisect_left(self.prefix_sums, value)
        x1, y1, x2, y2 = self.rects[idx]
        return [randint(x1, x2), randint(y1, y2)]
