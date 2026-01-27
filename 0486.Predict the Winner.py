from functools import cache


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        """Minimax with memoization on score difference.

        Intuition:
            At each turn, the current player picks from either end. Track
            the relative score difference: positive means the current player
            leads.

        Approach:
            Define dfs(i, j) as the maximum score advantage the current
            player can achieve from nums[i..j]. The player picks either
            nums[i] or nums[j] and the opponent plays optimally on the
            remainder. Player 1 wins if dfs(0, n-1) >= 0.

        Complexity:
            Time: O(n^2) — each subarray computed once
            Space: O(n^2)
        """

        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))

        return dfs(0, len(nums) - 1) >= 0
