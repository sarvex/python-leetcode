from math import inf


class Solution:
    def cheapestJump(self, coins: list[int], maxJump: int) -> list[int]:
        """Reverse DP to find lexicographically smallest minimum-cost path.

        Intuition:
        Work backwards from the last position to compute minimum cost to reach
        the end from each position. Then greedily reconstruct the path forward.

        Approach:
        1. Initialize cost array with infinity; set cost[n-1] = coins[n-1].
        2. From right to left, for valid positions, try all jumps up to maxJump.
        3. Track minimum cost to reach the end from each position.
        4. Reconstruct path by following positions with matching cumulative cost.

        Complexity:
        Time: O(n * maxJump)
        Space: O(n)
        """
        if coins[-1] == -1:
            return []
        length = len(coins)
        min_cost = [inf] * length
        min_cost[-1] = coins[-1]
        for i in range(length - 2, -1, -1):
            if coins[i] != -1:
                for j in range(i + 1, min(length, i + maxJump + 1)):
                    if min_cost[i] > min_cost[j] + coins[i]:
                        min_cost[i] = min_cost[j] + coins[i]
        if min_cost[0] == inf:
            return []
        path = []
        remaining = min_cost[0]
        for i in range(length):
            if min_cost[i] == remaining:
                remaining -= coins[i]
                path.append(i + 1)
        return path
