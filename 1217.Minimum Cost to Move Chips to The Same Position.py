class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        """Minimum cost to move chips to the same position.

        Intuition:
            Moving a chip by 2 positions costs 0, so all chips on even positions
            can be grouped for free, and all on odd positions likewise. The cost
            is moving the smaller group to the larger.

        Approach:
            Count chips at odd positions. The answer is the minimum of odd count
            and even count.

        Complexity:
            Time: O(n) where n is the number of chips
            Space: O(1)
        """
        odd_count = sum(p % 2 for p in position)
        even_count = len(position) - odd_count
        return min(odd_count, even_count)
