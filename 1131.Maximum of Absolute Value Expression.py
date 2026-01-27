from itertools import pairwise
from math import inf


class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        """Find the maximum of |arr1[i]-arr1[j]| + |arr2[i]-arr2[j]| + |i-j|.

        Intuition:
            Expanding absolute values yields four linear expressions. The
            maximum difference of each expression across all indices gives a
            candidate answer.

        Approach:
            For each of 4 sign combinations (a, b), compute a*x + b*y + i for
            all indices. The answer is the max difference (max - min) across
            all sign combinations.

        Complexity:
            Time: O(n) where n is the length of the arrays
            Space: O(1) extra space
        """
        directions = (1, -1, -1, 1, 1)
        result = -inf
        for sign_a, sign_b in pairwise(directions):
            current_max = -inf
            current_min = inf
            for i, (x, y) in enumerate(zip(arr1, arr2)):
                value = sign_a * x + sign_b * y + i
                current_max = max(current_max, value)
                current_min = min(current_min, value)
                result = max(result, current_max - current_min)
        return result
