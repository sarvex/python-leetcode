from typing import List
from math import inf

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        Optimal sweep over sorted points to count valid pairs.

        Intuition:
        Sort by x ascending and y descending so that for each left point we only
        need to track the best bottom y while scanning to the right.

        Approach:
        - Sort by (x, -y).
        - For each i, set top = points[i][1] and bot = -inf.
        - Scan j > i; whenever bot < y <= top, count it and set bot = y.
          Early-exit if bot == top since no further y can satisfy.

        Complexity:
        Time: O(n log n + n^2)
        Space: O(1)
        """
        points.sort(key=lambda p: (p[0], -p[1]))
        result = 0
        for i, (_, top) in enumerate(points):
            bot = -inf
            for _, y in points[i + 1:]:
                if bot < y <= top:
                    result += 1
                    bot = y
                    if bot == top:
                        break
        return result
