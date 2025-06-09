from typing import List
from itertools import pairwise

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Greedy approach: Take profit whenever possible

        Intuition:
        Unlike the first problem where we can only make one transaction,
        here we can make multiple transactions. The key insight is that
        we should capture every possible profit opportunity by buying at
        local minimums and selling at local maximums.

        Approach:
        Iterate through adjacent pairs of prices. For each pair, if the
        second price is higher than the first, we can make a profit by
        buying at the first price and selling at the second. Sum up all
        these profits.

        Complexity:
        Time: O(n) where n is the length of the prices array
        Space: O(1) as we only use constant extra space
        """
        return sum(max(0, b - a) for a, b in pairwise(prices))
